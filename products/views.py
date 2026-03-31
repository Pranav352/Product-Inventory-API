from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

# Create your views here.


class ProductViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAdminUser,IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
