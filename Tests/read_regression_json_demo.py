import json

from Utilities.path_utils import TESTDATA_DIR

with open(TESTDATA_DIR/"regression_login_data.json", "r") as f:
    data = json.load(f)
    scenarios = data["scenarios"]
    for scenario in scenarios:
        print(
            scenario["scenario"],
            scenario["username"],
            scenario["password"],
            scenario["exp_res"]
        )
        #if scenario["scenario"] == "valid_login":
        #    print(scenario["username"], scenario["password"], scenario["exp_res"])
        #elif scenario["scenario"] == "invalid_password":
         #   print(scenario["username"], scenario["password"], scenario["exp_res"])
        #elif scenario["scenario"] == "invalid_username":
         #   print(scenario["username"], scenario["password"], scenario["exp_res"])
        #else:
         #   print(scenario["username"], scenario["password"], scenario["exp_res"])