from . import shop 
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.blueprints.seller.models import Book
from app.blueprints.shop.models import Cart

@shop.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)

@shop.route('/view-cart')
def view_cart():
    title = "Cart"
    user_cart = ""
    books = [Book.query.filter(Book.id == cart.book_id).all()[0] for cart in current_user.my_cart.all()]
    total = sum([book.price for book in books])

    if books:
        cart = current_user.my_cart.all()
        user_cart = zip(books, cart)

    return render_template('view_cart.html', title=title, user_cart = user_cart, total = total)

@shop.route('/store')
def store():
    title = 'Store'
    books = Book.query.all()

    return render_template('store.html', tilte=title, books = books)

@shop.route('/full-item/<item_id>', methods=["GET", "POST"])
@login_required 
def full_item(item_id):
    item = Book.query.get_or_404(item_id)
    title = f"{item} Full Info"

    return render_template('full_item.html', title = title, item = item)

@shop.route('/add-to-cart/<item_id>')
@login_required 
def add_to_cart(item_id):
    item = Book.query.get_or_404(item_id)
    new_cart = Cart(user_id = current_user.id, book_id = item.id)
    flash(f"{item.title} has been added to your cart.", "success")
    return redirect(url_for('shop.store'))

@shop.route('/checkout')
@login_required 
def checkout():
    my_cart = current_user.my_cart.all()
    for cart in my_cart:
        cart.delete()
    flash(f"You have successfully checked out! Your cart is now empty.", "success")
    return redirect(url_for('shop.store'))

@shop.route('/remove-item/<cart_id>')
@login_required 
def remove_item(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    cart.delete()
    flash(f"Removed from your cart.", "info")
    return redirect(url_for('shop.view_cart'))