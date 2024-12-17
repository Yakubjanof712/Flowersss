from django import template
from ..models import Turlar

register = template.Library()

@register.simple_tag
def turlar():
    return Turlar.objects.all()
