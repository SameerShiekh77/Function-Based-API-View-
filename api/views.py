from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


# FUNCTION API VIEW

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def studentApi(request, pk=None):

    # GET ALL DATA FROM DATABASE
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


# POST DATA IN DATABASE
    elif request.method == 'POST':
        serializer = StudentSerializer(
            data=request.data, status=status.HTTP_201_CREATED)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data created", "data": serializer.data})
        return Response(serializer.errors)


# FOR COMPLETE UPDATE YOU NEED TO USE METHOD PUT
    elif request.method == 'PUT':
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(
                stu, data=request.data, status=status.HTTP_205_RESET_CONTENT)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "data complete updated", "data": serializer.data})
            return Response(serializer.errors)

# FOR PARTIALLY UPDATE DATA YOU NEED TO USE METHOD PATCH

    elif request.method == 'PATCH':
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(
                stu, data=request.data, partial=True, status=status.HTTP_206_PARTIAL_CONTENT)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "data partially updated", "data": serializer.data})
            return Response(serializer.errors)


# FOR DELETE

    elif request.method == "DELETE":
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "data deleted"})



# CLASS API VIEW
class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    

    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data created", "data": serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    def put(self,request,pk,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(
                stu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "data complete updated", "data": serializer.data}, status=status.HTTP_205_RESET_CONTENT)
            return Response(serializer.errors)

    def patch(self,request,pk,format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(
                stu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "data partially updated", "data": serializer.data}, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors)

    def delete(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "data deleted"})