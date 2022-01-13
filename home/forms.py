from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class FirstForm(forms.Form):
    LEVEL_CHOICES = (
        ('0', 'Không bị'),
        ('1', 'Bị Nhẹ'),
        ('2', 'Bị Vừa'),
        ('3', 'Bị Nặng'),
        )
    ACTIVITY_CHOICES = (
        ("0","không vận động hoặc ít vận động"),
        ("1","vận động nhẹ"),
        ("2","vận động"),
        ("3","không vận động"),
    )
    GENDER_CHOICES = (
        ("0", "nam"),
        ("1", "nữ"),
    )
    qs_ask_name = forms.CharField(help_text="Nhập tên của Quý khách: ", required=True)
    qs_gender = forms.ChoiceField(choices=GENDER_CHOICES, initial='0',help_text="Giới tính: ", required=True, widget=forms.RadioSelect)
    qs_weight = forms.FloatField(help_text="Cân nặng(kg) của Quý khách: ", required=True, validators=[MinValueValidator(0.0), MaxValueValidator(300)], widget=forms.TextInput(attrs={'placeholder': 'Đơn vị kg'}))
    qs_height = forms.FloatField(help_text="Chiều cao(cm) của Quý khách: ", required=True, validators=[MinValueValidator(0.0), MaxValueValidator(300)],  widget=forms.TextInput(attrs={'placeholder': 'Đơn vị cm'}))
    qs_age = forms.IntegerField(help_text="Tuổi của Quý khách: ", required=True, validators=[MinValueValidator(60), MaxValueValidator(200)])
    qs_activity_level = forms.ChoiceField(choices=ACTIVITY_CHOICES, initial='0',widget=forms.RadioSelect,help_text='Cường động vận động của quý khách như thế nào ?')

    qs_viem_gan = forms.ChoiceField(choices=LEVEL_CHOICES, initial='0', widget=forms.RadioSelect(), help_text='Quý khách có bị viêm gan không ?')
    qs_hen_xuyen = forms.ChoiceField(choices=LEVEL_CHOICES, initial='0', widget=forms.RadioSelect(), help_text='Quý khách có bị hen xuyễn không ?')
    qs_dai_thao_duong = forms.ChoiceField(choices=LEVEL_CHOICES,initial='0', widget=forms.RadioSelect(), help_text='Quý khách có bị đái tháo đường không ?')
    qs_xuong_khop = forms.ChoiceField(choices=LEVEL_CHOICES,initial='0', widget=forms.RadioSelect(), help_text='Quý khách có bị đau nhức xương khớp không ?')
    qs_cao_huyet_ap = forms.ChoiceField(choices=LEVEL_CHOICES,initial='0', widget=forms.RadioSelect(), help_text='Quý khách có bị cao huyết áp không ?')
    qs_parkinson = forms.ChoiceField(choices=LEVEL_CHOICES,initial='0', widget=forms.RadioSelect(), help_text='Quý khách có bị parkinson không ?')
    qs_giam_tri_nho = forms.ChoiceField(choices=LEVEL_CHOICES,initial='0', widget=forms.RadioSelect(), help_text='Quý khách có bị giảm trí nhớ không ?')
    

class LastForm(forms.Form):
    # cá, thịt, sữa, hoa quả, cơm , rau
    qs_ca = forms.IntegerField(help_text="Một tuần Quý khách ăn bao nhiêu gam cá: ", required=True, widget=forms.TextInput(attrs={'placeholder': 'Đơn vị: gam'}))
    qs_thit = forms.IntegerField(help_text="Một tuần Quý khách ăn bao nhiêu gam thịt: ", required=True, widget=forms.TextInput(attrs={'placeholder': 'Đơn vị: gam'}))
    qs_sua = forms.IntegerField(help_text="Một tuần Quý khách uống bao nhiêu cốc sữa: ", required=True, widget=forms.TextInput(attrs={'placeholder': 'Đơn vị: cốc sữa'}))
    qs_rau_cu_qua = forms.IntegerField(help_text="Một tuần Quý khách ăn bao nhiêu gam hoa quả: ", required=True, widget=forms.TextInput(attrs={'placeholder': 'Đơn vị: gam'}))
    qs_com = forms.IntegerField(help_text="Một ngày Quý khách ăn bao nhiêu bát cơm: ", required=True, widget=forms.TextInput(attrs={'placeholder': 'Đơn vị: bát'}))    
    # => qs_tdee 


