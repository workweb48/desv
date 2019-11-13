from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='الإيميل')
    username = forms.CharField(max_length=50, required=True, label='اسم المستخدم')
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label='الاسم الأخير')

    password1 = forms.CharField(max_length=50,widget=forms.PasswordInput(), required=True, label='كلمة المرور')
    password2 = forms.CharField(max_length=50,widget=forms.PasswordInput(), required=True, label='تأكيد كلمة المرور')

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']




class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='الاسم الأول')
    last_name = forms.CharField(label='الاسم الأخير')
    email = forms.EmailField(label='البريد الإلكتروني')
    mobile = forms.CharField(max_length=20,  label='الجوال',widget=forms.TextInput(attrs={'placeholder': '+966500000000'}) )
    cv_img_url = forms.URLField(max_length=250,label='رابط صورة السيرة الذاتية')
    # key=forms.CharField(max_length=10,label='key')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','mobile','cv_img_url')

    # def clean_mobile(self,*args,**kwargs):
    #     mobile = self.cleaned_data.get('mobile')
    #     if not mobile.isdigit() :
    #         raise forms.ValidationError('MUST BE NUMBER')
    #     return mobile

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','mobile','cv_img_url',]