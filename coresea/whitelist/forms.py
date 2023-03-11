from django import forms
from .models import wl


class wl_form(forms.ModelForm):
    pass

    class Meta:
        model = wl
        fields = '__all__'
        labels = {
                    'twitter': 'Twitter handle',
                    'metamask': 'Metamask wallet address',
                    'nft_address': 'NFT holding address',
                    'follow': 'I follow @CoreSeaFi on twitter',
                    'retweet' : 'I have retweet the Whitelist tweet',

                }
        widgets = {
            'metamask': forms.TextInput(attrs={'class': 'field'}),
            'twitter': forms.TextInput(attrs={'class': 'field'}),
            'nft_address': forms.TextInput(attrs={'class': 'field'}),
            'follow': forms.CheckboxInput(attrs= {'class' : 'checks'}),
            'retweet' : forms.CheckboxInput(attrs= {'class': 'checks'}),
            
        }