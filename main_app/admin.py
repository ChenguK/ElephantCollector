from django.contrib import admin
from .models import Elephant, Care, Trainer

# Register your models here.

admin.site.register(Elephant)
admin.site.register(Care)
admin.site.register(Trainer)