class WeakForm(forms.Form):
    CHOICES = (
        ('0', 'Không'),
        ('1', 'Có')
    )
    qs1_vitamin_b12 = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có các biểu hiện ù tai, hoa mắt chóng mặt, da xanh xao không ạ?')
    qs2_vitamin_b12 = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có sưng, viêm lưỡi, khó thở không ạ?')
    
    qs1_vitamin_d = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có bị đau nhức xuơng khớp không ạ?')
    qs2_vitamin_d = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có dấu hiệu bị trầm cảm, suy giảm nhận thức không ạ?')
    
    qs1_vitamin_e = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có bị yếu cơ, liệt cơ, đi đứng lảo đảo không ạ?')

    qs1_tinhbot = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách cảm thấy mệt mỏi, khó tập trung không ạ?')
    qs2_tinhbot = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có khó tiêu không ạ?')
    
    qs1_chatbeo = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có thường xuyên cảm thấy đói bụng không ạ?')
    
    qs1_chatdam = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Tóc và móng tay của quý khách có bị mỏng và dễ gãy rụng không ạ?')
    qs2_chatdam = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có triệu chứng mất ngủ không ạ?')




class NormalForm(forms.Form):
    CHOICES = (
        ('0', 'Không'),
        ('1', 'Có')
    )
    qs1_vitamin_b12 = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có các biểu hiện ù tai, hoa mắt chóng mặt, da xanh xao không ạ?')
    qs2_vitamin_b12 = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có sưng, viêm lưỡi, khó thở không ạ?')
    
    qs1_vitamin_d = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có bị đau nhức xuơng khớp không ạ?')
    qs2_vitamin_d = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có dấu hiệu bị trầm cảm, suy giảm nhận thức không ạ?')

    qs1_nuoc = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text="Quý khách có biểu hiện đi tiểu ít không ạ?")
    qs2_nuoc = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text="Quý khách có bị khô da không ạ?")
    qs3_nuoc = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text="Nước tiểu của quý khách có màu nâu sẫm hoặc vàng sậm, đục không ạ?")
    
    qs1_chatxo = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text="Quý khách có bị táo bón hoặc đầy hơi không ạ?")
    
    

class FatForm(forms.Form):
    CHOICES = (
        ('0', 'Không'),
        ('1', 'Có')
    )
    qs1_vitamin_b12 = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có các biểu hiện ù tai, hoa mắt chóng mặt, da xanh xao không ạ?')
    qs2_vitamin_b12 = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có sưng, viêm lưỡi, khó thở không ạ?')
    
    qs1_vitamin_d = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có bị đau nhức xuơng khớp không ạ?')
    qs2_vitamin_d = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có dấu hiệu bị trầm cảm, suy giảm nhận thức không ạ?')
    
    qs1_vitamin_e = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có bị yếu cơ, liệt cơ, đi đứng lảo đảo không ạ?')

    qs1_chatbeo = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Gần đây quý khách có dấu hiệu tăng cân không ạ?')
    qs2_chatbeo = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có bị suy giảm trí nhớ không ạ?')

    qs1_tinhbot = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có bị nổi mụn trứng cá không ạ?')
    qs2_tinhbot = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có cảm giác thèm ăn không ạ?')

    qs1_chatdam = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có thường xuyên cảm thấy khát nước không ạ?')
    qs2_chatdam = forms.ChoiceField(choices=CHOICES, initial='0',widget=forms.RadioSelect,help_text='Quý khách có gặp các vấn đề về tiêu hóa không ạ?')
    
    


