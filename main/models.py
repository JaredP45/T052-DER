from django.db import models


class ContactSupport(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        app_label  = 'main'

    def __str__(self):
        return self.subject
