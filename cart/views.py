from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def view_cart(request):
    """
    View the cart content page
    """
    return render(request, "cart/cart.html")


@login_required()
def add_to_cart(request, id):
    """Add an item to the cart and increase or decrease quantity"""
    quantity = int(request.POST.get("quantity"))

    cart = request.session.get("cart", {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session["cart"] = cart

    return redirect(reverse("products-home"))


@login_required()
def modify_cart(request, id):
    """Enables the user to modify the cart items quantity"""
    cart = request.session.get("cart", {})
    quantity = int(request.POST.get("quantity"))

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session["cart"] = cart
    return redirect(reverse("view_cart"))

