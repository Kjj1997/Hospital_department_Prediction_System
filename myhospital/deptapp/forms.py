from django import forms



class VisitReasonForm(forms.Form):
    reason_text = forms.CharField(
        max_length=200,
        #widget=forms.TextInput(attrs={'id': 'reason_text'})
    )

