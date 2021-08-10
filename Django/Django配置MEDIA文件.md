[TOC]

# Django配置MEDIA文件

当我们需要向服务器发送图片或视频，需要对这些媒体文件进行保存时，需要指定保存在哪并将保存的路径添加到路由中。

## 设置setting.py

```python
MEDIA_URL = '/media/'  # 设置媒体文件的相对路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 设置媒体文件的绝对路径
# 将media也加入静态文件目录列表中
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]
```

## 设置路由urls.py

```python
from django.views.static import serve  # 导入相关静态文件处理的views控制包
from xxxx.settings import MEDIA_ROOT  # 导入项目文件夹中setting中的MEDIA_ROOT绝对路径

# 将路由加到urlpatterns路由列表中
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
]
```

## 设置Model中字段属性

```python
img = models.ImageField(upload_to='img')
```