from django.shortcuts import render, redirect, get_object_or_404
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
            item.created_by = request.user  # set creator to logged in user
            item.save()                     # save item to database
            return redirect("home")         # redirect to homepage
    else:
        form = ItemForm()                   # create empty form
    # display item form
    return render(request, "items/item_form.html", {"form": form})

@login_required
# display list of items for logged in users
def item_list(request):
    # filter/show items that are open or in claim review
    items = Item.objects.filter(status__in=['open', 'claim_in_review']).order_by('-created_at')
    # display item listings
    return render(request, 'items/item_list.html', {'items': items})

# require users to be logged in to delete items 
@login_required
def delete_item(request, pk):
    # get item only if logged-in user created it
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":            # check if delete was confirmed
        item.delete()                       # delete item from database
        return redirect("item_list")         # redirect to item list
    # display confirmation before deleting
    return render(request, "items/item_confirm_delete.html", {"item": item})
