from django.template import Library

from ..api import get_last_invalidation


register = Library()


register.assignment_tag(get_last_invalidation)
