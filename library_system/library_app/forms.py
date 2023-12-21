from django.forms import ModelForm
from .models import Book ,Author

class bookform(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class authorform(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


