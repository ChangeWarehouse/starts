from django.db import models


# Create your models here.
class User(models.Model):
    pid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=256, verbose_name='用户名', blank=True,null=True)
    name = models.CharField(max_length=256, verbose_name='姓名', blank=True,null=True)
    phone = models.CharField(max_length=256, verbose_name='手机号', blank=True,null=True)
    password = models.CharField(max_length=256, verbose_name='密码', blank=True,null=True)

    def __str__(self):
        return self.username


class Pictures(models.Model):
    url = models.CharField(max_length=1042, verbose_name='地址', blank=True,null=True)
    text = models.CharField(max_length=256, verbose_name='描述', blank=True,null=True)
    time_create = models.DateField('创建时间',default=None, help_text="格式yyyy-mm-dd")
    time_update = models.DateField('更新时间', auto_now_add=True, help_text="格式yyyy-mm-dd")
    sex_type = (('all', '全部'), ('phone', '手机端'),('PC', 'PC端'))
    type = models.CharField("图片类型", choices=sex_type, max_length=256, default='male', blank=True, null=True)  # all phone pc
    _status = models.CharField(max_length=256, blank=True,null=True)
    copyright_type = (('legal', '正版'), ('pirate', '盗版'))
    copyright = models.CharField("版权", choices=copyright_type, max_length=256, default='male', blank=True, null=True)  # 版权


class Videos(models.Model):
    url = models.CharField(max_length=1042, verbose_name='地址', blank=True,null=True)
    text = models.CharField(max_length=256, verbose_name='描述', blank=True,null=True)
    time_create = models.DateField('创建时间', default=None, help_text="格式yyyy-mm-dd")
    time_update = models.DateField('更新时间', auto_now_add=True, help_text="格式yyyy-mm-dd")
    sex_type = (('all', '全部'), ('phone', '手机端'), ('PC', 'PC端'))
    type = models.CharField("图片类型", choices=sex_type, max_length=256, default='male', blank=True, null=True)  # all phone pc
    _status = models.CharField(max_length=256, blank=True,null=True)  # 删除状态
    copyright_type = (('legal', '正版'), ('pirate', '盗版'))
    copyright = models.CharField("版权", choices=copyright_type, max_length=256, default='male', blank=True, null=True)   # 版权   正版:legal  盗版:pirate

