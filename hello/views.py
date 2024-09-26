from django.shortcuts import render, get_object_or_404
from hello.models import UsersDog
from hello.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def home(request):
    dogs = UsersDog.objects.all()
    return render(request, "index.html", {'dogs': dogs})

def dog_detail(request, dog_id):
    dog = get_object_or_404(UsersDog, id=dog_id)
    form = OrderForm(request.POST or None, initial={
        'dog': dog,
    })
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect('{}?sent=True'.format(reverse('dog_page', kwargs={'dog_id': dog.id})))

    return render(request, "dog_detail.html", {
        'dog': dog,
        'form': form,
        'sent': request.GET.get('sent', False)
    })

