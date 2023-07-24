from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from task.models import Position, Project, Task, Team, Worker


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
             "first_name", "last_name", "position"
        )


class WorkerUpdateForm(forms.ModelForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all())

    class Meta:
        model = Worker
        fields = ["first_name", "last_name", "position"]


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    priority = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Task.PRIORITY
        )

    deadline = forms.DateTimeField(
        widget=forms. DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class TeamSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class ProjectForm(forms.ModelForm):
    team = forms.ModelMultipleChoiceField(
        queryset=Team.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    status = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Project.STATUS_CHOICES
        )

    class Meta:
        model = Project
        fields = "__all__"


class TeamForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Team
        fields = "__all__"
