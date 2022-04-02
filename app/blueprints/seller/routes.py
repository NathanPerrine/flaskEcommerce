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