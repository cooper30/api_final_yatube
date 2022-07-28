from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('pub_date', 'author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('user', )

    def validate_following(self, value):
        user = self.context['request'].user
        if value == user:
            raise serializers.ValidationError(
                'Нельзя подписываться на самого себя!'
            )
        if Follow.objects.filter(user=user, following=value).exists():
            raise serializers.ValidationError(
                'Подписка уже существует!'
            )
        return value
