from tastypie import authorization
from django.conf.urls import patterns, url, include
from tastypie import resources
from tastypie.utils import trailing_slash
import json

class MentalArithmetic(object):
    def __init__(self):
        return None

class MentalArithmeticResource(resources.Resource):
    class Meta:
        resource_name = 'mentalarithmetic'
        allowed_methods = ()
        authorization = authorization.Authorization()
        object_class = MentalArithmetic

    def base_urls(self):
        return [
            url(r"^plugin/(?P<resource_name>%s)%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('dispatch_list'), name="api_dispatch_list"),
            url(r"^plugin/(?P<resource_name>%s)/schema%s$" % (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_schema'), name="api_get_schema"),
        ]
