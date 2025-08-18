from django.contrib import admin
from trainMap.models import TrainData


class TrainDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(TrainData, TrainDataAdmin)
