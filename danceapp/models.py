from django.db import models


class Dance(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    country = models.CharField(max_length=100)
    historical_review = models.TextField(help_text='Breve reseña histórica de la danza')
    map_image = models.CharField(
        max_length=255,
        help_text='Ruta estática para el mapa del país, por ejemplo danceapp/images/argentina-map.svg',
    )
    collage_images = models.JSONField(
        default=list,
        help_text='Lista de rutas a imágenes estáticas para el collage de la danza',
    )
    video_url = models.URLField(blank=True, help_text='URL del video embebido de la danza')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
