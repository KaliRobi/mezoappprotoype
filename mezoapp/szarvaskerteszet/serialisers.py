from rest_framework import serializers

from .models import OwnerDetails, BusinessDetails, BusinessTypes

class OwnerDetailsSerialzier(serializers.ModelSerializer):
    
    class Meta:
        model = OwnerDetails
        fields =  '__all__'
        read_only_fields = ['id',
                            'inser_time',
                            ]


class BusinessTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessTypes
        fields = '__all__'
        read_only_fields = '__app__'



class BusinessDetailsSerializer(serializers.ModelSerializer):
    owner = OwnerDetailsSerialzier(read_only=True)
    type_of_business = BusinessTypeSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(queryset=OwnerDetails.objects.all(), source='owner')
    type_of_business_id = serializers.PrimaryKeyRelatedField(queryset=BusinessTypes.objects.all(), source='type_of_business')

    class Meta:
        model = BusinessDetails
        fields = '__all__' 
        read_only_fields = ['id']

    def create(self, validated_data):
        owner = validated_data.pop('owner')
        type_of_business = validated_data.pop('type_of_business')
        business_details = BusinessDetails.objects.create(owner=owner, type_of_business=type_of_business, **validated_data)
        return business_details