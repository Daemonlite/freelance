from django.urls import path,re_path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_view
from find.views import *
from . import views
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    # path('register/',register_request, name='register'),
  
    path('',jobs,name='jobs'),
    path('application/',Application_form.as_view(),name='application'),
    path('add-company/',add_company.as_view(),name='add-company'),
    path('company/<str:pk>/',company_detail.as_view(),name='detail'),
    path('individual/',individual,name='individual'),
    path('individual-form/',Individual_form.as_view(),name='individual-form'),
   
   path('job_delete/<int:pk>/', views.company_delete, name='job-delete'),
    path('list/',list,name='list'),
    path('payment_method/',payment_method.as_view(),name='methods'),
    path('payment/',payments,name='payments'),


    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='base/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='base/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='base/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='base/password_reset_complete.html'),
         name='password_reset_complete'),
    
   
    path('post_detail/<int:pk>/',company_detail.as_view(),name="company-detail"),
]