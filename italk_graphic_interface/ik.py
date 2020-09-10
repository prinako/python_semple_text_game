import os
name = input(" what is your name: ")

singup = open("p.txt", "wt")
singup.write(name)
singup.close()
singup_lang = open("q.txt", "at")
singup_lang.write(name)
singup_lang.close()

if os.path.exists('p.txt'):
    os.remove('p.txt')
    os.remove('q.txt')
else:
    print('file dont exte;;;;;')
