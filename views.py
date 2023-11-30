# email_validation/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, generics
from .models import ValidatedEmail
from .serializers import ValidatedEmailSerializer
from django.core.exceptions import ValidationError

class ValidatedEmailListCreateView(generics.ListCreateAPIView):
    queryset = ValidatedEmail.objects.all()
    serializer_class = ValidatedEmailSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', None)

        if email:
            # Perform email validation logic here
            is_valid = self.is_valid_email(email)
            is_spam = self.is_spam_email(email)

            validated_email = ValidatedEmail.objects.create(email=email, is_valid=is_valid, is_spam=is_spam)
            serializer = self.get_serializer(validated_email)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Email not provided'}, status=status.HTTP_400_BAD_REQUEST)

    def is_valid_email(self, email):
        # Your email validation logic here (e.g., using regular expressions)
        # Return True if valid, False otherwise
        return True  # Placeholder logic, replace with actual validation

    def is_spam_email(self, email):
        # Simple spam check using spacy and common spam keywords
        try:
            import spacy

            nlp = spacy.load("en_core_web_sm")
            doc = nlp(email.lower())

            spam_keywords = ["win", "free", "click", "guarantee", "urgent"]

            for keyword in spam_keywords:
                if keyword in doc.text:
                    return True

            return False
        except Exception as e:
            print(f"Error in spam filtering: {e}")
            return False

class ValidatedEmailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ValidatedEmail.objects.all()
    serializer_class = ValidatedEmailSerializer
