from django.contrib import admin
from .models import *


@admin.register(Menu)
class MenuImage(admin.ModelAdmin):
    list_display = ['image']


@admin.register(About)
class AboutImage(admin.ModelAdmin):
    list_display = ['image']


@admin.register(AboutFeature)
class Features(admin.ModelAdmin):
    list_display = ['feature']


@admin.register(CountAbout)
class CountInfo(admin.ModelAdmin):
    list_display = ['icon', 'numbers', 'count_name']


# service_admin
@admin.register(Service)
class ServiceInfo(admin.ModelAdmin):
    list_display = ['icon', 'service_name', 'service_desc']


# event_admin
@admin.register(Event)
class AllEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


@admin.register(Wedding)
class WeddingEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


@admin.register(Corporate)
class CorporateEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


@admin.register(Cocktail)
class CocktailEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


@admin.register(Buffet)
class BuffetEvent(admin.ModelAdmin):
    list_display = ['image', 'imgtype']


# menu_admin
@admin.register(MenuStarter)
class Starter(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuMain)
class MainCourse(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuDrinks)
class Drinks(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


# bookadmin
@admin.register(Booking)
class BookForm(admin.ModelAdmin):
    list_display = ['image']


@admin.register(MenuOffers)
class Offers(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(MenuSpecial)
class Special(admin.ModelAdmin):
    list_display = ['image', 'food_name', 'price', 'food_desc']


@admin.register(ChefAbout)
class ChefInfo(admin.ModelAdmin):
    list_display = ['image', 'chef_name', 'chef_type']


@admin.register(ServiceCustomers)
class CustomersInfo(admin.ModelAdmin):
    list_display = ['image', 'name', 'profession', 'review']


# blogadmin
@admin.register(Blog)
class BlogInfo(admin.ModelAdmin):
    list_display = ['image', 'date', 'month', 'test']


# Contactadmin
@admin.register(Contact)
class ContactInfo(admin.ModelAdmin):
    list_display = ['address', 'email1', 'email2', 'phone1', 'phone2']


