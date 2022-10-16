# http://www.pythonchallenge.com/pc/def/map.html
import string
l = string.ascii_lowercase
t = str.maketrans(l, l[2:] + l[:2])
m = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. 
     bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
     sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
     map"""
print(m.translate(t))

# letters = "abcdefghijklmnopqrstuvwxyz"

# def convert_letter(c):
#      if c.isalpha():
#           idx = letters.index(c)
#           idx = (idx + 2) % 26
#           return letters[idx]
#      else:
#           return c
     
# messege = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
# map
# """
# result = ""
# for c in messege:
#      result += convert_letter(c)
# print(result)