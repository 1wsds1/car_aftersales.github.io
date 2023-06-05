from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home',),
    # path('repair_list.html',views.RepairList,name='repair_list'),
    # path('repair_create.html',views.RepairCreate,name='repair_create'),
    # path('repair_update.html',views.RepairUpdate,name='repair_update'),
    # path('repair_delete.html',views.RepairDelete,name='repair_delete'),
    path('repair_log_create.html',views.RepairLogCreate,name='repair_log_create'),
    path('inspection_report_create.html',views.InspectionReportCreate,name='inspection_report_create'),
    path('log_detail.html', views.log_detail, name='repair_logs'),
    path('inspection_detail.html', views.inspection_detail, name='inspections'),
    # path('repairs/', views.RepairList.as_view(), name='repair_list'),
    # path('repairs/create/', views.RepairCreate.as_view(), name='repair_create'),
    # path('repairs/update/<int:pk>/', views.RepairUpdate.as_view(), name='repair_update'),
    # path('repairs/delete/<int:pk>/', views.RepairDelete.as_view(), name='repair_delete'),
    # path('repairs/log/<int:pk>/', views.RepairLogCreate.as_view(), name='repair_log_create'),
    # path('repairs/inspection/<int:pk>/', views.InspectionReportCreate.as_view(), name='inspection_report_create'),
]
