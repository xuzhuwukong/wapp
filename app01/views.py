from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import time
def timer(request):
    rtime = time.time()
    return render(request, "index.html", {"rtime":rtime})

def login(request):
    rtime = time.asctime( time.localtime(time.time()) )
    if request.method == "GET":
        return render(request,"index.html", {"rtime":rtime})
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("Ok")