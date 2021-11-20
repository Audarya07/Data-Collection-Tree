from django.urls import path
from .views import default, insert, query

urlpatterns = [
    path("", default, name="default"),
    path("insert/", insert, name="insert"),
    path("query/", query, name="query"),
]
