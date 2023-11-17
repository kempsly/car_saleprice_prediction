from django.urls import path
from django.conf.urls.static import static
from .views import index_func, homeView, document_view, contact_view


urlpatterns = [
    path('', homeView, name='home-page'),
    path('model', index_func, name='model-page'),
    path('document', document_view, name='document-page'),
    ]