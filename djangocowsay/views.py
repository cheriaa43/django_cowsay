from django.shortcuts import render
from djangocowsay.models import Bubble
from djangocowsay.forms import SpeakForm
import subprocess

# worked with Chris Warren

# Create your views here.
def index(request):
    cow_says = ''
    if request.method == "POST":
        form = SpeakForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Bubble.objects.create(
                text=data.get("text")
            )
            text = data.get("text")
            cow_says = subprocess.check_output(["cowsay", text], text=True)
            print(cow_says)
    form = SpeakForm()
    return render(request, "index.html", {
        "title": "Cowsay - See what the cow says!",
        "form": form,
        "cow_says": cow_says
    })


def history_view(request):
    cow_says = Bubble.objects.order_by('-id')[:10]
    return render(request, "history.html", {"title": "Cowsay - See what the cow said!", "data": cow_says})
