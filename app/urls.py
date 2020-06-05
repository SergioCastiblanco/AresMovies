from django.urls import path 
from . import views 

app_name = 'app' 
urlpatterns = [
    path('AresMovies/', views.index, name='index'),


    #registro como usuario
    path('AresMovies/registry/', views.from_registro, name='registro'),
    path('registrar/', views.registrar, name='registrar'),


    #registro como administrador
    path('AresMovies/admin/adminConf/registry', views.form_admin, name='form_admin'),
    path('registrar_admin/', views.registrar_admin, name='registrar_admin'),


    #login
    path('AresMovies/login/', views.form_login, name='form_login'),
    path('AresMovies/autenticar/', views.autenticar, name='autenticar'), 
    

    #logout
    path('logout/', views.view_logout, name='view_logout'),
    

    #Buscar pelicula
    path('AresMovies/busqueda/', views.busqueda, name='busqueda'),


    #configuracion administrador
    path('AresMovies/admin/adminConf/', views.administradorConf, name='administradorConf'),


    #ver categoria 
    path('AresMovies/category/', views.categoria, name='categoria'),

    #crear categoria(administrador)
    path('crearCat/', views.CreaCat, name='CreaCat'),
    path('AresMovies/admin/adminConf/CreaCat/', views.form_crea_categoria, name='form_crea_categoria'),


    #ver pelicula
    path('AresMovies/movie/', views.ver_pelicula, name='ver_pelicula'),

    #calificar pelicula
    path('AresMovies/cal_movie/', views.califica_peli, name='califica_peli'),

    #comentar pelicula
    path('AresMovies/comentar', views.comentar, name='comentar'),

    #cambiar estado comentario
    path('AresMovies/c_estado', views.cambiar_est_com, name='cambiar_est_com'),

    #editar pelicula
    path('AresMovies/edit_peli', views.edit_peli, name='edit_peli'),

    #agrega pelicula a categoria
    path('AresMovies/agrega_cat', views.agrega_categoria, name='agrega_categoria'),


    #crear pelicula(administrador)
    path('crearMov/', views.CreaMov, name='CreaMov'),
    path('AresMovies/admin/adminConf/CreaMov/', views.form_crea_peliculas, name='form_crea_peliculas'),
   
]