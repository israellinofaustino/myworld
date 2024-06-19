from django.forms import ModelForm, Textarea
from .models import FeedBack



class PostForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
        widgets = {
            'text': Textarea()
        }