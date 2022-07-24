from django.urls.conf import path

from api.views import Customer_View

urlpatterns = [
    path('customers/', Customer_View.as_view(), name='Customer')
]
