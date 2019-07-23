import hmac
import base64
from hashlib import sha1
import requests
import qiniu
import time

access_key = "4o8fd-5QVgP1Q5hO8uidQKlmPVT1cH01DDUf3GJU" # 替换成自己 Qiniu 账号的 AccessKey
secret_key = "d9q_qGPQ3jEfzjcd5h7cDoyKIMQADxPS7kMkglry" # 替换成自己 Qiniu 账号的 SecretKey
hub_name = "ruketang" # 直播空间名称， Hub 必须事先存在
stream_url = 'http://pili.qiniuapi.com/v2/hubs/%s/streams' % hub_name
RTMPPublishDomain = 'pili-publish.realtime-live.iruyue.tv' #推流域名 
RTMPPlayDomain = 'pili-live-rtmp.realtime-live.iruyue.tv' #RTMP播放域名 
HLSPlayDomain = 'pili-live-hls.realtime-live.iruyue.tv' #HLS播放域名 
HDLPlayDomain = 'pili-live-hdl.realtime-live.iruyue.tv' #HDL播放域名 

domain = 'http://pili-vod.realtime-live.iruyue.tv/'
def get_author():
    author = qiniu.auth.QiniuMacAuth(access_key, secret_key) 
    author = qiniu.auth.QiniuMacRequestsAuth(author)
    return author

def string_to_base64(string):
    return base64.b64encode(string.encode()).decode()

def changetime(str1):
    Unixtime = int(time.mktime(time.strptime(str1, '%Y-%m-%d %H:%M:%S')))
    return Unixtime
def strftime(timeStamp, form):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime(form, timeArray)
    return otherStyleTime

def query_stream(stream_title):
    '''
    查询直播流
    参数:
        stream_title:直播流名称
    '''
    author = get_author()
    stream_title = string_to_base64(stream_title) 
    url = stream_url + '/%s' % stream_title
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    res = requests.get(url, headers=headers, auth=author)
    content = res.json()
    content['status'] = res.status_code
    return content

def query_stream_list(liveonly='false', prefix='', limit=10, marker=''):
    '''
    查询流列表
    参数:
        liveonly: true/false,true表示查询的是正在直播的流，false表示返回所有的流
        prefix: 限定只返回带以 prefix 为前缀的流名
        limit:整数，限定返回的流个数，不指定表示遵从系统限定的最大个数
        marker:上一次查询返回的标记，用于提示服务端从上一次查到的位置继续查询，不指定表示从头查询
    '''
    author = get_author()

    url = stream_url + '?liveonly=%s&prefix=%s&limit=%s&marker=%s' % (liveonly, prefix, limit, marker)
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    res = requests.get(url, headers=headers, auth=author)
    content = res.json()
    content['status'] = res.status_code
    return content


def create_stream(stream_title):
    author = get_author()

    url = stream_url 
    headers = {'Content-Type':'application/json'}
    data = {'key':stream_title}
    res = requests.post(url, headers=headers, json=data, auth=author)
    content = res.json()
    content['status'] = res.status_code

    return content 

def disable_stream(stream_title, disabledTill):
    '''
    禁止推流和播流 
    参数:
        stream_title:直播流名称
        disabledTill:整数，Unix 时间戳，表示流禁播的结束时间，单位 s(秒)，-1 表示永久禁播。0 表示解除禁播
    '''

    author = get_author()
    stream_title = string_to_base64(stream_title) 
    url = stream_url + '/%s/disabled' % stream_title

    headers = {'Content-Type':'application/json'}
    data = {
        "disabledTill": disabledTill 
    }
    res = requests.post(url, headers=headers, json=data, auth=author)
    content = res.json()
    content['status'] = res.status_code

    return content 

def query_stream_live(stream_title):
    author = get_author()
    stream_title = string_to_base64(stream_title) 
    url = stream_url + '/%s/live' % stream_title
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    res = requests.get(url, headers=headers, auth=author)
    content = res.json()
    content['status'] = res.status_code

    return content 

def query_stream_lives(streams):
    author = get_author()
    url = 'http://pili.qiniuapi.com/v2/hubs/%s/livestreams' % hub_name
    data = {'items':streams}
    headers = {'Content-Type':'application/json'}
    res = requests.post(url, headers=headers, json=data, auth=author)
    return res.json()

def query_historyactivity(stream_title, start_time, end_time):
    author = get_author()
    stream_title = string_to_base64(stream_title) 
    if start_time: 
        start = changetime(start_time) - 60
    else:
        start = 0
    if end_time:
        end = changetime(end_time) + 60
    else:
        end = 0
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    url = stream_url +'/%s/historyactivity?start=%d&end=%d' % (stream_title,
            start, end)
    res = requests.get(url, headers=headers, auth=author)
    content = res.json()
    content['status'] = res.status_code
    items = content['items']
    for item in items:
        item['start_time'] = strftime(item['start'], '%Y-%m-%d %H:%M:%S')
        item['end_time'] = strftime(item['end'], '%Y-%m-%d %H:%M:%S')
        item['play_back_title'] = strftime(item['start'], '直播回放(%Y%m%d%H%S)')

    return content 

def play_back(stream_title, start_time, end_time, fname=None):
    history = query_historyactivity(stream_title, start_time, end_time)
    items = history['items']
    if not items:
        return None
    else:
        item = items[0]
        start = item['start']
        end = item['end']

    author = get_author()
    EncodedStreamTitle = string_to_base64(stream_title)
    url = stream_url + '/%s/saveas' % EncodedStreamTitle
    headers = {'Content-Type':'application/json'}
    
    data = {'start':start,
            'end':end}
    if fname:
        data['fname'] = fname
    res = requests.post(url, headers=headers, json=data, auth=author)
    content = res.json()
    content['status'] = res.status_code
    if res.status_code == 200:
        content['fname'] = domain + content['fname']

    return content 

def pull_stream_url(stream):
    return 'rtmp://%s/%s/%s' % (RTMPPublishDomain, hub_name, stream)

def play_url_rtmp(stream):
    return 'rtmp://%s/%s/%s' %(RTMPPlayDomain, hub_name, stream)

def play_url_hls(stream):
    return 'http://%s/%s/%s.m3u8' % (HLSPlayDomain,
            hub_name, stream)

def play_url_hdl(stream):
    return 'http://%s/%s/%s.flv' % (HDLPlayDomain,
            hub_name, stream)

def get_play_urls(stream):
    return dict(rtmp_url=play_url_rtmp(stream),
            hls_url=play_url_hls(stream),
            hdl_url=play_url_hdl(stream))


if __name__ == '__main__':
    datas = query_stream('test11111')
    #datas = query_stream_list()
    #datas = create_stream('test2')
    #datas = disable_stream('test2', 1560742936)
    #datas = query_stream_live('test2')
    #datas = query_stream_lives(['test', 'test2'])
    #datas = query_historyactivity('livestream', 0, 0)
    #datas = pull_stream_url('livestream')
    #datas = get_play_urls('livestream')
    #datas = play_back('livestream', '2019-07-18 10:35:00', '2019-07-18 10:37:00')
    print(datas)

