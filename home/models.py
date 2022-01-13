from tkinter.tix import Tree
from turtle import Turtle
from django.db import models

# Create your models here.
class Calories(models.Model):
    name = models.TextField(null=True, max_length=200)
    calo = models.IntegerField(null=True)
    
    def __str__(self) -> str:
        return f"{self.id}. {self.name} - {self.calo}"

class CaseCBR(models.Model):
    name = models.TextField(null=True, max_length=64)
    gender = models.IntegerField(null=True)
    bmi = models.FloatField(null=True)
    tdee_thechat = models.FloatField(null=True)
    tdee_cungcap = models.FloatField(null=True)
    ts_viem_gan = models.IntegerField(null=True)
    ts_hen_xuyen = models.IntegerField(null=True)
    ts_dai_thao_duong = models.IntegerField(null=True)
    ts_xuong_khop = models.IntegerField(null=True)
    ts_cao_huyet_ap = models.IntegerField(null=True)
    ts_parkinson = models.IntegerField(null=True)
    ts_giam_tri_nho = models.IntegerField(null=True)
    nc_qs1_vitamin_b12 = models.IntegerField(null=True)
    nc_qs2_vitamin_b12 = models.IntegerField(null=True)
    nc_qs1_vitamin_d = models.IntegerField(null=True)
    nc_qs2_vitamin_d = models.IntegerField(null=True)
    nc_qs1_vitamin_e = models.IntegerField(null=True)
    nc_qs1_tinhbot = models.IntegerField(null=True)
    nc_qs2_tinhbot = models.IntegerField(null=True)
    nc_qs1_chatbeo = models.IntegerField(null=True) 
    nc_qs1_chatdam = models.IntegerField(null=True)
    nc_qs2_chatdam = models.IntegerField(null=True)
    bt_qs1_vitamin_b12 = models.IntegerField(null=True)
    bt_qs2_vitamin_b12 = models.IntegerField(null=True)
    bt_qs1_vitamin_d = models.IntegerField(null=True)
    bt_qs2_vitamin_d = models.IntegerField(null=True)
    bt_qs1_nuoc = models.IntegerField(null=True)
    bt_qs2_nuoc = models.IntegerField(null=True)
    bt_qs3_nuoc = models.IntegerField(null=True)
    bt_qs1_chatxo = models.IntegerField(null=True)
    tc_qs1_vitamin_b12 = models.IntegerField(null=True)
    tc_qs2_vitamin_b12 = models.IntegerField(null=True)
    tc_qs1_vitamin_d = models.IntegerField(null=True)
    tc_qs2_vitamin_d = models.IntegerField(null=True)
    tc_qs1_vitamin_e = models.IntegerField(null=True)
    tc_qs1_chatbeo = models.IntegerField(null=True)
    tc_qs2_chatbeo = models.IntegerField(null=True)
    tc_qs1_tinhbot = models.IntegerField(null=True)
    tc_qs2_tinhbot = models.IntegerField(null=True)
    tc_qs1_chatdam = models.IntegerField(null=True)
    tc_qs2_chatdam = models.IntegerField(null=True)
    result = models.TextField(null=True, max_length=64)

    def __str__(self) -> str:
        return f"{self.id}. {self.name}"

class Weight(models.Model):
    name = models.TextField(max_length=32, null=True)
    weight = models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.id}. {self.name} - {self.weight}"

class Advision(models.Model):
    name = models.TextField(null=True,max_length=200)
    desciption = models.TextField(null=True,max_length=500)
    
    def __str__(self) -> str:
        return f"{self.id}. {self.name}"