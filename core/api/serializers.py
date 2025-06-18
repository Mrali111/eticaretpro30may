from rest_framework import serializers
from core.models import Product, Wishlist, SiteSettings, CustomUser
from django.contrib.auth.password_validation import validate_password

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser 
        fields = ("username", "password")


    def validate(self, data):
        validate_password(data["password"])
        return data
    
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]

        user = CustomUser.objects.create_user(
            username = username,
            password = password  
        )
        # user.set_password(password)
        # user.save()
        return user
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserCreateSerializer()
    class Meta:
        model = Wishlist
        fields = "__all__"


class WishlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("product",)

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"





        

