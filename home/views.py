from asyncio.base_subprocess import WriteSubprocessPipeProto
import contextlib
from http import client
from os import close
from re import template
import re
from tkinter import N
from typing import ContextManager
from unittest import result
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
# Create your views here.
from .forms import FirstForm, LastForm, WeakForm, NormalForm, FatForm
import redis
from home.utils import bmi_calculator, cbr_calculator, byte2string, tdee_calculator
from .models import Calories,CaseCBR,Advision, Weight


red = redis.StrictRedis(host='localhost', port=6379)

class FirstFormView(View):

    def get(self, request):
        form = FirstForm()
        context = {
            'form': form
        }
        return render(request, template_name='home/first_form.html', context=context)

    def post(self, request):
        form = FirstForm(request.POST)
        if form.is_valid():
            qs_ask_name = form.cleaned_data['qs_ask_name']
            qs_height = float(form.cleaned_data['qs_height'])
            qs_weight = float(form.cleaned_data['qs_weight'])
            qs_age = int(form.cleaned_data['qs_age'])
            qs_activity_level = int(form.cleaned_data['qs_activity_level'])
            qs_gender = int(form.cleaned_data['qs_gender'])

            bmi = bmi_calculator(qs_weight, qs_height) 
            tdee = tdee_calculator(qs_weight,qs_height,qs_age, qs_activity_level, qs_gender)
            print(f"tdee_thechat: {tdee}")
            red.set('name', qs_ask_name)
            red.set('bmi', bmi)
            red.set('gender', form.cleaned_data['qs_gender'])
            red.set('tdee_thechat', tdee)
            red.set('ts_viem_gan',form.cleaned_data['qs_viem_gan'])
            red.set('ts_hen_xuyen',form.cleaned_data['qs_hen_xuyen'])
            red.set('ts_dai_thao_duong',form.cleaned_data['qs_dai_thao_duong'])
            red.set('ts_xuong_khop',form.cleaned_data['qs_xuong_khop'])
            red.set('ts_cao_huyet_ap',form.cleaned_data['qs_cao_huyet_ap'])
            red.set('ts_parkinson',form.cleaned_data['qs_parkinson'])
            red.set('ts_giam_tri_nho',form.cleaned_data['qs_giam_tri_nho'])
            return redirect('/next_form')
        context = {
            'form':form
        }
        return render(request, template_name='home/first_form.html', context=context)


