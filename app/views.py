from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from app.models import Categoria, Pelicula, PeliculaCategoria, Calificacion, Comentario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

#ANONIMO

def index(request):

#Billboards
    lista_categorias = Categoria.objects.all()
    lista_peliculas = Pelicula.objects.all()
    lista_encartelera = Pelicula.objects.filter(enCartelera=1)

# Ulitmas peliculas
    lista_pelis = Pelicula.objects.order_by('id')
    ultimas_pelis = lista_pelis.reverse()[:3]

#Ranking
    promedio = Calificacion.objects.values('pelicula__titulo').annotate(average_rating=Avg('valor')).order_by('average_rating')
        
    contexto = {
       'lista_categorias': lista_categorias,
       'lista_peliculas': lista_peliculas,
       'lista_encartelera': lista_encartelera,
       'ultimas_pelis': ultimas_pelis,
       'promedio': promedio,
       
    }

    return render(request, 'app/index.html', contexto)


def categoria(request):
    id_categoria = request.POST['categoria']
    lista_categorias = Categoria.objects.all()
    category = Categoria.objects.get(id=id_categoria)
    titulo = category.nombre
    pelis_categoria = PeliculaCategoria.objects.filter(categoria_id=id_categoria)
    peliculas = []
    for peli in pelis_categoria:
        n = peli.pelicula_id
        p = Pelicula.objects.get(id=n)
        peliculas.append(p)
    


    contexto = {
        'titulo':titulo,
        'lista_categorias': lista_categorias,
        'pelis_categoria': pelis_categoria,
        'peliculas': peliculas
    }
    return render(request, 'app/Categoria.html', contexto)


def busqueda(request):
    parametro = request.POST['parametro']
    busca = Pelicula.objects.filter(titulo__contains=parametro) 
    lista_categorias = Categoria.objects.all()   
    contexto = {
        'busca' : busca,
        'lista_categorias': lista_categorias,
    }
    return render(request, 'app/BuscarPeli.html', contexto)


#REGISTRO DE USUARIO

def from_registro(request):
    return render(request, 'app/form_reg.html') 

def registrar(request):
    # Obtiene los datos
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
 
    # Crea el objeto usuario
    usuario = User(username=username, first_name=firstname, last_name=lastname, email=email, password=password, is_superuser=False)
    usuario.set_password(password)
    # Guarda el usuario en la base de datos
    usuario.save()
 
    return redirect('app:form_login')


#MUESTRA PELICULA

def ver_pelicula(request):
    lista_categorias = Categoria.objects.all()
    id_pelicula = request.POST['pelicula']
    pelicula = Pelicula.objects.get(id=id_pelicula)

    #categorias
    filtro = PeliculaCategoria.objects.filter(pelicula_id=id_pelicula)
    categorias_pelicula = []
    for ob in filtro:
        cat_d = ob.categoria_id
        categ = Categoria.objects.get(id=cat_d)
        categorias_pelicula.append(categ)


    #calificacion
    peli_cal_id = Calificacion.objects.filter(pelicula_id=id_pelicula)
    suma=0
    i = 0
    lista_valores = []
    for calificacion in peli_cal_id:
        a = calificacion.valor
        lista_valores.append(a)
        i += 1
    if i is not 0:
        suma = sum(lista_valores)
        promedio = suma/i
    else:
        promedio = 0
    

    #comentarios
    comentarios = Comentario.objects.filter(pelicula_id=id_pelicula)
    
    
    contexto = {
        'lista_categorias': lista_categorias,
        'pelicula': pelicula,
        'suma':suma,
        'promedio': promedio,
        'comentarios' : comentarios,
        'categorias_pelicula': categorias_pelicula,
        
    }
    return render(request, 'app/Pelicula.html', contexto) 


#Comentar una pelicula
def comentar(request):
    comentario = request.POST['comment']
    usuario = request.user.id
    pelicula = request.POST['peli_id']

    com = Comentario(texto=comentario, usuario_id=usuario, pelicula_id=pelicula, activo=True)

    com.save()

    return redirect('app:index')

#calificar pelicula
def califica_peli(request):
    calificacion = request.POST['options']
    usuario_id = request.user.id
    pelicula_id = request.POST['peli_id']

    new_cal = Calificacion(valor=calificacion, pelicula_id=pelicula_id, usuario_id=usuario_id)
    new_cal.save()

    return redirect('app:index')

