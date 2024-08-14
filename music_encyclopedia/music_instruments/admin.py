from django.contrib import admin
from .models import Category, Country, People, Instrument

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(People)
admin.site.register(Instrument)

#регистрируем наши модели в админку