# http://www.pythonchallenge.com/pc/def/map.html
import string
l = string.ascii_lowercase
t = str.maketrans(l, l[2:] + l[:2])
m = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
     bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
     sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
     map"""
print(m.translate(t))