#cambiar estado comentario
def cambiar_est_com(request):
    id_comment = request.POST['com_id']
    estado = bool(request.POST['cambio'])
    
    t_com = Comentario.objects.get(id=id_comment)
    t_com.activo = estado
    t_com.save()

    return redirect('app:index')

#editar pelicula
def edit_peli(request):
    titulo = request.POST['title']
    year = request.POST['year']
    sinopsis = request.POST['synopsis']
    protagonistas = request.POST['protagonist']
    duracion = request.POST['duration']
    en_cartel = bool(request.POST['billboard'])
    pelicula = request.POST['peli_id']

    peli = Pelicula.objects.get(id=pelicula)

    peli.titulo = titulo
    peli.anio = year
    peli.sinopsis = sinopsis
    peli.actores = protagonistas
    peli.duracion = duracion
    peli.enCartelera = en_cartel

    peli.save()

    return redirect('app:index')

#agregar categorias
def agrega_categoria(request):
    categoria = request.POST['categoria']
    pelicula_id = request.POST['peli_id']
    
    if categoria is not None:
        crea = PeliculaCategoria(pelicula_id=pelicula_id, categoria_id=categoria)
    crea.save()
    
    return redirect('app:index')




#CONFIGURACION DEL ADMINISTRADOR
@login_required
def administradorConf(request):

    lista_peliculas = Pelicula.objects.all()
    lista_categorias = Categoria.objects.all()

    contexto = {
        'lista_peliculas': lista_peliculas,
        'lista_categorias': lista_categorias
    }
    return render(request, 'app/administrador/Configuracion.html', contexto)


#REGISTRO DE ADMINISTRADOR
@login_required
def form_admin(request):
    return render(request, 'app/administrador/form_admin.html') 

def registrar_admin(request):
    # Obtiene los datos
    username = request.POST['username']
    firstname = request.POST['first_name']
    lastname = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
 
    # Crea el objeto usuario
    usuario = User(username=username, first_name=firstname, last_name=lastname, email=email, password=password, is_superuser=True)
    usuario.set_password(password)
    # Guarda el usuario en la base de datos
    usuario.save()
 
    return redirect('app:administradorConf')


#LOGIN

def form_login(request):
    return render(request, 'app/form_login.html')


def autenticar(request):
     # Obtiene los datos del formulario de autenticación
    tipo = bool(request.POST['is_superuser'])
    username = request.POST['username']
    password = request.POST['password']

 
    # Obtiene el usuario
    usuario = authenticate(request, username=username, password=password, is_superuser=tipo)
 
    # Verifica si el usuario existe en la base de datos
    # 
    if usuario is not None:

        if tipo == True and usuario.is_superuser:

            login(request, usuario)
            return redirect('app:index')
                
        elif tipo == True and not usuario.is_superuser:

            return redirect('app:form_login')
                
        elif tipo == False and usuario.is_superuser:

            return redirect('app:form_login')
            
        elif tipo == False and not usuario.is_superuser:

            login(request, usuario)
            return redirect('app:index')
           
        else:
            return redirect('app:form_login')
    else:
        return redirect('app:form_login')


#LOGOUT

def view_logout(request):
  # Cierra la sesión del usuario
  logout(request)
 
  # Redirecciona la página de login
  return redirect('app:form_login')



#CREAR CATEGORIA
@login_required
def form_crea_categoria(request):
    return render(request, 'app/administrador/CrearCat.html')


def CreaCat(request):
    nombre_categoria = request.POST['nombre']
    newcategoria = Categoria(nombre= nombre_categoria)
    newcategoria.save()

    return redirect('app:form_crea_categoria')


#CREAR PELICULAS
@login_required
def form_crea_peliculas(request):
    return render(request, 'app/administrador/CrearPeli.html')


def CreaMov(request):
    peli_titulo = request.POST['titulo']
    peli_sinopsis = request.POST['sinopsis']
    peli_anio = int(request.POST['anio'])
    peli_actores = request.POST['actores']
    peli_duracion = int(request.POST['duracion'])
    peli_enCartelera = bool(request.POST['enCartelera'])
    new_pelicula = Pelicula(titulo=peli_titulo, sinopsis=peli_sinopsis, anio=peli_anio, actores=peli_actores, duracion=peli_duracion, enCartelera=peli_enCartelera)
    new_pelicula.save()

    return redirect('app:form_crea_peliculas')
    #return HttpResponse(peli_titulo)