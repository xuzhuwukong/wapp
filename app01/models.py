from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)   # AutoField自增，primary_key=True限制主键约束
    title = models.CharField(max_length=32)   # Charfield字符串，max_length=32 最大长度不能超过32
    pub_date = models.DateField()       # DateField日期
    price = models.DecimalField(max_digits=8, decimal_places=2)    # DecimalField浮点型，最大位数8位，其中有两位为小数
    publish = models.CharField(max_length=32)
