from django.db import models
from django.db.models.signals import pre_delete #删除文件
from django.dispatch.dispatcher import receiver #删除文件

# Create your models here.

#草药类型
class Herbstype(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name
    class Meta():
        verbose_name = "香药类型"
        verbose_name_plural = verbose_name 

#草药
class Herbs(models.Model):
    title = models.CharField(max_length=50)
    Herbs_type = models.ForeignKey(Herbstype,on_delete=models.DO_NOTHING) 
    content = models.TextField()
    image = models.ImageField(upload_to='herbs')
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Herb:%s>" % self.title

    class Meta():
        verbose_name = "香药"
        verbose_name_plural = verbose_name

@receiver(pre_delete, sender=Herbs)
def download_delete(instance, **kwargs):
    instance.image.delete(False)


#药方类型
class Prestype(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

    class Meta():
        verbose_name = "药方类型"
        verbose_name_plural = verbose_name 

#药方
class Pres(models.Model):
    title = models.CharField(max_length=50)
    Pres_type = models.ForeignKey(Prestype,on_delete=models.DO_NOTHING) 
    content = models.TextField()
    image = models.ImageField(upload_to='pres')
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Pres:%s>" % self.title


    class Meta():
        verbose_name = "药方"
        verbose_name_plural = verbose_name 

@receiver(pre_delete, sender=Pres)
def download_delete(instance, **kwargs):
    instance.image.delete(False)


#成果
class Achs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='achs')
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "<Achs:%s>" % self.title

    class Meta():
        verbose_name = "成果"
        verbose_name_plural = verbose_name 


@receiver(pre_delete, sender=Achs) #sender=要删除或修改文件字段所在的类
def download_delete(instance, **kwargs):
    instance.image.delete(False) #file是保存文件或图片的字段名

#首页列表
class home_line(models.Model):
    herb_title = models.CharField(max_length=50)
    pres_title = models.CharField(max_length=50)
    achs_title = models.CharField(max_length=50)

    class Meta():
        verbose_name = "首页列表"
        verbose_name_plural = verbose_name 

class herb_sel(models.Model):
    herb_title = models.CharField(max_length=50)

    class Meta():
        verbose_name = "精选页面列表之香药（名字即可）"
        verbose_name_plural = verbose_name 

class pres_sel(models.Model):
    pres_title = models.CharField(max_length=50)

    class Meta():
        verbose_name = "精选页面列表之药方（名字即可）"
        verbose_name_plural = verbose_name     

class achs_sel(models.Model):
    achs_title = models.CharField(max_length=50)
    class Meta():
        verbose_name = "精选页面列表之成果（名字即可）"
        verbose_name_plural = verbose_name 


class file_open(models.Model):
    title = models.CharField(max_length=50)
    files = models.FileField( upload_to="up_file",blank=True,null=True,verbose_name="上传文件" )
    class Meta():
        verbose_name = "上传文件"
        verbose_name_plural = verbose_name  

@receiver(pre_delete, sender=file_open)
def download_delete(instance, **kwargs):
    instance.files.delete(False) 






