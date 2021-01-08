from django.db import models

# Create your models here.
class Student(models.Model):
    """
    Student data of all students in school
    """
    #id = models.IntegerField(primary_key=True, verbose_name='Id')
    name = models.CharField(max_length=200, verbose_name='Name')
    surname = models.CharField(max_length=200, verbose_name='Surname')
    age = models.IntegerField(blank=True, verbose_name='Age')
    sex = models.TextField(blank=True, verbose_name='Sex')
    address = models.TextField(blank=True, verbose_name='Address')
    description = models.TextField(blank=True, verbose_name='Description')
    birthday = models.DateField(blank=True, verbose_name="birthday")
    email = models.EmailField(blank=True, verbose_name="Email")


    def __str__(self):
        return self.name