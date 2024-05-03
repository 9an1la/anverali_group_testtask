from django.shortcuts import render
from .forms import UserRegistrationForm, CustomUserEditForm, CustomerProfileEditForm, ExecutorProfileEditForm
from .models import CustomerProfile, ExecutorProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# регистрация
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            if user_form.cleaned_data['type_of_user'] == '1':  # Если регистрация как заказчик
                new_user.is_customer = True
                new_user.save()
                CustomerProfile.objects.create(customer=new_user)
            elif user_form.cleaned_data['type_of_user'] == '2':  # Если регистрация как исполнитель
                new_user.is_executor = True
                new_user.save()
                ExecutorProfile.objects.create(executor=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


# просмотр профиля
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# редактирование профиля
@login_required
def edit(request):
    print(request.user)
    if request.method == 'POST':
        user_form = CustomUserEditForm(instance=request.user, data=request.POST)
        profile_form = ''
        if request.user.is_customer:
            profile_form = CustomerProfileEditForm(instance=request.user.customerprofile, data=request.POST,
                                                   files=request.FILES)
        elif request.user.is_executor:
            profile_form = ExecutorProfileEditForm(instance=request.user.executorprofile, data=request.POST,
                                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно изменён')
        else:
            messages.error(request, 'Ошибка изменения профиля')
    else:
        user_form = CustomUserEditForm(instance=request.user)
        profile_form = ''
        if request.user.is_customer:
            profile_form = CustomerProfileEditForm(instance=request.user.customerprofile)
        elif request.user.is_executor:
            profile_form = ExecutorProfileEditForm(instance=request.user.executorrprofile)
    return render(request, 'accounts/edit.html', {'user_form': user_form, 'profile_form': profile_form})