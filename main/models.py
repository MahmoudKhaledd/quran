from django.db import models
 
class QuranReg(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    quota = models.CharField(max_length=200)

class TajweedReg(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    quota = models.CharField(max_length=200)

class EgazatReg(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=200)
    quota = models.CharField(max_length=200)