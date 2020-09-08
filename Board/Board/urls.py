"""Board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    # pybo/ 로 시작되는 URL이 요청되면 이제 pybo/urls.py 파일의 매핑정보를 읽어서 처리하라는 의미이다.
    # 따라서 이제 pybo/question/create, pybo/answer/create등의 URL이 추가되더라도
    # config/urls.py 파일을 수정할 필요없이 pybo/urls.py 파일만 수정하면 될것이다.

    # 뒤에 슬래시를 붙여주면 웹브라우저 주소창에 http://localhost:8000/pybo 라고 입력해도 자동으로 http://localhost:8000/pybo/ 처럼 변환된다. 이렇게 되는 이유는
    # URL을 정규화하는 장고의 기능 때문이다.
]
