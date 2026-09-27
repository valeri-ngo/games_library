from django import forms

from .models import Genre


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre

        fields = [
            "name",
            "description",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter genre name.",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Enter a short genre description",
                }
            ),
        }

        labels = {
            "name": "Genre name",
            "description": "Genre description",
        }

        help_texts = {
            "name": "Game genre",
            "description": "Genre description",
        }

        error_messages = {
            "name": {
                "required": "Please enter a game genre.",
                "unique": "This genre already exists.",
            },
        }
