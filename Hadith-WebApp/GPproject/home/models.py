from django.db import models
from django.utils import timezone

class Login(models.Model):
    name = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['date_added']

class Answer(models.Model):
    login = models.ForeignKey(Login, related_name='question', on_delete=models.CASCADE, null=False, default=1)
    question_text = models.CharField(max_length=255, null=True)
    answer_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Now use auto_now_add

    def __str__(self):
        return f"Answer by {self.login.name}"

    class Meta:
        ordering = ['created_at']
