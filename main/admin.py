from django.contrib import admin
from .models import QuranReg, TajweedReg, EgazatReg
 
@admin.register(QuranReg)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in QuranReg._meta.get_fields()]

@admin.register(TajweedReg)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in QuranReg._meta.get_fields()]

@admin.register(EgazatReg)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in QuranReg._meta.get_fields()]