import json

from Utilities.path_utils import TESTDATA_DIR

with open(TESTDATA_DIR/"smoke_login_data.json", "r") as f:
    data = json.load(f)
    valid_user = data["valid_user"]
    username = valid_user["username"]
    password = valid_user["password"]

print(valid_user)
print(username)
print(password)