from django.core.mail import EmailMessage
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from .token import account_activation_token

# Create your views here.
def activate(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_email_verified = True
        user.is_active = True

        user.save()
        messages.success(request, 'Your account emial was activated successfully!')
        
        return redirect('login')
    else:
        messages.error(request, 'Your account email token failed to activete')



def activateEmail(request, user, to_email):
    mail_subject = "Activate your account"
    message = render_to_string(
        "accounts/template_activate_email.html",{
            "user": user.username,
            "domain":  get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocal": "https" if request.is_secure() else 'http'
        }
    )
    
    email = EmailMessage(mail_subject, message, to=[to_email])
    
    if email.send():
        messages.success(request, f"Dear {user}, please confirm signup in your email {to_email}")
    else:
        messages.error(request, f"There was a problem sending email to {to_email}")


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            messages.success(request, 'Your account was created successfully!')
            return redirect(login)
    else:
        form = CustomUserCreationForm()

    template = 'accounts/signup.html'
    context = {
        'form': form
    }

    return render(request, template, context)


def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if not user:
            messages.error(request, 'You account email has not be confirmed.')
        else:
            auth_login(request, user)
            return redirect('/')
    
    form = AuthenticationForm()
    template = 'accounts/login.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def profile(request):
    template = 'profile.html'
    context = {}

    return render(request, template, context)