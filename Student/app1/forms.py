from django.forms import ModelForm
from .models import Registration

class Registration_Form(ModelForm):
	class Meta:
		model=Registration
		fields=['srollno','sname','scity']