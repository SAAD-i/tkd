from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.shortcuts import get_object_or_404
from .models import Tool, ToolCategory, ToolUsage
from .serializers import ToolSerializer, ToolCategorySerializer, ToolUsageSerializer



class ToolView(APIView):
    def get(self, request, id):
        tool = get_object_or_404(Tool, id=id)
        serializer = ToolSerializer(tool, many=False)
        if serializer:
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        tool = ToolSerializer(data = request.data, many=False)
        if tool.is_valid():
            tool.save()
            return Response(tool.data, status.HTTP_200_OK)
        return Response(tool.errors, status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id):
        tool = get_object_or_404(Tool, id = id)
        if tool:
            tool.delete()
            serializer = ToolSerializer(tool, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        tool = get_object_or_404(Tool, id=id)
        if tool:
            tool.name = request.data['name']
            tool.category = request.data['category']
            tool.is_enabled = request.data['is_enabled']
            tool.free_limit = request.data['free_limit']
            tool.free_mb_limit = request.data['free_mb_limit']
            tool.pro_limit = request.data['pro_limit']
            tool.save()
            serializer = ToolSerializer(tool, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

class ToolsView(APIView):
    def get(self, request):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        if serializer:
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    

class ToolUsageView(APIView):
    def get(self, request, id):
        tool_usage = get_object_or_404(ToolUsage, id = id)
        serializer = ToolUsageSerializer(tool_usage, many=False)
        if serializer:
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        tool_usage = ToolUsageSerializer(data = request.data, many=False)
        if tool_usage.is_valid():
            tool_usage.save()
            return Response(tool_usage.data, status.HTTP_200_OK)
        return Response(tool_usage.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        tool_usage = get_object_or_404(ToolUsage, id=id)
        if tool_usage:
            tool_usage.delete()
            serializer = ToolUsageSerializer(tool_usage, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    
class ToolsUsageView(APIView):
    def get(self, request):
        tools_usage = ToolUsage.objects.all()
        serializer = ToolUsageSerializer(tools_usage, many=True)
        if serializer:
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
    
class ToolCategoryView(APIView):
    def get(self, request, id):
        tool_category = get_object_or_404(ToolCategory, id=id)
        serializer = ToolCategorySerializer(tool_category, many=False)
        if serializer:
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        tool_category = ToolCategorySerializer(data = request.data, many=False)
        if tool_category.is_valid():
            tool_category.save()
            return Response(tool_category.data, status.HTTP_200_OK)
        return Response(tool_category.errors, status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        tool_category = get_object_or_404(ToolCategory, id=id)
        if tool_category:
            tool_category.name = request.data['name']
            tool_category.desc = request.data['desc']
            tool_category.save()
            serializer = ToolCategorySerializer(tool_category, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        
    def delete(self, request, id):
        tool_category = get_object_or_404(ToolCategory, id=id)
        if tool_category:
            tool_category.delete()
            serializer = ToolCategorySerializer(tool_category, many=False)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    
class ToolCategoriesView(APIView):
    def get(self, request):
        tool_categories = ToolCategory.objects.all()
        serializer = ToolCategorySerializer(tool_categories, many=False)
        if serializer:
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



#All Tools Code will be written here.