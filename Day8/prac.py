def calculate_love_score(name1, name2):
    name = name1 + name2
    T = name.count('t').lower()
    R = name.count('r').lower()
    U = name.count('u').lower() 
    E = name.count('e').lower()
    L = name.count('l').lower()
    O = name.count('o').lower() 
    V = name.count('v').lower()
    E = name.count('e').lower()
    love_score = int(str(T+R+U+E) + str(L+O+V+E))
    print(f"Your love score is {love_score}")

calculate_love_score("ravi", "sri")