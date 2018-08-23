from django import forms
from django.forms import Textarea
from questions.models import Case
from common.models import Comment, Comment_2_Comment, LegalAidOrg, User
from questions.models import UploadFile
from django.forms.widgets import CheckboxSelectMultiple
from tinymce.widgets import TinyMCE

class DocumentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Document Name'})
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Document Description'})


    # name = forms.CharField()
    class Meta:
        model = UploadFile
        fields = ('name','description','file_type', 'document', )


class CaseForm(forms.ModelForm):
    # visible = forms.ModelMultipleChoiceField(queryset=LegalAidOrg.objects.all())
    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs = {"class": "form-control"}
        # self.fields['visible_to'].queryset = LegalAidOrg.objects.all()
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Title'})
        self.fields['related_document_name'].widget.attrs.update({
            'placeholder': 'Document Title'})
        self.fields['related_document_desc'].widget.attrs.update({
            'placeholder': 'Document Description (Optional)'})
        self.fields['issue_summary'].widget.attrs.update({
            'placeholder': 'Summary'})
        self.fields['issue_detail'].widget.attrs.update({
            'placeholder': 'Details', 'widget':'Textarea'})
        self.fields['related_cite'].widget.attrs.update({
            'placeholder': 'Case Citation - 123 So.2d 456'})

        self.fields['related_document_name'].required = False
        self.fields['rel_statute_link'].required = False
        self.fields['related_document'].required = False
        self.fields['related_document_desc'].required = False
        self.fields['issue_detail'].required = False
        self.fields['issue_summary'].required = False
        # self.fields['issue_area'].required = False
        self.fields['related_cite'].required = False
        # self.fields['visible_to'].choices = LegalAidOrg.objects.all()
        self.fields['visible_to'].widget = CheckboxSelectMultiple()
        self.fields["visible_to"].queryset = LegalAidOrg.objects.all()
        # issue_detail = forms.CharField(widget=forms.Textarea)
        issue_detail = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Case
        # widgets = {
        #     'issue_detail': Textarea(attrs={'size': 80, 'rows': 20, 'title':'issue_detail'})
        # }
        fields = ('title', 'issue_area', 'related_document_name',
        'rel_statute_link', 'issue_summary', 'issue_detail',
        'related_document', 'related_document_desc', 'related_cite',
        'visible_to'
        )

    def clean_name(self):
        name = self.cleaned_data['title']

        case = Case.objects.filter(name__iexact=name).exclude(id=self.instance.id)
        # if case:
        #     raise forms.ValidationError("Case Already Exists with this Name")
        # return name


class CaseCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CaseCommentForm, self).__init__(*args, **kwargs)
        comment = forms.CharField(max_length=1000, required=True)
        self.fields['related_document'].required = False


    class Meta:
        model = Comment
        fields = ('comment', 'case', 'commented_by', 'related_document' )


class CommentCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentCommentForm, self).__init__(*args, **kwargs)
        comment = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = Comment_2_Comment
        fields = ('comment', 'commented_by')
