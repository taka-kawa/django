from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    """/トップページ"""
    # return HttpResponse("Hello world", charset='cp932')

    context = {
        'name':'takashi'
    }
    # 第一引数:request
    # 第二引数:djangoアプリケーション内(first)のtemplatesフォルダを自動で読み取る
    return render(request, 'myapp/index.html', context)

    """
    render使わない場合
    # tenplate取得
    template = loder.get_template('myapp/index.html')
    context = {
        'name':'takashi'
    }
    # 変数を埋め込む
    response_src = template.render(context, request)
    return HttpResponse(response_src)
    """

def about(request):
    """/aboutページ"""
    return render(request, 'myapp/about.html')


def info(request):
    """/infoページ"""
    return render(request, 'myapp/info.html')