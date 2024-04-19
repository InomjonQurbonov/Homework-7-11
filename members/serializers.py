from rest_framework import serializers
from members.models import Members, Organizations


class MembersSerializer(serializers.ModelSerializer):
    member_details = serializers.SerializerMethodField()

    def get_member_details(self, instance):
        return f'http://127.0.0.1:8000/members/members/detail/{instance}'

    class Meta:
        model = Members
        fields = ['id', 'memeber_name', 'member_president', 'member_image', 'member_details']


class MembersDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'


class CreateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['memeber_name', 'member_president', 'member_image', 'memmber_added_date']


class UpdateMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['memeber_name', 'member_president', 'member_image', 'memmber_added_date']


class DeleteMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', ]


class OrganizationsSerializer(serializers.ModelSerializer):
    organization_details = serializers.SerializerMethodField()

    def get_organization_details(self, instance):
        return f'http://127.0.0.1:8000/members/organizations/detail/{instance}'

    class Meta:
        model = Organizations
        fields = ['id', 'organization_name', 'organization_president', 'organization_logo', 'organization_details']


class OrganizationsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = '__all__'


class CreateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = ['organization_name', 'organization_president', 'organization_logo', 'organization_organizate_date']


class UpdateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = ['organization_name', 'organization_president', 'organization_logo', 'organization_organizate_date']


class DeleteOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['id', ]
