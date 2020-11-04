from app.main.models import Judgment
from rest_framework import serializers


class JudgmentSerializer(serializers.ModelSerializer):
    """Judgment Serializer."""

    class Meta:
        model = Judgment
        read_only_fields = (
            "actor",
            "defendant",
            "court",
            "state",
            "case_file",
            "notifications",
            "resume",
        )

        exclude = (
            "is_active",
            "created_at",
            "updated_at",
        )
