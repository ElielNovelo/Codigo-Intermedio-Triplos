import re

temp = 0
cadena = ''
CA = 0
CB = 0
CC = 0
#declaracion de patron

def prioridades(operando):
    #declaracion de variables 
    global temp
    exp = operando
    
    #sentencia de validacion con respecto a prioridades Multiplicacion
    if  '*' in exp :
        posicion = exp.find('*')
        print(f"t{temp} =", exp[posicion-2], exp[posicion],  exp[posicion + 2], sep=" ")
        temp += 1
    #sentencia de validacion con respecto a prioridades Division
    if '/' in exp :
        #caso si es prioridad 
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
                #temp para acumular las acciones
                temp += 1
            else :
                print(f"t{temp} =", f"t{temp-1}", exp[posicion],  exp[posicion+2] , sep=" ")
                temp += 1
        else:
            pass
    #sentencia de validacion con respecto a prioridades Suma
    if '+' in exp:
        #Caso para terceros
        if '*' or '/' in exp:
            posicion = exp.find('+')
            if posicion < 10 :
                print(f"t{temp} =", f"t{temp-1}", exp[posicion],  exp[posicion + 2], sep=" ")
                #temp para acumular las acciones
                temp += 1
            elif posicion < 10:
                print(f"t{temp} =", exp[posicion - 2], exp[posicion],  f"t{temp-1}", sep=" ")
                temp += 1
        else:
            pass
     #sentencia de validacion con respecto a prioridades Resta
    if '-' in exp:
        posicion = exp.find('-')
        #caso si es prioridad 
        if '+' in exp :
            posicion2 = exp.find('+')    
            print(f"t{temp} =", exp[posicion2-2], exp[posicion2],  exp[posicion2 + 2], sep=" ")
            temp += 1
        else:
            pass
        #Caso para terceros
        if posicion == 10:
           print(f"t{temp} =", f"t{temp-1}", exp[posicion],  exp[posicion + 2], sep=" ")
           temp += 1
        elif posicion < 10:
            print(f"t{temp} =", exp[posicion - 2], exp[posicion],  f"t{temp-1}", sep=" ")
            temp += 1
        
def prioridades_2(operando):
    #declaracion de variables 
    global CA, CB, CC, temp
    exp_c = operando
     
                      
    for i in exp_c: #inicializacion de for para recorrer la lista
        CA += 1
        #comparaciones con respecto a prioridad
        if '/' in i: 
            #recorrido en caso de prioridad /
            print(f"t{temp} =", exp_c[CA-2], exp_c[CA - 1] , exp_c[CA], sep=" ")
            #temp para acumular las acciones
            temp += 1
            for i in exp_c:
                CB += 1
                #recorrido en caso de *
                if '*' in i: 
                    print(f"t{temp} =", exp_c[CB-2], exp_c[CB-1], exp_c[CB], sep=" ")
                    temp += 1
                    for i in exp_c:
                        CC += 1
                        #recorrido en caso de que alguno de estas se cumpla
                        if '+' or '-' in i :
                            print(f"t{temp} =", f"t{temp-2}", exp_c[CC-5], f"t{temp-1}", sep=" ")
                            break
            temp = 0
            break
        #recorrido en caso de prioridad *
        elif i == "*":
            #recorrido en caso de prioridad * 
            print(f"t{temp} =", exp_c[CA-2], exp_c[CA - 1] , exp_c[CA], sep=" ")
            #temp para acumular las acciones
            temp += 1
            for i in exp_c:
                CB += 1
                #recorrido en caso de /
                if '/' in i:
                    print(f"t{temp} =", exp_c[CB-2], exp_c[CB-1], exp_c[CB], sep=" ")
                    temp += 1
                    for i in exp_c:
                        CC += 1
                        #recorrido en caso de que alguno de estas se cumpla
                        if '+' or '-' in i:
                            print(f"t{temp} =", f"t{temp-2}", exp_c[CC-5], f"t{temp-1}", sep=" ")
                            break
            break

