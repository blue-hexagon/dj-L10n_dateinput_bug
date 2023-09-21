from django.shortcuts import render, redirect

from book_store.forms import BookForm


def create_book(request):
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get("HTTP_REFERER", request.path_info))
        else:
            # Add message
            return redirect(request.META.get("HTTP_REFERER", request.path_info))

    form = BookForm()
    return render(
        request,
        template_name="create_book.html",
        context={
            "form": form,
        },
    )
