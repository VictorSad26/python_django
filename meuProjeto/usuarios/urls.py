from django.urls import path
from .views import create_superuser

urlpatterns = [
    path("cadastro/", create_superuser, name="cadastro"),
    # outras urls...
]
