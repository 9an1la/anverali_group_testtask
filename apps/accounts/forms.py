from django import forms
from apps.accounts.models import CustomUser, CustomerProfile, ExecutorProfile

USER_TYPE_CHOICE = [(1, 'Заказчик'), (2, 'Исполнитель')]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя')
    email = forms.EmailField(label='Электронная почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    type_of_user = forms.ChoiceField(label='Кто вы?', choices=USER_TYPE_CHOICE, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'type_of_user']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if CustomUser.objects.filter(email=data).exists():
            raise forms.ValidationError('Адрес почты уже занят.')
        return data


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Электронная почта',
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = CustomUser.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Адрес почты уже занят.')
        return data


class CustomerProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['contact_info', 'experience']
        labels = {
            'contact_info': 'Контактная информация',
            'experience': 'Опыт',
        }


class ExecutorProfileEditForm(forms.ModelForm):
    class Meta:
        model = ExecutorProfile
        fields = ['contact_info', 'experience']
        labels = {
            'contact_info': 'Контактная информация',
            'experience': 'Опыт',
        }