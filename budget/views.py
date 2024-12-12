from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from budget.models import Budget
from budget.serializers import BudgetSerializer


# Create your views here.
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = BudgetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list(request):
    budgets = Budget.objects.all()
    serialization = BudgetSerializer(budgets, many=True)

    if serialization:
        return Response(serialization.data)

    return Response(serialization.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request, id):
    budget = Budget.objects.get(id=id)
    serializer = BudgetSerializer(instance=budget, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_one(request, id):
    budget = Budget.objects.get(id=id)
    serialization = BudgetSerializer(budget)

    if serialization:
        return Response(serialization.data)

    return Response(serialization.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request, id):
    budget = Budget.objects.get(id=id)
    budget.delete()
    return Response("Dette supprimer !!!")