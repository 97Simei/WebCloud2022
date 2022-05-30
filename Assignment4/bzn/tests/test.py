import os
import sys
from titanic import Titanic

sample_train = "/data/train.csv"
sample_test = "/data/test.csv"
output_path = "/data/"

def train_titanic():
    test1 = Titanic(sample_train)
    test1.train(sample_train)
    assert path.exists("/data/clf.pickle") is True

def test_titanic():
    test2 = Titanic(sample_test, output_path)
    test2.test(sample_test, output_path)
    assert path.exists("/data/prediction.csv") is True
    