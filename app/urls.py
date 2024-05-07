from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('turmas', views.turmas, name='turmas'),
    path('adicionar_medidas', views.adicionar_medidas, name='adicionar_medidas')

]
