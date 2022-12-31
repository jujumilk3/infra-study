import os

test = "Hi"


def test():
    print("Hello World")
    a = 1


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")
