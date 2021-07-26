from django.contrib import admin
from .models import FoodItems, SetGoal, Previous_records
# Register your models here.

class PreRecAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(FoodItems)
admin.site.register(SetGoal)
admin.site.register(Previous_records, PreRecAdmin)