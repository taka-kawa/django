from django.db import models
from django.utils import timezone


class TextCategory(models.Model):
    """文章の属性のテーブル"""
    class Meta:
        db_table = 'text_cat'
    category = models.CharField('カテゴリー名', max_length=32)


class Text(models.Model):
    """メールの文章のテーブル"""
    class Meta:
        db_table = 'text'
    text = models.TextField('メールの文章')
    category_id = models.ForeignKey(TextCategory, on_delete=models.PROTECT)
    created = models.DateTimeField('作成日', default=timezone.now)
    shaped_text = models.TextField('整形後の文章')


class Feature(models.Model):
    """特徴量の詳細のテーブル"""
    class Meta:
        db_table = 'feature'
    text_id = models.ForeignKey(Text, on_delete=models.SET_NULL, null=True)
    category = models.CharField('素性の種類', max_length=32)
    vector = models.TextField('ベクトル')
    dim = models.IntegerField('次元数')
    note = models.TextField('備考')
    created = models.DateTimeField('作成日', default=timezone.now)
    corpus = models.TextField('コーパス')


class Relation(models.Model):
    """関係性のテーブル"""
    class Meta:
        db_table = 'relation'
    inquiry_id = models.ForeignKey(Text, on_delete=models.SET_NULL, null=True, related_name='inquiry_id')
    reply_id = models.ForeignKey(Text, on_delete=models.SET_NULL, null=True, related_name='reply_id')
    receipt_num = models.CharField('受付番号', max_length=32)
    company_code = models.CharField('企業コード', max_length=32)