from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django import forms
from django.utils import timezone

from .models import Accomplishment


class RangeInput(forms.NumberInput):
    input_type = "range"


class AccomplishmentCreateForm(forms.ModelForm):
    accomplishment_date = forms.DateField(
        initial=timezone.localdate,
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Add Accomplishment",
                "name",
                "accomplishment_date",
                "challenge",
                "reward",
                "notes",
                "tags",
            ),
            Submit("submit", "Submit"),
        )

    class Meta:
        model = Accomplishment
        fields = [
            "name",
            "accomplishment_date",
            "challenge",
            "reward",
            "notes",
            "tags",
        ]
        widgets = {
            "name": forms.TextInput(),
            "challenge": RangeInput(attrs={"min": 0, "max": 10, "class": "form-range"}),
            "reward": RangeInput(attrs={"min": 0, "max": 10, "class": "form-range"}),
        }


class AccomplishmentUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Update Accomplishment",
                "name",
                "accomplishment_date",
                "challenge",
                "reward",
                "notes",
                "tags",
            ),
            Submit("submit", "Submit"),
        )

    class Meta:
        model = Accomplishment
        fields = [
            "name",
            "accomplishment_date",
            "challenge",
            "reward",
            "notes",
            "tags",
        ]
        widgets = {
            "name": forms.TextInput(),
            "accomplishment_date": forms.DateInput(attrs={"type": "date"}),
            "challenge": RangeInput(attrs={"min": 0, "max": 10, "class": "form-range"}),
            "reward": RangeInput(attrs={"min": 0, "max": 10, "class": "form-range"}),
        }


class AccomplishmentDeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Submit("submit", "Confirm deletion", css_class="btn-danger"),
        )
