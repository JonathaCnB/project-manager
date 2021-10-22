from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    error_css_class = "error-field"
    required_css_class = "required-field"

    class Meta:
        model = Project
        fields = [
            "name",
            "start_date",
            "end_date",
            "value",
            "risk",
            "participants",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_data = {
                "placeholder": f"{str(field)}",
                "class": "form-control",
            }
            self.fields[str(field)].widget.attrs.update(new_data)
            self.fields[str(field)].label = ""
