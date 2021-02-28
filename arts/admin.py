from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Arts
# Register your models here.

class ArtsAdmin(admin.ModelAdmin):
    list_display = ('photo_image',)
    #"photo_image"を追加
    
    #以下、photo_imageの定義を追加する。サイズ等の設定は自由です。
    def photo_image(self, obj):
        return mark_safe('<img src="{}" style="width:200px; height:auto;">'.format(obj.image.url))


admin.site.register(Arts, ArtsAdmin)