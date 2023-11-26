from django.db import models


class uploader(models.Model):
    uploader_name=models.CharField(max_length=30)
    uploader_last=models.CharField(max_length=30)
    uploader_add=models.CharField(max_length=40)
    uploader_type=models.CharField(max_length=35)
    uploader_img=models.ImageField(upload_to='uploader',blank=True)
                            
