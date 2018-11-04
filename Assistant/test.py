import hashlib

c = input("Enter Key: ")
hash_object = hashlib.md5(c.encode()).hexdigest()
print(hash_object)
