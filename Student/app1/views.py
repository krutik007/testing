from django.shortcuts import render
from django.http import HttpResponse
from .forms import Registration_Form
from .models import Registration
# Create your views here.
def home(Request):
	return render(Request,"home.html")

def reg(Request):
	form=Registration_Form()
	context={
		'form' : form,
		'data' : "Add Student"
	}
	return render(Request,"reg.html",context)
def insert(Request):
	name=Request.POST.get('sname')
	rno=Request.POST.get('srollno')
	city=Request.POST.get('scity')
	Registration.objects.create(srollno=rno,sname=name,scity=city)
	data=Registration.objects.all()
	p={
		'data' : p
	}
	return render(Request,"Display.html",dic)

def display(Request):
	p=Registration.objects.all()
	dic={
		'data' : p
	}
	return render(Request,"Display.html",dic)

def delete(Request):
	sid=Request.GET.get('rno')
	obj=Registration.objects.get(srollno=sid)
	obj.delete()
	p=Registration.objects.all()
	dic={
		'data' : p
	}
	return render(Request,"Display.html",dic)	