from django.db import models
from live_app.qiniu_tool import get_play_urls, pull_stream_url
import time
import requests
import datetime

# Create your models here.
class LiveUser(models.Model):
    name = models.CharField(max_length=20,verbose_name='用户名称')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "直播用户"
        verbose_name_plural = verbose_name
        db_table = 'live_user'

class LiveStream(models.Model):
    user = models.ForeignKey(LiveUser, verbose_name='用户', on_delete=None)
    name = models.CharField(max_length=20,verbose_name='直播流名称')
    pull_stream_url = models.CharField(max_length=100, null=True,
            verbose_name='推流地址')
    rtmp_stream_url = models.CharField(max_length=100, null=True,
            verbose_name='rtmp直播地址')
    hls_stream_url = models.CharField(max_length=100, null=True,
            verbose_name='hls直播地址')

    hdl_stream_url = models.CharField(max_length=100, null=True,
            verbose_name='hdl直播地址')
    state = models.IntegerField('直播流状态', default=1) #0 禁播 1 启用



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "直播流"
        verbose_name_plural = verbose_name
        db_table = 'live_stream'

    def set_stream_url(self):
        stream_urls = get_play_urls(self.name)
        self.rtmp_stream_url = stream_urls['rtmp_url']
        self.hls_stream_url = stream_urls['hls_url']
        self.hdl_stream_url = stream_urls['hdl_url']
        self.pull_stream_url = pull_stream_url(self.name)
        self.save()


    def get_play_streams(self):
        data = []
        data.append(dict(stream_name=self.name,
                live_type='rtmp',
                stream_url=self.rtmp_stream_url,
                state=1))
        data.append(dict(stream_name=self.name,
                live_type='hls',
                stream_url=self.hls_stream_url,
                state=1))
        data.append(dict(stream_name=self.name,
                live_type='hdl',
                stream_url=self.hdl_stream_url,
                state=1))
        return data



    def get_info(self):
        return dict(stream_id=self.id,
                pull_stream_url=self.pull_stream_url,
                play_streams=self.get_play_streams(),
                )


class LiveRecord(models.Model):
    user = models.ForeignKey(LiveUser, verbose_name='用户', on_delete=None)
    title = models.CharField(max_length=20,verbose_name='直播标题')
    speaker = models.CharField(max_length=20,verbose_name='主讲人')
    image_url = models.CharField(max_length=100, null=True, verbose_name='封面图片url')
    details = models.TextField('详细介绍', null=True)
    start_time = models.DateTimeField('开始时间')
    last_time = models.IntegerField('直播时间', default=0)
    pull_stream_url = models.CharField(max_length=100, null=True,
            verbose_name='推流地址')
    state = models.IntegerField('直播状态', default=0) #0 未开播，1 正在直播 2 直播完成

    def __str__(self):
        return self.title

    def get_play_streams(self):
        play_streams = PlayStream.objects.filter(live_record=self)
        return [play_stream.get_info() for play_stream in play_streams]

    def set_state(self):
        now = datetime.datetime.now()
        end = self.start_time + datetime.timedelta(minutes=self.last_time)
        if now < self.start_time:
            self.state = 0
        elif now > end:
            self.state = 2
        else:
            self.state = 1
        self.save()

    def get_info(self):
        self.set_state()
        return dict(live_record_id=self.id,
                user_id=self.user_id,
                title=self.title,
                speaker=self.speaker,
                image_url=self.image_url,
                details=self.details,
                start_time=self.start_time.strftime('%Y-%m-%d %H:%M:%S'),
                last_time=self.last_time,
                pull_stream_url=self.pull_stream_url,
                play_streams = self.get_play_streams(),
                state=self.state)

    class Meta:
        verbose_name = "直播记录"
        verbose_name_plural = verbose_name
        db_table = 'live_record'

class PlayStream(models.Model):
    user = models.ForeignKey(LiveUser, verbose_name='用户', on_delete=None)
    live_record = models.ForeignKey(LiveRecord, verbose_name='直播', on_delete=None)
    stream_name = models.CharField(max_length=20,verbose_name='直播流名称')
    live_type = models.CharField(max_length=20, null=True,
            verbose_name='直播类型')
    stream_url = models.CharField(max_length=100, null=True,
            verbose_name='直播地址')
    state = models.IntegerField('直播流状态', default=0) #0 可编辑  1 不可编辑



    def __str__(self):
        return self.stream_name

    class Meta:
        verbose_name = "播放流"
        verbose_name_plural = verbose_name
        db_table = 'play_stream'

    def get_info(self):
        return dict(play_stream_id=self.id,
                live_record_id=self.live_record_id,
                stream_name=self.stream_name,
                live_type=self.live_type,
                stream_url=self.stream_url,
                state=self.state)

class LivePlayBack(models.Model):
    user = models.ForeignKey(LiveUser, verbose_name='用户', on_delete=None)
    is_vip = models.IntegerField('是否仅会员观看', default=0)
    title = models.CharField(max_length=20,verbose_name='回放标题')
    speaker = models.CharField(max_length=20,verbose_name='主讲人')
    image_url = models.CharField(max_length=100, null=True, verbose_name='封面图片url')
    details = models.TextField('详细介绍', null=True)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    last_time = models.IntegerField('时长', default=0)
    state = models.IntegerField('直播状态', default=2) #0 未开播，1 正在直播 2 直播完成
    media_type = models.IntegerField('视频类型', default=0) #0 回放 1 手动上传
    media_url = models.CharField(max_length=100, null=True,
            verbose_name='视频地址')
    live_info =  models.CharField(max_length=100, null=True,
            verbose_name='直播信息')
    play_count = models.IntegerField('播放次数', default=0)

    def __str__(self):
        return self.title

    def get_info(self):
        return dict(play_back_id=self.id,
                user_id=self.user_id,
                title=self.title,
                is_vip=self.is_vip,
                media_type=self.media_type,
                speaker=self.speaker,
                image_url=self.image_url,
                details=self.details,
                create_time=self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                last_time=self.last_time,
                state=self.state,
                media_url=self.media_url)

    def is_collected(self, client_id):
        collect = PlayBackCollect.objects.filter(user=self.user, play_back=self, client_id=client_id)
        if collect:
            return 1
        else:
            return 0

    def add_last_time(self):
        url = self.media_url + '?avinfo'
        resp = requests.get(url)
        avinfo = resp.json()
        if 'format' in avinfo and 'duration' in avinfo['format']:
            duration = avinfo['format']['duration']
            self.last_time = int(float(duration))
            self.save()

    class Meta:
        verbose_name = "回放"
        verbose_name_plural = verbose_name
        db_table = 'live_play_back'

class PlayBackCollect(models.Model):
    user = models.ForeignKey(LiveUser, verbose_name='用户', on_delete=None)
    play_back = models.ForeignKey(LivePlayBack, verbose_name='回放', on_delete=None)
    client_id = models.IntegerField('客户端user_id', default=0)

    class Meta:
        verbose_name = "收藏"
        verbose_name_plural = verbose_name
        db_table = 'play_back_collect'






