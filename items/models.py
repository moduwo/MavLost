from django.conf import settings
from django.db import models

# Create your models here.
# model representing a lost or found item
class Item(models.Model):
    # link item to user who reported it
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                   on_delete=models.CASCADE, related_name="items",)
    # lost/found item name and description
    name = models.CharField(max_length=200)
    description = models.TextField()
    # item either lost or found
    report_type = models.CharField(max_length=5, 
                                   choices=[("lost", "Lost"), ("found", "Found"),], )
    # current status of lost/found item
    status = models.CharField(max_length=20, 
                              choices=[
                                  ("open", "Open"), 
                                  ("claim_in_review", "Claim in review"),
                                  ("claimed", "Claimed"), ("returned", "Returned"),
                                  ], default="open", )
    # when and where item was lost or found
    location = models.CharField(max_length=200)
    date_lost_or_found = models.DateField()

    # optional photo of lost/found item
    photo = models.ImageField(upload_to="items/", blank=True)

    # post creation date automatically set
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

