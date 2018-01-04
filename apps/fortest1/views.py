from django.shortcuts import render

# Create your views here.



def testpage(request):
    return render(request,'test.html')


def login(requests):
    return render(requests,'login.html')