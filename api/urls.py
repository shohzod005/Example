from django.urls import path,include
from .views import *
urlpatterns = [
    path('category/<slug:slug>/', CategoryRetirieveUpdateDeleteAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path("inventory/", InventryListCreateAPIView.as_view()),
    path("inventory/<int:pk>/", InventaryRetirieveUpdateDeleteAPIView.as_view()),
    path("user/<int:pk>/", CostumUserRetirieveUpdateDeleteAPIView.as_view()),
    path("order/", OrderListCreateAPIView.as_view()),
    path("order/<int:pk>/", OrderRetirieveUpdateDeleteAPIView.as_view()),
    path('product/', ProductListCreateAPIView.as_view()),
    path('product/<slug:slug>/', ProductRetirieveUpdateDeleteAPIView.as_view()),
    path("photo/", ProductPhotoListCreateAPIView.as_view()),
    path("photo/<int:pk>/",ProductPhotoRetirieveUpdateDeleteAPIView.as_view()),
    path("",CostumUserListCreateAPIView.as_view())
]
