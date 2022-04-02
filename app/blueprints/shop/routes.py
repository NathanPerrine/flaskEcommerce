from . import shop 
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
# from .forms import shop
# from .models import ShopItem

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

    return render_template('store.html', tilte=title)