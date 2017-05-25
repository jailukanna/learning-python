"""Helper module for gathering Dashboard data."""

from models import User, Secret


def get_recent_secrets():
    """Gets 3 most recent secrets."""

    # Get all secrets, order by created at (most recent), take top 3 items in returned list.
    most_recent_3 = Secret.objects.all().order_by('-created_at')[:3]
    return most_recent_3

def get_popular_secrets():
    """Gets 4 most popular secrets."""

    # Get all secrets, order by likes and take the top 4 in the list:
    most_popular_4 = Secret.objects.all().order_by('likes')[:4]
    return most_popular_4
