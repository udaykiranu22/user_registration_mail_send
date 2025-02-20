from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

def registration(request):
    EUMFO = UserMF()
    EPMFO = ProfileMF()
    d = {'EUMFO': EUMFO, 'EPMFO': EPMFO}
    if request.method == 'POST' and request.FILES:
        NMUMFDO = UserMF(request.POST)
        NMPMFDO = ProfileMF(request.POST, request.FILES)
        if NMUMFDO.is_valid() and NMPMFDO.is_valid():
            MUMFDO = NMUMFDO.save(commit=False)
            password1 = NMUMFDO.cleaned_data['password']
            MUMFDO.set_password(password1)
            MUMFDO.save()

            MPMFDO = NMPMFDO.save(commit=False)
            MPMFDO.user_name = MUMFDO
            MPMFDO.save()
            send_mail('registration successfully', 'your registration is successfully done.','lordmax414@gmail.com',[MUMFDO.email], fail_silently = False)
            return HttpResponse('registration successfully done.')
        else:
            return HttpResponse('invaild data')
    return render(request, 'registration.html', d)
