from django import forms
from django.forms import Textarea
from questions.models import Case
from common.models import Comment
from questions.models import UploadFile
from knowledge_base.models import KB_Item

class KnowledgebaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(KnowledgebaseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}


        self.fields['title'].widget.attrs.update({
            'placeholder': 'Title'})
        self.fields['kb_area'].widget.attrs.update({
            'label': 'Area'})
        self.fields['citation'].widget.attrs.update({
            'placeholder': 'Citation'})
        self.fields['judge'].widget.attrs.update({
            'placeholder': 'Judge'})
        self.fields['statute_chapter'].widget.attrs.update({
            'placeholder': 'Statute Chapter'})
        self.fields['statute_number'].widget.attrs.update({
            'placeholder': 'Statute Number'})
        self.fields['statute_heading'].widget.attrs.update({
            'placeholder': 'Statute Heading'})
        self.fields['body'].widget.attrs.update({
            'placeholder': 'Body', 'widget':'Textarea'})

        self.fields['judge'].required = False
        self.fields['citation'].required = False
        self.fields['statute_chapter'].required = False
        self.fields['statute_number'].required = False
        self.fields['statute_heading'].required = False
        self.fields['trigger'].required = False
        self.fields['aff_resp'].required = False
        self.fields['neg_resp'].required = False
        self.fields['body'].required = False
        self.fields['plain_body'].required = False

        issue_detail = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = KB_Item
        widgets = {
            'body': Textarea(attrs={'size': 80, 'rows': 20, 'title':'body'})
        }
        fields = (
                'kb_area',
                'kb_type',
                'title',
                'citation',
                'judge',
                'statute_chapter',
                'statute_number',
                'statute_heading',
                'state',
                'body',
                'plain_body',
                'kb_area',
                'trigger',
                'aff_resp',
                'neg_resp',
                )

    def clean_name(self):
        name = self.cleaned_data['title']

        kb_item = KB_Item.objects.filter(name__iexact=name).exclude(id=self.instance.id)
