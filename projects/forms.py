from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    error_css_class = "error-field"
    required_css_class = "required-field"

    start_date = forms.CharField(
        required=True,
        label="Data de início",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "date",
            },
        ),
    )
    end_date = forms.CharField(
        required=True,
        label="Data de término",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "date",
            }
        ),
    )

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
                "class": "form-control",
            }
            self.fields[str(field)].widget.attrs.update(new_data)

    def clean(self):
        cleaned_data = super(ProjectForm, self).clean()
        validation_error_msgs = {}
        cleaned = self.cleaned_data
        if cleaned["end_date"] < cleaned["start_date"]:
            validation_error_msgs[
                "end_date"
            ] = "Data Final não pode ser anterior a Data Inicial"
        if cleaned["value"] < 0:
            validation_error_msgs[
                "value"
            ] = "Valor do projeto não pode ser negativo"
        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))
        return cleaned_data


class InvestCalcForm(forms.Form):
    investment_value = forms.IntegerField(
        label="Valor Total de Investimento",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control text-black",
                "autofocus": True,
                "type": "number",
            }
        ),
    )
