a = '$56.00'
b = a.replace("\$|,", "").strip().astype(float)
print(b)
