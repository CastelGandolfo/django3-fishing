from django.contrib import admin
from .models import Product, About, Contact, HomeInfo
# Register your models here.
# class AuthorAdmin(admin.ModelAdmin):
    # exclude  = ('progress', 'checkpoint_count', 'eplan_count', 'device_count', 'user_edited', 'user_verified')


admin.site.register(Product)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(HomeInfo)