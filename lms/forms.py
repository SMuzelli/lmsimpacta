from django import forms

from django.core.mail import send_mail

ASSUNTOS = (
    ('B', 'Bug'),
    ('R', 'Reclamação'),
    ('S', 'Sugestão')
)

class ContatoForm(forms.Form):

    nome = forms.CharField(
        label="Nome Completo"
    )

    email = forms.EmailField(
        label="E-Mail"
    )

    assunto = forms.ChoiceField(
        label="Assunto",
        choices=ASSUNTOS
    )

    mensagem = forms.CharField(
        label="Mensagem",
        max_length=255,
        widget=forms.Textarea
    )

    def enviar_email(self):
        send_mail(
            'Mensagem Assunto '+self.get_assunto_display(),
            self.cleaned_data['mensagem'],
            from_email,
            [recepient]
        )