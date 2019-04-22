work = "<link rel=\"stylesheet\" type=\"text/css\" href=\"{% static \'style.css\' %}\">"
dont = "<link rel=\"stylesheet\" type=\"text/css\" href=\"{% static \'style.css\' %)\">"

for a in dont:
    print(ord(a))

