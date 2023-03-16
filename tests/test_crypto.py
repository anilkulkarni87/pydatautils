"""This is a test Module."""
from pydatautils import encryption


def test_encrypt_data() -> None:
    """This is a test function."""
    res = encryption.encrypt_data("Prison break")
    print(res)
    assert res == "6K8Gd/yV51hIk+sG0LGWsQ=="


def test_decrypt_data() -> None:
    """This is a test function."""
    res = encryption.decrypt_data("6K8Gd/yV51hIk+sG0LGWsQ==")
    print(res)
    assert res == "Prison break"
