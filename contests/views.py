from django.shortcuts import render, render_to_response, RequestContext
from django.http import Http404
from contests.models import Contest
from .forms import ContestForm


def index(request):
    form = ContestForm(request.POST or None)
    cunts = Contest.objects.all()

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render(request, 'contests/index.html', {
        'form': form,
        'cunts': cunts,
    })
