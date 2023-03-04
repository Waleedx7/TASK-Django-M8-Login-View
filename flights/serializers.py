from rest_framework import serializers


from .models import Booking, Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["destination", "time", "price", "id"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "id"]


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "passengers", "id"]


class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["date", "passengers"]




# class UserLogin(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def vaidate(self, data):
#         my_username = data.get("username")
#         my_password = data.get("password")

#         try: 
#             user_obj = User.objects.get(username=my_username)
#         except User.DoesNotExist:
#             raise serializers.ValidationError("This username does not exist")
#         if not user_obj.check_password(my_password):
#             raise serializers.ValidationError("Incorrect username/password combination!")
#         return data
    