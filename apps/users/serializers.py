from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['phone', 'email', 'name', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            phone=validated_data['phone'],
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        phone = data.get("phone")
        password = data.get("password")
        if phone and password:
            try:
                user = CustomUser.objects.get(phone=phone)
                if not user.check_password(password):
                    raise serializers.ValidationError("Incorrect password.")
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("User does not exist.")
        else:
            raise serializers.ValidationError("Both phone and password are required.")
        data['user'] = user
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone', 'email', 'name']
