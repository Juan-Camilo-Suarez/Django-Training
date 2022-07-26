from .models import User


def register_user(email: str, password: str, avatar) -> User:
    user = User(email=email, avatar=avatar)
    user.set_password(password)
    user.save()
    return user
