from django.shortcuts import render
from .models import Task, Domain
from django.views import View

def index(request, *args, **kwargs):
    task_list = Task.objects.order_by('-id')[:4]
    domain_list = Domain.objects.all()
    context = {
        'task_list' : task_list,
        'domain_list' : domain_list,
    }
    return render(request, 'job/index.html', context)


class CreateJob(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')