from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('delete/<list_id>', views.delete, name='delete'),
	path('completed/<list_id>', views.completed, name='completed'),
	path('n_completed/<list_id>', views.n_completed, name='n_completed'),
	path('edit/<list_id>', views.edit, name='edit'),
]
