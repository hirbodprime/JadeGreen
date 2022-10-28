from django.shortcuts import render

def homeview(req):
    return render(req , 'home/index.html')