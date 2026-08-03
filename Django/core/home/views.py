from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def home(request):
    return render(request,"index.html")
def succesful_page(request):
    return HttpResponse('''<h1>This is a Success page Thanks for coming</h>
                        <br>
                        <h3>This page is create in django
                        ''')
def css_file(request):
    return HttpResponse('''
                        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>icon</title>
    <!-- <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,400,0,0&icon_names=person" /> -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&icon_names=search" />
</head>
<body>
    <span class="material-symbols-outlined">
person
</span>
<span class="material-symbols-outlined">
search
</span>
</body>
</html>
''')