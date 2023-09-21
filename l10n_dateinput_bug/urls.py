from django.contrib import admin
from django.urls import path, include

from book_store.views import create_book

urlpatterns = [
    path("book/create/", create_book, name="create-book"),
    path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
]
