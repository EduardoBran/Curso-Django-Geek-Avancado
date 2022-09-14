from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContatoForm
from .models import Funcionario, Preco, Recurso, Servico


# FormView -> página web que possui um formulário
class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['servicos'] = Servico.objects.order_by('?').all()  # aleatório
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['precos'] = Preco.objects.all()

        # solução simples
        # context['recursos1'] = Recurso.objects.all()[:3]
        # context['recursos2'] = Recurso.objects.all()[3:6]

        # solução elegante
        recursos = Recurso.objects.all()
        context['recursosLeft'] = recursos[0:int(len(recursos) / 2)]
        context['recursosRight'] = recursos[int(len(recursos) / 2):]

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
