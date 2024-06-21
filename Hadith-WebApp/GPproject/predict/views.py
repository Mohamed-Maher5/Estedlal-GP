from django.shortcuts import render
from django.shortcuts import render, redirect
from gradio_client import Client
# Create your views here.



def predict(request):
    # predicted_label=" "
    result=" "
    if request.method == 'POST':
      question = request.POST.get("questionpredict")
      client = Client("Mohamed-Maher/Hadith_Classification")
      result = client.predict(
		input_text=question,
		api_name="/predict"
         )


    #   input_text=question
    #   predicted_label = predict_label(input_text)
      
   
    
    

    return render(request, 'predict/predict.html',{'predict': result})
    # return render(request, 'predict/predict.html',{'predict': predicted_label})


def haraka(request):
     return render(request, 'home/intermediate.html')



