def hourTomins(seconds):
    minutes, sec = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60) 
    return hours, minutes, sec

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

h, m, s = hourTomins(3725)
# minutes = int(input("Enter minutes: "))
print(h, m, s)
print(to_seconds(h, m, s))

