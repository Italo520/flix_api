from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from generos.models import Genero
from generos.serializers import GeneroSerializer




class GeneroListaCriarAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class GeneroRetrieveUpdateDestroiAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer







#Codigo antigo usando JsonResponse e csrf_exempt
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404 

# @csrf_exempt
# def criar_listar_generos_view(request):
#     if request.method == 'GET':
#         generos = Genero.objects.all()
#         dados = [{'id': genero.id, 'nome': genero.nome} for genero in generos]
#         return JsonResponse(dados,safe=False)
    
#     elif request.method == 'POST':
#         dados = json.loads(request.body.decode('utf-8'))
#         novo_genero = Genero(nome=dados['nome'])
#         novo_genero.save()
#         return JsonResponse({'id': novo_genero.id, 'nome': novo_genero.nome},status=201,)
    

# @csrf_exempt
# def detalhe_genero_view(request, pk):
#     genero = get_object_or_404(Genero, pk=pk)

#     if request.method == 'GET':
#         dado = {'id': genero.id, 'nome': genero.nome}
#         return JsonResponse(dado)

#     elif request.method == 'PUT':
#         dado = json.loads(request.body.decode('utf-8'))
#         genero.nome = dado['nome']
#         genero.save()
#         return JsonResponse({'id': genero.id, 'nome': genero.nome},status=200,)
    
#     elif request.method == 'DELETE':
#         genero.delete()
#         return JsonResponse({'message': 'Genero Excluido com sucesso.'}, status=204,)