from django.shortcuts import render, render_to_response, RequestContext
from django.http import Http404
from contests.models import Contest
from .forms import ContestForm


def index(request):
    cunts_num = Contest.objects.count()
    available = 20 - cunts_num

    cunts = Contest.objects.all()
    form = ContestForm()
    if request.method == 'POST':
        form = ContestForm(request.POST or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
        else:
            form = ContestForm(request.POST or None)

    return render(request, 'contests/index.html', {
        'available': available,
        'form': form,
        'cunts': cunts,
    })
