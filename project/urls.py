
from django.urls import path
from .views import *
app_name = "project"
urlpatterns =[

    path('', project_list_view, name='list_view' ),
    path('create/',project_create_view, name = 'create_view'),
    path('<id>/',project_detail_view, name = 'detail_view'),
    path('edit/<id>/',project_edit_view, name = 'edit_view')
    
]