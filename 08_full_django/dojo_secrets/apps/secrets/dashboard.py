"""Helper module for gathering Dashboard data."""

from models import User, Secret
from django.db.models import Count

def get_recent_secrets():
    """Gets 3 most recent secrets."""

    # Get all secrets, order by created at (most recent), take top 3 items in returned list.
    most_recent_3 = Secret.objects.all().order_by('-created_at')[:3]
    return most_recent_3

def get_popular_secrets():
    """Gets 4 most popular secrets."""

    # Count likes, order all Secrets by like count and take the top 4 in the list:
    most_popular_4 = Secret.objects.annotate(like_count=Count('likes')).order_by('-like_count')[:4]
    return most_popular_4

def get_like_count(recent_secrets, popular_secrets):
    """Gets like count for each recent and popular secret."""

    # Loop through Recent Secrets and count each Secret's likes, and append to each Secret object:
    for secret in recent_secrets:
        secret.like_count = secret.likes.all().count()
        secret.liked_users = secret.likes.all()

    # Loop through Popular Secrets and count each Secret's likes, and append to each Secret object:
    for secret in popular_secrets:
        secret.like_count = secret.likes.all().count()
        secret.liked_users = secret.likes.all()

    # Return a dictionary with our modified secret lists which now contain a `like_count` property on each Secret:
    like_count_data = {
        "recent_secrets": recent_secrets,
        "popular_secrets": popular_secrets,
    }

    return like_count_data

def populate_data(id):
    """
    Create dictionary for Dashboard Template.

    Parameters:
    - `id` - Session user id of currently logged in user.
    """

    # Generate a `like_count` property on each Secret, counting its # of likes:
    like_data = get_like_count(get_recent_secrets(), get_popular_secrets())

    # Prepare data for Dashboard by running functions above, which collect the data we need:
    dashboard_data = {
        "recent_secrets": like_data["recent_secrets"], # 3 most recent secrets with new `like_count` property
        "popular_secrets": like_data["popular_secrets"], # 4 most popular secrets with new `like_count` property
        "logged_in_user": User.objects.get(id=id), # provides current user, note: `id` is request.session["user_id"] value.
    }

    # Send back dashboard data which contains most recent and popular secrets with like counts, and the logged in user:
    return dashboard_data
