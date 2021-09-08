from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
# User = get_user_model()
from blog.models import User2


class UserAvatarSerializer(ModelSerializer):
    class Meta:
        model = User2
        fields = ["avatar"]

    def save(self, *args, **kwargs):
        if self.instance.avatar:
            self.instance.avatar.delete()
        return super().save(*args, **kwargs)