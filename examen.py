danger ="\033[91m"	
warning ="\033[93m"
success ="\033[92m"
info ="\033[94m"
reset ="\033[0m"
inventory = {}
count_id = 1

# The next functions are for validation diferent forms and conditions
# For example, that not are number negative or words  

def add_product5():
    # Llamar a las funciones de validación
    product_check = validation_product()
    price_check = validation_price()
    quantity_check = validation_quantity()
    id = max(inventory.keys(), default=0) + 1
    # Verificar si el producto ya existe en el inventario
    for i in inventory.values():
        if i["name"].lower() == product_check.lower():
            print(danger +"El producto ya existe en el inventario."+ reset)
            return
    # Agregar el producto al inventario con el ID generado
    inventory[id] = {
        "name": product_check,
        "price": price_check,
        "quantity": quantity_check
        }
    # Mostrar el producto agregado
    print(f"Producto con ID: {id} Nombre: {product_check} Precio: ${price_check} Cantidad: {quantity_check}.")
    print(success+"Agregado con éxito."+reset)
    # Preguntar al usuario si desea agregar otro producto
    
    print(info+"========== Su inventario actual =========="+reset)
    for id, data in inventory.items():
        print(f"ID: {id}, Nombre: {data['name']}, Precio: ${data['price']}, Cantidad: {data['quantity']}")    
    print("Regresando al menú principal...")            

def validation_id():
    while True:
        id = input(info +"Ingrese el ID del producto: "+ reset)
        if not id.isdigit():
            print(danger + "Error: ingresa solo números, no texto." + reset)
            continue
        # Converse to number int
        id = int(id)
        if id in inventory:
            print(danger +"El ID ya existe. Por favor, elija otro."+ reset)
        # check that number is not negative
        if id < 0:
            print(danger +"El ID no puede ser negativo."+ reset)
            continue
        print(success + f"ID válido: {id}"+ reset)
        #retur the id for other moments
        return id    

 #this function is similar to previus, but search an id exist. 
def search_id():
    while True:
        id = input(info +"Ingrese el ID del producto, : " + reset)
        if not id.isdigit():
            print(danger +"Error: ingrese solo números."+ reset)
            continue
        id = int(id)
        if id < 0:
            print(danger +"El ID no puede ser negativo."+ reset)
            continue
        # Check if the product is in stock
        if id not in inventory:
            print(danger +"ID no encontrado en el inventario."+ reset)
            continue
        return id

  #check the name input, yours conditional, not numbers.      
def validation_name():
    while True:
        name = input(info +"Ingrese el nombre del producto: " + reset).strip()
        #delete space clear.
        #that user can using word
        if name == "":
            print(danger +"Error: ingresa un nombre de producto."+ reset)     
            continue
        #validation the words
        elif all(x.isalpha() or x.isspace() for x in name):
            print(success + f"Nombre válido: {name}"+ reset)
            
            return name
        
                   
def validation_product():
    while True:
        product = input(info +"Ingrese el nombre del producto: " + reset).strip()
        #that user can whrite two or more words.
        if product == "":
            print(danger +"Error: ingresa un nombre de producto."+ reset)   
            continue
        ##delete space clear.
        elif all(x.isalpha() or x.isspace() for x in product):
            print(success + f"Nombre válido: {product}"+ reset)
            return product
                
def validation_price():
    while True:
        price = input(info +"Ingrese el primer/nuevo precio del producto: "+ reset)
        #check that the price be a number positive and not another thing 
        if not price.replace('.', '', 1).isdigit():
            print(danger +"ERROR: lo que ingresaste no es positivo y/o no es un número"+ reset)
            continue
        price = float(price)
        if price <= 0:
            print(danger + " El precio debe ser mayor que cero." + reset)
            continue
        return price
            
