from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

class UtilisateurSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password']

    def save(self, **kwargs):
        new_user = User.objects.create_user(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            password=self.validated_data['password']
        )
        new_user.save()

        #new_token = Token.objects.create(user=new_user)

        return new_user
