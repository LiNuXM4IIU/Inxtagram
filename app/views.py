
from django.shortcuts import render,redirect

def main(request):
 print(request.GET)
 return render(request, "app.html")

def com(request):
 return redirect("https://www.instagram.com/p/CCvhPD8pHPmTWeIWMpzm055Qf3UVIbpYdfKA_U0/?igshid=wsdgttq8dt9s")