from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    class Role(models.IntegerChoices):
        TEACHER = 1,'Teacher'
        STUDENT = 2,'Student'
        ADMIN = 3,'Admin'

    role = models.IntegerField(choices=Role.choices, default=Role.TEACHER)

    class Meta:
        ordering = ['id']
        verbose_name = 'My User'
        verbose_name_plural = 'My Users'

    def __str__(self):
        return f"{self.role} - {self.username}"
    

class Student(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    subject = models.CharField(max_length=256, null=True, blank=True)
    mark = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name} ({self.subject} - {self.mark})"
