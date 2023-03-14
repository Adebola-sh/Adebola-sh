from django import forms
from .models import wl


class wl_form(forms.ModelForm):
    pass

    class Meta:
        model = wl
        fields = '__all__'
        labels = {
                    'twitter': 'Twitter handle',
                    'discord': 'Discord handle',
                    'metamask': 'Submit wallet address',
                    'nft_address': 'NFT holding address',
                    'follow': 'I follow CoreSea on twitter',
                    'retweet' : 'I have retweeted',

                }
        widgets = {
            'metamask': forms.TextInput(attrs={'class': 'field'}),
            'discord': forms.TextInput(attrs={'class': 'field'}),
            'twitter': forms.TextInput(attrs={'class': 'field'}),
            'nft_address': forms.TextInput(attrs={'class': 'field'}),
            'follow': forms.CheckboxInput(attrs= {'class' : 'checks'}),
            'retweet' : forms.CheckboxInput(attrs= {'class': 'checks'}),
            
        }