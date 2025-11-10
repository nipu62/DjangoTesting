from django.views.generic import ListView
from AnimalZoo.models import Animal

class AnimalListView(ListView):
    model = Animal
    template_name = "animals.html"
    context_object_name = "animals"
