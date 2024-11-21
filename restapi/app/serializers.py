from rest_framework import serializers

class user_serializer(serializers.Serializer):
    roll_no=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()
    