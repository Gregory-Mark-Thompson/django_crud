from django import forms
from .models import Battle

class BattleForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = ['date', 'location', 'enemy', 'losses', 'enemy_losses', 'outcome', 'discussion']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }