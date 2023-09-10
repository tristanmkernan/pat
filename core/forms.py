from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit
from django import forms
from django.forms.widgets import ClearableFileInput
from django.utils import timezone

from .models import Accomplishment, Compliment


class RangeInput(forms.NumberInput):
    input_type = "range"


class AccomplishmentForm(forms.ModelForm):
    accomplishment_date = forms.DateField(
        initial=timezone.localdate,
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    def __init__(self, *args, **kwargs):
        common_tags = kwargs.pop("common_tags", None)

        super().__init__(*args, **kwargs)

        if common_tags:
            common_tags_display = ", ".join([tag.name for tag in common_tags])
            self.fields["tags"].help_text += f" Common tags: {common_tags_display}."

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Add Accomplishment"
                if self.instance is None
                else "Edit Accomplishment",
                "name",
                "accomplishment_date",
                "challenge",
                "reward",
                "notes",
                "image",
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
            "image",
            "tags",
        ]
        widgets = {
            "name": forms.TextInput(),
            "challenge": RangeInput(attrs={"min": 0, "max": 10, "class": "form-range"}),
            "reward": RangeInput(attrs={"min": 0, "max": 10, "class": "form-range"}),
            "image": ClearableFileInput(),
        }


class AccomplishmentDeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Submit("submit", "Confirm deletion", css_class="btn-danger"),
        )


class ComplimentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        common_tags = kwargs.pop("common_tags", None)
        common_sources = kwargs.pop("common_sources", None)

        super().__init__(*args, **kwargs)

        self.fields["description"].label = "Compliment"
        self.fields["source"].label = "From"

        if common_tags:
            common_tags_display = ", ".join([tag.name for tag in common_tags])
            self.fields["tags"].help_text += f" Common tags: {common_tags_display}."

        if common_sources:
            common_sources_display = ", ".join([source for source in common_sources])
            self.fields[
                "source"
            ].help_text += f" Common sources: {common_sources_display}."

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Edit Compliment" if self.instance is None else "Add Compliment",
                "source",
                "description",
                "tags",
            ),
            Submit("submit", "Submit"),
        )

    class Meta:
        model = Compliment
        fields = [
            "source",
            "description",
            "tags",
        ]
        widgets = {
            "source": forms.TextInput(),
        }


class ComplimentDeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Submit("submit", "Confirm deletion", css_class="btn-danger"),
        )
