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




import io
from django.http import FileResponse
from rest_framework.parsers import JSONParser
from gtts import gTTS
class TextToAudioTool(APIView):
    parser_classes = [JSONParser]
    
    def post(self, request):
        text = request.data.get('text', '')
        if not text:
            return Response({'message': 'Text field is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Generate audio using gTTS
        tts = gTTS(text)
        
        # Create a BytesIO object to store the audio
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        # Create a FileResponse object to send the audio file
        response = FileResponse(fp, as_attachment=True, filename='audio.mp3')
        response['Content-Type'] = 'audio/mpeg'
        response['Content-Disposition'] = 'attachment; filename="audio.mp3"'
    

        return response
    

import os
import tempfile
from pdf2docx import Converter
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class PdfToWordTool(APIView):
    def post(self, request):
        pdf_file = request.FILES['pdf']

        # Create a temporary directory within the base path component
        with tempfile.TemporaryDirectory(dir=settings.MEDIA_ROOT) as temp_dir:
            # Save the uploaded PDF file to the temporary directory
            temp_pdf_file_path = os.path.join(temp_dir, 'temp.pdf')
            with open(temp_pdf_file_path, 'wb+') as f:
                f.write(pdf_file.read())

            # Convert PDF to DOCX
            word_file_io = io.BytesIO()
            cv = Converter(temp_pdf_file_path)
            cv.convert(word_file_io)
            cv.close()

            # Ensure the cursor is at the beginning of the BytesIO object
            word_file_io.seek(0)

            # Return the generated Word document in the response
            response = HttpResponse(word_file_io.read(), content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename="converted-document.docx"'
            return response