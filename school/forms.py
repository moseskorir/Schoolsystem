from django import forms

from .models import Student
from .models import ReportCard

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
  
class ReportCardForm(forms.ModelForm):
    class Meta:
        model = ReportCard
        fields = "__all__"