from django.shortcuts import render
from whitelist.forms import wl_form

# Create your views here.


def wl(request):
    form = wl_form
    if request.method == 'POST':
        form = wl_form(request.POST)
        if form.is_valid():
            handle = {'handle':form.cleaned_data['twitter']}
            form.save(commit=True)
            print('success')
            return render(request, 'success_page.html', context= handle)
    return render(request, 'form.html', context= {'form': form})


def success(request):
    pass