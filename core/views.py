from django.shortcuts import render
from django.views import View
from .models import Student
# Create your views here.
class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html', {'studata':stu_data})
    
    
class Add_Student(View):
    def grt(self, request):
        return render(request, 'core/add-student.html')
    