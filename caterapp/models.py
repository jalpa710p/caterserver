from django.db import models


class Menu(models.Model):
    image = models.ImageField(upload_to='menu/')


class About(models.Model):
    image = models.ImageField(upload_to='about/')


class AboutFeature(models.Model):
    feature = models.CharField(max_length=100)


class CountAbout(models.Model):
    icon = models.CharField(max_length=50)
    numbers = models.IntegerField()
    count_name = models.CharField(max_length=50)

# service_models
class Service(models.Model):
    icon = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    service_desc = models.CharField(max_length=100)


# event_models
class Event(models.Model):
    image = models.ImageField(upload_to='event/')
    imgtype = models.CharField(max_length=50)


class Wedding(models.Model):
    image = models.ImageField(upload_to='event/')
    imgtype = models.CharField(max_length=50)


class Corporate(models.Model):
    image = models.ImageField(upload_to='event/')
    imgtype = models.CharField(max_length=50)


class Cocktail(models.Model):
    image = models.ImageField(upload_to='event/')
    imgtype = models.CharField(max_length=50)


class Buffet(models.Model):
    image = models.ImageField(upload_to='event/')
    imgtype = models.CharField(max_length=50)

# menu_models
class MenuStarter(models.Model):
    image = models.ImageField(upload_to=('Menu'))
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuMain(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuDrinks(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuOffers(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)


class MenuSpecial(models.Model):
    image = models.ImageField(upload_to='Menu/')
    food_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    food_desc = models.CharField(max_length=100)



class Booking(models.Model):
    image = models.ImageField(upload_to='book/')


class ChefAbout(models.Model):
    image = models.ImageField(upload_to='chefabout/')
    chef_name = models.CharField(max_length=50)
    chef_type = models.CharField(max_length=50)


class ServiceCustomers(models.Model):
    image = models.ImageField(upload_to='Service/')
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    review = models.TextField()


# blogmodels
class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    test = models.CharField(max_length=50)


# contactmodels
class Contact(models.Model):
    address = models.CharField(max_length=100)
    email1 = models.EmailField()
    email2 = models.EmailField()
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50)


