from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.contrib.auth import logout

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from wgis.models import EmailVerificationToken
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from wgis.models import OTPToken
from django.contrib.auth import get_user_model,login

from django.contrib.auth.models import User
import requests

from wgis.models import Result
from .models import DownloadableResource, News
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
import base64
import json

# --------------------------------------------------------INDEX_FUNCTION-------------------------------------------------------
def index(request):
    return render(request, 'wgis/index.html')

# --------------------------------------------------------BASE_FUNCTION --------------------------------------------------------
def base(request):
    return render(request,'wgis/base.html')

# --------------------------------------------------------LOGOUT_FUNCTION --------------------------------------------------------  
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('wgis:home')



# --------------------------------------------------------GOOGLE_SIGN_IN_FUNCTION --------------------------------------------------------
def google_login(request):
    google_auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={settings.GOOGLE_OAUTH2_CLIENT_ID}&"
        f"redirect_uri={settings.GOOGLE_OAUTH2_REDIRECT_URI}&"
        f"response_type=code&"
        f"scope=openid%20email%20profile&"
        f"access_type=offline"
    )
    return redirect(google_auth_url)

def google_callback(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponse("Authorization failed. No code provided.", status=400)

    # Exchange the authorization code for tokens
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        'code': code,
        'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
        'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        'redirect_uri': settings.GOOGLE_OAUTH2_REDIRECT_URI,
        'grant_type': 'authorization_code',
    }
    response = requests.post(token_url, data=data)
    if response.status_code != 200:
        return HttpResponse("Failed to retrieve access token.", status=400)

    tokens = response.json()
    access_token = tokens['access_token']

    # Use the access token to fetch user info
    user_info_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    headers = {'Authorization': f'Bearer {access_token}'}
    user_info_response = requests.get(user_info_url, headers=headers)
    if user_info_response.status_code != 200:
        return HttpResponse("Failed to fetch user info.", status=400)

    user_info = user_info_response.json()
    email = user_info['email']

    # Authenticate or create a user in your Django app
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = User.objects.create_user(
            username=email,
            email=email,
        )
        user.set_unusable_password()  # Since authentication is via Google
        user.save()

    # Log the user in
    login(request, user)
    return redirect('wgis:dashboard')  # Redirect to your desired page after login

