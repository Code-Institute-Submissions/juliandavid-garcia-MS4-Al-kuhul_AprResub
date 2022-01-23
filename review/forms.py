from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ('review')

        def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'review': 'Add your comment here!',
        }
