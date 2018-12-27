from django.contrib import admin

from pizzas.models import Pizza, Entry

admin.site.register(Pizza)
admin.site.register(Entry)