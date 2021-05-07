import re

temp = 0
cadena = ''
CA = 0
CB = 0
CC = 0
#declaracion de patron

def prioridades(operando):
    global temp
    exp = operando
    
    if  '*' in exp :
        posicion = exp.find('*')
        print(f"t{temp} =", exp[posicion-2], exp[posicion],  exp[posicion + 2], sep=" ")
        temp += 1
    if '/' in exp :
        posicion = exp.find('/')
        if '*' in exp :
            pass 
        else:
            posicion = exp.find('/')
            print(f"t{temp} =", exp[posicion-2], exp[posicion],  exp[posicion + 2], sep=" ")
            temp += 1
        
        if '*' in exp:
            if posicion < 10 :
                print(f"t{temp} =", exp[posicion-2], exp[posicion],  f"t{temp-1}" , sep=" ")
                temp += 1
            else :
                print(f"t{temp} =", f"t{temp-1}", exp[posicion],  exp[posicion+2] , sep=" ")
                temp += 1
        else:
            pass
    if '+' in exp:
    
        if '*' or '/' in exp:
            posicion = exp.find('+')
            if posicion < 10 :
                print(f"t{temp} =", f"t{temp-1}", exp[posicion],  exp[posicion + 2], sep=" ")
                temp += 1
            elif posicion < 10:
                print(f"t{temp} =", exp[posicion - 2], exp[posicion],  f"t{temp-1}", sep=" ")
                temp += 1
        else:
            pass
    
    if '-' in exp:
        posicion = exp.find('-')
        
        if '+' in exp :
            posicion2 = exp.find('+')    
            print(f"t{temp} =", exp[posicion2-2], exp[posicion2],  exp[posicion2 + 2], sep=" ")
            temp += 1
        else:
            pass
        
        if posicion == 10:
           print(f"t{temp} =", f"t{temp-1}", exp[posicion],  exp[posicion + 2], sep=" ")
           temp += 1
        elif posicion < 10:
            print(f"t{temp} =", exp[posicion - 2], exp[posicion],  f"t{temp-1}", sep=" ")
            temp += 1
        
def prioridades_2(operando):
    global CA, CB, CC, temp
    exp_c = operando
                       
    for i in exp_c:
        CA += 1
        if '/' in i: 
            print(f"t{temp} =", exp_c[CA-2], exp_c[CA - 1] , exp_c[CA], sep=" ")
            temp += 1
            for i in exp_c:
                CB += 1
                if '*' in i: 
                    print(f"t{temp} =", exp_c[CB-2], exp_c[CB-1], exp_c[CB], sep=" ")
                    temp += 1
                    for i in exp_c:
                        CC += 1
                        if '+' or '-' in i :
                            print(f"t{temp} =", f"t{temp-2}", exp_c[CC-5], f"t{temp-1}", sep=" ")
                            break
            temp = 0
            break
        elif i == "*": 
            print(f"t{temp} =", exp_c[CA-2], exp_c[CA - 1] , exp_c[CA], sep=" ")
            temp += 1
            for i in exp_c:
                CB += 1
                if '/' in i:
                    print(f"t{temp} =", exp_c[CB-2], exp_c[CB-1], exp_c[CB], sep=" ")
                    temp += 1
                    for i in exp_c:
                        CC += 1
                        if '+' or '-' in i:
                            print(f"t{temp} =", f"t{temp-2}", exp_c[CC-5], f"t{temp-1}", sep=" ")
                            break
            break

def prioridades_3(operando):
    global temp
    SE = []
    valor = operando
    POS = -1
    for i in valor:
        if i != " ":
            SE.append(i)
    print(SE)
    for i in SE:
        POS +=1 
        if i =="(" or i == ")":
            t0 = f"t{temp} = " + " " +  SE[POS-3] + " " + SE[POS-2] + " " + SE[POS-1]
    temp += 1
    print(t0)
    for i in SE:
        if '*' or '/' in i:
            if SE[2] == "(" :
                t1 = f"t{temp} = "+ f"t{temp-1}" + ' ' + SE[POS-3] + ' ' +  SE[POS-2] + ' '
            else:
                t1 = f"t{temp} = " + " " + SE[POS-6] + " " + SE[POS-5] + " " +  f"t{temp-1}"
    temp += 1
    print(t1)        
    for i in SE:
        if '+' or '-' in i: 
            if SE[2] == "(" :
                t2 = f"t{temp} = "+ f"t{temp-1}" + " " + SE[POS-1] + " " +  SE[POS] + " " 
            else:
                t2 = f"t{temp} = "+ " " + SE[POS-8] + " " +  SE[POS-7]  + " " +  f"t{temp-1}"
    temp += 1
    print(t2)


opcion = 0
while opcion != 11:
    print('--------------------------------------------------------------------------------------------')
    print('\nSelecciona una Opción')
    print('1.- 2 símbolos aritméticos con diferente prioridad')
    print('2.- 3 símbolos aritméticos con diferente prioridad.')
    print('3.- 2 símbolos aritméticos con paréntesis')
    opcion = int(input("Opción a realizar: "))

    if opcion == 1:
        print('--- codigo ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "\w+\s?\=\s?\w+\s?[+*-/]\s?\w+\s?[+*-/]\s?\w"
        reg = re.compile(regex)
        for line in textfile:
            lstentrada = reg.findall(line)
        prioridades(lstentrada[0])
        print(lstentrada[0][0:3], f"t{temp-1}")
        textfile.close()
    if opcion == 2:
        print('--- codigo ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+"
        reg = re.compile(regex)
        for line in textfile:
            lstentrada = reg.findall(line)
        sep_s = lstentrada[0]
        exp = sep_s.split()
        prioridades_2(exp)
        print(lstentrada[0][0:3], f"t{temp-1}")
        textfile.close()
    if opcion == 3:
        print('--- codigo ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        regex = "\w+\s\=\s[(]\s\w+\s[+*-/]\s\w+\s[)]\s\/\s\w+\s[+*-/]\s\w+$|^\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s[(]\s\w+\s[+*-/]\s\w+\s[)]$|^\w+\s\=\s\w+\s[+*-/]\s[(]\s\w+\s[+*-/]\s\w+\s[)]\s[+*-/]\s\w+$|^\w+\s\=\s[(]\s\w+\s[+*-/]\s\w+\s[)]\s[+*-/]\s\w+\s[+*-/]\s\w+"
        reg = re.compile(regex)
        for line in textfile:
            lstentrada = reg.findall(line)
        prioridades_3(lstentrada[0])
        print(lstentrada[0][0:3], f"t{temp-1}")
        textfile.close()
    else:
        print('Ingresa valores dentro de las opciones')
        