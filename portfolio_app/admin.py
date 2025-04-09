from django.contrib import admin
from .models import DownloadCV, Projects, Languages, Skills, Awards, Educations, Experiences, Icons

@admin.register(DownloadCV)
class DownloadCVAdmin(admin.ModelAdmin):
    list_display = ('id', 'cv')

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'github_link', 'is_deployed', 'deployed_link', 'image')

@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('language', 'rate', )

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill',)

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Educations)
class EducationsAdmin(admin.ModelAdmin):
    list_display = ('venue', 'degree', 'year', )

@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'year', )

@admin.register(Icons)
class ExperiencesAdmin(admin.ModelAdmin):
    list_display = ('link', 'class_link', )