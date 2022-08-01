
from django.urls import path
from .views import *
app_name = "project"
urlpatterns =[

    path('', project_list_view, name='list_view' ),
    
    path('create/',project_create_update_view, name = 'create_view'),
    path('<id>/update/',project_create_update_view, name = 'update_view'),
    path('deactivate/',project_deactivate_view, name = 'deactivate_view'),
    
    path('<id>/',project_detail_view, name = 'detail_view'),
    path('contrib/create',project_contribution_create_view, name='contrib_create_view')

    
]