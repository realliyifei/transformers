import os

import pickle

load_conceptor = lambda path: pickle.load(open(path,'rb'))['negC']

package_directory=os.path.dirname(os.path.abspath(__file__))
path = os.path.join(package_directory, "negc", "bert-tiny")
negc0 = load_conceptor(os.path.join(path, "sst-bert-tiny-layer0-percentile1-and-negc.pkl"))
negc1 = load_conceptor(os.path.join(path, "sst-bert-tiny-layer1-percentile1-and-negc.pkl"))
negc2 = load_conceptor(os.path.join(path, "sst-bert-tiny-layer2-percentile1-and-negc.pkl"))

print(negc0.shape)
print(negc0)
print(negc1)
print(negc2)