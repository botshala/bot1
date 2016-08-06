from django.conf.urls import include, url
urlpatterns = []
from .views import MyQuoteBotView

urlpatterns = [
                  url(r'^foo/?$', MyQuoteBotView.as_view()) 
               ]