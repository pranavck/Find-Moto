def user_directory_path(instance,file_name):
    return f"user_{instance.user.id}/{file_name}"