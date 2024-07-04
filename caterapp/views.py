from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutFeatureViewSet(viewsets.ModelViewSet):
    queryset = AboutFeature.objects.all()
    serializer_class = AboutFeatureSerializer


class CountAboutViewSet(viewsets.ModelViewSet):
    queryset = CountAbout.objects.all()
    serializer_class = CountAboutSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class WeddingViewSet(viewsets.ModelViewSet):
    queryset = Wedding.objects.all()
    serializer_class = WeddingSerializer


class CorporateViewSet(viewsets.ModelViewSet):
    queryset = Corporate.objects.all()
    serializer_class = CorporateSerializer


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer


class BuffetViewSet(viewsets.ModelViewSet):
    queryset = Buffet.objects.all()
    serializer_class = BuffetSerializer


class MenuStarterViewSet(viewsets.ModelViewSet):
    queryset = MenuStarter.objects.all()
    serializer_class = MenuStarterSerializer


class MenuMainViewSet(viewsets.ModelViewSet):
    queryset = MenuMain.objects.all()
    serializer_class = MenuMainSerializer


class MenuDrinksViewSet(viewsets.ModelViewSet):
    queryset = MenuDrinks.objects.all()
    serializer_class = MenuDrinksSerializer


class MenuOffersViewSet(viewsets.ModelViewSet):
    queryset = MenuOffers.objects.all()
    serializer_class = MenuOffersSerializer


class MenuSpecialViewSet(viewsets.ModelViewSet):
    queryset = MenuSpecial.objects.all()
    serializer_class = MenuSpecialSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ChefAboutViewSet(viewsets.ModelViewSet):
    queryset = ChefAbout.objects.all()
    serializer_class = ChefAboutSerializer


class ServiceCustomersViewSet(viewsets.ModelViewSet):
    queryset = ServiceCustomers.objects.all()
    serializer_class = ServiceCustomersSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# Create your views here.


def c404(request):
    return render(request, '404.html')


def about(request):
    image = About.objects.all()
    desc = AboutFeature.objects.all()
    chef_team = ChefAbout.objects.all()
    count = CountAbout.objects.all()
    return render(request, 'about.html', {'image': image, 'desc': desc, 'chef_team': chef_team, 'count': count})


def blog(request):
    blogdesc = Blog.objects.all()
    return render(request, 'blog.html', {'blogdesc': blogdesc})


def book(request):
    form = Booking.objects.all()
    return render(request, 'book.html', {'form': form})


def contact(request):
    contact = Contact.objects.all()
    return render(request, 'contact.html', {'contact': contact})


def event(request):
    all_event = Event.objects.all()
    wedding = Wedding.objects.all()
    corporate = Corporate.objects.all()
    cocktail = Cocktail.objects.all()
    buffet = Buffet.objects.all()
    return render(request, 'event.html', {'all_event': all_event,
                                          'wedding': wedding,
                                          'corporate': corporate,
                                          'cocktail': cocktail,
                                          'buffet': buffet})


def footer(request):
    # items = FooterItem.objects.all()
    return render(request, 'footer.html')


def index(request):
    menu = Menu.objects.all()
    image = About.objects.all()
    desc = AboutFeature.objects.all()
    count = CountAbout.objects.all()
    service = Service.objects.all()
    all_event = Event.objects.all()
    wedding = Wedding.objects.all()
    corporate = Corporate.objects.all()
    cocktail = Cocktail.objects.all()
    buffet = Buffet.objects.all()
    starter = MenuStarter.objects.all()
    main_course = MenuMain.objects.all()
    drinks = MenuDrinks.objects.all()
    offers = MenuOffers.objects.all()
    special = MenuSpecial.objects.all()
    form = Booking.objects.all()
    chef_team = ChefAbout.objects.all()
    customers = ServiceCustomers.objects.all()
    customerss = ServiceCustomers.objects.all()
    blogdesc = Blog.objects.all()
    return render(request, 'index.html', {'menu': menu,
                                          'image': image, 'desc': desc,
                                          'count': count,
                                          'service': service,
                                          'all_event': all_event,
                                          'wedding': wedding, 'corporate': corporate, 'cocktail': cocktail, 'buffet': buffet,
                                          'starter': starter, 'main_course': main_course, 'drinks': drinks,'offers': offers,'special': special,
                                          'form': form,
                                          'chef_team': chef_team,
                                          'customers': customers, 'customerss': customerss,
                                          'blogdesc': blogdesc})


def menu(request):
    starter = MenuStarter.objects.all()
    main_course = MenuMain.objects.all()
    drinks = MenuDrinks.objects.all()
    offers = MenuOffers.objects.all()
    special = MenuSpecial.objects.all()
    return render(request, 'menu.html', {'starter': starter,
                                         'main_course': main_course,
                                         'drinks': drinks,
                                         'offers': offers,
                                         'special': special})


def service(request):
    service = Service.objects.all()
    customers = ServiceCustomers.objects.all()
    customerss = ServiceCustomers.objects.all()
    return render(request, 'service.html', {'service': service, 'customers': customers, 'customerss': customerss})


def team(request):
    chef_team = ChefAbout.objects.all()
    return render(request, 'team.html', {'chef_team': chef_team})


def testimonial(request):
    customers = ServiceCustomers.objects.all()
    customerss = ServiceCustomers.objects.all()
    return render(request, 'testimonial.html', {'customers': customers, 'customerss': customerss})


