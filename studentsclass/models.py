from django.db import models
from school.models import Student

# Create your models here.

class Subjects(models.Model):
    STUDENTCLASS = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four')
    )
    TERM = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three')
    )
    student = models.ForeignKey(default=1, on_delete=models.CASCADE, to='school.Student')
    student_class = models.CharField(max_length=30, choices=STUDENTCLASS)
    term = models.CharField(max_length=1, choices=TERM)
    math_subject = models.IntegerField()
    english_subject = models.IntegerField()
    kiswahili_subject = models.IntegerField()
    physics_subject = models.IntegerField(blank=True, null=True)
    chemistry_subject = models.IntegerField(blank=True, null=True)
    biology_subject = models.IntegerField(blank=True, null=True)
    social_studies_subject = models.IntegerField(blank=True, null=True)
    geography_subject = models.IntegerField(blank=True, null=True)
    history_subject = models.IntegerField(blank=True, null=True)
    business_subject = models.IntegerField(blank=True, null=True)
    total_student_marks = models.IntegerField(default=1)


    def calculate_student_mark(self):
        student_marks = (self.math_subject + self.english_subject + self.kiswahili_subject + self.physics_subject + self.chemistry_subject + self.biology_subject + self.social_studies_subject + self.geography_subject + self.history_subject + self.business_subject)
        return total_student_marks