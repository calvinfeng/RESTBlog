from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        print "Inside PostCreateUpdateSerializer #create"
        return super(PostCreateUpdateSerializer, self).create((validated_data))

    def validate(self, data):
        print "Validate all data"
        return data

    def validate_title(self, title):
        print "Validate title"
        return title


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'user',
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]
