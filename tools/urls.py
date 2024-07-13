from django.urls import path

from .views import ToolView, ToolsView, ToolUsageView
from .views import ToolsUsageView, ToolCategoryView, ToolCategoriesView
# from .views import image_to_text

urlpatterns = [
    
    
    path('get/<str:id>', ToolView.as_view(),name='get_tool_view'),
    path('post/', ToolView.as_view(),name='post_tool_view'),
    path('delete/<str:id>', ToolView.as_view(),name='delete_tool_view'),
    path('update/<str:id>', ToolView.as_view(),name='update_tool_view'),
    path('getall/', ToolsView.as_view(),name='get_all_tool_view'),
    path('usage/get/<str:id>', ToolUsageView.as_view(),name='get_usage_view'),
    path('usage/post/', ToolUsageView.as_view(),name='post_usage_view'),
    path('usage/delete/<str:id>', ToolUsageView.as_view(),name='delete_usage_view'),
    path('usage/getall/', ToolUsageView.as_view(),name='get_all_usage_view'),
    path('category/get/<str:id>', ToolCategoryView.as_view(),name='get_category_view'),
    path('category/post/', ToolCategoryView.as_view(),name='post_category_view'),
    path('category/delete/<str:id>', ToolCategoryView.as_view(),name='delete_category_view'),
    path('category/update/<str:id>', ToolCategoryView.as_view(),name='update_category_view'),
    path('categories/getall/', ToolCategoriesView.as_view(),name='get_all_categories_view'),
    
    ##############################################
    
    # path('image_to_text/',image_to_text(),name="image_to_text"),
    # path('text_to_image/',view_name,name=view_name),
    # path('jpg_to_png/',view_name,name=view_name),
    # path('png_to_jpg/',view_name,name=view_name),
    # path('json_to_xml/',view_name,name=view_name),
    # path('html_minifier/',view_name,name=view_name),
    # path('website_screenshot_generator/',view_name,name=view_name),
    # path('converters/',view_name,name=view_name),
    # path('calculators/',view_name,name=view_name),
]
