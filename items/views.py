from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Item

# Create your views here.

# display home page
def home(request):
    return render(request, "items/home.html")

# require users to be logged in to submit item posts
@login_required
def create_item(request):
    if request.method == "POST":            # check if form was submitted
        form = ItemForm(request.POST, request.FILES) 

        if form.is_valid():
            item = form.save(commit=False)  # create item w/o saving yet
            item.created_by = request.user  # set creator to logged-in user
            item.save()                     # save item to database
            return redirect("home")         # redirect to homepage
    else:
        form = ItemForm()                   # create empty form
    # display item form
    return render(request, "items/item_form.html", {"form": form})

@login_required
# display list of items for logged-in users
def item_list(request):
    # filter/show items that are open or in claim review
    items = Item.objects.filter(status__in=['open', 'claim_in_review']).order_by('-created_at')
    # display item listings
    return render(request, 'items/item_list.html', {'items': items})
