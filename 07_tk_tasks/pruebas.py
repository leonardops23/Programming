import hashlib


pass_w = "asdf"
salt = "5gz"

x = hashlib.md5(pass_w.encode())
print(x)
if x == pass_w + salt:
    print(True)
else:
    print(False)