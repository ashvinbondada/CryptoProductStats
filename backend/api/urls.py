from django.urls import path
from .views import hello_world, InterestFormView, ListProductStatsView, DeleteProductStatsView

urlpatterns = [
    path('hello/', hello_world, name="hello world"),
    path('submit/', InterestFormView.as_view(), name="submit"),
    path('products/', ListProductStatsView.as_view(), name="products"),
    path('delete/<int:pk>/', DeleteProductStatsView.as_view(), name="delete")
]
