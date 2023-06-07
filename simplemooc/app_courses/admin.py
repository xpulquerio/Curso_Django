from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',) } #Preencher o campo de slug igual ao campo de nome na página de admin

admin.site.register(Course, CourseAdmin)


#Super usuário login: pulquerio
#Super usuário email: pulquerio.x@gmail.com
#Super usuário senha: 123456