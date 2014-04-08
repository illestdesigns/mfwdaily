from django.db import models

# Create your models here.

class MFW(models.Model):

    def __unicode__(self):
		return self.mfw_title

    mfw_title = models.CharField(max_length=200)
    mfw_date = models.DateField()
    mfw_text = models.CharField(max_length=200)
    #mfw_link = models.ForeignKey(CoinWebsite, blank=True, null=True)
 
    #objects = CoinManager()
    #scrape = models.CharField(max_length=200)
    #cash_value = models.FloatField(blank=True, null=True, editable=False)
 
    mfw_img_num = models.CharField(max_length=300)
    mfw_img_alt = models.CharField(max_length=200)
    
    mfw_img_width = models.IntegerField()
    mfw_img_height = models.IntegerField()

    active = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

class MFWLink(models.Model):

    def __unicode__(self):
		return self.mfw_content_text

    mfw_content_link = models.URLField()
    mfw_content_text = models.CharField(max_length=200)
    mfw_object = models.ForeignKey(MFW, blank=True, null=True)

class TestLink(models.Model):

    def __unicode__(self):
		return self.mfw_content_text

    mfw_content_link = models.URLField()
    mfw_content_text = models.CharField(max_length=200)
    mfw_object = models.ForeignKey(MFW, blank=True, null=True)