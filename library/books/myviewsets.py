from rest_framework import viewsets
from books.models import Books
from books.my_serializers import Booksserializers


class Booksviewsets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = Booksserializers
