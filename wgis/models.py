from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

from django.contrib.auth import get_user_model
import random
from datetime import timedelta

class EmailVerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_valid(self):
        # Token expires after 24 hours
        return (timezone.now() - self.created_at).days < 1
    
class OTPToken(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"OTP for {self.user.username}"

    def generate_otp(self):
        """Generate a 6-digit OTP"""
        self.token = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.save()
        return self.token

    def is_valid(self):
        """Check if OTP is still valid (within 10 minutes)"""
        return self.created_at >= timezone.now() - timedelta(minutes=10)

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    course_code = models.CharField(max_length=10)
    course_title = models.CharField(max_length=100)
    course_credit = models.IntegerField()
    exam_score = models.DecimalField(max_digits=5, decimal_places=2)
    total_score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)
    remark = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.student.username} - {self.course_code}"

class DownloadableResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='resources/pdfs/')
    icon_class = models.CharField(max_length=50, default='fas fa-file-pdf')
    
    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['-date']

    def __str__(self):
        return self.title
    