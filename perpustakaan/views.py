from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response    
from rest_framework.views import APIView    



def perpus(request, pk):
    return HttpResponse("Ini adalah halaman perpustakaan dengan ID " + str(pk))


@api_view(['GET', 'POST'])
def perpusHome(request):
    return Response({"data" : 'helo'})


class PerpusHome(APIView):
    def post(self, req):

        return Response