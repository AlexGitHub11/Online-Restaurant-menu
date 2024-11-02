from django.urls import path
from . import views

urlpatterns = [
    path("", views.MenuList.as_view(), name="home"),
    # Using pk of db row to make url dynamic
    path("item/<int:pk>/", views.MenuItemDetail.as_view(), name="menu_item")
]