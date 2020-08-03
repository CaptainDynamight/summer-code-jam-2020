from django import forms

from .models import Quiz


def validate_answer(answer):
    if len(answer) > 4 and 2020 < int(answer) < 1950:
        raise forms.ValidationError('Please input year in the form "yyyy", between 1950 and 2020')
    return answer


class QuizForm(forms.ModelForm):
    answer = forms.CharField(
        validators=[validate_answer],
        required=True,
        max_length=4,
        help_text="Enter the approximate year in the form 'yyyy'"
    )

    class Meta:
        model = Quiz
        fields = ('answer', )
