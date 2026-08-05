from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def home(request):
    
    students = [
        "Naruto",
        "Luffy",
        "Zoro",
        "Itachi",
        "Gojo"
    ]

    return render(request,"index.html",context={"students":students})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def fruit(request):
    fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes"
]
    nums = [
        1,2,3,4,5
    ]
    return render(request,"fruit.html",context={"fruits":fruits,"nums":nums})
    
def succesful_page(request):
    return HttpResponse('''<h1>This is a Success page Thanks for coming</h>
                        <br>
                        <h3>This page is create in django
                        ''')
def filtter(request):
    context = {
        "name" : "inzamam",
        "nname" : "Naruto",
        "lname" : "monkey D. luffy"
        }
    return render(request,"filtter.html",context=context)
