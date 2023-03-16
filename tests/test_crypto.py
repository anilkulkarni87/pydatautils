from pysnippets import encryption


def test_encrypt_data():
    res = encryption.encrypt_data("Prison break")
    print(res)
    assert res == "6K8Gd/yV51hIk+sG0LGWsQ=="


def test_decrypt_data():
    res = encryption.decrypt_data("6K8Gd/yV51hIk+sG0LGWsQ==")
    print(res)
    assert res == "Prison break"
