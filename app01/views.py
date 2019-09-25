from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
from app01.models import Book

# 添加书籍
def addbook(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        # 生成的记录对象
        book_obj = Book.objects.create(title=title, price=price,pub_date=date, publish=publish)
        # return HttpResponse("OK")
        return redirect('/books/')   # 添加书籍后重定向

    return render(request, 'addbook.html')

# 查看书籍
def books(request):
    book_list = Book.objects.all()   # [obj1,obj2....]

    return render(request, "books.html", locals())  # 局部变量直接传入模板，变量名一一对应

# 删除书籍
def delbook(request, id):
    Book.objects.filter(id=id).delete()
    # 删除完成后重定向
    return redirect('/books/')

# 编辑数据
def changebook(request, id):
    # 拿到点击按钮对应条目的对象
    book_obj = Book.objects.filter(id=id).first()

    if request.method=="POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")

        Book.objects.filter(id=id).update(title=title, price=price, pub_date=date, publish=publish)

        return redirect("/books/")

    # 返回一个修改页面
    return render(request, 'changebook.html', {"book_obj":book_obj})


def query(request):
    # 查询老男孩出版社出版过的价格大于200的书籍
    ret = Book.objects.filter(publish="老男孩出版社",price__gt=200)
    print(ret)  # <QuerySet [<Book: Book object (6)>]>

    # 查询2017年8月出版的所有以py开头的书籍名称
    ret = Book.objects.filter(title__startswith="py", pub_date__year=2017, pub_date__month=8).values('title')
    print(ret)   # <QuerySet [{'title': 'python解析'}]>

    # 查询价格为50, 100或者150的所有书籍名称及其出版社名称
    ret = Book.objects.filter(price__in=[50,100,150]).values('title', 'publish')
    print(ret)   # <QuerySet [{'title': '金瓶梅', 'publish': '金桔出版社'}, {'title': '融资公告', 'publish': '人民出版社'}]>

    # 查询价格在100到200之间的所有书籍名称及其价格
    ret = Book.objects.filter(price__range=[100,200]).values('title', 'price')
    print(ret)   # <QuerySet [{'title': '金瓶梅', 'price': Decimal('150.00')}, {'title': 'python解析', 'price': Decimal('134.00')}]>

    # 查询所有人民出版社出版的书籍的价格（从高到低排序，去重）
    ret = Book.objects.filter(publish='人民出版社').values("price").distinct().order_by('-price')
    print(ret)   # <QuerySet [{'price': Decimal('134.00')}, {'price': Decimal('50.00')}]>

    return HttpResponse("OK")

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