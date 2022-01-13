from django.urls import path
from .views import FirstFormView, NextFormView, ResultView, LastFormView, UpdateDB


urlpatterns = [
    path('',FirstFormView.as_view(), name='first-form'),
    path('next_form/', NextFormView.as_view(), name='next-form'),
    path('last_form/', LastFormView.as_view(), name='last-form'),
    path('result/', ResultView.as_view(), name='result-view'),
    path('update/', UpdateDB.as_view(), name='updatedb-view'),
]
