from rest_framework.generics import CreateAPIView, ListAPIView
from core.models import CustomUser
from core.api.serializers import UserCreateSerializer, WishlistSerializer, WishlistCreateSerializer, SiteSettingsSerializer
from core.models import Wishlist, SiteSettings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer


class WishlistListAPIView(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAdminUser,)    

class UserWishlistListAPIView(ListAPIView):
    def get_queryset(self):
        return Wishlist.objects.filter(
            user = self.request.user
        )  
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated,)

  
class WishlistCreateAPIView(CreateAPIView):
    queryset = Wishlist.objects.all()  
    serializer_class = WishlistCreateSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SiteSettingsListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer






        # Wishlist.objects.create(
        #     user = request.user,
        #     product = request.data["product"]
        # )
        # return Response(request.data, )


