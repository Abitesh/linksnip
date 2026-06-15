from django import forms


class URLForm(forms.Form):
    original_url = forms.URLField(
        label="Paste your URL",
        widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "https://example.com"})
    )