from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from .models import ClassRoom
from .forms import ClassRoomForm
# Create your views here.

class AdministracionView(TemplateView):
    template_name = "administracion/index.html"
    extra_context = {"classrooms": ClassRoom.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classrooms"] = ClassRoom.objects.all()
        return context

class ClassRoomCreate(FormView):
    model=ClassRoom
    template_name="administracion/create.html"
    form_class=ClassRoomForm

    def form_valid(self,form):
        ClassRoom.objects.create(**form.cleaned_data)
        return redirect("index")


def deleteClassRoom(request,id):
    classroom= ClassRoom.objects.get(id=id)
    classroom.delete()
    return redirect("index")