class NextFormView(View):
    
    def get(self, request):
        bmi = red.get('bmi')
        bmi = float(byte2string(bmi))
        form = None
        form_type = None
        if bmi < 18.5:
            form = WeakForm()
            form_type = "Nhẹ cân"
            red.set('form_type', 'WeakForm')
        elif 18.5 <= bmi < 23.0:
            form  = NormalForm()
            form_type = "Bình thường"
            red.set('form_type', 'NormalForm')
        else:
            form = FatForm()
            form_type = "Thừa cân"
            red.set('form_type', 'FatForm')
        
        context = {
            'form_type': form_type,
            'form': form
        }
        return render(request, template_name='home/next_form.html', context=context)

    def post(self, request):
        form_type = byte2string(red.get('form_type'))
        form = None
        if form_type == "WeakForm":
            form = WeakForm(request.POST)
        if form_type == "NormalForm":
            form = NormalForm(request.POST)
        if form_type == "FatForm":
            form = FatForm(request.POST)
        if form.is_valid():
            form_type = red.get('form_type')
            form_type = byte2string(form_type)
            
            if form_type == 'WeakForm':
                red.set('nc_qs1_vitamin_b12', form.cleaned_data['qs1_vitamin_b12'])
                red.set('nc_qs2_vitamin_b12', form.cleaned_data['qs2_vitamin_b12'])
                red.set('nc_qs1_vitamin_d', form.cleaned_data['qs1_vitamin_d'])
                red.set('nc_qs2_vitamin_d', form.cleaned_data['qs2_vitamin_d'])
                red.set('nc_qs1_vitamin_e', form.cleaned_data['qs1_vitamin_e'])
                red.set('nc_qs1_tinhbot', form.cleaned_data['qs1_tinhbot'])
                red.set('nc_qs2_tinhbot', form.cleaned_data['qs2_tinhbot'])
                red.set('nc_qs1_chatbeo', form.cleaned_data['qs1_chatbeo'])
                red.set('nc_qs1_chatdam', form.cleaned_data['qs1_chatdam'])
                red.set('nc_qs2_chatdam', form.cleaned_data['qs2_chatdam'])                
            if form_type == 'NormalForm':
                red.set('bt_qs1_vitamin_b12', form.cleaned_data['qs1_vitamin_b12'])                
                red.set('bt_qs2_vitamin_b12', form.cleaned_data['qs2_vitamin_b12'])                
                red.set('bt_qs1_vitamin_d', form.cleaned_data['qs1_vitamin_d'])                
                red.set('bt_qs2_vitamin_d', form.cleaned_data['qs2_vitamin_d'])                
                red.set('bt_qs1_nuoc', form.cleaned_data['qs1_nuoc'])                
                red.set('bt_qs2_nuoc', form.cleaned_data['qs2_nuoc'])                
                red.set('bt_qs3_nuoc', form.cleaned_data['qs3_nuoc'])                
                red.set('bt_qs1_chatxo', form.cleaned_data['qs1_chatxo'])                                              
            if form_type == 'FatForm':
                red.set('tc_qs1_vitamin_b12', form.cleaned_data['qs1_vitamin_b12'])                                              
                red.set('tc_qs2_vitamin_b12', form.cleaned_data['qs2_vitamin_b12'])                                              
                red.set('tc_qs1_vitamin_d', form.cleaned_data['qs1_vitamin_d'])                                              
                red.set('tc_qs2_vitamin_d', form.cleaned_data['qs2_vitamin_d'])                                              
                red.set('tc_qs1_vitamin_e', form.cleaned_data['qs1_vitamin_e'])                                              
                red.set('tc_qs1_chatbeo', form.cleaned_data['qs1_chatbeo'])                                              
                red.set('tc_qs2_chatbeo', form.cleaned_data['qs2_chatbeo']) 
                red.set('tc_qs1_tinhbot', form.cleaned_data['qs1_tinhbot'])                                              
                red.set('tc_qs2_tinhbot', form.cleaned_data['qs2_tinhbot']) 
                red.set('tc_qs1_chatdam', form.cleaned_data['qs1_chatdam'])                                              
                red.set('tc_qs2_chatdam', form.cleaned_data['qs2_chatdam'])                                              
            return redirect('/last_form')
        context = {
            'form':form
        }
        return render(request, template_name='home/next_form.html', context=context)


class LastFormView(View):
    
    def get(self, request):
        form = LastForm()
        context = {
            'form': form
        }
        return render(request, template_name='home/last_form.html', context=context)

    def post(self, request):
        form = LastForm(request.POST)
        if form.is_valid():
            qs_ca = int(form.cleaned_data['qs_ca'])/7
            qs_thit = int(form.cleaned_data['qs_thit'])/7
            qs_sua = int(form.cleaned_data['qs_sua'] * 100)/7
            qs_rau_cu_qua = int(form.cleaned_data['qs_rau_cu_qua'])/7
            qs_com = int(form.cleaned_data['qs_com']) * 100
            
            calo_ca = Calories.objects.filter(name__icontains='cá')[0].calo
            calo_thit = Calories.objects.filter(name__icontains='thịt')[0].calo
            calo_sua = Calories.objects.filter(name__icontains='sữa')[0].calo
            calo_rau_cu_qua = Calories.objects.filter(name__icontains='rau')[0].calo
            calo_com = Calories.objects.filter(name__icontains='gạo')[0].calo

            total_calo = qs_ca*calo_ca/100 + calo_thit*qs_thit/100 + calo_sua*qs_sua/100 + calo_rau_cu_qua*qs_rau_cu_qua/100 + calo_com*qs_com/100
            print(f"total calo: {total_calo}")
            red.set('tdee_cungcap', total_calo)
            return redirect('/result/')
        context = {
            "form": form
        }
        return render(request, template_name='home/last_form.html', context=context)


