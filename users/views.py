from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from board.models import Topic,Board
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash



def register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,'تم تسجيلك بنجاح، سجل دخول الان ')
                return redirect('login')

        else:
            form = UserRegisterForm()
        return render(request,'register.html',{'form':form})


@login_required(login_url='login')
def profile(request):
    topics = Topic.objects.filter(created_by=request.user)
    topics_list = Topic.objects.filter(created_by=request.user)
    paginator = Paginator(topics_list, 12)
    a_boards = Board.objects.filter(active=True)
    page = request.GET.get('page')
    try:
        topics_list = paginator.page(page)
    except PageNotAnInteger:
        topics_list = paginator.page(1)
    except EmptyPage:
        topics_list = paginator.page(paginator.num_page)

    context = {
        'title': 'الملف الشخصي',
        'topics_profil': topics,
        'page': page,
        'topics_list': topics_list,
        'a_boards': a_boards,

    }

    return render(request, 'profile.html',context )


@login_required(login_url='login')
def profile_update(request):
    try:
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid and profile_form.is_valid:
                user_form.save()
                profile_form.save()
                messages.success(
                    request, 'تم تحديث الملف الشخصي.')
                return redirect('profile')
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'title': 'تعديل الملف الشخصي',
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, 'profile_update.html', context)


    except:
        messages.error(
            request, 'يوجد خطأ بأحد المدخلات')
        return redirect('profile')






@login_required(login_url='login')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(
                request, 'تم تحديث كلمة المرور بنجاح')
            return redirect('profile')
        else:
            return redirect('change-password')
    else:
        form = PasswordChangeForm(user=request.user)

        context={
           'form':form,
        }

        return render(request, 'password_change_form.html', context)




def Conditions(request):
    return render(request, 'Conditions.html')