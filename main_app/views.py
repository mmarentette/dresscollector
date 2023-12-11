from django.shortcuts import render

dresses = [
    {'style': 'Mira', 'collection': 'Eternal', 'designer': 'Daalarna', 'size': 0},
    {'style': 'Minty', 'collection': 'Provence', 'designer': 'Tom Sebastien', 'size': 0}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dresses_index(request):
    # We are namespacing the index.html template by putting it in a new tempates/dresses folder for organization purposes
    # We pass a dictionary as a third positional argument in render; we can access the values in the template by using the key 'dresses'
    return render(request, 'dresses/index.html', {
        'dresses': dresses
    })