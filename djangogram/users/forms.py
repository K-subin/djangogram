from django.contrib.auth import forms, get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms as django_forms

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

class SignUpForm(django_forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password']

        # 패스워드가 보여지지 않게 하기 위해
        widgets = {
            'email' : django_forms.TextInput(attrs={'placeholder' : '이메일 주소'}),
            'name' : django_forms.TextInput(attrs={'placeholder' : '성명'}),
            'username' : django_forms.TextInput(attrs={'placeholder' : '사용자 이름'}),
            'password' : django_forms.PasswordInput(attrs={'placeholder':'비밀번호'}),
        }

    # 유효한 패스워드 저장하기 위해 오버라이딩
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ProfileForm(django_forms.ModelForm):
    username = django_forms.CharField(widget=django_forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Username'}))
    email = django_forms.EmailField(widget=django_forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    phone_number = django_forms.CharField(widget=django_forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Username'}))
    
    class Meta:
        model = User
        fields = ['profile_photo','username', 'email', 'phone_number', 'gender']
    
    #password = django_forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    #password_confirm = django_forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password_confirm'}))