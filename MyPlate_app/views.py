from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView
from .models import FoodItems, Previous_records, SetGoal
from django.urls import reverse_lazy, reverse
from .filters import FoodFilter

# Create your views here.

class FoodListView(ListView):
    model = FoodItems
    template_name = 'MyPlate_app/list.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['filter'] = FoodFilter(self.request.GET, queryset = self.get_queryset())
        return context

class GoalCreateView(CreateView):
    model = SetGoal
    fields = ['goal',]
    success_url = reverse_lazy('myplate_app:list')

class CheckOutView(TemplateView):
    template_name = 'MyPlate_app/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal'] = SetGoal.objects.values().last().get("goal")   #creates a dict with key value pair, where id and goal are the keys. The last() method is used to retrieve the last value. get() method retrives the value of the key 'goal'
        return context

def save_records(request):
    if request.method=="POST":
        user = request.POST.get('user', '')
        totalCalories= request.POST.get('totalCalories', '')
        goal=request.POST.get('goal_set', '')

        pre_records = Previous_records(user= user, totalCalories=totalCalories, goal_set=goal,)
        pre_records.save()
        return redirect('../previous_records')
    return render(request, 'MyPlate_app/save_rec.html')

class PreRecordsView(ListView):
    model = Previous_records
    template_name = 'MyPlate_app/previous_records.html'
    context_object_name = 'records'

    def get_queryset(self):
        filtered_list = Previous_records.objects.filter(user = self.request.user.first_name + ' ' + self.request.user.last_name)
        return filtered_list.order_by('-date')[:10]
    