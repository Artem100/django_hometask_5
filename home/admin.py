from django.contrib import admin

from .models import Student

class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'sex', 'address', 'description', 'birthday', 'email')
    list_display_links = ('id', 'name', ) # Колонка становиться ссылкой
    search_fields = ('name', 'surname') # Колонки по которым производится поиск
    list_filter = ('name', 'surname') # Дополнительный фильтр

admin.site.register(Student, StudentsAdmin)