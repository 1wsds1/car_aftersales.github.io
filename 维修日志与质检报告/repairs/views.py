from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Repair, Log, Inspection
from .forms import RepairForm, LogForm, InspectionForm
from django.shortcuts import get_object_or_404

# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Repair, RepairLog, InspectionReport
# from .forms import RepairForm, RepairLogForm, InspectionReportForm
#
#

def home(request):
    return render(request,'base.html',{})

def RepairList(request):
    return render(request,'repair_list.html',{})

def RepairCreate(request):
    return render(request,'repair_create.html',{})

def RepairUpdate(request):
    return render(request,'repair_update.html',{})

def RepairDelete(request):
    return render(request,'repair_delete.html',{})



def RepairLogCreate(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_detail')
    else:
        form = LogForm()
    return render(request, 'repair_log_create.html', {'form': form})

def InspectionReportCreate(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inspection_detail')
    else:
        form = InspectionForm()
    return render(request, 'inspection_report_create.html', {'form': form})


def log_detail(request):
    logs = Log.objects.all()
    return render(request, 'log_detail.html', {'logs': logs})

def inspection_detail(request):
    inspections = Inspection.objects.all()
    return render(request, 'inspection_detail.html', {'inspections': inspections})



# class RepairList(ListView):
#     model = Repair
#     template_name = 'repairs/repair_list.html'
#     context_object_name = 'repairs'
#
# class RepairCreate(CreateView):
#     model = Repair
#     form_class = RepairForm  # 指定关联的模型表单
#     template_name = 'repairs/repair_create.html'
#     success_url = reverse_lazy('repair_list')
#
# class RepairUpdate(UpdateView):
#     model = Repair
#     form_class = RepairForm  # 指定关联的模型表单
#     template_name = 'repairs/repair_update.html'
#     success_url = reverse_lazy('repair_list')
#
# class RepairDelete(DeleteView):
#     model = Repair
#     template_name = 'repairs/repair_delete.html'
#     success_url = reverse_lazy('repair_list')
#
# class RepairLogCreate(CreateView):
#     model = RepairLog
#     form_class = RepairLogForm  # 指定关联的模型表单
#     template_name = 'repairs/repair_log_create.html'
#     success_url = reverse_lazy('repair_list')
#
# class InspectionReportCreate(CreateView):
#     model = InspectionReport
#     form_class = InspectionReportForm  # 指定关联的模型表单
#     template_name = 'repairs/inspection_report_create.html'
#     success_url = reverse_lazy('repair_list')
