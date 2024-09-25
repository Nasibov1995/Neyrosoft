from django.contrib import admin
from . models import Blog, Service, Contact, Portfolio, SiteSetting
from parler.admin import TranslatableAdmin

admin.site.register(Blog, TranslatableAdmin)
admin.site.register(Service, TranslatableAdmin)
admin.site.register(Contact)
admin.site.register(Portfolio, TranslatableAdmin)
admin.site.register(SiteSetting)

