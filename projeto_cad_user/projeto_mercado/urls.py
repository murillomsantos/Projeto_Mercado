from django.urls import path
from app_cad_user import views

urlpatterns = [
    #rota, viewresponsavel, nome de referencia
    #usuarios.com
    path('',views.home,name='home'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
