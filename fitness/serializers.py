from rest_framework import serializers

from .models import Weight

class WeightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weight
        fields = ['weight_weight', 'weight_date']