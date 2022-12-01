from django.urls import path
from .views import AdministracionView, ClassRoomCreate, deleteClassRoom

urlpatterns = [
    path('', AdministracionView.as_view(), name="index"),
    path("create/", ClassRoomCreate.as_view(), name="create"),
    path('delete/<int:id>', deleteClassRoom, name="delete")
]