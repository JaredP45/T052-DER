from django.db import models


class ContactSupport(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    file_upload = models.FileField(
        upload_to='contact/submissions/documents/',
        help_text='max. 42 megabytes',
        blank=True,
        default='contact/submissions/documents/default.txt'
    )

    class Meta:
        app_label  = 'main'

    def __str__(self):
        return self.subject
