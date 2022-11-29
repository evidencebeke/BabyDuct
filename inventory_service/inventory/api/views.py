from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from inventory.models import Product, ProductsImage
from inventory.api.serializers import ProductSerializers, ReviewSerializers, ProductsImageSerializers
from .helper import image_input_saver

class ProductCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewSerializers

class ProductsImageCreateView(APIView):
    serializer_class = ProductsImageSerializers
    parser_class = [MultiPartParser, FormParser]
    # queryset = ProductsImage.objects.all()

    def post(self, request):
        product = Product.objects.get(id=request.data["product"])

        # getting images from post request
        images = request.FILES.getlist("image")
        if images :
            request.data.pop("image")

            uploaded_images = []
            for image in images:
                uploaded_images.append(ProductsImage.objects.create(product=product, image=image))
            
            data = {}
            data["id"] = request.data["product"]
            data["image"] = [img.id for img in uploaded_images]
            serializer = ProductsImageSerializers(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(list(serializer.data))
            else :
                return Response(serializer.errors)
        else:
            _serializer = ProductsImageSerializers(data=request.data)
            if _serializer.is_valid():
                _serializer.save()
                return Response(_serializer.data)
            else :
                return Response(_serializer.errors)