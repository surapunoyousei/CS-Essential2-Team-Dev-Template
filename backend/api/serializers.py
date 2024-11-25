from rest_framework import serializers
from app.models import User_Model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Model
        fields = ('user_id', 'user_name','user_email')
