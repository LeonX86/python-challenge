#http://www.pythonchallenge.com/pc/def/peak.html
import pickle
fname = "./L05/banner.p"
with open(fname,'rb') as fs:
    data=pickle.load(fs)

for line in data:
    print("".join(x[0]*x[1] for x in line))