from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'password1', 'password2', )
















# # from django import forms
# # from django.contrib.auth.models import User
# # from django.contrib.auth.forms import UserCreationForm
# # from accounts.models import Profile


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# # class SignUpForm(UserCreationForm):
# #     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# #     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# #     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
# #     birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

#     # class Meta:
#     #     model = User
#     #     fields = ('username', 'birth_date', 'first_name', 'last_name', 'email', 'password1', 'password2', )
#     #



# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)


# # class RegisterForm(UserCreationForm):
# #     # fields we want to include and customize in our form
# #     first_name = forms.CharField(max_length=100,
# #                                  required=True,
# #                                  widget=forms.TextInput(attrs={'placeholder': 'First Name',
# #                                                                'class': 'form-control',
# #                                                                }))
# #     last_name = forms.CharField(max_length=100,
# #                                 required=True,
# #                                 widget=forms.TextInput(attrs={'placeholder': 'Last Name',
# #                                                               'class': 'form-control',
# #                                                               }))
# #     username = forms.CharField(max_length=100,
# #                                required=True,
# #                                widget=forms.TextInput(attrs={'placeholder': 'Username',
# #                                                              'class': 'form-control',
# #                                                              }))
# #     email = forms.EmailField(required=True,
# #                              widget=forms.TextInput(attrs={'placeholder': 'Email',
# #                                                            'class': 'form-control',
# #                                                            }))
# #     password1 = forms.CharField(max_length=50,
# #                                 required=True,
# #                                 widget=forms.PasswordInput(attrs={'placeholder': 'Password',
# #                                                                   'class': 'form-control',
# #                                                                   'data-toggle': 'password',
# #                                                                   'id': 'password',
# #                                                                   }))
# #     password2 = forms.CharField(max_length=50,
# #                                 required=True,
# #                                 widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
# #                                                                   'class': 'form-control',
# #                                                                   'data-toggle': 'password',
# #                                                                   'id': 'password',
# #                                                                   }))

# #     class Meta:
# #         model = User
# #         fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']





# # class ProfileForm(forms.ModelForm):
# #     first_name = forms.CharField(max_length=255)
# #     last_name = forms.CharField(max_length=255)
# #     email = forms.EmailField()

# #     class Meta:
# #         model = Profile
# #         fields = '__all__'
# #         exclude = ['user']


# # def form_validation_error(form):
# #     """
# #     Form Validation Error
# #     If any error happened in your form, this function returns the error message.
# #     """
# #     msg = ""
# #     for field in form:
# #         for error in field.errors:
# #             msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
# #     return msg

