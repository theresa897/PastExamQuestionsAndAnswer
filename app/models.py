from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    logo = models.FileField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

<<<<<<< HEAD
=======

>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
class User(User):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    image = models.FileField(null=True, blank=True,upload_to='uploads/user')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return "{}".format(self.email)

class Exam(models.Model):
<<<<<<< HEAD
    subject = models.CharField(max_length=255)
    content = models.TextField()
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/exam')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    vote = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
=======
    id = models.PositiveBigIntegerField(primary_key=True)
    subject = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=20, unique=True)
    content = models.CharField(max_length=20)
    file = models.FileField(upload_to="uploads/exam")
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    vote = models.PositiveBigIntegerField()
    delete = models.BooleanField()
    user_uploaded = models.ForeignKey(User, on_delete=models.CASCADE)

class UserExam:
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.CharField(max_length=50)
>>>>>>> b1ce08c1bf083affc37742833f736154ebe11708
    
class Answer(models.Model):
    content = models.TextField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='answer_files/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Answer to {self.exam.title}'

