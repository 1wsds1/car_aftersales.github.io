# from django import forms
# from .models import Repair, RepairLog, InspectionReport
#
# class RepairForm(forms.ModelForm):
#     class Meta:
#         model = Repair
#         fields = ['order_state']  # 只包含order_state字段
#
# class RepairLogForm(forms.ModelForm):
#     class Meta:
#         model = RepairLog
#         fields = ['order_state']  # 只包含order_state字段
#
# class InspectionReportForm(forms.ModelForm):
#     class Meta:
#         model = InspectionReport
#         fields = ['order_state']  # 只包含order_state字段
#
from django import forms
from .models import Repair, Log, Inspection

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = '__all__'

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = '__all__'
