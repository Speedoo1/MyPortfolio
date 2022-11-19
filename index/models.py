from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class profile(AbstractUser):
    username = models.CharField(unique=True, max_length=200)
    bio = RichTextField(blank=True, null=True, )
    age = models.DateField(blank=True, null=True)
    dp = models.ImageField(null=True)
    tel = models.CharField(max_length=20, null=True)
    home_address = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=2000, null=True)


class testimonial(models.Model):
    name = models.CharField(max_length=200)
    dp = models.ImageField(null=True)
    message = RichTextField(blank=True, null=True, )
    email = models.EmailField(null=True)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)


class Resume(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class resumetitle(models.Model):
    task = models.ForeignKey(Resume, on_delete=models.CASCADE)
    startyear = models.DateField(null=True)
    endyear = models.DateField(null=True)
    post = models.CharField(max_length=200, null=True)
    about = models.TextField(null=True)

    def __str__(self):
        return str(self.post)


class myfield(models.Model):
    fieldname = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    about = RichTextField(null=True)

    def __str__(self):
        return str(self.fieldname)


class client(models.Model):
    logo = models.ImageField(null=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.company_name)


class myskills(models.Model):
    name = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=3, null=True)

    def __str__(self):
        return str(self.name)


class project(models.Model):
    img = models.ImageField(null=True)
    projectname = models.CharField(max_length=200, null=True)
    projecttype = models.CharField(max_length=200, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return str(self.projectname)