class ResultView(View):

    weak_type_fields = [
            'bmi','ts_viem_gan','ts_hen_xuyen','ts_dai_thao_duong','ts_xuong_khop',
            'ts_cao_huyet_ap',
            'ts_parkinson',
            'ts_giam_tri_nho',
            'tdee_thechat',
            'tdee_cungcap',
            'nc_qs1_vitamin_b12',
            'nc_qs2_vitamin_b12',
            'nc_qs1_vitamin_d',
            'nc_qs2_vitamin_d',
            'nc_qs1_vitamin_e',
            'nc_qs1_tinhbot',
            'nc_qs2_tinhbot',
            'nc_qs1_chatbeo',
            'nc_qs1_chatdam',
            'nc_qs2_chatdam',
        ]

    normal_type_fields = [
        'bmi',
        'ts_viem_gan',
        'ts_hen_xuyen',
        'ts_dai_thao_duong',
        'ts_xuong_khop',
        'ts_cao_huyet_ap',
        'ts_parkinson',
        'ts_giam_tri_nho',
        'tdee_thechat',
        'tdee_cungcap',
        'bt_qs1_vitamin_b12',
        'bt_qs2_vitamin_b12',
        'bt_qs1_vitamin_d',
        'bt_qs2_vitamin_d',
        'bt_qs1_nuoc',
        'bt_qs2_nuoc',
        'bt_qs3_nuoc',
        'bt_qs1_chatxo'
    ]
    
    fat_type_fields = [
        'bmi',
        'ts_viem_gan',
        'ts_hen_xuyen',
        'ts_dai_thao_duong',
        'ts_xuong_khop',
        'ts_cao_huyet_ap',
        'ts_parkinson',
        'ts_giam_tri_nho',
        'tdee_thechat',
        'tdee_cungcap',
        'tc_qs1_vitamin_b12',
        'tc_qs2_vitamin_b12',
        'tc_qs1_vitamin_d',
        'tc_qs2_vitamin_d',
        'tc_qs1_vitamin_e',
        'tc_qs1_chatbeo',
        'tc_qs2_chatbeo',
        'tc_qs1_tinhbot',
        'tc_qs2_tinhbot',
        'tc_qs1_chatdam',
        'tc_qs2_chatdam'
    ]

    def get_red_list(self, form_type):
    
        if form_type == 'WeakForm':
            client_data = [byte2string(red.get(field)) for field in self.weak_type_fields]
        if form_type == 'NormalForm':
            client_data = [byte2string(red.get(field)) for field in self.normal_type_fields]
        if form_type == 'FatForm':
            client_data = [byte2string(red.get(field)) for field in self.fat_type_fields]
        return client_data
 
    def get_weight_list(self,form_type):
        ans = []
        if form_type == 'WeakForm':
            for field in self.weak_type_fields:
                ans.append(Weight.objects.filter(name__icontains=field)[0].weight)
        if form_type == 'NormalForm':
            for field in self.normal_type_fields:                
                ans.append(Weight.objects.filter(name__icontains=field)[0].weight)
        if form_type == 'FatForm':
            for field in self.fat_type_fields:
                ans.append(Weight.objects.filter(name__icontains=field)[0].weight)
        ans = [float(i) for i in ans]
        return ans 

    def get_case_list(self, case, form_type):
        case_data = None
        if form_type == 'WeakForm':
            case_data = [getattr(case, field) for field in self.weak_type_fields]
        if form_type == 'NormalForm':
            case_data = [getattr(case, field) for field in self.normal_type_fields]
        if form_type == 'FatForm':
            case_data = [getattr(case, field) for field in self.fat_type_fields]
        return case_data
    



    def get_best_case(self, gender:int, client_data: list):
        cases = CaseCBR.objects.filter(gender=gender)

        form_type = byte2string(red.get('form_type'))
        normalized_cases = [self.get_case_list(case, form_type) for case in cases]
        weights = self.get_weight_list(form_type)
        index = cbr_calculator(problem=client_data, cases = normalized_cases, weights=weights)
        print(f"index: {index}")
        print(f"cases: {len(cases)}")
        return cases[index]

    def get_result(self, result):
        ans = []
        if result == "":
            ans = [
                "Chế độ dinh dưỡng của Quý khách ở tình trạng tốt. Hãy duy trì như chế độ ăn uống này và chăm chỉ tập luyện thể dục thể thao!"
            ]
            return ans
        resutls = result.split('|')
        for result in resutls:
            advice = Advision.objects.filter(name__icontains=result)[0].desciption
            ans.append(advice)
        return ans



    # METHOD GET HTTP
    def get(self, request):
        form_type = byte2string(red.get('form_type'))
        client_data = self.get_red_list(form_type)
        client_data = [float(val) for val in client_data]
        gender = int(byte2string(red.get('gender')))
        client_name = byte2string(red.get('name'))


        # CBR 
        best_case = self.get_best_case(gender, client_data)
        print("best_case: ", best_case)
        print(best_case.result)
    

        # MAP TO DB TO GET ADVICE
        results = self.get_result(best_case.result)
        print("resutls: ", results)
        client_gender = None
        if gender == 0:
            client_gender = "ông"
        else:
            client_gender = "bà"
        tdee_cungcap = byte2string(red.get('tdee_cungcap')) 
        tdee_thechat = byte2string(red.get('tdee_thechat'))
        print(f"tdee_cungcap: {tdee_cungcap} - tdee_thechat: {tdee_thechat}")
        context = {
            "client_name": client_name,
            "client_gender": client_gender,
            "results": results  
        }
        return render(request, template_name='home/result.html', context=context)


