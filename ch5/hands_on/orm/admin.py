from django.contrib import admin

from orm.models import CustomUser, Profile
import csv
from django.http import HttpResponse

class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1

def export_as_csv(modeladmin, request, queryset):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    field_names = [field.name for field in modeladmin.model._meta.fields]
    writer.writerow(field_names)

    for obj in queryset:
        # ["admin", "admin@example...", "2024-01-01", ...]
        row = [getattr(obj, field) for field in field_names]
        writer.writerow(row)

    return response

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_joined")
    search_fields = ("username", )
    list_filter = ("is_staff", )
    inlines = (ProfileInline, )
    actions = [export_as_csv]