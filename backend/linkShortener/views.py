from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortLink
import string
import random
from django.http import JsonResponse

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_code = generate_short_code()
        ShortLink.objects.create(long_url=long_url, short_code=short_code)
        return JsonResponse({
            'short_url': f"http://127.0.0.1:8000/linkShortener/{short_code}",
        })
    return render(request, 'linkShortener.html')

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

def redirect_to_long_url(request, short_code):
    short_link = get_object_or_404(ShortLink, short_code=short_code)
    return redirect(short_link.long_url)
