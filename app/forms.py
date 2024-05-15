from django import forms

class FiltroForm(forms.Form):
    nome = forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'filtro.submit(); '}))
    categoria = forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'filtro.submit(); '}))
    turma = forms.ChoiceField(widget=forms.Select(attrs={'onchange': 'filtro.submit(); '}))
    order = forms.ChoiceField(choices=[(0, 'Mais recentes'), (1, 'Mais antigos'), (2, 'A-z'), (3, 'Z-a')], widget=forms.Select(attrs={'onchange': 'filtro.submit(); '}))

    def __init__(self, *args, **kwargs):
        super(FiltroForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-select'
    
        self.fields['nome'].widget.attrs['class'] ="form-control border selectpicker"
        self.fields['nome'].widget.attrs['data-live-search'] = "true"
        self.fields['nome'].widget.attrs['data-live-search-style'] = "startsWith"

        self.fields['turma'].widget.attrs['class'] ="form-control border selectpicker"
        self.fields['turma'].widget.attrs['data-live-search'] = "true"
        self.fields['turma'].widget.attrs['data-live-search-style'] = "contains"

        self.fields['categoria'].widget.attrs['class'] ="form-control border selectpicker"
        self.fields['order'].widget.attrs['class'] ="form-control border selectpicker"