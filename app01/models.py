from django.db import models

# Create your models here.
class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 与AuthorDetail 建立一对一关系
    authorDetail = models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class AuthorDetail(models.Model):
    nid = models.AutoField(primary_key=True)
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)   # AutoField自增，primary_key=True限制主键约束
    title = models.CharField(max_length=32)   # Charfield字符串，max_length=32 最大长度不能超过32
    pub_date = models.DateField()       # DateField日期
    price = models.DecimalField(max_digits=8, decimal_places=2)    # DecimalField浮点型，最大位数8位，其中有两位为小数
    publish = models.ForeignKey(to="Publish", to_field="nid", on_delete=models.CASCADE)
    author = models.ManyToManyField(to="Author")
    def __str__(self):
        return self.title
