from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import ClassesSerializer
from .models import Classes


class ClassesListView(ListCreateAPIView):
    queryset=Classes.objects.all()
    serializer_class= ClassesSerializer


class ClassesDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Classes.objects.all()
    serializer_class= ClassesSerializer
