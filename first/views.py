from django.shortcuts import render
from django.http import HttpResponse

def my_first(request):
    return render(
        request,
        'pages/index.html',
        {
            'dfd' : 'gfdgfgfdfgdgdfdsfgdfsdfsdgfsg',

            'ff' : ["title", "dsfsd", 111, 3453] 
                
        }   
    )
