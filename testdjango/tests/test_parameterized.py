import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
@pytest.mark.parametrize('username, password', [
    ('user1', 'password1'),
    ('user2', 'password2'),
    ('user3', 'password3'),
])
def test_parameterized_user_creation(username, password):
    User.objects.create_user(username=username, password=password)
    assert User.objects.filter(username=username).exists()
