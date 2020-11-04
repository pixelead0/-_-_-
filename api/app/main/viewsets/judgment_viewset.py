
# Django REST Framework
from rest_framework import generics

# Models
from app.main.models import Judgment

# Serializers
from app.main.serializers import JudgmentSerializer


class JudgmentCreate(generics.CreateAPIView):
    queryset = Judgment.objects.actives()
    serializer_class = JudgmentSerializer
