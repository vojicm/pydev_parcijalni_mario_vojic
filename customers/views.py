
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Customer

# Create your views here.
class CustomerListView(ListView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'customers/customer_form_create.html'
    success_url = reverse_lazy('customers:customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customers:customer_list')

