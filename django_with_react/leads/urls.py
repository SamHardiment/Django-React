from django.urls import path
from . import views

urlpatterns = [
    path("api/home", views.home, name='user-home'),
    path("api/about", views.about, name='user-about'),
    path('api/lead/', views.LeadListCreate.as_view() ),

]
