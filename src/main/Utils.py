def user_listing_path(instance,file_name):
    return f"user_{instance.seller.user.id}/listing/{file_name}"