def f():
    lel=int(input("Digite un numero"))
    if lel%1==0 and lel%lel==0:
        if lel>4:
            if lel%2!=0 or lel%3!=0:
                print(lel,"Es primo")
                if lel%6!=0:
                    print(lel,"Es primo hermano")
                else:
                    print(lel,"No es primo hermano")
            else:
                print(lel,"No es primo")
        else:
            if lel==2 or lel==3:
                print(lel,"Es primo")
            else:
                print(lel,"No es primo")
    else:
        print(lel,"No es primo")
f()