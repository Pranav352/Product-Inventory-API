from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser,IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
