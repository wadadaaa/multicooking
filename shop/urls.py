from django.conf.urls import patterns, url
from .views import *

urlpatterns = [
               url(r'^catalog/list/$',
                   CatalogList.as_view(), name='catalog_list'),
               url(r'^catalog/detail/(?P<slug>\w+)/$',
                   CatalogDetail.as_view(), name='catalog_detail'),
               url(r'^$',
                   ProductList.as_view(), name='product_list'),
               url(r'^product/detail/(?P<slug>[-_\w]+)/$',
                   ProductDetail.as_view(), name='product_detail'),
               url(r'^testimonial/list/$',
                   TestimonialList.as_view(), name='testimonial_list'),
               url(r'^testimonial/detail/(?P<slug>[-_\w]+)/$',
                   TestimonialDetail.as_view(), name='testimonial_detail'),
               ]
