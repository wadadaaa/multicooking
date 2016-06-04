from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from shop.models import (
    Catalog,
    Product,

)


class ProductMixin(object):
    model = Product


class ProductDetail(ProductMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        return context


class ProductList(ProductMixin, ListView):
    pass


DIRECTION_WEIGHT = {
    'up': 1,
}


class CatalogMixin(object):
    model = Catalog


class CatalogList(CatalogMixin, ListView):
    pass


class CatalogDetail(CatalogMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(CatalogDetail, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(catalog=Catalog)

        return context



