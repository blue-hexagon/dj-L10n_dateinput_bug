from django.shortcuts import render, redirect

from book_store.forms import BookForm
from book_store.models import Book


def create_book(request):
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get("HTTP_REFERER", request.path_info))
        else:
            # Add message
            return redirect(request.META.get("HTTP_REFERER", request.path_info))
    all_books = Book.objects.all()
    form = BookForm()
    return render(
        request,
        template_name="bug_display.html",
        context={
            "form": form,
            "all_books": all_books,
        },
    )
