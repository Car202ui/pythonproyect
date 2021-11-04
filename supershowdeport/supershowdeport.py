import csv

while True:

    print()
    print('1) Guardar nuevo producto')
    print('2) Consultar Productos')
    print('3) Stock Productos')
    print('4) Consultar Proveedores')
    print('5) Compra a Proveedores')
    print('6) Venta al cliente')
    print('7) Consultar Transacciones')
    print('8) Salir')
    opc=input('Elija una opción: ')

    if opc=='1':
        with open('Productos.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            idproduct=1
            val = 1
            for line in csv_reader:
                idproduct=idproduct+1
        
        arch=open('Productos.csv', 'a')
        nom=input('Ingresa el nombre del producto: ')
        
        while val == 1:
            idprov=input('Que código de proveedor va a distribuir el producto: ')
            try:
                idprov = int(idprov)
                val = 0
                
            except ValueError:
                print ('Escriba un código de proveedor correcto porfavor')
        
        val = 1
        while val == 1:
            precio=input('Que precio unitario tiene el producto: ')
            try:
                precio = int(precio)
                val = 0
                
            except ValueError:
                print ('Escriba un precio correcto porfavor')
        
        linea='\n'+str(idproduct)+';'+str(nom)+';'+str(precio)
        arch.write(linea)
        arch.close()
    
        arch=open('Stock.csv', 'a')
        linea='\n'+str(idproduct)+';'+str(nom)+';'+str(idprov)+';'+'0'
        arch.write(linea)
        arch.close()

    elif opc=='2':
        with open('Productos.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            print('idproducto;Nombre;Precio')
            for line in csv_reader:
                print(line)
    
    elif opc=='3':
        with open('Stock.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            print('idproducto;Nombre;idproveedor;Unidades Disponibles')
            for line in csv_reader:
                print(line)
    
    elif opc=='4':
        with open('Proveedores.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            print('idproveedor;NIT;Nombre Proveedor')
            for line in csv_reader:
                print(line)

    elif opc=='5':
        
        mat = list();
        val = 1
        while val == 1:
            cod=input('Ingresa el código de producto a comprar: ')
            try:
                cod = int(cod)
                val = 0
                
            except ValueError:
                print ('Escriba un código de producto correcto porfavor')
        
        val = 1
        while val == 1:
            idp=input('Ingresa el código de proveedor a quien le va a comprar: ')
            try:
                idp = int(idp)
                val = 0
                
            except ValueError:
                print ('Escriba un código de proveedor correcto porfavor')

        val = 1
        while val == 1:
            cant=input('Ingresa la cantidad de producto a comprar: ')
            try:
                cant = int(cant)
                val = 0
                
            except ValueError:
                print ('Escriba una cantidad correcta porfavor')
        
        with open('Stock.csv', "r+") as csv_file: 
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                delim = row[0].split(';')
                if int(delim[0]) == cod and int(delim[2]) == idp :
                    (delim[3]) = int(delim[3]) + cant 
                    
                mat.append(delim)        

        with open('Stock.csv', "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerows(mat) 

    elif opc=='6':
        
        mat = list();
        matdos = list();
        fac = 1

        val = 1
        while val == 1:
            cod=input('Ingresa el código de producto a comprar: ')
            try:
                cod = int(cod)
                val = 0
                
            except ValueError:
                print ('Escriba un código de producto correcto porfavor')
        val = 1
        while val == 1:
            cant=input('Ingresa la cantidad de producto a comprar: ')
            try:
                cant = int(cant)
                val = 0
                
            except ValueError:
                print ('Escriba una cantidad correcta porfavor')
        
        exist = 0

        with open('Stock.csv', "r+") as csv_file: 
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                delim = row[0].split(';')
                if int(delim[0]) == cod :
                    if cant <= int(delim[3]) :
                        (delim[3]) = int(delim[3]) - cant
                        transprov = (delim[2]) 
                        exist = 1
                    else:
                        exist = 2
                mat.append(delim)        

        if exist == 1:
            print('Venta exitosa')
            with open('Stock.csv', "w", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerows(mat)

            with open('Productos.csv', "r+") as csv_file: 
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    delim = row[0].split(';')
                    if int(delim[0]) == cod :
                        transprod = (delim[1])
                        transventa = cant * int(delim[2])

            with open('Proveedores.csv', "r+") as csv_file: 
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    delim = row[0].split(';')
                    if int(delim[0]) == int(transprov) :
                        transnit = (delim[1])
                        transnom = (delim[2])

            
            with open('Transacciones.csv', "r+") as csv_file: 
                csv_reader = csv.reader(csv_file)
                idconsecutivo=1
                for row in csv_reader:
                    delim = row[0].split(';')
                    idconsecutivo=idconsecutivo+1
                         
                        
            
            delim[0]= str(idconsecutivo)
            delim[1]= str(cod)
            delim[2]= str(transprod)
            delim[3]= str(transprov)
            delim[4]= str(transnit)    
            delim[5]= str(transnom)
            delim[6]= str(cant)
            delim[7]= str(transventa)
            
            matdos.append(delim)

            with open('Transacciones.csv', "a", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                writer.writerows(matdos)

            
            
        elif exist == 2:
            print('Venta no exitosa. No disponemos la cantidad de producto solicitado')
        else:
            print('Código de producto no existe.')

    elif opc=='7':
        with open('Transacciones.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            print('idtransacción;idproducto;Nombre Producto;idproveedor;NIT;Proveedor;Unidades Vendidas;Valor a Pagar')
            for line in csv_reader:
                print(line)
    

    elif opc=='8':
        print('Adios')
        break