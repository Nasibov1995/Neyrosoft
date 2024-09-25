from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from main.models import Blog, Service, Contact, Portfolio, SiteSetting

class BlogSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Blog)

    class Meta:
        model = Blog
        fields = ['translations', 'status', 'view_count', 'created_at', 'updated_at']

class ServiceSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Service)

    class Meta:
        model = Service
        fields = ['translations', 'created_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class PortfolioSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Portfolio)

    class Meta:
        model = Portfolio
        fields = ['translations', 'image', 'created_at']

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSetting
        fields = ['logo', 'navbar_items']