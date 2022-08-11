from django.shortcuts import render, redirect
from django.http import HttpResponse
from googletrans import Translator
from gtts import gTTS  
from playsound import playsound  

# Create your views here.

def home(request):
     return render(request,'home.html')

def translate(request):
    if request.method == "POST":
        lang1 = request.POST.get("lang", None)
        txt = request.POST.get("text1", None)
        translator = Translator()
        tr = translator.translate(txt, dest=lang1)
        obj=tr.text
        ob = gTTS(text=obj, lang=lang1, slow=False)  
        ob.save("static/audio/exam.mp3")  
        return render(request, 'home.html', {"result":obj})
    else:
       return render(request,'home.html')

