from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from .models import *
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404


class ProductListCreateAPIView(APIView):
    serializer_class = ProductSerializer
    def get(self,request,*args,**kwargs):
        product = Product.objects.all()
        
        serializer =self.serializer_class(product,many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class ProductRetirieveUpdateDeleteAPIView(APIView):
    
    serializer_class = ProductSerializer
    def get(self,request,slug):
        category = get_object_or_404(Product, slug=slug)
        serializer = self.serializer_class(instance=category)
        return Response(data=serializer.data)

    def put(self, request,slug):
        data= request.data
        ganre = get_object_or_404(Product, slug=slug)
        serializer =self.serializer_class(instance=ganre,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,slug):
        data= request.data
        ganre = get_object_or_404(Product, slug=slug)
        serializer =self.serializer_class(instance=ganre,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request,slug):
        ganre = get_object_or_404(Product, slug=slug)
        ganre.delete()
        return Response(data={"deleted":"product"},status=status.HTTP_204_NO_CONTENT)


class CostumUserListCreateAPIView(APIView):
    serializer_class = CostumUserSerializer
    def get(self,request,*args,**kwargs):
        product = CostumUser.objects.all()
        serializer =self.serializer_class(product,many=True)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class CostumUserRetirieveUpdateDeleteAPIView(APIView):
    
    serializer_class = CostumUserSerializer
    def get(self,request,pk):
        category = get_object_or_404(CostumUser, id=pk)
        serializer = self.serializer_class(instance=category)
        return Response(data=serializer.data)

    def put(self, request,pk):
        data= request.data
        ganre = get_object_or_404(CostumUser, id=pk)
        serializer =self.serializer_class(instance=ganre,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        ganre = get_object_or_404(CostumUser, id=pk)
        serializer =self.serializer_class(instance=ganre,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request,pk):
        ganre = get_object_or_404(CostumUser, id=pk)
        ganre.delete()
        return Response(data={"deleted":"CostumUser"},status=status.HTTP_204_NO_CONTENT)

class OrderListCreateAPIView(APIView):
    serializer_class = orderSerializer
    def get(self,request,*args,**kwargs):
        product = order.objects.all()
        serializer =self.serializer_class(product,many=True)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class OrderRetirieveUpdateDeleteAPIView(APIView):
    
    serializer_class = orderSerializer
    def get(self,request,pk):
        category = get_object_or_404(order, id=pk)
        serializer = self.serializer_class(instance=category)
        return Response(data=serializer.data)

    def put(self, request,pk):
        data= request.data
        ganre = get_object_or_404(order, id=pk)
        serializer =self.serializer_class(instance=ganre,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        ganre = get_object_or_404(order, id=pk)
        serializer =self.serializer_class(instance=ganre,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request,pk):
        ganre = get_object_or_404(order, id=pk)
        ganre.delete()
        return Response(data={"deleted":"order"},status=status.HTTP_204_NO_CONTENT)

class ProductPhotoListCreateAPIView(APIView):
    serializer_class = ProductPhotoSerializer
    def get(self,request,*args,**kwargs):
        product = product_photo.objects.all()
        serializer =self.serializer_class(product,many=True)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class ProductPhotoRetirieveUpdateDeleteAPIView(APIView):
    
    serializer_class = ProductPhotoSerializer
    def get(self,request,pk):
        category = get_object_or_404(product_photo, id=pk)
        serializer = self.serializer_class(instance=category)
        return Response(data=serializer.data)

    def put(self, request,pk):
        data= request.data
        ganre = get_object_or_404(product_photo, id=pk)
        serializer =self.serializer_class(instance=ganre,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        ganre = get_object_or_404(product_photo, id=pk)
        serializer =self.serializer_class(instance=ganre,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request,pk):
        ganre = get_object_or_404(product_photo, id=pk)
        ganre.delete()
        return Response(data={"deleted":"product_photo"},status=status.HTTP_204_NO_CONTENT)

class CategoryRetirieveUpdateDeleteAPIView(APIView):
    
    serializer_class = CategorySerializer
    def get(self,request,slug):
        category = get_object_or_404(Category, slug=slug)
        serializer = self.serializer_class(instance=category)
        return Response(data=serializer.data)

    def put(self, request,slug):
        data= request.data
        ganre = get_object_or_404(Category, slug=slug)
        serializer =self.serializer_class(instance=ganre,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,slug):
        data= request.data
        ganre = get_object_or_404(Category, slug=slug)
        serializer =self.serializer_class(instance=ganre,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request,slug):
        ganre = get_object_or_404(Category, slug=slug)
        ganre.delete()
        return Response(data={"deleted":"Category"},status=status.HTTP_204_NO_CONTENT)

class CategoryListCreateAPIView(APIView):
    serializer_class = CategorySerializer
    def get(self,request,*args,**kwargs):
        product = Category.objects.all()
    
        serializer =self.serializer_class(product,many=True)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)


class InventryListCreateAPIView(APIView):
    serializer_class = InventorySerializer
    def get(self,request,*args,**kwargs):
        product = Inventory.objects.all()
        serializer =self.serializer_class(product,many=True)
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class InventaryRetirieveUpdateDeleteAPIView(APIView):
    
    serializer_class = InventorySerializer
    def get(self,request,pk):
        category = get_object_or_404(Inventory, id=pk)
        serializer = self.serializer_class(instance=category)
        return Response(data=serializer.data)

    def put(self, request,pk):
        data= request.data
        ganre = get_object_or_404(Inventory, id=pk)
        serializer =self.serializer_class(instance=ganre,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request,pk):
        data= request.data
        ganre = get_object_or_404(Inventory, id=pk)
        serializer =self.serializer_class(instance=ganre,data=data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request,pk):
        ganre = get_object_or_404(Inventory, id=pk)
        ganre.delete()
        return Response(data={"deleted":"Inventory"},status=status.HTTP_204_NO_CONTENT)
