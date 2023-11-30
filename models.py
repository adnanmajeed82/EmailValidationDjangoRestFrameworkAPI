# email_validation/models.py

from django.db import models

class ValidatedEmail(models.Model):
    email = models.EmailField(unique=True)
    is_valid = models.BooleanField(default=False)
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return self.email
 