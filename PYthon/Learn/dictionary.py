Info = {
    "key": "value",
    "name": "Nil",
    "age": 20,
    "rating":4.5,
    "T/F":True,
    "sub": ["phy","chem","math"],
    101:"hi",
    (1,2,3):"valid",
    True:"yess"
}

print(Info)
print(Info["name"])
print(Info[101])
print(Info[True])

Info["name"] = "new Nil"
Info["new"] = False
print(Info)

null_dict = {}
print(null_dict)

std = {
    "name":"RahuKetu",
    "marks": {
        "phy" : 20,
        "che" : 19,
        "bio" : 21
    }
}

print(std)
print(std["marks"])
print(std["marks"]["phy"])

# Return All keys
print(Info.keys())

# Type Casting
print(list(Info.keys()))

# Return All values
print(std.values())

# Return key values pairs as tuples
print(Info.items())

# Return None if key absent otherwise value
print(std.get("gum"))
print(std.get("name"))

# Update with new key value pair
new_std_data = {"name":"nil","rate":99}
std.update(new_std_data)
print(std)

print("THE END",end='')