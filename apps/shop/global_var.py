from tmall import settings


def get_url(request):
    return {'static_url': settings.TEMP_STATIC_URL, 'media_url': settings.TEMP_MEDIA_URL}
