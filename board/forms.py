from django import forms
from .models import Topic
from django.contrib.auth.models import User



class Creat_form(forms.ModelForm):
    title = forms.CharField(max_length=65,label='اسم العمل',
                            widget=forms.TextInput(attrs={
                            'placeholder': 'عدد الأحرف 65 حرف',    }))
    description = forms.CharField(max_length=450,label='وصف للعمل',
                            widget=forms.Textarea(attrs={"rows":5, "cols":20,'placeholder': 'اكتب لا يوجد وصف في حالة ليس لديك ما تكتبه ',}))

    img_url = forms.URLField(max_length=250, label='رابط الصورة')


    class Meta:
        model = Topic

        fields = ['title','description', 'img_url', 'board',]


