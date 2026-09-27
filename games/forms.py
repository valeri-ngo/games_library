from django import forms

from games.models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            "name",
            "description",
            "publisher",
            "genres",
            "release_date",
            "rating",
            "cover_url",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter game title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Enter game description",
                }
            ),
            "genres": forms.CheckboxSelectMultiple(),
            "release_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "rating": forms.NumberInput(
                attrs={
                    "min": "0",
                    "max": "10",
                    "step": "0.01",
                }
            ),
            "cover_url": forms.URLInput(
                attrs={
                    "placeholder": "Enter image url",
                }
            ),
        }

        labels = {
            "name": "Game title",
            "description": "Game description",
            "publisher": "Publisher",
            "genres": "Genres",
            "release_date": "Release date",
            "rating": "Rating",
            "cover_url": "Cover image url",
        }

        help_texts = {
            "genres": "Select one or more genres.",
            "rating": "Enter a rating between 0 and 10.",
            "cover_url": "Enter a direct URL to the game cover.",
        }

        error_messages = {
            "name": {
                "required": "Please enter the game title.",
                "unique": "A game with this title already exists.",
            },
            "publisher": {
                "required": "Please select a publisher.",
            },
            "genres": {
                "required": "Please select at least one genre.",
            },
            "release_date": {
                "invalid": "Please enter a valid release date.",
            },
            "rating": {
                "invalid": "Please enter a valid number.",
            },
            "cover_url": {
                "invalid": "Please enter a valid URL.",
            },
        }
