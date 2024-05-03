import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_nonexistent_record():
    with pytest.raises(ObjectDoesNotExist):
        User.objects.get(username='admin')
