from rest_framework import serializers
from .models import vacations


class vacationSerializer(serializers.ModelSerializer):

    class Meta:
        model = vacations
        fields = (
            'id', 'user_name', 'from_date_time', 'to_date_time', 'description'
        )

