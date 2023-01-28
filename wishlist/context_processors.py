from wishlist.forms import WishlistForm


def WishlistFormContextProcessor(request):
    wishlist_form = WishlistForm
    return {
        'wishlist_form': wishlist_form,
    }
