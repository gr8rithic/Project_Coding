from django.shortcuts import render
from django.http import HttpResponse
import pyttsx3 as p
import pywhatkit as pwk 
# Create your views here.

def hel(request):
	p.speak("This is a website owned by Rithic")
	return render(request, "first/h.html")

def add(request):
	language = request.GET['num1']
	syntax = request.GET['num2']
	yesno = request.GET["num3"]
	if yesno =="Y" or yesno=="y":
		p.speak("So you want youtube videos on"+""+language+""+"and"+""+syntax)
		pwk.playonyt(language+" "+syntax)
		return render(request, 'first/h2.html',{'lang':language,'syn':syntax})
	elif yesno =="N" or yesno =="n":
		p.speak("So you want textual document on"+""+language+""+"and"+""+syntax)
		pwk.search(language+" "+syntax)
		return render(request,'first/h3.html',{'lang':language,'syn':syntax})
	else:
		return render(request,'first/error.html')