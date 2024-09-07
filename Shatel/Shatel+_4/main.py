import requests as re
import unicodedata


print("Please Enter Youre Question\n---------------------------")
question = input("=> ")
print("---------------------------")
out = re.get(f"http://5.161.91.18/chat?text={question}")
text = unicodedata.normalize("NFKD", out.json())
print(text)