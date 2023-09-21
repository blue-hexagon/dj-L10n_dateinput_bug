from django.contrib import admin

from book_store.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "borrowed_from_date", "borrowed_to_date")
    list_display_links = ("title",)

