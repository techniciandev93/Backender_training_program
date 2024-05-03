import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user_account():
    user, created = User.objects.get_or_create(
        username='test_user',
        defaults={'password': 'test_password'}
    )
    assert created
