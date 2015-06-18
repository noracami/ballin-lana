from django.db import models

# Create your models here.
class Team(models.Model):
    """docstring for Team"""

    team_name = models.CharField('單位名稱', max_length=20)
    team_order = models.IntegerField('排序')

    class Meta:
        verbose_name = '單位'

    def __str__(self):
        return self.team_name

    def get_team_status(self):
        status = ''
        return {'status': status,}

class ServiceItem(models.Model):
    """docstring for ServiceItem"""

    service_item_name = models.CharField('系統名稱', max_length=20)
    service_item_status = models.BooleanField('狀況正常', default=False)
    team = models.ForeignKey(Team, related_name='service_items')

    class Meta:
        verbose_name = '系統'

    def __str__(self):
        return "%s'%s" % (self.team, self.service_item_name)

class ServiceItemMessage(models.Model):
    """docstring for ServiceItemMessage"""

    service_item = models.ForeignKey(ServiceItem, related_name='messages')
    is_fine = models.BooleanField('狀況正常', default=False)
    notes = models.CharField('訊息', max_length=140, default='', blank=True)
    update_time = models.DateTimeField('存取時間', auto_now_add=True)
    comment_user = models.CharField('提供者', max_length=20, default='anonymous')

    class Meta:
        verbose_name = '訊息'

    def __str__(self):
        return '%s(%s)' % (self.comment_user, self.update_time)