class UpdateDB(View):
    def update_calo(self):
        calories = Calories.objects.all().delete()
        filename = 'home/db_tmp/test.txt'
        f = open(filename, 'r')
        index1 = 0
        index2 = 5
        tmp_name = ""
        tmp_calo = None
        for index,line in enumerate(f):
            if index == index1:
                index1 += 6
                tmp_name = line[:-1]
            if index == index2:
                index2 += 6
                tmp_calo = line[:-1]
                cal = Calories.objects.create(name=tmp_name, calo=tmp_calo)
                
    def update_weight(self):
        w = Weight.objects.all().delete()
        filename1 = 'home/db_tmp/weight1.txt'
        filename2 = 'home/db_tmp/weight2.txt'
        f1 = open(filename1, 'r')
        f2 = open(filename2, 'r')
        lines1 = [line[:-1] for line in f1]
        lines2 = [line[:-1] for line in f2]
        for i in range(len(lines1)):
            print(lines1[i], lines2[i])
            w = Weight.objects.create(name=lines1[i], weight=lines2[i])

    def update_cbr(self):
        w = CaseCBR.objects.all().delete()
        from csv import reader
        fields = ['name', 'gender', 'bmi', 'tdee_thechat', 'tdee_cungcap', 'ts_viem_gan', 'ts_hen_xuyen', 'ts_dai_thao_duong', 'ts_xuong_khop', 'ts_cao_huyet_ap', 'ts_parkinson', 'ts_giam_tri_nho', 'nc_qs1_vitamin_b12', 'nc_qs2_vitamin_b12', 'nc_qs1_vitamin_d', 'nc_qs2_vitamin_d', 'nc_qs1_vitamin_e', 'nc_qs1_tinhbot', 'nc_qs2_tinhbot', 'nc_qs1_chatbeo', 'nc_qs1_chatdam', 'nc_qs2_chatdam', 'bt_qs1_vitamin_b12', 'bt_qs2_vitamin_b12', 'bt_qs1_vitamin_d', 'bt_qs2_vitamin_d', 'bt_qs1_nuoc', 'bt_qs2_nuoc', 'bt_qs3_nuoc', 'bt_qs1_chatxo', 'tc_qs1_vitamin_b12', 'tc_qs2_vitamin_b12', 'tc_qs1_vitamin_d', 'tc_qs2_vitamin_d', 'tc_qs1_vitamin_e', 'tc_qs1_chatbeo', 'tc_qs2_chatbeo', 'tc_qs1_tinhbot', 'tc_qs2_tinhbot', 'tc_qs1_chatdam', 'tc_qs2_chatdam', 'result']
        with open('home/db_tmp/handmade.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            index = 0
            for row in csv_reader:
                if index == 0:
                    index += 1
                    continue
                row = row[1:2] + row[5:]   
                print(row)
                d = dict(zip(fields, row)) 
                w = CaseCBR.objects.create(**d)
        

        
    def get(self, request):
        # self.update_calo()
        # self.update_weight()
        self.update_cbr()
        return HttpResponse("<h1>Updating database successfully!</h1>")