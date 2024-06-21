from django.shortcuts import render, redirect
# from .models import Login,Answer
from gradio_client import Client
from .forms import HadithForm
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Answer
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Answer, Login

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render, HttpResponse
from .models import Answer, Login




from django.shortcuts import render
# from .models import Login

def home(request):
    return_url = request.session.pop('return_url', None)
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Check if email already exists in the database
        if Login.objects.filter(email=email).exists():
            messages.error(request,'email is elready exist')
            return render(request, 'home/home.html', {'error_message': 'Email already exists.'})
        
        # Save the new user if email is unique
        if username and email and password:
            data = Login(name=username, email=email, password=password)
            data.save()
            return render(request, 'home/home.html')
        else:
            return render(request, 'home/home.html', {'error_message': 'Please provide all required fields.'})
    else:
        return render(request, 'home/home.html' ,{'return_url': return_url})






def intermediate(request):




     return render(request, 'home/intermediate.html' )




def loginUser(request ):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        logins=Login.objects.all()
     

        user = Login.objects.filter(email=email, password=password).first()
        if user is not None:

            request.session['user_email'] = user.email
            return render(request, 'home/intermediate.html' )
            # return redirect('intermediate')
            # return redirect('answer')

        else:
             request.session['return_url'] = 'Invalid email or password.'
             return redirect('home')  # استخدم redirect بدلاً من render هنا
            
            # # Login failed
            # return render(request, 'home/home.html', {'return_url': 'Invalid email or password.'})
            # # return redirect('login')
    else:
        return render(request, 'home/home.html')





def predict(request):
    return render(request, 'predict/predict.html')






from gradio_client import Client

def answer(request):
    if request.method == 'POST':
        question_text = request.POST.get('question', '')
        user_email = request.session.get('user_email')

        if user_email:
            try:
                user = Login.objects.get(email=user_email)
            except Login.DoesNotExist:
                return HttpResponse("User does not exist.")  
        else:
            return HttpResponse("You need to log in to ask questions.")

  
        client = Client("Mohamed-Maher/Hadith-QA-System")
        result = client.predict(
            question=question_text,
            api_name="/predict"
        )


        answer = Answer.objects.create(
            question_text=question_text,
            answer_text=result,
            login=user  
        )

        posts = Answer.objects.filter(login=user)
        return render(request, 'home/chat.html', {'posts': posts})
    else:
        user_email = request.session.get('user_email')
        if user_email:
            try:
                user = Login.objects.get(email=user_email)
            except Login.DoesNotExist:
                return HttpResponse("User does not exist.")  

            posts = Answer.objects.filter(login=user)
        else:
            posts = Answer.objects.none() 

        return render(request, 'home/chat.html', {'posts': posts})





def delete_chat(request):
    user_email = request.session.get('user_email')

    if user_email:
        try:
            user = Login.objects.get(email=user_email)
            Answer.objects.filter(login=user).delete()
            messages.success(request, 'All chat messages have been deleted.')
        except Login.DoesNotExist:
            messages.error(request, 'User does not exist.')
    else:
        messages.error(request, 'You need to log in to delete chat messages.')

    return redirect('answer')

def haraka(request):
     return render(request, 'home/intermediate.html')