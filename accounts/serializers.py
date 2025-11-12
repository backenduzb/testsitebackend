from rest_framework import serializers
from .models import User, Class
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import generate_username
from scores.serializers import ScoreSerialzer

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class_name = ClassSerializer(read_only=True)
    scores = ScoreSerialzer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'class_name', 'scores']

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        
        data = super().validate(attrs)
        
        data['username'] = self.user.username


        return data

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    password2 = serializers.CharField(write_only=True, required=False)
    class_name =serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'password', 'password2', 'class_name']
        extra_kwargs     = {
            'username': {'required': False}
        }
    
    def validate(self, data):
            password = data.get('password')
            password2 = data.get('password2')

            if password or password2:
                if password != password2:
                    raise serializers.ValidationError({"password": "Parollar mos emas"})
            return data

    def create(self, validated_data):
        full_name = validated_data.get('full_name', 'user')
        usps = generate_username(full_name)

        username = usps

        password = usps
        password2 = usps

        if not password and not password2:
            auto_password = usps
            password = auto_password
            password2 = auto_password

        if password != password2:
            raise serializers.ValidationError({"password": "Parollar mos emas"})
        
        sinfi = Class.objects.get(name=validated_data.get('class_name'))
        print(sinfi.id)
        user = User(
            username=username,
            full_name=full_name,
            class_name=sinfi
        )
        user.set_password(password)
        user.save()
        self._generated_username = username
        self._generated_password = password

        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['username'] = getattr(self, '_generated_username', instance.username)
        rep['password'] = getattr(self, '_generated_password', None)
        rep['password2'] = getattr(self, '_generated_password', None)  
        return rep        