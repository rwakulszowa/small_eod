from django.db.models import Q

from ..search.searchset import BaseSearchSet


class NoteSearchSet(BaseSearchSet):
    search_fields = ["comment"]
    filters = {
        "id": lambda value: Q(pk=value),
        "case": lambda value: Q(case__pk=value),
    }
