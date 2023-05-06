from django.contrib import admin
from lada.models import Lada
@admin.register(Lada)
class LadaAdmin(admin.ModelAdmin):
    list_display = ['id','Anno','Marca','Color','Combustible','NumPuertas','Traccion']
