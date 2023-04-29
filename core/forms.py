from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field
from crispy_bootstrap5.bootstrap5 import FloatingField
from django import forms
from django.forms.widgets import ClearableFileInput
from django.urls import reverse_lazy


from .models import Accomplishment


class RangeInput(forms.NumberInput):
    input_type = "range"


class AccomplishmentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Add Accomplishment",
                "name",
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

    # content_ = forms.ImageField(
    #     widget=ClearableFileInput(
    #         attrs={
    #             "hx-post": reverse_lazy("meme_create_suggested_tags"),
    #             "hx-target": "#suggested-tags",
    #             "hx-encoding": "multipart/form-data",
    #             "hx-swap": "outerHTML",
    #         }
    #     )
    # )


class AccomplishmentUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Update Accomplishment",
                "name",
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


class AccomplishmentDeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Submit("submit", "Confirm deletion", css_class="btn-danger"),
        )
