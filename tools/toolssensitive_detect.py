import os
import json
import re


def tools_sensitive_detect():

    out_path = os.path.join(os.path.dirname(__file__), "..", "cases")
    out_file = os.path.join(out_path, "injection_cases.json")

    with open(out_file,"r") as f:
        re.match()

def main():
    print("main")

if __name__ =="__main___":
    main()