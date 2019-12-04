from django.urls import path
from .views import monster1View

urlpatterns = [
    path("",monster1View.as_view(),name="monster"),
    path("<int:id>/",monster1View.as_view(),name="monster"),
]