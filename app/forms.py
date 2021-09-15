from django import forms
from django.core import validators
g=[('MALE','maLE'),('FEMALE','femALE')]
c=[('python','PYTHON'),('Django','django')]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    #email=forms.EmailField()
    #url=forms.URLField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=200,widget=
                                 forms.Textarea(attrs={'cols':5,'rows':5}))
    #gender=forms.ChoiceField(choices=g)
    #course=forms.MultipleChoiceField(choices=c)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)


class TopicForm(forms.Form):
    topicname=forms.CharField(max_length=100)