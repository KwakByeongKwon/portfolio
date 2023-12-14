from django import forms
from .models import PlayerInfo,Opponent,Record

class PlayerInfoForm(forms.ModelForm):
    class Meta:
        model = PlayerInfo
        fields = ['schoolname','grade','playername','age','pitchingtype','intro']
        widgets = {
            'intro':forms.Textarea(attrs={'rows': 7, 'cols':30,'placeholder':'입력 하세요'}),
            
            'schoolname':forms.TextInput(attrs={'placeholder':'00고등학교'}),
    
            'playername':forms.TextInput(attrs={'placeholder':'홍길동'}),
            
            'age':forms.TextInput(attrs={'placeholder':'17'}),
            
            'pitchingtype':forms.TextInput(attrs={'placeholder':'R/O (Right/Over hand)'}),
        }

class SpeedForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['speed']
        widgets = {
            'speed':forms.NumberInput(attrs={'style':'width: 100px'})
        }

class OpponentForm(forms.ModelForm):
    class Meta:
        model = Opponent
        fields = ['opponent_date','opponent_name']
        widgets = {
            'opponent_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'opponent_name':forms.TextInput(attrs={'placeholder':'00고등학교'}),
        }

    

    

