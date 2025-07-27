from rest_framework import serializers
from .models import (
    BmbcChecksheet, BogieChecksheet, BogieDetails, BogieChecksheetForm,
    WheelFields, WheelSpecificationForm
)

# BOGIE CHECKSHEET SERIALIZERS

class BmbcChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BmbcChecksheet
        fields = '__all__'

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields = '__all__'

class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieDetails
        fields = '__all__'

class BogieChecksheetFormSerializer(serializers.ModelSerializer):
    bmbcChecksheet = BmbcChecksheetSerializer()
    bogieChecksheet = BogieChecksheetSerializer()
    bogieDetails = BogieDetailsSerializer()

    class Meta:
        model = BogieChecksheetForm
        fields = '__all__'

    def create(self, validated_data):
        bmbc_data = validated_data.pop('bmbcChecksheet')
        bogie_data = validated_data.pop('bogieChecksheet')
        details_data = validated_data.pop('bogieDetails')

        bmbc = BmbcChecksheet.objects.create(**bmbc_data)
        bogie = BogieChecksheet.objects.create(**bogie_data)
        details = BogieDetails.objects.create(**details_data)

        return BogieChecksheetForm.objects.create(
            bmbcChecksheet=bmbc,
            bogieChecksheet=bogie,
            bogieDetails=details,
            **validated_data
        )

# WHEEL SPECIFICATION SERIALIZERS

class WheelFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelFields
        fields = '__all__'

class WheelSpecificationFormSerializer(serializers.ModelSerializer):
    fields = WheelFieldsSerializer()

    class Meta:
        model = WheelSpecificationForm
        fields = '__all__'
