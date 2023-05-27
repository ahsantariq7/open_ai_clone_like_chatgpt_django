from django.shortcuts import render
from .forms import QuestionForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .utils import openai_fun
# Create your views here.

class question_view(CreateView):
    form_class=QuestionForm
    template_name='home.html'
    success_url = '/home/'
    
    def form_valid(self, form):
        #post_value = self.request.POST['ques']
        post_value = form.cleaned_data['ques']
        print(post_value)
        ah=openai_fun(post_value)
        print(ah)
        self.object = form.save()
        context = self.get_context_data(form=form)
        context['ans'] = ah
        context['que'] = post_value

        return self.render_to_response(context)

    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'extra_context':self.extra_context})
        return context
'''



    
    
    
    
    