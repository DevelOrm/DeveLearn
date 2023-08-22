from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def main(request):
    return render(request, 'test.html')