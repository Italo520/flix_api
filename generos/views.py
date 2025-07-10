import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from generos.models import Genero


@csrf_exempt
def genero_view(request):
    if request.method == 'GET':
        generos = Genero.objects.all()
        dados = [{'id': genero.id, 'nome': genero.nome} for genero in generos]
        return JsonResponse(dados,safe=False)
    
    elif request.method == 'POST':
        dados = json.loads(request.body.decode('utf-8'))
        novo_genero = Genero(nome=dados['nome'])
        novo_genero.save()
        return JsonResponse({'id': novo_genero.id, 'nome': novo_genero.nome},status=201,)