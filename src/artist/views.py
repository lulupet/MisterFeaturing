from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Artist
from .utils import build_graph, find_shortest_path, get_detailed_path


def home_view(request):
    return render(request, 'home.html')


@api_view(['POST'])
def get_featuring_view(request):
    artist_name_1 = request.data['artist_1']
    artist_name_2 = request.data['artist_2']
    try:
        artist_1 = Artist.objects.get(name=artist_name_1)
    except Artist.DoesNotExist:
        return Response(status.HTTP_400_NOT_FOUND, data={})
    try:
        artist_2 = Artist.objects.get(name=artist_name_2)
    except Artist.DoesNotExist:
        return Response(status.HTTP_400_NOT_FOUND, data={})
    graph = build_graph()
    path = find_shortest_path(graph, str(artist_1.id), str(artist_2.id))
    if path in ['no existing path', 'same artists']:
        return Response(status.HTTP_400_NOT_FOUND, data={})
    else:
        detailed_path = get_detailed_path(path)
        return Response(status.HTTP_200_OK, data={'path': detailed_path})
