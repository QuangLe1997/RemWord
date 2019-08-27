from django.contrib import admin

from .models import Vocabulary, Topic, Predict,Example

admin.site.register(Topic)
admin.site.register(Vocabulary)
admin.site.register(Predict)
admin.site.register(Example)

