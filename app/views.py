from django.shortcuts import render

# Create your views here.
def html1(request):
    return render(request,'html1.html')

def html2(request):
    return render(request,'html2.html')

def html3(request):
    return render(request,'html3.html')

def html4(request):
    return render(request,'html4.html')          