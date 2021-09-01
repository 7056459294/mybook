from django.urls import path
from . import views
urlpatterns = [
    path('',views.login, name='login'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('index/',views.index, name='index'),
    path('index1/',views.index1, name='index1'),
    path('signup/',views.signup, name='signup'),
    path('addbooks/',views.addbooks, name='addbooks'),
    path('deletebooks/',views.deletebooks, name='deletebooks'),
    path('modifybooks/',views.modifybooks, name='modifybooks'),
    path('soldbook/',views.soldbook, name='soldbook'),
    path('buybook/',views.buybook, name='buybook'),
]