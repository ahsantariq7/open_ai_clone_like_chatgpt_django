from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    like = forms.BooleanField(required=False, help_text='Optional')
    
    
    class Meta:
        model = Question
        fields = [
            'ques' 
            ]