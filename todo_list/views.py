from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):

	if request.method=='POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()

		# Now to redirect to the Home Page with the new list item added from top-right corner add list button...
		all_items = List.objects.all
		messages.success(request, 'List-Item has been added Successfully.')
		return	render(request, 'home.html', {'all_items':all_items,'view_style':True})
				
	else:
		all_items = List.objects.all
		return	render(request, 'home.html', {'all_items':all_items,'view_style':True})

def about(request):
	
	context = {'first_name':'Abhishek', 'last_name':'Bhatnagar'}

	return	render(request, 'about.html', context)


def delete(request, list_id):
	
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has been Deleted Successfully.'))
	return redirect('home')


def edit(request, list_id):
	
	if request.method=='POST':
		
		item = List.objects.get(pk=list_id)

		form = ListForm(request.POST or None,instance=item)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item has been Edited Successfully.'))

			# Now to redirect to the Home Page with the new list item added from top-right corner add list button...
			return	redirect('home')
				
	else:
		item = List.objects.get(pk=list_id)
		return	render(request, 'edit.html', {'item':item})
