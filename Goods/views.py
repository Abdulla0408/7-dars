from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import ProductEnterForm


def banner(request):
    banners = models.Banner.objects.filter(is_active=True)[:5]
    context = {'banners': banners}
    return render(request, 'index.html', context)


def footer(request):
    footers = models.Footer.objects.all()
    context = {'footers': footers}
    return render(request, 'index.html', context)


def list(request):
    products = models.ProductEnter.objects.all()
    context = {'products': products}
    return render(request, 'list.html', context)


def create(request):
    if request.method == 'POST':
        form = ProductEnterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_product_enter')
    else:
        form = ProductEnterForm()
    
    return render(request, 'create.html', {'form': form})


def update(request, pk):
    product = get_object_or_404(models.ProductEnter, pk=pk)
    if request.method == 'POST':
        form = ProductEnterForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
    else:
        form = ProductEnterForm(instance=product)
    context = {'form': form}
    return render(request, 'update.html', context)


def delete(request, pk):
    product = models.ProductEnter.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('list_product_enter')
    context = {'product': product}
    return render(request, 'delete.html', context)
