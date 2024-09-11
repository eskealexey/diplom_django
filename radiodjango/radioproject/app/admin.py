from django.contrib import admin
from app.models import Transistor, TypeTransistor, KorpusTransistor

# Register your models here.
admin.site.register(Transistor)
admin.site.register(TypeTransistor)
admin.site.register(KorpusTransistor)