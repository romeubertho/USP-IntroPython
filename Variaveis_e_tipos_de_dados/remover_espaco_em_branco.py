usp = "   Universidade de sao paulo   "
print(usp.title())
print(usp.upper())
print(usp.lower())
print("-------- strip whitespace --------")
print(usp.lstrip() + "!")
print(usp.rstrip() + "!")
print(usp.strip() + "!")
#strip character
print("-------- strip character 'A' --------")
usp="AAAAAAAAAAAUniversidade de sao pauloAAAAAAAAAAAAA"
print(usp)
print(usp.lstrip('A') + "!")
print(usp.rstrip('A') + "!")
print(usp.strip('A') + "!")

dia =18
msg="lalala"
msg=msg+" "+str(dia)
print(msg)