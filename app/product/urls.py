from django.urls import path
from app.product.views import (
    CategoryAPIView, TypesAPIView, ProductAPIView,
    ProductCreateAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, ProductDeleteAPIView,
    CategoryCreateAPIView, CategoryRetrieveAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView,
    TypesCreateAPIView, TypesRetrieveAPIView, TypesUpdateAPIView, TypesDeleteAPIView
)

urlpatterns = [
    path("category-list", CategoryAPIView.as_view(), name='category-list'),
    path("type-list", TypesAPIView.as_view(), name='type-list'),
    path("product-list", ProductAPIView.as_view(), name='product-list'),

    path("product-create", ProductCreateAPIView.as_view(), name='create'),
    path("product-detail/<uuid:uuid>/", ProductRetrieveAPIView.as_view(), name='detail'),
    path("product-update/<uuid:uuid>/update", ProductUpdateAPIView.as_view(), name='update'),
    path("product-delete/<uuid:uuid>/delete", ProductDeleteAPIView.as_view(), name='delete'),

    path("category-create", CategoryCreateAPIView.as_view(), name='category-create'),
    path("category-detail/<int:pk>/", CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path("category-update/<int:pk>/update", CategoryUpdateAPIView.as_view(), name='category-update'),
    path("category-delete/<int:pk>/delete", CategoryDeleteAPIView.as_view(), name='category-delete'),

    path("type-create", TypesCreateAPIView.as_view(), name='type-create'),
    path("type-detail/<int:pk>/", TypesRetrieveAPIView.as_view(), name='type-detail'),
    path("type-update/<int:pk>/update", TypesUpdateAPIView.as_view(), name='type-update'),
    path("type-delete/<int:pk>/delete", TypesDeleteAPIView.as_view(), name='type-delete'),
]
