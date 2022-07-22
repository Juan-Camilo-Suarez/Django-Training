from .models import User


def register_user(email: str, password: str) -> User:
    user = User(email=email)
    user.set_password(password)
    user.save()
    return user
