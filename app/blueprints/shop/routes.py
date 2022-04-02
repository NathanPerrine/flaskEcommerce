from . import shop 
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
# from .forms import shop
from app.blueprints.seller.models import Book

@shop.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)

@shop.route('/cart')
def cart():
    title = "Cart"
    
    return render_template('cart.html', title=title)

@shop.route('/store')
def store():
    title = 'Store'
    books = Book.query.all()

    return render_template('store.html', tilte=title, books = books)

@shop.route('/full-item/<item_id>', methods=["GET", "POST"])
@login_required 
def edit_contact(item_id):
    item = Book.query.get_or_404(item_id)
    title = f"{item} Full Info"

    return render_template('full_item.html', title = title, item = item)