s1="banana"
s2='banana'
print(s1,s2)
s1='John said"How are you". They replied "I\'m smart"'
print(s1)
s1="I can print \" and another \'"
print(s1)


s="0123456789"
print(s[1],s[7],s[9])
print(s[-1],s[-4])
print(f"the length is:{len(s)}")



s="0123456789"
print(s)
print(s[1:2])
print(s[1:7])
print(s[:7])
s="I go to school early in the morning"
print(s[:20])
print(s[20:])
print(s[:])

print(s[::2])
print(s[::-1])
print("Racecar"[::-1])
s1="hello"
s2="world"
print(s1+" "+s2)
print(s1)
print("hello")
s1="hello"
s2=4*s1
print(s2)
print((4//2)*s1)

s="hello"
useful_methods=[m for m in dir(s) if "__" not in m]
print(useful_methods)

print(help(s.capitalize))
print(s.capitalize())

print("HELLO".casefold()) # same as .lower() method

print("hello".center(50))
print("hello".center(50,"*"))
print("I see a little dove".count("e")) # how many times do I see 'e'
print("bana".count("ana"))
x="I do not cook nor compare"
print(f"There are {x.count("o")}os inside: |{x}'")
print("hellooo00".find("l",10))
s="bob goes to bob so they can take their bober and go bobbing"
pos=0
while True:
    start=s.find("bob",pos)
    if start==-1:
        break
    print("found bob on position",start)
    pos=start+1
items=["cat","rat","mouse","house"]
print("+another+".join(items))
print("I LIKE to go HIKIng!!".lower().upper())
print("i like to go skiing".title())

print("i like to go skiing".replace("i","1").replace("e","3"))
print("I like to go skiing".split())