# --------------------------------------------------------SIGNUP_FUNCTION --------------------------------------------------------  
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = 'wgis/signup.html'
    success_url = reverse_lazy('wgis:login')
    success_message = "Your account was created successfully. Please verify your account to log in."

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('wgis:dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.save(commit=False)
        
        # Create verification token
        verification_token = EmailVerificationToken.objects.create(user=user)
        
        # Build verification URL
        verify_url = self.request.build_absolute_uri(
            reverse_lazy('wgis:verify_email', kwargs={'token': verification_token.token})
        )
        
        # Prepare email
        context = {
            'user': user,
            'verify_url': verify_url,
        }
        html_message = render_to_string('wgis/verification_Emessage.html', context)
        plain_message = strip_tags(html_message)
        
        # Send email
        send_mail(
            'Verify Your Email Address',
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        messages.success(self.request, self.success_message)
        return response

# --------------------------------------------------------VERIFY_EMAIL_FUNCTION --------------------------------------------------------  
def verify_email(request, token):
    verification_token = get_object_or_404(EmailVerificationToken, token=token)
    
    if not verification_token.is_valid():
        messages.error(request, 'Verification link has expired. Please request a new one.')
        return redirect('wgis:login')
    
    if not verification_token.is_verified:
        user = verification_token.user
        user.is_active = True
        user.save()
        
        verification_token.is_verified = True
        verification_token.save()
        
        messages.success(request, 'Your email has been verified. You can now login.')
    else:
        messages.info(request, 'Your email was already verified. You can login.')
    
    return redirect('wgis:login')

# --------------------------------------------------------LOGIN_FUNCTION --------------------------------------------------------   
class CustomLoginView(SuccessMessageMixin, LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'wgis/login.html'
    success_message = "Welcome back, %(username)s!"


    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if 'password_reset_message' in request.session:
            messages.success(request, request.session.pop('password_reset_message'))
        if request.user.is_authenticated:
            return redirect('wgis:dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        remember_me = form.cleaned_data.get('remember_me')
        
        # Store remember_me preference in session
        self.request.session['remember_me'] = remember_me
        
        # Generate and send OTP
        otp_token = OTPToken.objects.create(user=user)
        otp = otp_token.generate_otp()
        
        # Prepare email
        context = {
            'user': user,
            'otp': otp,
        }
        html_message = render_to_string('wgis/otp_message.html', context)
        plain_message = strip_tags(html_message)
        
        # Send OTP email
        send_mail(
            'Your Login OTP',
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        # Store user_id in session for OTP verification
        self.request.session['user_id_for_otp'] = user.id
        
        return redirect('wgis:verify_otp')

# --------------------------------------------------------VERIFY_OTP_FUNCTION --------------------------------------------------------      
def verify_otp(request):
    """Handle OTP verification"""
    user_id = request.session.get('user_id_for_otp')
    if not user_id:
        messages.error(request, 'Please login first.')
        return redirect('wgis:login')
    
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user = get_user_model().objects.get(id=user_id)
        
        # Get the latest OTP token for the user
        otp_token = OTPToken.objects.filter(user=user, is_verified=False).latest('created_at')
        
        if otp_token and otp_token.is_valid() and otp_token.token == otp:
            # Mark OTP as verified
            otp_token.is_verified = True
            otp_token.save()
            
            # Log the user in
            login(request, user)
            
            # Set session expiry based on remember_me
            remember_me = request.session.get('remember_me', False)
            if not remember_me:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(30 * 24 * 60 * 60)
            
            # Clean up session
            del request.session['user_id_for_otp']
            del request.session['remember_me']
            
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('wgis:dashboard')
        else:
            messages.error(request, 'Invalid or expired OTP. Please try again.')
    
    return render(request, 'wgis/otp_form.html')

# --------------------------------------------------------GET_SUCCESS_URL_FUNCTION --------------------------------------------------------   
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url and self.is_safe_url(next_url):
            return next_url
        return reverse_lazy('wgis:dashboard')

    def is_safe_url(self, url):
        from django.utils.http import url_has_allowed_host_and_scheme
        allowed_hosts = self.request.get_host()
        return url_has_allowed_host_and_scheme(url, allowed_hosts)


# --------------------------------------------------------DASHBOARD_FUNCTION --------------------------------------------------------       
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'wgis/dashboard.html'
    login_url = 'wgis:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_login'] = self.request.user.last_login
        context['date_joined'] = self.request.user.date_joined
        
        # Get user's results
        context['results'] = Result.objects.filter(student=self.request.user)
        context['semesters'] = Result.objects.filter(student=self.request.user).values_list('semester', flat=True).distinct()
        context['academic_years'] = Result.objects.filter(student=self.request.user).values_list('academic_year', flat=True).distinct()
        
        return context

# Add these imports at the top


# Signal handlers
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """Log user login and update last login time"""
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    """Log user logout"""
    pass


# --------------------------------------------------------PASSWORD_RESET_FUNCTION --------------------------------------------------------      
class CustomPasswordResetView(PasswordResetView):
    template_name = 'wgis/reset_form.html'
    email_template_name = 'wgis/reset_email.html'
    success_url = reverse_lazy('wgis:login')

    @method_decorator(csrf_protect)
    def dispatch(self, args, **kwargs):
        return super().dispatch(args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data['email']
        # Add custom success message
        response = super().form_valid(form) 
        self.request.session['password_reset_message'] = \
            f"Check your email, We sent an email to {email} with instructions to reset your password."
        return response


    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    

# --------------------------------------------------------PASSWORD_RESET_CONFIRM_FUNCTION --------------------------------------------------------      
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'wgis/reset_password.html'
    success_url = reverse_lazy('wgis:login')
    
    def form_valid(self, form):
        messages.success(self.request, 
            "Your password has been successfully reset. You can now login with your new password.")
        return super().form_valid(form)


# --------------------------------------------------------ABOUT_FUNCTION --------------------------------------------------------      
def about(request):
    return render(request, 'wgis/about.html')

# --------------------------------------------------------HOME_FUNCTION --------------------------------------------------------      
def home(request):
    news_items = News.objects.all()[:6]  # Limit to 6 most recent items
    return render(request, 'wgis/home.html', {'news_items': news_items})

# --------------------------------------------------------ACADEMICS_FUNCTION --------------------------------------------------------       
def academics(request):
    return render(request, 'wgis/academics.html')

# --------------------------------------------------------ADMISSIONS_FUNCTION --------------------------------------------------------      
def admissions(request):
    return render(request, 'wgis/admissions.html')

# --------------------------------------------------------STAFF_FUNCTION --------------------------------------------------------      
def staff(request):
    return render(request, 'wgis/staff.html')

# --------------------------------------------------------STUDENTS_FUNCTION --------------------------------------------------------      
def students(request):
    return render(request, 'wgis/students.html')

# --------------------------------------------------------MORE_FUNCTION --------------------------------------------------------      
def more(request):
    resources = DownloadableResource.objects.all()
    return render(request, 'wgis/more.html', {'resources': resources})

# --------------------------------------------------------NEWS_DETAIL_FUNCTION --------------------------------------------------------       
def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'wgis/news_detail.html', {
        'news_item': news_item
    })

