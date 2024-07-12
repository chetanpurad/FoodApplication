from django.urls import path

from . import views


app_name= 'foodapp'

urlpatterns = [
    path('home/',views.home),
   
    path('add_item/',views.add_item,name='add_items'),
    path('items/',views.item_list,name='items'),
    path('<int:item_id>/',views.detail_item,name='detail_item'),
    path('update_item/<int:id>/',views.update_item,name='update_item'),
    path('delete_item/<int:id>/',views.delete_item,name='delete_item'),
]