def validation_quantity():
    while True:
            quantity = input(info+"Ingrese la cantidad del producto: "+reset)
            #check that the quantity be a value positive
            if not quantity.replace('.', '', 1).isdigit():
                print(danger +"ERROR: lo que ingresaste no es positivo y/o no es un número"+ reset)
                continue
            quantity = int(quantity)
            if quantity<= 0:
                print(danger + " El precio debe ser mayor que cero." + reset)
                continue
            return quantity  

# Funtion for add products
def add_product():
    # Llamar a las funciones de validación
    product_check = validation_product()
    price_check = validation_price()
    quantity_check = validation_quantity()
    id = max(inventory.keys(), default=0) + 1
    # Verificar si el producto ya existe en el inventario
    for i in inventory.values():
        if i["name"].lower() == product_check.lower():
            print(danger +"El producto ya existe en el inventario."+ reset)
            return
    # Agregar el producto al inventario con el ID generado
    inventory[id] = {
        "name": product_check,
        "price": price_check,
        "quantity": quantity_check
        }
    # Mostrar el producto agregado
    print(f"Producto con ID: {id} Nombre: {product_check} Precio: ${price_check} Cantidad: {quantity_check}.")
    print(success+"Agregado con éxito."+reset)
    # Preguntar al usuario si desea agregar otro producto
    next= input(info +"¿Desea agregar otro producto? (s/n): "+reset)
    if next.lower() == 's':
        add_product()
    else:
        print(info+"========== Su inventario actual =========="+reset)
        for id, data in inventory.items():
            print(f"ID: {id}, Nombre: {data['name']}, Precio: ${data['price']}, Cantidad: {data['quantity']}")    
        print("Regresando al menú principal...")       


def search_product():
    if not inventory:
        print(danger +"El inventario está vacío."+ reset)
        return
    # Ask to user if want search for name or id.
    search = input(info+"¿Desea consultar por ID o nombre? (id/nombre): "+reset).lower()
    if search == "id":
        id_search = search_id()
        product = inventory.get(id_search)
        if product:
            print(f"ID: {id_search}, Nombre: {product['name']}, Precio: ${product['price']}, Cantidad: {product['quantity']}")
        else:
            print(danger +"Producto no encontrado."+ reset)
            return
    
    #search by name
    elif search == "nombre":
        search_name = validation_name()
        found = False

        for id, data in inventory.items():
            if data["nombre"].lower() == search_name.lower():
                print(f"ID: {id}, Nombre: {data['name']}, Precio: ${data['price']}, Cantidad: {data['quantity']}")
                found = True
                break
        if not found:
            print(danger +"Producto no encontrado."+ reset)
            return
    else:
        print(danger+"Opción no válida. Por favor, elija 'id' o 'nombre'."+reset)
        # we ask if user want search another product
    next = input(info+"¿Desea consultar otro producto? (s/n): "+reset)
    if next.lower() == 's':
        search_product()
    else:
        print("Regresando al menú principal...")        

#next funtions           
def update_product():
    while True:
        if not inventory:
            print(danger + "El inventario está vacío." + reset)
            return

        # See all products before the search
        print(info + "====== Inventario actual ======" + reset)
        for id, data in inventory.items():
            print(f"ID: {id}, Nombre: {data['name']}, Precio: ${data['price']}, Cantidad: {data['quantity']}")
        print("=" * 40)

        # Ask to user if want search for name or id.
        search_tipe= input(info + "¿Desea buscar el producto por ID o nombre? (id/nombre): " + reset).lower()

        # search by ID
        if search_tipe == "id":
            id = search_id()
            if id in inventory:
                product = inventory[id]
            else:
                print(danger + "Producto no encontrado." + reset)
                continue

        # search by name
        elif search_tipe == "nombre":
            name_search = validation_name()
            product = 0
            id = 0
            for identification, data in inventory.items():
                if data["name"].lower() == name_search.lower():
                    product = data
                    id = identification
                    break
            if not product:
                print(danger + "Producto no encontrado." + reset)
                continue

        else:
            print(danger + "Opción no válida. Por favor, elija 'id' o 'nombre'." + reset)
            continue

        # print the product found
        print(f"ID: {id}, Nombre: {product['name']}, Precio: ${product['price']}, Cantidad: {product['quantity']}")

        #check and clear the product in the dictionary
        new_price = validation_price()
        inventory[id]["price"] = new_price
        print(success + f"Producto {product['name']} actualizado con éxito." + reset)

        next = input(info + "¿Desea actualizar el precio de otro producto? (s/n): " + reset)
        if next.lower() != 's':
            print("Regresando al menú principal...")
            break

