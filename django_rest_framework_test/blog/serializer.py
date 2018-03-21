from rest_framework import serializers

from .models import User, Entry

"""シリアライズとは、ソフトウェア内部で扱っているデータを丸ごと、
ファイルで保存したりネットワークで送受信することができるように変換すること。"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')