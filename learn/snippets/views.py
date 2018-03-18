from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.response import Response 
from snippets.models import Snippnet
from snippets.serializer import SnippetsSerializer 

import logging

logger = logging.getLogger("__name__")
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new Snippnet.
    """
    logger.info(request.data);
    if request.method == 'GET':
        snippets = Snippnet.objects.all()
        Snippnet.objects.filter()
        serializer = SnippetsSerializer(snippets, many=True)
        logging.info(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logging.info(serializer.data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippnet.objects.get(pk=pk)
    except Snippnet.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = SnippetsSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=204)
    
    
'''
We can also write our API views using class-based views, rather than function based views. 
As we'll see this is a powerful pattern that allows us to reuse common functionality, and 
helps us keep our code DRY.
'''
