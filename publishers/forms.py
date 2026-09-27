from django import forms
from django.utils import timezone

from publishers.models import Publisher


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher

        fields = [
            "name",
            "description",
            "country",
            "founded_year",
            "website",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter publisher name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Input some description",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "placeholder": "Enter country",
                }
            ),
            "founded_year": forms.NumberInput(
                attrs={
                    "min": "1800",
                    "max": str(timezone.localdate().year),
                }
            ),
            "website": forms.URLInput(
                attrs={"placeholder": "https://example.com"},
            ),
        }

        labels = {
            "name": "Publisher name",
            "description": "Publisher description",
            "country": "Publisher country",
            "founded_year": "Founded year",
            "website": "Publisher's website",
        }

        help_texts = {
            "founded_year": "The year founded",
            "website": "Publisher's website",
        }

        error_messages = {
            "name": {
                "required": "Please enter the publisher name.",
                "unique": "A publisher with this name already exists.",
            },
            "founded_year": {
                "invalid": "Please enter a valid year.",
            },
            "website": {
                "invalid": "Please enter a valid URL.",
            },
        }

    def clean_founded_year(self):
        founded_year = self.cleaned_data.get("founded_year")
        current_year = timezone.localdate().year

        if founded_year is None:
            return founded_year

        if founded_year < 1800:
            raise forms.ValidationError("Founded year cannot be earlier than 1800.")

        if founded_year > current_year:
            raise forms.ValidationError("Founded year cannot be in the future.")

        return founded_year
