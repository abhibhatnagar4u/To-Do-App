from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.home, name='home'),
	path('about/',views.about, name='about'),
	path('delete/<list_id>',views.delete, name='delete'),
	path('edit/<list_id>',views.edit, name='edit'),
]
