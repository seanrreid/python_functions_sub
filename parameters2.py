def make_formal_greeting(name, title):
    return f"This is {name}, the {title}!"

result = make_formal_greeting("Jason", "Red Ranger")
oops = make_formal_greeting("Red Ranger", "Jason")

# print(result)
# print(oops)

def blend(setting, time):
    return f"Blend on {setting} for {time} minutes."

numberOfMinutes = input("how long should this blend?")
desiredSetting = input("what setting should we use?")

print(blend(desiredSetting, numberOfMinutes))