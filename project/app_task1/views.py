from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.http import HttpResponse
from .forms import RegistrationForm

# Create your views here.
# функция для компановки всего вместе с базами данных
def database(request):
    # подключение моделей из базы данных и сохранение
    Buyers = Buyer.objects.all()
    Games = Game.objects.all()

    context = {
        'Buyers':Buyers,
        'Games':Games
    }

    return render(request, 'database.html', context)





# Create your views here
# функции для отображения рядовых страниц
def index_cart(request):
    return render(request, 'cart.html')

def index_primary(request):
    return render(request, 'primary.html')

def index_store(request):
    games = Game.objects.all()
    context = {'games' : games}
    return render(request, 'store.html', context)






# Create your views here
# функции для регистрации пользователей      
def sign_up(request):
    users = Buyer.objects.all()
    info = {}
    context = {'info':info,
               'users':users
               }
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration.html', context)
            if int(age) < 18:
                info['error'] = 'Вы несовершеннолетний'
                return render(request, 'registration.html', context)
            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Такой пользователь уже существует'
                return render(request, 'registration.html', context)
            else:
                Buyer.objects.create(name=username, age=age)
                return HttpResponse("Регистрация прошла успешно!")
                
    else:
        form = RegistrationForm()     
    return render(request, 'registration.html', context)




  
        
    
  
      




