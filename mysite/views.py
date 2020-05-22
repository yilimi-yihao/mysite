from django.shortcuts import render
from herb.models import Herbs,Pres,Achs,home_line


def home(request):
    context = {}
    home_line_1 = home_line.objects.get(pk=1)
    context['herbs'] = Herbs.objects.filter(title = home_line_1.herb_title)[:1]
    context['press'] = Pres.objects.filter(title = home_line_1.pres_title)[:1]
    context['achss'] = Achs.objects.filter(title = home_line_1.achs_title)[:1]
    return render(request,'home.html',context)

