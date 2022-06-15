from django.db import models

class Event(models.Model):
    event_image = models.ImageField(upload_to='shop/img/')
    text_title = models.CharField(max_length=200)
    event_text = models.TextField()

    def __str__(self):
        return self.text_title

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукции'