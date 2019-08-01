import os
import re
import time
import uuid
from base64 import b64decode

from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from qiniu import Auth, put_file, urlsafe_base64_encode, PersistentFop

# 七牛云配置

access_key = 'hJjSQyowyh5VtHAmBOihJX-jbtBc_5vfCoJHwXTj'
secret_key = 'yBpN1fL6Pb5o00rFM-TB3HTtzzOZrC6fxK9lwOU7'
bucket_name = 'yuanshi'
# bucket_domain = 'http://cdn.hopyun.cn/'
bucket_domain = 'https://cdn.yuans.xin/'
# bucket_name = 'media'
# bucket_domain = 'https://cdn.iruyue.tv'

_letter_cases = "abcdefghjkmnpqrstuvwxy"  # 小写字母，去除可能干扰的i，l，o，z
_upper_cases = _letter_cases.upper()  # 大写字母
_numbers = ''.join(map(str, range(3, 10)))  # 数字
init_chars = ''.join([_letter_cases, _upper_cases, _numbers])


# 图片上传格式后缀
# AVATAR_SUFFIX_LIMIT = "*.gif; *.jpg; *.jpeg; *.png;"
def upload_path(instance, filename):
    """
    Generate filename.

    :param instance: ImageField.
    :param filename: str.

    :return: str.
    """
    str_now_d = time.strftime('%Y/%m/%d')
    ext = filename.split('.')[-1]
    return 'static/{}/{}.{}'.format(
        str_now_d,
        uuid.uuid4().hex,
        ext
    )


def _upload(file):
    """图片上传函数"""
    if file:
        # if file.size / 1024 > 10240:
        #     return (False, "文件大小超过 10M限制")
        # 判断图片格式
        #        if AVATAR_SUFFIX_LIMIT.find(file.name.split(".")[-1]) == -1:
        #            return (False, "文件必须为GIF/JPG/PNG/BMP格式")
        file_name = '{}.{}'.format(str(uuid.uuid1()), file.name.split('.')[-1])
        f = open(settings.BASE_DIR + '/static/files/{}'.format(file_name), 'wb')
        f.write(file.read())
        f.close()
        return (True, file_name)
    return (False, "文件上传失败")


def upload_qiniu(pic_name):
    """
    从本地上传的文件中找到图片，上传到七牛云
    :param pic_name: 来自_avatar_upload()
    :return: 成功返回信息
    """
    auth = Auth(access_key, secret_key)

    file_name = pic_name
    token = auth.upload_token(bucket_name, file_name)

    localpath = os.path.join(os.path.dirname(__file__)).replace('tools', '')
    localfile = localpath + file_name
    ret, info = put_file(token, file_name, localfile)
    if info.status_code == 200:
        return True
    else:
        return False


def upload_file(file):
    """通过b64编码上传"""
    partten = re.compile("data:image/(.*);base64,(.*)")
    groups = partten.match(file)
    if groups:
        name, file = groups[1], groups[2]
    else:
        name = "jpg"
    if file:
        file_name = '{}.{}'.format(str(uuid.uuid1()), name)
        with open("static/files/{}".format(file_name), 'wb') as f:
            f.write(b64decode(file))
        return (True, file_name)
    return (False, "文件上传失败")


def b64_upload(code):
    result, file_name = upload_file(code)

    ret_url = ''
    if result:
        file_name = 'static/files/' + file_name
        if upload_qiniu(file_name):
            ret_url = bucket_domain + file_name
    return ret_url


def image_upload(request, name, need_water=False):
    """上传图片 返回图片路径"""
    files = [i for i in request.files.values()]
    files = [request.files[name], ] if name in request.files else []
    url_list = []
    for file in files:
        result = _upload(file)
        if result[0] == True:
            file_name = 'static/files/' + result[1]
            info_to_qiniu = upload_qiniu(file_name)
            # info_to_qiniu = upload_qiniu(result[1])
            if info_to_qiniu == True:
                url = bucket_domain + file_name
                if need_water:
                    # 添加水印
                    url_water = async_watermark(url)
                    url_list.append(url_water)
                else:
                    url_list.append(url)

    return url_list


def shortcut(localfile):
    auth = Auth(access_key, secret_key)
    fops = "vframe/jpg/offset/1/w/480/h/360"
    saveas_key = urlsafe_base64_encode('bucket_saved:bucket_saved')
    fops = fops + '|saveas/' + saveas_key
    policy = {
        'persistentOps': fops,
    }

    key = '352b0bfe-c135-11e8-95a8-9a000b94ea20.mp4'
    token = auth.upload_token(bucket_name, '352b0bfe-c135-11e8-95a8-9a000b94ea20.mp4', 3600, policy)
    ret, info = put_file(token, key, localfile)
    import ipdb;
    ipdb.set_trace()
    print(info, ret)


def async_watermark(url):
    auth = Auth(access_key, secret_key)
    fops = gen_watermark().replace("?", "")

    key = re.sub("http://[^/]*/", "", url)
    new_key = re.sub("[~\.]*(\.)", "r.", key)
    if "miaoduowang" in url:
        # 之前喵哆旺的先不做处理
        bucket_name = 'miaoduowang'
        bucket_domain = 'http://cdn.miaoduowang.com/'
    else:
        bucket_name = 'yuanshi'
        bucket_domain = 'http://cdn.hopyun.cn/'

    saveas_key = urlsafe_base64_encode(f'{bucket_name}:{new_key}')
    fops = fops + '|saveas/' + saveas_key
    pfop = PersistentFop(auth, bucket_name)

    ops = []
    ops.append(fops)
    ret, info = pfop.execute(key, ops, 1)
    return f"{bucket_domain}{new_key}"


# 生成token 15 * 24 * 60 * 60
def generate_token(role, id, expiration=15 * 24 * 60 * 60):
    """
    :param use: Model
    :param expiration: limit time
    :return: token
    """
    s = Serializer(settings.SECRET_KEY, expires_in=expiration)
    user_info = dict(
        id=id,
        role=role
    )
    token = s.dumps(user_info).decode()
    return token


def gen_watermark():
    code = urlsafe_base64_encode(settings.WATERMARK)
    return f"?watermark/1/gravity/Center/image/{code}/dissolve/80"


if __name__ == '__main__':
    # shortcut('/Users/zhenjieyu/work/thailand_house/static/files/35d97a74-c135-11e8-8692-9a000b94ea20.mp4')
    url = "http://cdn.hopyun.cn/static/files/93a161f0-c16d-11e8-9f6b-00163e0aa258.jpg"
    async_watermark(url)
