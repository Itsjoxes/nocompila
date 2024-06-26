import json

#DATOS DEL USUARIO
nombre = ""
apellido = ""
sueldobruto = 250000
sueldoliquido = 0
trabajo = ""

#DESCUENTOS
dsctafp = 0
dsctsalud = 0
dscttotal = 0

#Listas
totalpersonas = []
personas = []

#MENU
opc = ""
opctrabajo = ""
buscarpega = ""

while True:
    print(''' 
    NOCOMPILA
    ---------
    1) Registrar Datos
    2) Mostrar Personas
    3) Buscar Personas
    4) Guardar Datos
    
    ''')
    opc = input("Ingrese un numero: ")
    if opc.isnumeric() == False:
        print("Eso no es un numero")
    else:
        opc = int(opc)

    if opc == 1:
        nombre = input("Ingrese su Nombre: ").capitalize()
        apellido = input("Ingrese su Apellido: ").capitalize()
        while True:
            print('''   INGRESE SU TRABAJO
                  1) MESERO
                  2) CAJERO
                  3) COCINERO 
                  ''')
            opctrabajo = input("Ingrese un numero: ")
            if opctrabajo.isnumeric() == False:
                print("Eso no es un numero")
            else:
                opctrabajo = int(opctrabajo)

            if opctrabajo == 1:
                trabajo = "Mesero"
                break
            if opctrabajo == 2:
                trabajo = "Cajero"
                break
            if opctrabajo == 3:
                trabajo = "Cocinero"
                break

        while True:
            sueldobruto = input("Ingrese su Sueldo: ")
            if sueldobruto.isnumeric() == False:
                print("Eso no es un numero")
            else:
                sueldobruto = int(sueldobruto)
                dsctafp = sueldobruto * 7 / 100
                dsctsalud = sueldobruto * 10 / 100
                dscttotal = dsctafp + dsctsalud
                sueldoliquido = sueldobruto - dscttotal
                print(sueldobruto)

                personas = []
                personas.append(nombre) #0
                personas.append(apellido) #1
                personas.append(trabajo) #2
                personas.append(sueldobruto) #3
                personas.append(dsctafp) #4
                personas.append(dsctsalud) #5
                personas.append(dscttotal) #6
                personas.append(sueldoliquido) #7
 
                totalpersonas.append(personas)

                break

    if opc == 2:
        for items in totalpersonas:
            print(f'''
        Nombre y Apellido: {items[0]} {items[1]}
        Trabajo: {items[2]}
        Sueldo Bruto: {items[3]}
        Descuento AFP: {items[4]}
        Descuento Salud: {items[5]}
        Descuento Todal: {items[6]}
        - o -
        Sueldo Liquido: {items[7]}

            ''')

            
    if opc == 3:
        while True:
            print('''   INGRESE SU TRABAJO
                  1) MESERO
                  2) CAJERO
                  3) COCINERO 
                  ''')
            opctrabajo = input("Ingrese un numero: ")
            if opctrabajo.isnumeric() == False:
                print("Eso no es un numero")
            else:
                opctrabajo = int(opctrabajo)

            if opctrabajo == 1:
                buscarpega = "Mesero"
                for items in totalpersonas:
                    if items[2] == buscarpega:
                        print(F'''
        Nombre y Apellido: {items[0]} {items[1]}
        Trabajo: {items[2]}
        Sueldo Bruto: {items[3]}
        Descuento AFP: {items[4]}
        Descuento Salud: {items[5]}
        Descuento Todal: {items[6]}
        - o -
        Sueldo Liquido: {items[7]}
                             ''')
                break
            if opctrabajo == 2:
                buscarpega = "Cajero"
                for items in totalpersonas:
                    if items[2] == buscarpega:
                        print(F'''
        Nombre y Apellido: {items[0]} {items[1]}
        Trabajo: {items[2]}
        Sueldo Bruto: {items[3]}
        Descuento AFP: {items[4]}
        Descuento Salud: {items[5]}
        Descuento Todal: {items[6]}
        - o -
        Sueldo Liquido: {items[7]}
                             ''')
                break
            if opctrabajo == 3:
                buscarpega = "Cocinero"
                for items in totalpersonas:
                    if items[2] == buscarpega:
                        print(F'''
        Nombre y Apellido: {items[0]} {items[1]}
        Trabajo: {items[2]}
        Sueldo Bruto: {items[3]}
        Descuento AFP: {items[4]}
        Descuento Salud: {items[5]}
        Descuento Todal: {items[6]}
        - o -
        Sueldo Liquido: {items[7]}
                             ''')
                break


    if opc == 4:
        with open('Datos.json','w') as totalpersonas:
            json.dump(totalpersonas)     

    
    if opc == 5:
        with open('Datos.json','r') as archivo:
            totalpersonas = json.load()