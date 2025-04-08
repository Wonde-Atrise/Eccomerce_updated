from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Product  # Import your Product model


# Create your views here.
 
def Index(request):
    

    return render(request, 'index.html')
def Shop(request):
    return render(request, 'shop.html')
def Product_Single(request): 

    # Prefetch related comments in a single query
    products_with_comments = Product.objects.prefetch_related('comments__user').all()

    context = {
        'product_value': products_with_comments,
    }
    return render(request, 'product-single.html', context)
def Shope_Sider(request):
    return render(request, 'shop-sidebar.html')
def Cart(request):
    return render(request, 'cart.html')
def Checkout(request):
    return render(request, 'checkout.html')
def Pricing(request):
    return render(request, 'pricing.html')
def Confirm(request):
    return render(request, 'confirmation.html')

def comments(request, id):
    product = get_object_or_404(Product, pk=id)  # Get the Product instance

    if request.method == "POST":
        Comment.objects.create(
            product=product,  # Assign the Product instance
            user=request.user,
            text=request.POST.get('comment')
        )
        return redirect('product-single') # Pass product ID if needed in the URL
    else:
        # Handle GET requests if needed (e.g., display existing comments)
        existing_comments = Comment.objects.filter(product=product).order_by('-created_at')
        context = {'product': product, 'comments': existing_comments}
        return render(request, 'product_detail.html', context) # Adjust template name