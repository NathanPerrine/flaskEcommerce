from . import seller 
from flask import render_template, redirect, url_for, flash 
from flask_login import login_required, current_user
from .forms import BookForm
from .models import Book, BookList

@seller.route('/') 
def index():
    return redirect(url_for('shop.index'))

@seller.route('/upload-item', methods=['GET', 'POST'])
@login_required
def upload_item():
    title = "Upload Book For Sale"
    form = BookForm()

    if form.validate_on_submit():
        booktitle = form.title.data 
        author = form.author.data 
        desc = form.desc.data 
        price = form.price.data 
        image = form.image.data 

        new_book = Book(title = booktitle, author = author, desc = desc, price = price)
        if image: 
            new_book.upload_to_cloudinary(image)
        
        seller_id = current_user.id 
        book_id = new_book.id

        new_book_list = BookList(seller_id = seller_id, book_id = book_id)

        flash(f"{booktitle} has been added to your Store.", "primary")
        return redirect(url_for('shop.index'))

    return render_template('upload_item.html', title=title, form=form)

@seller.route('/view-listings')
@login_required 
def view_listing():
    title = 'View My Listings'
    user_cart = ""
    books = [Book.query.filter(Book.id == cart.book_id).all()[0] for cart in current_user.my_listings.all()]
    total = sum([book.price for book in books])

    if books:
        cart = current_user.my_listings.all()
        user_cart = zip(books, cart)

    return render_template('view_listing.html', title=title, user_cart = user_cart)

@seller.route('/edit-listing/<book_id>', methods=["GET", "POST"])
@login_required 
def edit_listing(book_id):
    title = "Edit Listing"
    book = Book.query.get_or_404(book_id)
    form = BookForm()

    if form.validate_on_submit():
        book.update(**form.data)
        flash(f"{book.title} has been updated.", "warning")
        return redirect(url_for('seller.view_listing'))

    return render_template('edit_listing.html', title = title, book = book, form = form)