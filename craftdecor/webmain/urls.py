from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products_cat/<int:cat_id>/', views.products_cat, name='products_cat'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('contact/', views.contact, name='contact'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)