hoje = input().lower()
medico = input().lower()

hoje = hoje.count('a')
medico = medico.count('a')

if hoje >= medico:
    print("go")
elif hoje < medico:
    print("no")