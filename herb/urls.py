from django.urls import path
from . import views
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    # http://120.0.0.1:8000/herb
    path('',views.whole_list,name='whole_list'),
    # http://120.0.0.1:8000/herb/sel
    path('selpage', views.selpage, name='selpage'),
    # http://120.0.0.1:8000/herb/herb/1
    path('herb/<int:herb_pk>',views.herb_detail,name="herb_detail"),
    # http://120.0.0.1:8000/herb/pres/1   
    path('pres/<int:pres_pk>',views.pres_detail,name="pres_detail"),
    # http://120.0.0.1:8000/herb/achs/1
    path('achs/<int:achs_pk>',views.achs_detail,name="achs_detail"),
    # http://120.0.0.1:8000/herb/herbtype/1   
    path('herbtype/<int:herb_type_pk>',views.herbs_with_type,name="herbs_with_type"),
    # http://120.0.0.1:8000/herb/prestype/1   
    path('prestype/<int:pres_type_pk>',views.pres_with_type,name="pres_with_type"),
    # http://120.0.0.1:8000/herb/achstype
    path('achstype',views.achs_list,name="achs_list"),
    # http://120.0.0.1:8000/herb/file_list 
    path('file_list',views.file_list,name="file_list"),
    # http://120.0.0.1:8000/herb/file_list/1 
    path('file_list/<int:file_pk>',views.file_download,name="file_download"),
    
    url(r'^images/(?P<path>.*)$', serve, {'document_root': '../mysite/static/images'}), 
]