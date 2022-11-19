from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from index.models import profile, testimonial, Resume, resumetitle, myfield, client, myskills


def index(request):
    pro = profile.objects.get(email='azeezadedeji638@gmail.com')
    title = None
    context = None
    test = testimonial.objects.all()
    desu = Resume.objects.all().count()
    cli = client.objects.all()
    resu = Resume.objects.get(id=1)

    rrs = resu.resumetitle_set.all()

    field = myfield.objects.all()
    skills = myskills.objects.all()
    if request.method == 'POST':
        mail = request.POST.get('email')
        name = request.POST.get('fullname')
        message = request.POST.get('message')
        send_mail(subject=name, message=message + "\n" + "This is my email address: " + mail,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=['azeezadedeji638@gmail.com'])

    context = {'profiles': pro,
               'test': test,
               'rrs': rrs,
               'resu': resu,
               "client": cli,
               'field': field,
               'skills': skills

               }
    return render(request, 'index/index.html', context)
