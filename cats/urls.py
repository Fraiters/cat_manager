from django.urls import path
from .views import *

urlpatterns = [
    path(r'cats/', ShowCatList.as_view(), name='cats'),
    path(r'cats/add_cat/', AddCat.as_view(), name='add_cat'),
    path(r'cats/<slug:cat_slug>/', ShowCat.as_view(), name='cat_id'),
    path(r'cats/<slug:cat_slug>/upd_cat/', UpdateCat.as_view(), name='upd_cat'),
    path(r'cats/<slug:cat_slug>/del_cat/', DeleteCat.as_view(), name='del_cat'),

    path(r'register/', RegisterUser.as_view(), name='register'),
    path(r'login/', LoginUser.as_view(), name='login'),
    path(r'logout/', logout_user, name='logoutt'),
]
