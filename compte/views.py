from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from compte.models import Compte
from compte.serializers import CompteSerializer


# Create your views here.
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = CompteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list(request):
    comptes = Compte.objects.all()
    serialization = CompteSerializer(comptes, many=True)

    if serialization:
        return Response(serialization.data)

    return Response(serialization.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    compte = Compte.objects.get(id=id)
    serializer = CompteSerializer(instance=compte, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_one(request, id):
    compte = Compte.objects.get(id=id)
    serialization = CompteSerializer(compte)

    if serialization:
        return Response(serialization.data)

    return Response(serialization.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    compte = Compte.objects.get(id=id)
    compte.delete()
    return Response("Compte supprimer !!!")