#function for delete product
def delete_product():
    if not inventory:
        print(danger +"El inventario está vacío."+ reset)
        return
    print(info + "====== Inventario actual ======" + reset)
    for id, data in inventory.items():
        print(f"ID: {id}, Nombre: {data['name']}, Precio: ${data['price']}, Cantidad: {data['quantity']}")
    print("=" * 40)
    # call the id 
    #Check if the product is in stock
    id_search = search_id()
    product = inventory.get(id_search)
    if product:
        print(f"ID: {id_search}, Nombre: {product['name']}, Precio: ${product['price']}, Cantidad: {product['quantity']}" )
    else:
        print(danger +"Producto no encontrado."+reset)
        return
    # We delete product from the inventory
    if id_search in inventory:
        del inventory[id_search]
        print(success +f"Producto con ID {id_search} eliminado con éxito."+reset)
    else:
        print(danger+"Producto no encontrado."+ reset)
       
    next= input(info+"¿Desea consultar otro producto? (s/n): "+reset)
    if next.lower() == 's':
        delete_product()
    else:
        print("Regresando al menú principal...")  
        
def total_value_inventory():
    if not inventory:
        print(danger +"El inventario está vacío."+ reset)
        return
    # Calculate the value total to inventory in the stock using the funtion lambda
    # multiplicamos alls the values of price with alls the values of quantity
    total = sum(map(lambda x: x["price"] * x["quantity"], inventory.values()))   # print alls values the inventory       
    print(info +f"El valor total del inventario es: ${total}"+reset)
    next = input(info+"¿Desea consultar otro producto? (s/n): "+reset)
    if next.lower() == 's':
        search_product()
    else:
        print("Regresando al menú principal...")


 # Funtion principal  
 
def menu():
    while True:  
        print(info +"======INVENTARIO MINI MERCADO======"+ reset)
        print("1.Agregar productos")
        print("2.Consultar productos con ID o nombre")
        print("3.Actualizar precio con Id o nombre")
        print("4.Eliminar productos con ID")
        print("5.Cálcular valor total de inventario")
        print("6.Salir")
        print(info+"==================================="+reset)

        option_menu = input(info +"Elige una opcion: " + reset)
        
        if option_menu.isdigit():
            option_menu = int(option_menu)  # Converse to number int for operations the conditionals.

            if 1 <= option_menu <= 6:
                print(success +"Entrada válida. Continuamos..."+ reset)
                break  
            else:
                print(danger +"Error: opción inválida."+ reset)
        else:
            print(danger +"Error: ingresa solo números, no texto."+ reset)
            break

    match option_menu:
        case 1:
            print("======Agrega un producto======")
            add_product()
            
        case 2:
            print("======Consulta de productos======")
            search_product()
            
        case 3:
            print("======Actualizar productos======")
            update_product()   
            
        case 4:
            print("======Eliminar productos======")
            delete_product()
        
        case 5:
            print("======Cálcular valor total de inventario======")
            total_value_inventory()
            
        case 6:
            print("======Salir======")
            print("Gracias por usar el sistema de inventario.")
            False
                
                
    print(menu())

print("Debes ingresar 5 productos inicialmente")
count_id = 1
add_product5() 
add_product5() 
add_product5() 
add_product5() 
add_product5() 
print(menu())


