from flask import Flask, jsonify, request
from products import productos

app = Flask(__name__)

@app.route('/')
def inicio():
    return jsonify({"message":"Inicio"})

@app.route('/productos')
def getProductos():
    return jsonify({"mensaje": "Lista de productos","Productos": productos})

@app.route('/productos/<string:nombre_producto>')
def getProducto(nombre_producto):
    productoEncontrado = [producto for producto in productos if producto['nombre'] == nombre_producto]

    if productoEncontrado:
        return jsonify({"producto": productoEncontrado[0]})
    else:
        return jsonify({"error": "Error, producto no encontrado"})
    
@app.route('/productos', methods=['POST'])
def addProducto():
    # print(request.json)

    nuevo_producto = {
        "nombre": request.json['nombre'],
        "precio": request.json['precio'],
        "cantidad": request.json['cantidad'],
    }

    productos.append(nuevo_producto)
    return jsonify({"success": "producto agregado correctamente", "productos": productos})

@app.route('/productos/<string:nombre_producto>', methods=['PUT'])
def editProducto(nombre_producto):

    producto_encontrado = [producto for producto in productos if producto['nombre'] == nombre_producto]

    if producto_encontrado:
        producto_encontrado[0]['nombre'] = request.json['nombre']
        producto_encontrado[0]['precio'] = request.json['precio']
        producto_encontrado[0]['cantidad'] = request.json['cantidad']
        return jsonify({"success": "producto actualizado", "producto": producto_encontrado[0]})
    else:
        return jsonify({"error": "producto no encontrado"})
    
@app.route('/productos/<string:nombre_producto>', methods=['DELETE'])
def deleteProducto(nombre_producto):

    producto_encontrado= [producto for producto in productos if producto['nombre'] == nombre_producto]

    if producto_encontrado:
        productos.remove(producto_encontrado[0])
        return jsonify({"success": "producto eliminado exitosamente", "productos": productos})
    else:
        return jsonify({"error": "producto no encontrado"})
    

if __name__ == '__main__':
    app.run(debug=True)