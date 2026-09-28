from django import template
from django.forms.boundfield import BoundField

register = template.Library()


@register.filter
def add_class(field: BoundField, css_classes: str) -> str:
    return field.as_widget(
        attrs={
            "class": css_classes,
        }
    )
