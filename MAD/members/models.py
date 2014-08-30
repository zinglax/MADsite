from django.db import models
import datetime

# Models for the MAD Club


    
########################################################################
class Meeting(models.Model):
    """ Meeting Information """
    
    # Date
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)    
    
    # Notes
    notes = models.CharField(max_length=500, blank=True, null=True)  
    
    # QRcode ex. MAD128
    qr_code = models.CharField(max_length=150, blank=True, null=True)
    

    #----------------------------------------------------------------------
    def __unicode__(self):
        return self.name

    
########################################################################
class Member(models.Model):
    """ Each Member of the club """
    
    # Name
    name = models.CharField(max_length=150)
    
    # Description
    description = models.CharField(max_length=500, blank=True, null=True) 
    
    # QRcode ex. MAD128
    qr_code = models.CharField(max_length=150, blank=True, null=True)
    
    # Meetings
    meetings = models.ManyToManyField(Meeting, blank=True, null=True)
    
    # Email
    email = models.EmailField(blank=True, null=True)
    

    #----------------------------------------------------------------------
    def __unicode__(self):
        return self.name        
        
    
    
