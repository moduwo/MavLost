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


# display list of items for logged in users
@login_required
def item_list(request):
    # get search query from URL and remove whitespace
    query = request.GET.get('q', '').strip()
    # show active items w/ newest first
    items = Item.objects.filter(status__in=['open', 'claim_in_review']).order_by('-created_at')
    # filter items when search query is given
    if query:
        items = (
            items.filter(name__icontains=query) |
            items.filter(description__icontains=query) |
            items.filter(location__icontains=query)
        ).order_by('created_at')

    # display item listings
    return render(request, 'items/item_list.html', {'items': items, 'query': query})


# require users to be logged in to delete items 
@login_required
def delete_item(request, pk):
    # get item only if logged in user created it
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":            # check if delete was confirmed
        item.delete()                       # delete item from database
        return redirect("item_list")         # redirect to item list
    # display confirmation before deleting
    return render(request, "items/item_confirm_delete.html", {"item": item})


# require user to be logged in to edit user-created item
@login_required
def edit_item(request, pk):
    # get item created by logged in user
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":            # check if form was submitted
        # fill form w/ submitted changes
        form = ItemForm(request.POST, request.FILES, instance=item,)
        
        if form.is_valid():
            form.save()                  # update existing item in database
            return redirect("item_list") # return to item list
    else:
        # fill form w/ existing item data
        form = ItemForm(instance=item)
    # display item form 
    return render(request, "items/item_form.html", {"form": form})
