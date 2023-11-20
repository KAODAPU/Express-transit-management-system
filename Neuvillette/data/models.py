from django.db import models
from django.utils import timezone


# Create your models here.

# 物品表
class Item(models.Model):
    item_id = models.BigIntegerField()  # 物品id
    client_id = models.BigIntegerField()  # 寄件人id
    name = models.CharField(max_length=100)  # 物品名
    ship_date = models.DateTimeField(auto_now_add=True)  # 揽件时间
    receive_date = models.DateTimeField(default=None)  # 收货时间
    weight = models.FloatField()  # 物品重量
    ship_address_id = models.BigIntegerField()  # 寄件地址id
    receive_address_id = models.BigIntegerField()  # 收件地址id
    remark = models.TextField(blank=True, default='')  # 备注
    is_send = models.BooleanField(default=False)  # 是否揽件
    is_receive = models.BooleanField(default=False)  # 是否收货


# 快递站地址表
class Address(models.Model):
    Address_id = models.BigIntegerField()  # 地址id
    name = models.CharField(max_length=100)  # 地址名


# 快递中转查询表
class Item2Address(models.Model):
    item_id = models.BigIntegerField()  # 物品id
    Address_id = models.BigIntegerField()  # 地址id
    line_id = models.IntegerField()  # 快递线路id
    transfer_id = models.IntegerField()  # 中转id(注：用于查询在线路中第几站)
    date = models.DateTimeField(auto_now_add=True)  # 录入时间


# 快递线路表
class Line(models.Model):
    line_id = models.AutoField(primary_key=True)  # 线路id


# 快递线路从表，存储线路上每个地址
class LineAddress(models.Model):
    address_id = models.BigIntegerField()  # 地址id
    transfer_id = models.AutoField(primary_key=True)  # 中转id(注：用于查询在线路中第几站)
    line = models.ForeignKey('data.Line', on_delete=models.CASCADE)  # 作为快递线路表从表


# 用户表
class User(models.Model):
    login_id = models.BigIntegerField()  # 账户id
    login_password = models.TextField()  # 密码
    authority_level = models.BigIntegerField()  # 权限等级
    phone = models.BigIntegerField()  # 电话号码
    name = models.CharField(max_length=100)  # 用户名
