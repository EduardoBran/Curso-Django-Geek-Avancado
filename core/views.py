from django.views.generic import TemplateView

from .models import Funcionario, Preco, Recurso, Servico


class IndexView(TemplateView):
    template_name = 'index.html'

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
