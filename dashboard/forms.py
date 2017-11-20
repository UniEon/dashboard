from django import forms
from .models import Question, Answer, Story, Comment, Profile, Feedback
from django.contrib.auth.models import User

#question forms
class QuestionForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'maxlength':150}))
    class Meta:
        model = Question
        fields = ('title','body','tags')


class AnswerForm(forms.ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={
        'rows': '5',
        'cols': '80'}))
    class Meta:
        model = Answer 
        fields = {'body'}


#news forms

class StoryForm(forms.ModelForm):
    title=forms.CharField(widget=forms.Textarea(attrs={
        'rows':'2',
        'cols':'70'}))
    class Meta:
        model = Story
        fields = ('title','source','tags')

class CommentForm(forms.ModelForm):
    body=forms.CharField(widget=forms.Textarea(attrs={
        'rows':'3',
        'cols':'50'}))
    class Meta:
        model=Comment
        fields={'body'}

#login form

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
class SignupForm(forms.ModelForm):
    password=forms.CharField(label='Password',
                             widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ('username','email')
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields= ('first_name','last_name','email')
class ProfileEditForm(forms.ModelForm):
    date_of_birth=forms.CharField(label="Date of Birth",widget=forms.TextInput(attrs={'placeholder':'y-m-d'}))
    work_or_study=forms.CharField(label="Bio",widget=forms.TextInput(attrs={'placeholder':'something interesting about you'}))
    skills=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'what are you good at?'}))
    class Meta:
        model= Profile
        fields = ('date_of_birth','work_or_study','skills')
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=('name','email','feedback')
