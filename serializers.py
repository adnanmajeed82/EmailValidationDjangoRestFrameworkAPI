# email_validation/serializers.py

from rest_framework import serializers
from .models import ValidatedEmail

class ValidatedEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidatedEmail
        fields = ['id', 'email', 'is_valid', 'is_spam']
