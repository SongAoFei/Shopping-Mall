from django.shortcuts import render, redirect
from shop import models
from django.core.paginator import Paginator

# Create your views here.


# 商品换行
threeList = []
for i in range(1, 100):
    if i % 3 == 0:
        threeList.append(i)


# 首页
def home(request, pageNum=1):
    page = models.Goods.objects.all()
    paginator = Paginator(page, 12)
    homepageList = paginator.page(pageNum)
    lis = threeList
    goodsOrders = models.Cart.objects.filter(username=request.user.username)
    context = {
        'omepageList': homepageList,
        'lis': lis,
        'goodsOrders': goodsOrders,
    }
    return render(request, "index.html", context)
