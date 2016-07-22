from rest_framework import serializers

from .models import User, Post

class UserSerializer(serializers.Model):
	posts = serializers.HyperlinkedIdentityField('post', view_name='userpost-list', lookup_field='username')

	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email', 'posts', )

class PostSerializer(serializers.ModeSerializer):
	author = UserSerializer(required=False)

	def get_validation_exclusions(self):
		exclusions = super(PostSerializer, self).get_validation_exclusions()
		return exclusions + ['author']

	class Meta:
		model = Post