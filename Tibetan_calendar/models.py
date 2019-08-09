import datetime
from django.db import models
from Tibetan_calendar.grpc_tools.client import get_calendar_list

week_day_list = ['一', '二','三','四','五','六','日']

# Create your models here.
class TibetanCalendar(models.Model):
    gregorian = models.CharField(max_length=20,verbose_name='公历')
    chinese = models.CharField(max_length=20,verbose_name='农历')
    tibetan = models.CharField(max_length=20,verbose_name='藏历')
    holiday = models.CharField(max_length=200,null=True, verbose_name='节日')
    shareUrl = models.CharField(max_length=200,null=True, verbose_name='分享链接')
    mark = models.CharField(max_length=500,null=True, verbose_name='备注')
    img = models.CharField(max_length=200,null=True, verbose_name='日期主题图片')
    tibetanYear = models.CharField(max_length=200,null=True, verbose_name='藏历年')
    tibetanMonth = models.CharField(max_length=200,null=True, verbose_name='藏历月')
    tibetanDay = models.CharField(max_length=200,null=True, verbose_name='藏历日')
    year = models.IntegerField('年', default=2019)
    month = models.IntegerField('月', default=1)

    def __str__(self):
        return self.gregorian

    class Meta:
        verbose_name = "汉藏佛历"
        verbose_name_plural = verbose_name
        db_table = 'tibetan_calendar'

    @classmethod
    def add_calendar(cls, year, month):
        count = cls.objects.filter(year=year, month=month).count()
        if count > 0:
            return None
        else:
            calendar_list = get_calendar_list(year, month)
            for day in calendar_list:
                cls.objects.create(gregorian=day.gregorian,
                        chinese=day.chinese,
                        tibetan=day.tibetan,
                        holiday=day.holiday,
                        img=day.img,
                        mark=day.content,
                        shareUrl=day.shareUrl,
                        tibetanYear=day.tibetanYear,
                        tibetanMonth=day.tibetanMonth,
                        tibetanDay=day.tibetanDay,
                        year=year,
                        month=month)
            return True
    @classmethod
    def get_month_data(cls, year, month):
        cls.add_calendar(year, month)
        tibetan_calendars = cls.objects.filter(year=year, month=month)
        tibetan_calendar_list = [tibetan_calendar.get_info() for tibetan_calendar in tibetan_calendars]
        return tibetan_calendar_list

    @classmethod
    def get_date(cls, gregorian):
        date = cls.objects.filter(gregorian=gregorian).first()
        if not date:
            year = int(gregorian[:4])
            month = int(gregorian[4:6])
            cls.get_month_data(year, month)
            date = cls.objects.filter(gregorian=gregorian).first()
        if date:
            return date.get_info()
        else:
            return None





    def week_day(self):
        date = datetime.datetime.strptime(self.gregorian, '%Y%m%d')
        weekday = week_day_list[date.weekday()]
        return weekday

    def get_info(self):
        return dict(gregorian=self.gregorian,
                chinese=self.chinese,
                tibetan=self.tibetan,
                holiday=self.holiday,
                img=self.img,
                year=self.year,
                month=self.month,
                mark=self.mark,
                week_day=self.week_day())








