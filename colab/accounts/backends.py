from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class UsernameOrEmailBackend(ModelBackend):

    def authenticate(self, username=None, password=None):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(
                Q(username=username) | Q(email=username)
            )
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None
        except:
            return None
