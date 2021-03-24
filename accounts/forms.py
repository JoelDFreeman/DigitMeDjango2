from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = '__all__'

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class TagCreateForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = '__all__'

class CustomerCreateForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class CustomerAddressCreateForm(forms.ModelForm):
	class Meta:
		model = CustomerAddress
		fields = [
			'addressline1',
			'county',
			'postcode',
		]		

class ProductImageForm(forms.ModelForm):
	class Meta:
		model = ProductImage
		fields = [
			'name',
			'product_Main_Img',
		]	

class UserListView(forms.ModelForm):
    model = Customer
    template_name = 'customers.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'customers'  # Default: object_list
    paginate_by = 5
    queryset = Customer.objects.all()  # Default: Model.objects.all()			