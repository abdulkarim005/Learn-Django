from django.shortcuts import render

def my_view(request):
    contxt = {
        'name': 'Abdul Karim',
        'age': 25,
        'country': 'Bangladesh'
    }
    return render(request, 'index.html', contxt )


def  product(request):
    return render(request, 'product.html', )
     