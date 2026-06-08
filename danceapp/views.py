from django.http import Http404
from django.shortcuts import render

from .models import Dance


def _static_dance_catalog():
    """Datos iniciales para el proyecto sin depender de la base de datos.
    Esto permite que las rutas sean dinámicas y escalables.
    """
    return {
        'joropo': {
            'slug': 'joropo',
            'name': 'Joropo',
            'country': 'Venezuela',
            'historical_review': (
                'El Joropo es una danza venezolana tradicional que celebra la vida en ' \
                'los llanos. Está llena de energía, ritmo de arpa y cuatro, y es ' \
                'un símbolo muy fuerte de la identidad venezolana.'
            ),
            'map_image': 'danceapp/images/venezuela-map.svg',
            'collage_images': [
                'danceapp/images/joropo-1.svg',
                'danceapp/images/joropo-2.svg',
            ],
            'video_url': 'https://www.youtube.com/embed/rf7d1ihznT4',
        },
        'tango': {
            'slug': 'tango',
            'name': 'Tango',
            'country': 'Argentina',
            'historical_review': (
                'El Tango nació en Buenos Aires y Montevideo a finales del siglo XIX. ' \
                'Es una danza apasionada que mezcla influencias europeas y criollas, ' \
                'y se convirtió en un ícono mundial del baile argentino.'
            ),
            'map_image': 'danceapp/images/argentina-map.svg',
            'collage_images': [
                'danceapp/images/tango-1.svg',
                'danceapp/images/tango-2.svg',
                'danceapp/images/tango-3.svg',
            ],
            'video_url': 'https://www.youtube.com/embed/o2hZzJz4X3c',
        },
    }


def _dance_to_dict(dance):
    return {
        'slug': dance.slug,
        'name': dance.name,
        'country': dance.country,
        'historical_review': dance.historical_review,
        'map_image': dance.map_image,
        'collage_images': dance.collage_images,
        'video_url': dance.video_url,
    }


def _get_dance_catalog():
    if Dance.objects.exists():
        return {dance.slug: _dance_to_dict(dance) for dance in Dance.objects.all()}
    return _static_dance_catalog()


def home(request):
    """Página principal que muestra las danzas disponibles."""
    dances = list(_get_dance_catalog().values())
    return render(request, 'danceapp/home.html', {'dances': dances})


def dance_stage(request, dance_name, stage):
    """Vista genérica que maneja cada etapa de la danza usando el nombre y la etapa."""
    catalog = _get_dance_catalog()
    dance = catalog.get(dance_name.lower())
    if not dance:
        raise Http404('Danza no encontrada.')

    stage = stage.lower()
    stage_templates = {
        'principal': 'danceapp/principal_danza.html',
        'fotos': 'danceapp/fotos_danza.html',
        'video': 'danceapp/video_danza.html',
    }
    template_name = stage_templates.get(stage)
    if not template_name:
        raise Http404('Etapa inválida.')

    context = {
        'dance': dance,
        'stage': stage,
    }
    return render(request, template_name, context)
