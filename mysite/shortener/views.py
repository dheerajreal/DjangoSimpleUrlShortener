from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import UrlForm
from .models import UrlRecord
from .utilities import short_url_generate
# Create your views here.


def create_urltag():
    urltag = short_url_generate()
    qs_exists = UrlRecord.objects.filter(short_url=urltag).exists()
    if qs_exists:
        return create_urltag()
    return urltag


def index(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        original_url = form.cleaned_data["original_url"]
        try:
            # see if url already exists in database
            url_record = UrlRecord.objects.get(original_url=original_url)
        except:
            # create in database and fetch
            form.instance.short_url = create_urltag()  # generate urltag
            form.save()
            url_record = get_object_or_404(
                UrlRecord, original_url=original_url)

        urltag = url_record.short_url
        context = {
            "urltag": urltag
        }
        return render(request, "shortener/detail.html", context)

    context = {
        "form": form
    }
    return render(request, "shortener/index.html", context)


def resolve(request, urltag):
    if len(urltag) != 4:
        raise Http404
    url_record = get_object_or_404(UrlRecord, pk=urltag)
    original_url = url_record.original_url
    return redirect(original_url)
