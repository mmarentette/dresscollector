from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Dress, Store
from .forms import ReviewForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dresses_index(request):
    # We are namespacing the index.html template by putting it in a new tempates/dresses folder for organization purposes
    # We pass a dictionary as a third positional argument in render; we can access the values in the template by using the key 'dresses'
    dresses = Dress.objects.all()
    return render(request, 'dresses/index.html', {
        'dresses': dresses
    })

def dresses_detail(request, dress_id):
    dress = Dress.objects.get(id=dress_id)
    # Create a list of the store ids a dress DOES have
    store_id_list = dress.stores.all().values_list('id')
    # Then, query for stores whose ids are not in the list using exclude
    # Exclude is similar to filter except that it returns objects that DON'T meet the criteria
    # id__in is a Django 'field lookup' that checks if the model's id is in a list
    stores_not_carrying = Store.objects.exclude(id__in=store_id_list)
    review_form = ReviewForm()
    return render(request, 'dresses/detail.html', {
        'dress': dress,
        'review_form': review_form,
        'stores_not_carrying': stores_not_carrying
    })

def add_review(request, dress_id):
    # Create a ModelForm instance using the data in request.POST (which is similar to req.body in Express)
    form = ReviewForm(request.POST)
    # Validate the form
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.dress_id = dress_id
        new_review.save()
    
    # Always redirect instead of render if data has been changed in the database
    return redirect('detail', dress_id=dress_id)

def assoc_store(request, dress_id, store_id):
    Dress.objects.get(id=dress_id).stores.add(store_id)
    # Note that in the above, we add the store_id instead of the store object
    return redirect('detail', dress_id=dress_id)

class DressCreate(CreateView):
    model = Dress
    fields = '__all__' # fields can be used to limit or change the ordering of attributes from the model that are generated in the ModelForm

class DressUpdate(UpdateView):
    model = Dress
    fields = '__all__'

class DressDelete(DeleteView):
    model = Dress
    success_url = '/dresses'

class StoreList(ListView):
    model = Store

class StoreDetail(DetailView):
    model = Store

class StoreCreate(CreateView):
    model = Store
    fields = '__all__'

class StoreUpdate(UpdateView):
    model = Store
    fields = ['street_address', 'city', 'province', 'postal_code', 'website_url']

class StoreDelete(DeleteView):
    model = Store
    success_url = '/stores'
