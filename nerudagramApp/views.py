from django.shortcuts import render
from nerudagramApp.forms import NerudagramForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from nerudagramApp.models import NerudagramModel


class NerudagramHomePage(TemplateView):
    template_name = "nerudagram.html"

class NerudagramComoFuncionaView(TemplateView):
    template_name = "como_funciona.html"

class NerudagramPoemListView(ListView):
    context_object_name = 'poemas'
    model = NerudagramModel
    # paginate_by = 100  # if pagination is desired
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

class NerudagramPoemDetailView(DetailView):
    context_object_name = 'poem_details'
    model = NerudagramModel
    template_name = "nerudagramApp/nerudagrammodel_detail.html"

class NerudagramCreateView(CreateView):
    model = NerudagramModel
    form_class = NerudagramForm

    def form_valid(self, form):
        title, poem = form.generate_poem()
        form.instance.title = title
        form.instance.poem = poem
        form.save()
        return super().form_valid(form)

class NerudagramUpdateView(UpdateView):
    context_object_name = 'poem_details'
    model = NerudagramModel
    fields = ['title', 'poem']
    template_name = "nerudagramApp/nerudagrammodel_update.html"
    # template_name_suffix = '_update_form'
