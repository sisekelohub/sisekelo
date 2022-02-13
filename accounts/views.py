from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from .forms import SignUpForm
from django.utils.encoding import force_str
from .tokens import account_activation_token


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})

def dashboard(request):
    return render(request, "registration/dashboard.html")

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Sisekelo Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'registration/account_activation_invalid.html')
















# from django.shortcuts import render, redirect 
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.utils.decorators import method_decorator
# from django.views import View

# from django.contrib import messages # import messages to show flash message in your page
# from accounts.forms import ProfileForm, form_validation_error # import the used form and related function to show errors
# from accounts.models import Profile # import the Profile Model


# from .forms import RegisterForm

# @login_required
# def profile(request):
#     return render(request, 'registration/profile.html')


# class RegisterView(View):
#     form_class = RegisterForm
#     initial = {'key': 'value'}
#     template_name = 'registration/register.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)

#         if form.is_valid():
#             form.save()

#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}')

#             return redirect(to='/')

#         return render(request, self.template_name, {'form': form})


# @method_decorator(login_required(login_url='login'), name='dispatch')
# class ProfileView(View):
#     profile = None

#     def dispatch(self, request, *args, **kwargs):
#         self.profile, __ = Profile.objects.get_or_create(user=request.user)
#         return super(ProfileView, self).dispatch(request, *args, **kwargs)

#     def get(self, request):
#         context = {'profile': self.profile}
#         return render(request, 'registration/profile.html', context)

#     def post(self, request):
#         form = ProfileForm(request.POST, request.FILES, instance=self.profile)

#         if form.is_valid():
#             profile = form.save()
            
#             # to save user model info
#             profile.user.first_name = form.cleaned_data.get('first_name')
#             profile.user.last_name  = form.cleaned_data.get('last_name')
#             profile.user.email      = form.cleaned_data.get('email')
#             profile.user.save()
            
#             messages.success(request, 'Profile saved successfully')
#         else:
#             messages.error(request, form_validation_error(form))
#         return redirect('profile')


# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

# ###
# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect
# from .forms import SignUpForm

# # def signup(request):
# #     if request.method == 'POST':
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             username = form.cleaned_data.get('username')
# #             raw_password = form.cleaned_data.get('password1')
# #             user = authenticate(username=username, password=raw_password)
# #             login(request, user)
# #             return redirect('home')
# #     else:
# #         form = UserCreationForm()
# #     return render(request, 'registration/register.html', {'form': form})

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/register.html', {'form': form})

# from django.contrib.sites.shortcuts import get_current_site
# from django.shortcuts import render, redirect
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# # from .forms import SignUpForm
# from .forms import CustomUserCreationForm
# from .tokens import account_activation_token

# from django.contrib.auth import login
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# # from django.utils.encoding import force_text
# from django.utils.encoding import force_str



# # def signup(request):
# #     if request.method == 'POST':
# #         form = SignUpForm(request.POST)
# #         if form.is_valid():
# #             user = form.save(commit=False)
# #             user.is_active = False
# #             # user.refresh_from_db()
# #             user.profile.birth_date = form.cleaned_data.get('birth_date')
# #             user.save()
# #             current_site = get_current_site(request)
# #             subject = 'Activate Your MySite Account'
# #             message = render_to_string('registration/account_activation_email.html', {
# #                 'user': user,
# #                 'domain': current_site.domain,
# #                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
# #                 'token': account_activation_token.make_token(user),
# #             })
# #             user.email_user(subject, message)
# #             return redirect('account_activation_sent')
# #     else:
# #         form = SignUpForm()
# #     return render(request, 'registration/register.html', {'form': form})


# # def activate(request, uidb64, token):
# #     try:
# #         uid = force_str(urlsafe_base64_decode(uidb64))
# #         user = User.objects.get(pk=uid)
# #     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
# #         user = None

# #     if user is not None and account_activation_token.check_token(user, token):
# #         user.is_active = True
# #         user.profile.email_confirmed = True
# #         user.save()
# #         login(request, user)
# #         return redirect('home')
# #     else:
# #         return render(request, 'registration/account_activation_invalid.html')






# def register(request):

#     if request.method == "GET":

#         return render(

#             request, "registration/register.html",

#             {"form": CustomUserCreationForm}

#         )

#     elif request.method == "POST":

#         form = CustomUserCreationForm(request.POST)

#         if form.is_valid():

#             user = form.save()

#             login(request, user)

#             return redirect(reverse("dashboard"))
