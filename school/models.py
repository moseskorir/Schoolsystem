from django.db import models
# from class import Class


class Student(models.Model):
    registration_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    email = models.EmailField(max_length=254)

class ReportCard(models.Model):
    TERM = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(max_length=1, choices=TERM)
    subject_name = models.CharField(max_length=30)
    subject_marks = models.IntegerField()




