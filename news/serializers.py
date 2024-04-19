from rest_framework import serializers
from .models import News, OurWorks


class NewsSerializer(serializers.ModelSerializer):
    news_detail = serializers.SerializerMethodField('get_news_detail')

    def get_news_detail(self, instance):
        return f"http://127.0.0.1:8000/news/detail/{instance.pk}"

    class Meta:
        model = News
        fields = ['id', 'news_title', 'news_date', 'news_author', 'news_image', 'news_detail']


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CreateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['news_title', 'news_description', 'news_image', 'news_author', 'news_content']


class UpdateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['news_title', 'news_description', 'news_image', 'news_author', 'news_content']


class DeleteNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', ]


class OurWorksSerializer(serializers.ModelSerializer):
    works_detail = serializers.SerializerMethodField('get_works_detail')

    def get_works_detail(self, instance):
        return f"http://127.0.0.1:8000/news/works/detail/{instance.pk}"

    class Meta:
        model = OurWorks
        fields = ['id', 'work_title', 'work_date', 'work_image', 'works_detail']


class OurWorksDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorks
        fields = '__all__'


class CreateOurWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorks
        fields = ['work_title', 'work_description', 'work_image', 'workers', 'work_date']


class UpdateOurWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorks
        fields = ['work_title', 'work_description', 'work_image', 'workers', 'work_date']


class DeleteOurWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurWorks
        fields = ['id', ]
