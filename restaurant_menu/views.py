from django.shortcuts import render
from django.views import generic
from .models import Item, MEAL_TYPE


class MenuList(generic.ListView):
    # page for menu
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """ Get values from MEAL_TYPE and return for jinja """
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context

class MenuItemDetail(generic.DetailView):
    # page for sub-menus
    model = Item
    template_name = "menu_item_detail.html"
