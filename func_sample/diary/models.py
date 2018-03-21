from django.db import models
# djangoでは、datetime.nowの代わりに、timezone.nowで現在日付・時刻を取得する
from django.utils import timezone

# models.Modelを継承
class Day(models.Model):
    """モデルができたらデータベースに反映"""
    # id = models.AutoField(primary_key=True)
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

