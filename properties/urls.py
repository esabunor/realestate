from django.conf.urls import url
from .views import property_details_view
urlpatterns = [
    url(r'^', property_details_view), 
]