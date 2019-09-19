from django.contrib import admin

# Register your models here.


from Dis import models


# class DocumentAdmin(admin.ModelAdmin):
#     pass
#
#
# class CommentAdmin(admin.ModelAdmin):
#     pass


admin.site.register(models.User)
admin.site.register(models.Pictures)
admin.site.register(models.Videos)
# admin.site.register(models.Video, CommentAdmin)