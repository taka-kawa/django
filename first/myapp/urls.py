from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    # /myapp以降がからの場合の''
    # 第二引数は呼び出す処理(views.pyのindex)
    path('', views.index, name='index'), # 127.0.0.01:8000/myapp に対応
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info')
    ]