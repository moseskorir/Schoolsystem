from django.db import models

# Create your models here.

class Subjects(models.Model):
    STUDENTCLASS = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four')
    )
    student_class = models.CharField(max_length=30, choices=STUDENTCLASS, unique=True)
    math_subject = models.CharField(max_length=30)
    english_subject = models.CharField(max_length=30)
    kiswahili_subject = models.CharField(max_length=30)
    physics_subject = models.CharField(max_length=30, null=True)
    chemistry_subject = models.CharField(max_length=30, null=True)
    biology_subject = models.CharField(max_length=30, null=True)
    social_studies_subject = models.CharField(max_length=30, null=True)
    geography_subject = models.CharField(max_length=30, null=True)
    history_subject = models.CharField(max_length=30, null=True)
    business_subject = models.CharField(max_length=30, null=True)

