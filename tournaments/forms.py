from django import forms

from .models import Tournament

class TournamentForm(forms.ModelForm):

    class Meta:

        model = Tournament

        fields = (
            'name',
            'description',
            'location',
            'surface',
            'start_date',
            'end_date',
            'max_players',
        )

        labels = {
            'name': 'Tournament name',
            'description': 'Description',
            'location': 'Location',
            'surface': 'Surface',
            'start_date': 'Start date',
            'end_date': 'End date',
            'max_players': 'Maximum players'
        }

        help_texts = {
            'name': 'Choose a clear name for your tournament',
            'max_players': 'How many players can participate at maximum'
        }

        widgets ={
            'name': forms.TextInput(
                attrs={'placeholder': 'eg. Melbourne Open'}
            ),

            'description': forms.Textarea(
                attrs={'placeholder': 'Describe your tournament'}
            ),

            'location': forms.TextInput(
                attrs={'placeholder': '[City], [Country]'}
            ),

            'start_date': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'end_date': forms.DateInput(
                attrs = {'type': 'date'}
            )
        }

    def clean(self):

        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        max_players = cleaned_data.get("max_players")

        if start_date and end_date and end_date < start_date:
            self.add_error(
                'end_date', 'The end date cannot be before the start date'
            )

        if max_players is not None and max_players < 2:
            self.add_error(
                'max_players', 'A tournament must have at least 2 players'
            )

        return cleaned_data

class TournamentRegistrationForm(forms.Form):
    pass