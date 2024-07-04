from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'image']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'image']

class AboutFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutFeature
        fields = ['id', 'feature']


class CountAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountAbout
        fields = ['id', 'icon', 'numbers','count_name']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'icon', 'service_name', 'service_desc']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'image', 'imgtype']


class WeddingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wedding
        fields = ['id', 'image', 'imgtype']


class CorporateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate
        fields = ['id', 'image', 'imgtype']


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ['id', 'image', 'imgtype']


class BuffetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buffet
        fields = ['id', 'image', 'imgtype']


class MenuStarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuStarter
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class MenuMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuMain
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class MenuDrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuDrinks
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class MenuOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuOffers
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class MenuSpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuSpecial
        fields = ['id', 'image', 'food_name', 'price', 'food_desc']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'image']


class ChefAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChefAbout
        fields = ['id', 'image', 'chef_name', 'chef_type']


class ServiceCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCustomers
        fields = ['id', 'image', 'name', 'profession', 'review']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'image', 'date', 'month', 'test']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'address', 'email1', 'email2', 'phone1', 'phone2']


