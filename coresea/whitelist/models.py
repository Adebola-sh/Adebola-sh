from django.db import models

#Create your models here.

class wl(models.Model):
    twitter = models.CharField(max_length=100, help_text='Follow Twitter & Retweet pinned post', unique= True)
    discord = models.CharField(max_length=100, unique= True, help_text= 'Join discord')
    metamask = models.CharField(max_length=50,)
    nft_address = models.CharField(max_length=50, 
            help_text='Hold any of these NFT (Moondogs, CorepunksV2,Core Id) Submit wallet address of holding')
    follow = models.BooleanField()
    retweet = models.BooleanField()
    


    def __str__(self) -> str:
        return self.twitter