# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import StreamingHttpResponse
from .models import Herbs,Herbstype,Pres,Prestype,Achs,herb_sel,pres_sel,achs_sel,file_open
# from itertools import chain


def whole_list(request):
    context = {}
    # whole_herbs = Herbs.objects.all()#传入
    # whole_press = Pres.objects.all()#传入
    # whole_achss = Achs.objects.all()#传入
    # context['wholes'] = chain(whole_herbs,whole_press,whole_achss)
    context['whole_herbs'] = Herbs.objects.order_by('-created_time')[:3]#传入
    context['whole_press'] = Pres.objects.order_by('-created_time')[:3]#传入
    context['whole_achss'] = Achs.objects.order_by('-created_time')[:3]#传入
    context['herb_types'] = Herbstype.objects.all()
    context['pres_types'] = Prestype.objects.all()
    herbs_count = Herbs.objects.all().count()#传入
    pres_count = Pres.objects.all().count()#传入
    achs_count = Achs.objects.all().count()#传入
    context['count'] = int(herbs_count)+int(pres_count)+int(achs_count)

    return render(request,'herb/whole_list.html',context)

def selpage(request):
    context = {}
    herb = herb_sel.objects.last()
    pres = pres_sel.objects.last()
    achs = achs_sel.objects.last()
    context['herb_sel'] = Herbs.objects.filter(title = herb.herb_title )[:1]
    context['pres_sel'] = Pres.objects.filter(title = pres.pres_title )[:1]
    context['achs_sel'] = Achs.objects.filter(title = achs.achs_title )[:1]
    context['herb'] = Herbs.objects.last()
    context['pres'] = Pres.objects.last()
    context['achs'] = Achs.objects.last()

    return render(request,'herb/selpage.html',context)


def herb_detail(request,herb_pk):
    context = {}
    context['herb_detail'] = get_object_or_404(Herbs,pk=herb_pk)#传入
    context['herb_types'] = Herbstype.objects.all()
    context['pres_types'] = Prestype.objects.all()
    return render(request,'herb/herb_detail.html',context)

def pres_detail(request,pres_pk):
    context = {}
    context['pres_detail'] = get_object_or_404(Pres,pk=pres_pk)#传入
    context['herb_types'] = Herbstype.objects.all()
    context['pres_types'] = Prestype.objects.all()
    return render(request,'herb/pres_detail.html',context)

def achs_detail(request,achs_pk):
    context = {}
    context['achs_detail'] = get_object_or_404(Achs,pk=achs_pk)#传入
    context['herb_types'] = Herbstype.objects.all()
    context['pres_types'] = Prestype.objects.all()
    return render(request,'herb/achs_detail.html',context)

def herbs_with_type(request,herb_type_pk):
    context = {}
    herb_type = get_object_or_404(Herbstype,pk=herb_type_pk)
    context['herbs'] = Herbs.objects.filter(Herbs_type=herb_type)#传入
    context['herb_type'] = herb_type#传入
    context['herb_types'] = Herbstype.objects.all()
    context['pres_types'] = Prestype.objects.all()
    return render(request,'herb/herb_with_type.html',context)

def pres_with_type(request,pres_type_pk):
    context = {}
    pres_type = get_object_or_404(Prestype,pk=pres_type_pk)
    context['press'] = Pres.objects.filter(Pres_type=pres_type)#传入
    context['pres_type'] = pres_type#传入
    context['herb_types'] = Herbstype.objects.all()
    context['pres_types'] = Prestype.objects.all()
    return render(request,'herb/pres_with_type.html',context)

def achs_list(request):
    context = {}
    context['achss'] = Achs.objects.all()#传入
    context['herb_types'] = Herbstype.objects.all()
    context['pres_types'] = Prestype.objects.all()
    return render(request,'herb/achs_list.html',context)

def file_list(request):
    context = {}
    context['files'] = file_open.objects.all()
    context['herb_types'] = Herbstype.objects.all()
    context['pres_types'] = Prestype.objects.all()
    return render(request,'herb/file_list.html',context)

def file_download(request,file_pk):
    context = {}
    download_name = file_open.objects.get(pk=file_pk)
    context['filelink'] = 'D:/360MoveData/Users/Administrator/Desktop/Herb_env/mysite/static/images/{}'.format(download_name.files)# 要下载的文件路径,服务器设置
    return render(request,'filelink.html',context)
