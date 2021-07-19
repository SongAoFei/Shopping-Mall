from django.db import models

# Create your models here.


# 用户
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.username


# 商品
class Goods(models.Model):
    name = models.CharField(max_length=100, verbose_name="商品名称")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="价格")
    picture = models.ImageField(upload_to="images", verbose_name="图片")
    describe = models.CharField(max_length=200, verbose_name="详细信息")

    def __str__(self):
        return self.name


# 地址
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.address


# 购物车
class Cart(models.Model):
    username = models.CharField(max_length=100, verbose_name="用户名")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    count = models.IntegerField()


# 订单
class Order(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)
    state = models.BooleanField()

    def __str__(self):
        return self.create_time


# 总订单
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()
