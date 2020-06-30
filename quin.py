# f = open("quin.py", "r")
# print(f.read())


a='a=%s%s%s;print(a%%(chr(39),a,chr(39)))'
print(a%(chr(39),a,chr(39)))