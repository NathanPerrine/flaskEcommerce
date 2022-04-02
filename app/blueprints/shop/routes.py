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
    
    return render_template('view_cart.html', title=title)

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