from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
from django.template.context_processors import csrf
from app01.models import *

def add(request):

    #一对多添加记录
    #pub_obj = Publish.objects.create(name="人民",email="2@2.com",city="北京")
    #  绑定出版社
    #book_obj = Book.objects.create(title="红龙梦",price=100, pub_date="2019-09-16",publish_id=1)
    #pub_obj = Book.objects.filter(title="红龙梦").first().publish
    #print(pub_obj)

    # 多对多添加
    #author_detail = AuthorDetail.objects.create(birthday="1980-01-01",telephone=1388888,addr="beijign")
    #author = Author.objects.create(name="alex",age=30,authorDetail=author_detail)
    #author_detail = AuthorDetail.objects.create(birthday="1980-01-01",telephone=1388888,addr="beijign")
    #author = Author.objects.create(name="andy",age=30,authorDetail=author_detail)
    alex = Author.objects.get(name="alex")
    andy = Author.objects.get(name="andy")
    #book_obj = Book.objects.create(title="西游记", price=100, pub_date="2019-09-16", publish_id=1)
    #book_obj.author.add(alex,andy)

    book_obj = Book.objects.get(id=8)
    #book_obj.author.remove(alex)
    #book_obj.author.clear()
    #book_obj.author.all()
    print(book_obj.author.all())
    ret = book_obj.author.all().values("name")
    print(ret)
    return HttpResponse("OK")

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
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request, 'addbook.html',{'author_list':author_list,'publish_list':publish_list})

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
    '''

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
    '''
    # 基于对象的跨表查询
    # 翻译的语句是子查询，多条查询
    # 查询西游记出版社的名字
    # 一对多查询
    # 正方向查询：正向查询，关联属性在A表中，通过A查B， 按字段查
    # book = Book.objects.filter(title="西游记").first()
    # print(book.publish)
    # 一对多反向查询 按表名_set, querset
    #publish = Publish.objects.filter(name="人民").first()
    #print(publish.book_set.all())

    #多对多查询 book author
    # 关联属性在author中
    # 查询西游记作者名称正向查询 book ---》author
    '''
    book = Book.objects.filter(title="西游记").first()
    print(book)
    author_list = book.author.all()
    for aut in author_list:
        print(aut.name)    
    '''

    # 反向查询   book《-----author
    # alex作者写的book
    '''
    author = Author.objects.filter(name="alex").first()
    booklist = author.book_set.all()
    for book in booklist:
        print(book)
    '''
    # 一对一查询 author authordetail 关联在author中

    return HttpResponse("OK")

# Create your views here.
import time
def timer(request):
    rtime = time.time()
    return render(request, "timer.html", {"rtime":rtime})

def login(request):
    rtime = time.asctime( time.localtime(time.time()) )
    if request.method == "GET":
        return render(request,"index.html", {"rtime":rtime})
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("Ok")

def main_base_view(request):
#    dictionary = dict(request=request)
#    dictionary.update(csrf(request))
    name = "gao"
    return render(request, 'main/main_base.html', {"name":name})
