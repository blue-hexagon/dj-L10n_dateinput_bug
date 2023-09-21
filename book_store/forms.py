from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from book_store.models import Book


class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Book
        localized_fields = (
            "borrowed_from_date",
            "borrowed_to_date",
        )
        fields = [
            "title",
            "borrowed_from_date",
            "borrowed_to_date",
            "is_returned"
        ]
        labels = {
            "title": _("Book Title"),
            "borrowed_from_date": _("Loaned From"),
            "borrowed_to_date": _("Loaned To"),
            "is_returned": _("Returned"),
        }
        widgets = {
            "title": forms.TextInput(attrs={"rows": 4}),
            "borrowed_from_date": forms.DateInput(attrs={"type": "date"}),
            "borrowed_to_date": forms.DateInput(attrs={"type": "date"}),
            "is_returned": forms.CheckboxInput(),
        }
