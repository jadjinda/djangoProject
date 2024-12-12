from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UtilisateurSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
@api_view(["POST"])
@permission_classes([AllowAny])
def inscription(request):
    serializer = UtilisateurSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)

        serializer = UtilisateurSerializer(user)

        data = {
            "user": serializer.data,
            "token": token.key
        }

        return Response(data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([AllowAny])
def connexion(request):
    data = request.data
    authenticate_user = authenticate(username=data['username'],
                                     password=data['password'])

    if authenticate_user is not None:
        user = User.objects.get(username=data['username'])
        serializer = UtilisateurSerializer(user)

        #token generation
        refresh = RefreshToken.for_user(authenticate_user)

        response_data = {
            'user': serializer.data,
            'bearer': str(refresh.access_token),
        }
        #token, created_token = Token.objects.get_or_create(user=user)

        #if token:
        #    response_data['token'] = token.key
        #elif created_token:
        #    response_data['token'] = created_token.key

        return Response(response_data)

    return Response({"detail": "User Not found"}, status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def profilUser(request):
    user_info = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "username": request.user.username
    }
    return Response(user_info)

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def TestView(request):
    if request.user.is_authenticated:
        return Response({"message": f"Bienvenue, {request.user.username} !"})
    else:
        return Response({"error": "Non authentifié"}, status=401)


@api_view(["POST"])
@permission_classes([AllowAny])
def refreshToken(request):
    refresh_token = request.data.get('refresh')  # Le jeton de rafraîchissement envoyé par le client

    if not refresh_token:
        return Response({"detail": "Refresh token is required"}, status=HTTP_400_BAD_REQUEST)

    try:
        # Vérifie et décode le refresh token
        refresh = RefreshToken(refresh_token)

        # Génère un nouveau access token
        access_token = str(refresh.access_token)

        return Response({
            "access": access_token,  # Nouveau jeton d'accès
        })
    except TokenError as e:
        return Response({"detail": "Invalid or expired refresh token"}, status=HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def deconnexion():
    pass