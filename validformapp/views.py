from django.shortcuts import render
from validformapp.forms import NameForm

# Create your views here.
def form_page(request):
    form = NameForm()

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print('Validation success')
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Text: {form.cleaned_data['text']}")

    return render(request, 'validformapp/form_page.html', {'form': form})
