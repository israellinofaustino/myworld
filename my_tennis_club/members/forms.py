from django.forms import ModelForm
from .models import FeedBack

class PostForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'