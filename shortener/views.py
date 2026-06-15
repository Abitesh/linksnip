import random
import string

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import URLForm
from .models import ShortURL


def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    code = "".join(random.choice(chars) for _ in range(length))
    while ShortURL.objects.filter(short_code=code).exists():
        code = "".join(random.choice(chars) for _ in range(length))
    return code


def home(request):
    form = URLForm()
    short_url_obj = None

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data["original_url"]
            obj, created = ShortURL.objects.get_or_create(original_url=original_url)
            if created:
                obj.short_code = generate_code()
                obj.save()
            short_url_obj = obj

    recent_links = ShortURL.objects.order_by("-created_at")[:10]

    context = {
        "form": form,
        "short_url_obj": short_url_obj,
        "recent_links": recent_links,
    }
    return render(request, "shortener/home.html", context)


def redirect_short_url(request, code):
    obj = get_object_or_404(ShortURL, short_code=code)
    obj.clicks = obj.clicks + 1
    obj.save()
    return redirect(obj.original_url)


def list_links(request):
    links = ShortURL.objects.order_by("-created_at")
    return render(request, "shortener/list.html", {"links": links})