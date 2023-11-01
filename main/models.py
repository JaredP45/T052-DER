from django.db import models


class Contact(models.Model):
    # TODO: Combine both classes for optional fields
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email


class ContactSupport(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        app_label  = 'main'

    def __str__(self):
        return self.email
