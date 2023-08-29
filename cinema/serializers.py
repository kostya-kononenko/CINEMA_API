from rest_framework import serializers

from cinema.models import Movie


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "tagline", "category")


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ("draft", )
