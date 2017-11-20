from django.contrib import admin
from .models import Question, Answer, Story, Comment, Profile, Feedback, q_notify, s_notify
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','created')
    list_filter = ('title','body')
    date_hierarchy = 'created'
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display=('body','created','active')
    list_filter=('active','created','updated')
    search_fields=('user','body')
admin.site.register(Answer, AnswerAdmin)

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title','created')
    list_filter = ('title','source')
    date_hierarchy = 'created'
admin.site.register(Story, StoryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('body','created','active')
    list_filter=('active','created','updated')
    search_fields=('user','body')
admin.site.register(Comment,CommentAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'date_of_birth','work_or_study']
admin.site.register(Profile, ProfileAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email','created')
admin.site.register(Feedback,FeedbackAdmin)

class q_notifyAdmin(admin.ModelAdmin):
    list_display=('Actor','Object','created')
admin.site.register(q_notify, q_notifyAdmin)

class s_notifyAdmin(admin.ModelAdmin):
    list_display=('Actor','Object','created')
admin.site.register(s_notify, s_notifyAdmin)
