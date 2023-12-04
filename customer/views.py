from django.shortcuts import render

# Create your views here.
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
    
class About(View):
     def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        pass
        #get each item from each category
        #pass int context
        #render the template
