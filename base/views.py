from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(request):
	return render(request, 'base/home.html')
def about(request):
	return render(request,'base/about.html')
def tags(request):
	return render(request,'base/tags.html')
def recipes(request):
	return render(request,'base/recipes.html')
def contact(request):
	return render(request,'base/contact.html')
def tagtemplate(request):
	return render(request,'base/tag-template.html')
def singlerecipe(request):
	return render(request,'base/singlerecipe.html')
def drinks(request):
	return render(request,'base/drinks.html')
def breakfast(request):
	return render(request,'base/breakfast.html')
def lunch(request):
	return render(request,'base/lunch.html')
def recipe1(request):
	return render(request,'base/recipe1.html')
def recipe2(request):
	return render(request,'base/recipe2.html')
def recipe3(request):
	return render(request,'base/recipe3.html')
def recipe4(request):
	return render(request,'base/recipe4.html')
def recipe5(request):
	return render(request,'base/recipe5.html')
def maxican(request):
	return render(request,'base/maxican.html')



# Create your views here.



