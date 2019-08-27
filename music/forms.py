from django import forms
from django.contrib.auth.models import User

from .models import Vocabulary, Predict, Topic

STATUS_CHOICES = (
    (1, "NOUN"),
    (2, "VERB"),
    (3, "ADJECTIVE"),
    (4, "ADVERB"),
)


class VocabularyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VocabularyForm, self).__init__(*args, **kwargs)
        self.fields['type'] = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Vocabulary
        fields = ['vocabulary_title', 'type', 'story', 'mean']


class PredictForm(forms.ModelForm):
    class Meta:
        model = Predict
        fields = ['vocabulary', 'predict_txt']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_title', 'topic_logo']


#
# class SongForm(forms.ModelForm):
#     class Meta:
#         model = Song
#         fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
