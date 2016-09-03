from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from shop.models import (
    Catalog,
    Product,
    Testimonial,
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


class TestimonialMixin(object):
    model = Testimonial


class TestimonialList(TestimonialMixin, ListView):
    pass


class TestimonialDetail(TestimonialMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(TestimonialDetail, self).get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()
        return context


class CatalogMixin(object):
    model = Catalog


class CatalogList(CatalogMixin, ListView):
    pass


class CatalogDetail(CatalogMixin, DetailView):
    def get_context_data(self, **kwargs):
        context = super(CatalogDetail, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(catalog=Catalog)

        return context
