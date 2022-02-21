from django.db import models
from django.contrib import admin
from django_ace import AceWidget
from .models import MockData

@admin.register(MockData)
class MockDataModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': AceWidget(
            mode='json', 
            wordwrap=True,
            theme='nord_dark', 
            width='900px',
            height='400px',
            fontsize='10pt',
        )}
    }

    list_display = ('id', 'status', 'message')
    # list_display = [field.name for field in MockData._meta.fields]