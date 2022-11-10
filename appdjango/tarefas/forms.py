from django.forms import ModelForm
from appdjango.tarefas.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields =['nome']