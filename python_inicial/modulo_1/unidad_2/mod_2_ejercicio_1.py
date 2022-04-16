import sys as s

print(s.argv[0])

if int(s.argv[1])%2 == 0 and int(s.argv[2])%2 == 0 and int(s.argv[3])%2 == 0:
    print("Son multiplos de 2")
else:
    print("No son multiplos e 2") 