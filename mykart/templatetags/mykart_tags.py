from django import template
from django.contrib.auth.models import User, Group

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    if User.objects.filter(username=user, groups__name=group_name).exists():
        return True
    else:
        return False
