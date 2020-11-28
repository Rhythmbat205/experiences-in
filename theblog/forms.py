from django import forms
from .models import Post, Category

#choices = [('IBM','IBM'), ('ZS','ZS'), ('Company','Company'),]

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-contol'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-contol'}),
            'author' : forms.TextInput(attrs={'class': 'form-contol','value':'', 'id':'elder','type':'hidden'}),
            #'author' : forms.Select(attrs={'class': 'form-contol'}),
            'category' : forms.Select(choices=choice_list,attrs={'class': 'form-contol'}),
            'body' : forms.Textarea(attrs={'class': 'form-contol'}),
        
        
        
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-contol', 'placeholder':'Company Name'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-contol'}),
            #'author' : forms.Select(attrs={'class': 'form-contol'}),
            'body' : forms.Textarea(attrs={'class': 'form-contol'}),
        
        
        
        }