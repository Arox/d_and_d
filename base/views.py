#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import FormView
from forms import BaseParametersForm
from models import BaseParameters

# Create your views here.
class BaseParametrCreateView(FormView):
    template_name = 'create_task.html'
    success_url = ''
    form_class = BaseParametersForm

    def form_valid(self, a_form):
        v_parametr = BaseParameters(
            m_name=a_form.m_name,
            m_description=a_form.m_description
        )
        v_parametr.save()
        return super(BaseParametrCreateView, self).form_valid(a_form)