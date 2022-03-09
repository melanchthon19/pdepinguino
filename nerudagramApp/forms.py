from django import forms
from nerudagramApp.models import NerudagramModel
from nerudagramApp.nerudagram import ngram_pablo_neruda

translate_ngram = {1: 'unigram', 2: 'bigram', 3: 'trigram', 4: 'fourthgram'}

class NerudagramForm(forms.ModelForm):

    def generate_poem(self):
        ngram = self.cleaned_data['ngram']
        wpt = self.cleaned_data['wpt']
        mwpl = self.cleaned_data['mwpl']
        lpp = self.cleaned_data['lpp']
        title, poem = ngram_pablo_neruda.generate(
                                        ngram=translate_ngram[ngram],
                                        wpt=wpt, mwpl=mwpl, lpp=lpp)
        return (title, poem)

    class Meta:
        model = NerudagramModel
        fields = "__all__"
        widgets = {'title': forms.HiddenInput(),
                    'poem': forms.HiddenInput()}
