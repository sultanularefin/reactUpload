"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# commented by arefin
"""


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

# commented by arefin ends here..

# modified working codes are below: 7:02 pm:


# from django.conf import settings
# from django.conf.urls.static import static

# above 2 lines were added from this video= > september 09: (1)
# 1. yt1s.io-Django Rest Framework Series - Image Uploading _ Handling with React Front-end  - Part-8.mp4
# commented the above 2 lines following this tutorial below:

# https://medium.com/django-rest/django-rest-framework-uploading-images-b01fbc19a555

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# copied from here ===> https://newbedev.com/django-rest-framework-image-upload
# class ProductViewSet(BaseViewSet, viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     @detail_route(methods=['post'])
#     def upload_docs(request):
#         try:
#             file = request.data['file']
#         except KeyError:
#             raise ParseError('Request has no resource file attached')
#         product = Product.objects.create(image=file, ....)


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]



# can't login with above:


"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""