def prioridades_3(operando):
    #declaracion de variables
    global temp
    SE = []
    valor = operando
    POS = -1
    #recorrido del texto y agregarlo a una lista por caracter
    for i in valor:
        if i != " ":
            SE.append(i)

    #primer caso cuando detecte un subconjunto entre parentesis
    for i in SE:
        POS +=1 
        if i =="(" or i == ")":
            #caso prioridad
            t0 = f"t{temp} = " + " " +  SE[POS-3] + " " + SE[POS-2] + " " + SE[POS-1]
    temp += 1
    print(t0)
    #caso de presendecia * -- / cualquiere de los casos
    for i in SE:
        if '*' or '/' in i:
            #en caso de encontrarse cerca del lado izq el subconjunto se evalua caso DRC
            if SE[2] == "(" :
                t1 = f"t{temp} = "+ f"t{temp-1}" + ' ' + SE[POS-3] + ' ' +  SE[POS-2] + ' '
            else:
                #en caso de encontrarse cerca del lado DRC el subconjunto se evalua caso IZQ
                t1 = f"t{temp} = " + " " + SE[POS-6] + " " + SE[POS-5] + " " +  f"t{temp-1}"
    temp += 1
    print(t1)        
    for i in SE:
        #caso de presendecia + -- - cualquiere de los casos
        if '+' or '-' in i:
            #en caso de encontrarse cerca del lado izq el subconjunto se evalua caso DR 
            if SE[2] == "(" :
                t2 = f"t{temp} = "+ f"t{temp-1}" + " " + SE[POS-1] + " " +  SE[POS] + " " 
            #en caso de encontrarse cerca del lado DRC el subconjunto se evalua caso IZQ
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
        #expresion regular
        regex = "\w+\s?\=\s?\w+\s?[+*-/]\s?\w+\s?[+*-/]\s?\w"
        reg = re.compile(regex)
        for line in textfile:
            lstentrada = reg.findall(line)
        #envio a funcion
        prioridades(lstentrada[0])
        print(lstentrada[0][0:3], f"t{temp-1}")
        print("")
        print("MARCO ANTONIO BAEZA CAHUM")
        print("REYES GUADALUPE KAUIL ESPADAS")
        print("ELIEL DAVID NOVELO CAHUM")
        textfile.close()
    if opcion == 2:
        print('--- codigo ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        #expresion regular 
        regex = "\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+"
        reg = re.compile(regex)
        for line in textfile:
            lstentrada = reg.findall(line)
        sep_s = lstentrada[0]
        exp = sep_s.split()
        #envio a funcion
        prioridades_2(exp)
        print(lstentrada[0][0:3], f"t{temp-1}")
        print("")
        print("MARCO ANTONIO BAEZA CAHUM")
        print("REYES GUADALUPE KAUIL ESPADAS")
        print("ELIEL DAVID NOVELO CAHUM")
        textfile.close()
    if opcion == 3:
        print('--- codigo ---')
        filename = "TextoPrac.txt"
        textfile = open(filename, "r")
        #ESPRESION REGULAR
        regex = "\w+\s\=\s[(]\s\w+\s[+*-/]\s\w+\s[)]\s\/\s\w+\s[+*-/]\s\w+$|^\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s[(]\s\w+\s[+*-/]\s\w+\s[)]$|^\w+\s\=\s\w+\s[+*-/]\s[(]\s\w+\s[+*-/]\s\w+\s[)]\s[+*-/]\s\w+$|^\w+\s\=\s[(]\s\w+\s[+*-/]\s\w+\s[)]\s[+*-/]\s\w+\s[+*-/]\s\w+"
        reg = re.compile(regex)
        for line in textfile:
            lstentrada = reg.findall(line)
        #ENVIO AL FUNCION
        prioridades_3(lstentrada[0])
        print(lstentrada[0][0:3], f"t{temp-1}")
        print("")
        print("MARCO ANTONIO BAEZA CAHUM")
        print("REYES GUADALUPE KAUIL ESPADAS")
        print("ELIEL DAVID NOVELO CAHUM")
        textfile.close()
    else:
        print('Ingresa valores dentro de las opciones')
        
