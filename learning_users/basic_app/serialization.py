from rest_framework import serializers
from .models import UserProfileInfo
class userserial(serializers.ModelSerializer):
    class Meta:
        model = UserProfileInfo
        fields = '__all__'
