from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .filterset import NoteFilterSet
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = NoteFilterSet
    ordering_fields = [
        "id",
        "case__name",
    ]
