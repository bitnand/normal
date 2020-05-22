#python3版本
import base64
f = input("请输入字符串：")
t = base64.b16decode(f)
print (t)