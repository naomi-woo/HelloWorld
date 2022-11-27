from django.db import models
import os

# Create your models here.
class User(models.Model):
    pkvalue = models.AutoField(primary_key=True)
    ID = models.CharField(max_length=25, unique=True)
    PW = models.CharField(max_length=25, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)


    # null=True 인 field
    email = models.EmailField(max_length=25, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=25, unique=True, null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'[{self.pkvalue}] {self.ID} :: {self.email} : {self.join_date}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, allow_unicode=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/bbs/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    pkvalue = models.AutoField(primary_key=True)
    title = models.CharField(max_length=25)
    content = models.TextField(max_length=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='bbs/fiels/%Y/%m/%d/', blank=True)

    # 일대다 관계
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pkvalue}] {self.title} :: {self.created_date}'

    def get_absolute_url(self):
        return f'/bbs/{self.pkvalue}/'
    
    def get_file_name(self):
        return os.path.basename(self.file.name)

class Comment(models.Model):
    pkvalue = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=None)

    # 일대다 관계
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pkvalue}] {self.content} :: {self.created_date}'
