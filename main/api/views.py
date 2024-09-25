from rest_framework.generics import ListAPIView, RetrieveAPIView
from main.models import Blog, Service, Portfolio, SiteSetting
from main.api.serializers import BlogSerializer, ServiceSerializer, ContactSerializer, PortfolioSerializer, SiteSettingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext as _
from django.utils import timezone
from datetime import timedelta, datetime

class MyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        message = _("Salam Dunya")
        return Response({'message': message})

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

    def get_object(self):
        blog = super().get_object()

        # İstifadəçi IP ünvanını alın
        user_ip = self.request.META.get('REMOTE_ADDR')

        # Sessiyadan oxuyun və ya boş siyahı yaradın
        viewed_ips = self.request.session.get(f'viewed_ips_{blog.id}', [])

        # Əgər istifadəçi bu bloga baxmayıbsa, baxış sayını artırın
        if user_ip not in viewed_ips:
            blog.view_count += 1
            blog.save()
            # İstifadəçinin IP ünvanını sessiyaya əlavə edin
            viewed_ips.append(user_ip)
            self.request.session[f'viewed_ips_{blog.id}'] = viewed_ips

        return blog

class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailAPIView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'


class ContactCreateAPIView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PortfolioListAPIView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioDetailAPIView(RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    lookup_field = 'id'


class SiteSettingListAPIView(ListAPIView):
    queryset = SiteSetting.objects.all()
    serializer_class = SiteSettingSerializer