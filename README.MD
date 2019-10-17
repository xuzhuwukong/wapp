# 基础需求：
1. 实现用户登录、注册
2. 列出图书列表、出版社列表、作者列表
3. 点击作者，会在新的页面列出该作者出版的图书列表
4. 点击出版社，会列出该出版社旗下图书列表
5. 可以创建、修改、删除 图书、作者、出版社

# 升级需求
1. 点击修改按钮，弹出模块框，模态框中展示该书的信息且信息可以修改，
2. 书名不可重复，不可修改
3. 修改图书信息时，使用ajax请求发送信息


# DJANGO LOGIN

## MODEL VIEW TEMPLATE
# url
  re_path
  re_path("^login/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$", views.login, name="Login")
  month_archive(request,y="2009",m="12")
  path
  内置转换器
  path("^login/<int:year>/$")
  str,slug,uuid,path  (除了？，左右分割)
  url

## 反向解析
    url起个别名name=“xxx”
    1.模板中 
    path（"login", views.login, name="Login"}
        {% url 'Login' %}
    2. 视图文件中
    from django.urls import reverse
    url = reverse("Login", args=(2009,))
    3. 名称空间
    app01,app02定义了两个别名"index"，
    repath（"^app01", include("app01.urls","app01")}
    url = reverse("app01:index")
# 模板文件
## 变量
    render(request, "index.html",{"n":name})
    变量非常多
        render(request, "index.html",Locals())
    {{ n }}
    1. 深度查询
        person.name
        list.0
        dict.name
    2. 过滤器
        {val| filter_name:}
        {now|date:"Y-m-d"}
        {link|safe}
        add:100
        upper
## 标签
    {% for i in list %}
    
    {% if user %}
    {% else %}
    {% endif %}
    
    {% with XX as x %}
    {% endwith %}
    
    {% url %}
    {% csrf_token %}
## 自定义过滤器
    {% load my_tag_filter %}
    
## 继承
    {% include "**.html" %}
# ORM

# 生成数据表
python manage.py startapp ***
python manage.py makemigrations
python manage.py migrate
