#python3版本
f = open("d:/a.txt","r+")
res=''
for i in range(42):
    s=eval('0b'+f.read(3))  #python3使用0o作为前导数表示八进制
    res+=chr(int(s))
print (res)