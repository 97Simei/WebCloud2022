#!/usr/bin/env python3

import pandas as pd 
import os
import sys
import yaml

def getdata():
    train_data = pd.read_csv("train.csv")
    test_data = pd.read_csv("test.csv")
    train_data.to_csv("/data/train.csv", index=False)
    test_data.to_csv("/data/test.csv", index=False)
    return "The dataset has been stored in the shared folder /data."

# The entrypoint of the script
if __name__ == "__main__":

    output = getdata()

    print(yaml.dump({"output": output}))


    