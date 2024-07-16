from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view
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
        serializer = ToolCategorySerializer(tool_categories, many=True)
        if serializer:
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



#All Tools Code will be written here.
from rest_framework.parsers import MultiPartParser, FormParser
import base64
from io import BytesIO
from rembg import remove
from PIL import Image

class RemoveImageBackgroundTool(APIView):
    
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        image_file = request.FILES['image']
        if image_file:
            image = Image.open(image_file)
            output = remove(image)
            buffer = BytesIO()
            output.save(buffer, format='PNG')
            buffer.seek(0)
            encoded_image = base64.b64encode(buffer.read()).decode('utf-8')
            return Response(status=status.HTTP_200_OK, data=encoded_image)
        return Response(status=status.HTTP_400_BAD_REQUEST, message="Image not found")

        
class JpgToPngTool(APIView):
    
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        image_file = request.FILES['image']
        if image_file:
            image = Image.open(image_file)
            buffer = BytesIO()
            image.save(buffer, format='PNG')
            buffer.seek(0)
            encoded_image = base64.b64encode(buffer.read()).decode('utf-8')
            return Response(status=status.HTTP_200_OK, data=encoded_image, content_type='image/png')
        return Response(status=status.HTTP_400_BAD_REQUEST, message="Image not found")
    
class PngToJpegTool(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request):
        try:
            image_file = request.FILES.get('image')
            if image_file:
                image = Image.open(image_file)
                buffer = BytesIO()
                # Convert PNG to JPEG
                image.convert('RGB').save(buffer, format='JPEG')
                buffer.seek(0)
                # Encode to base64
                encoded_image = base64.b64encode(buffer.read()).decode('utf-8')
                return Response(data={'encoded_image': encoded_image}, status=status.HTTP_200_OK)
            else:
                return Response(data={'message': 'Image not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class ImageToTextTool(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#     def(self, request):
#         image_file = request.files['image']
#         extracted_text = ''
#         image_data = np.fromstring(image_file.read(), np.uint8)
#         image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
#         if image is not None:
#             gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#             extracted_text = pytesseract.image_to_string(gray_image)
#             return extracted_text
#         else:
#             return "Error: Could not read the uploaded image."