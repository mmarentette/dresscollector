import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Dress, Store, Photo
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

def add_photo(request, dress_id):
    # photo-file will be name attribute on <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # generate uniqu "key" for S3 with image file extension
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # Build full url string:
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # Create a photo object ans assign to dress_id (if we already got the dress object within this function, we could have created the object from that side of the relationship too)
            Photo.objects.create(url=url, dress_id=dress_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', dress_id=dress_id)

def assoc_store(request, dress_id, store_id):
    Dress.objects.get(id=dress_id).stores.add(store_id)
    # Note that in the above, we add the store_id instead of the store object
    return redirect('detail', dress_id=dress_id)

def unassoc_store(request, dress_id, store_id):
    Dress.objects.get(id=dress_id).stores.remove(store_id)
    return redirect('detail', dress_id=dress_id)

class DressCreate(CreateView):
    model = Dress
    fields = ['name', 'designer', 'collection', 'style'] # fields can be used to limit or change the ordering of attributes from the model that are generated in the ModelForm

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
