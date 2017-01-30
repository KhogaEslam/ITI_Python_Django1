from django.contrib import admin


from .models import Student, Track
# Register your models here.
class StudentCustom(admin.StackedInline):
    model = Student
    extra = 1

class StudentCustom2(admin.ModelAdmin):
    list_display = ('stName','stAge','stTrack', 'isBornBefore1992')
    fieldsetes = (
        ['Personal Information',{'fields':['stName','stAge']}],
        ['Scholar Ship',{'fields':['stTrack']}]
    )
    search_fields = ['stName', 'stAge']
    list_filter = ['stName']

class TrackCustom(admin.ModelAdmin):
    inlines = [StudentCustom]

admin.site.register(Student, StudentCustom2)
admin.site.register(Track, TrackCustom)
