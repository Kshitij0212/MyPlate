from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views


app_name = 'myplate_app'

urlpatterns = [
    path('myplate_app_list/',views.FoodListView.as_view(), name='list'),
    path('set_goal/', views.GoalCreateView.as_view(), name='set_goal'),
    path('checkout/', views.CheckOutView.as_view(), name='checkout'),
    path('previous_records/',views.PreRecordsView.as_view(), name='pre_records'),
    path('save_rec/', views.save_records, name='save_rec'),
]