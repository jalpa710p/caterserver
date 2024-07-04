"""
URL configuration for caterserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from caterapp.views import *
    # MenuViewSet, AboutViewSet, AboutFeatureViewSet, CountAboutViewSet, ServiceViewSet,
    # EventViewSet, WeddingViewSet, CorporateViewSet, CocktailViewSet, BuffetViewSet,
    # MenuStarterViewSet, MenuMainViewSet, MenuDrinksViewSet, MenuOffersViewSet,
    # MenuSpecialViewSet, BookingViewSet, ChefAboutViewSet, ServiceCustomersViewSet,
    # BlogViewSet, ContactViewSet


router = DefaultRouter()
router.register(r'menus', MenuViewSet)
router.register(r'abouts', AboutViewSet)
router.register(r'about-features', AboutFeatureViewSet)
router.register(r'count-abouts', CountAboutViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'events', EventViewSet)
router.register(r'weddings', WeddingViewSet)
router.register(r'corporates', CorporateViewSet)
router.register(r'cocktails', CocktailViewSet)
router.register(r'buffets', BuffetViewSet)
router.register(r'menu-starters', MenuStarterViewSet)
router.register(r'menu-mains', MenuMainViewSet)
router.register(r'menu-drinks', MenuDrinksViewSet)
router.register(r'menu-offers', MenuOffersViewSet)
router.register(r'menu-specials', MenuSpecialViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'chef-abouts', ChefAboutViewSet)
router.register(r'service-customers', ServiceCustomersViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('caterapp.urls'), name='caterapp'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
