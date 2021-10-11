def greetings(input, print):
    s=input('What is your name?')
    if s.isalpha() and s[0].isupper() and (s[1:].islower() or len(s)==1):
        print("Hello, "+ s + "!")
        return
    print("Hello, World!")
    return