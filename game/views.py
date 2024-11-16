from django.http import HttpResponse

def index(request):
    line3='<a href="/play/">进入游戏界面</a>'
    line1='<h1 style="text-align:center">术士之战</h1>'
    line2='<img src="https://ts1.cn.mm.bing.net/th/id/R-C.12fe9e15979987f47bfc8b97a8c46179?rik=0L9CtkYv5CSVYw&riu=http%3a%2f%2fi2.hdslb.com%2fbfs%2farchive%2f1e78a4fe81164db388cdc99c353b1ba338c0eed1.jpg&ehk=YIieoNTTcG1XFMAcZLOEZfpQfHHg%2fTo7R4XSDHykGK4%3d&risl=&pid=ImgRaw&r=0" width=2000>'
    return HttpResponse(line1+line2+line3)

def play(request):
    line3='<a href="/">返回主界面</a>'
    line1='<h1 style="text-align:center">游戏界面</h1>'
    line2='<img src="https://mod.3dmgame.com/static/upload/mod/allimg/363_170406132854_4.png" width=2000>'
    return HttpResponse(line1+line2+line3)
