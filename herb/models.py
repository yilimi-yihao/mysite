from django.db import models

# Create your models here.

#草药类型
class Herbstype(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

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

#药方类型
class Prestype(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

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

#成果
class Achs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='achs')
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "<Achs:%s>" % self.title

#首页列表
class home_line(models.Model):
    herb_title = models.CharField(max_length=50)
    pres_title = models.CharField(max_length=50)
    achs_title = models.CharField(max_length=50)

class herb_sel(models.Model):
    herb_title = models.CharField(max_length=50)

class pres_sel(models.Model):
    pres_title = models.CharField(max_length=50)

class achs_sel(models.Model):
    achs_title = models.CharField(max_length=50)

class file_open(models.Model):
    title = models.CharField(max_length=50)
    files = models.FileField( upload_to="up_file",blank=True,null=True,verbose_name="上传文件" )
    class Meta():
        verbose_name = "上传文件"
        verbose_name_plural = verbose_name    




