from rest_framework import serializers
from .models import Listing, Booking, Review
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate_price(self, value):
        if value <= 0:
            raise ValidationError(_("Price must be a positive number."))
        return value


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('created_at',)

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise ValidationError(_("End date must be after start date."))
        return data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('created_at',)

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise ValidationError(_("Rating must be between 1 and 5."))
        return value


# class ListingImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ListingImage
#         fields = '__all__'
#         read_only_fields = ('created_at',)

#     def validate_image(self, value):
#         if not value.name.lower().endswith(('.png', '.jpg', '.jpeg')):
#             raise ValidationError(_("Image must be a PNG or JPEG file."))
#         return value
