from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Blog(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_("Başlıq")),
        content=models.TextField(verbose_name=_("Mətn")),
    )
    image = models.ImageField(upload_to='blog_images/', verbose_name=_("Şəkil"))

    view_count = models.PositiveIntegerField(verbose_name=_("Baxış sayı"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaradılma Tarixi"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yenilənmə Tarixi"))
    
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)
    
    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _('Bloglar')

class Service(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_("Adı")),
        description=models.TextField(verbose_name=_("Təsvir")),
    )
    image = models.ImageField(upload_to='service_images/', verbose_name=_("Şəkil"))

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaradılma Tarixi"))

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)

    class Meta:
        verbose_name = _("Xidmət")
        verbose_name_plural = _('Xidmətlər')

class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_("Ad"))
    last_name = models.CharField(max_length=50, verbose_name=_("Soyad"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=20, verbose_name=_("Nömrə"))
    subject = models.CharField(max_length=100, verbose_name=_("Mövzu"))
    message = models.TextField(verbose_name=_("Mesaj"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Göndərilmə Tarixi"))
    
    status = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
    
    class Meta:
        verbose_name = _("Əlaqə")
        verbose_name_plural = _('Əlaqələr')

class Portfolio(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_("Başlıq")),
        description=models.TextField(verbose_name=_("Təsvir")),
    )
    image = models.ImageField(upload_to='portfolio_images/', verbose_name=_("Şəkil"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaradılma Tarixi"))
    
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)
    
    class Meta:
        verbose_name = _("İş")
        verbose_name_plural = _('İşlərimiz')
        
        
class SiteSetting(models.Model):
    logo = models.ImageField(upload_to='logos/')
    navbar_items = models.JSONField(default=list)

    def __str__(self):
        return "Parametrlər"
    
    class Meta:
        verbose_name = _("Parametr")
        verbose_name_plural = _('Parametrlər')
