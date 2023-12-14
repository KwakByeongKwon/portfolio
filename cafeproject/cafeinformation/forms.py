from django import forms
from .models import CsvFile

class CsvFileForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = ['file_name','file']
        
class FileSelectForm(forms.Form):
    file_choices = [
        (file.id, file.file_name[9:12]) if len(file.file_name) == 16
        else (file.id, file.file_name[9:11]) if len(file.file_name) == 15
        else (file.id, file.file_name[9:13]) if len(file.file_name) == 17
        else None
        for file in CsvFile.objects.all()
    ]

    # None을 제외한 값만 선택지에 포함
    file_choices = [choice for choice in file_choices if choice is not None]

    file = forms.ChoiceField(choices=[('', '선택하세요')] + file_choices, widget=forms.Select(attrs={'class': 'form-select'}))