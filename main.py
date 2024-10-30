from flask import Flask, jsonify, request

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


app = Flask(__name__)

# Simulación de base de datos en memoria
usuarios = []

# Endpoint para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

# Endpoint para crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.json  # Aquí datos será una lista si envías un array JSON
    if isinstance(datos, list):
        for usuario in datos:
            nuevo_usuario = {
                "nombre": usuario.get("nombre"),
                "apellido": usuario.get("apellido"),
                "mail": usuario.get("mail")
            }
            usuarios.append(nuevo_usuario)
        return jsonify({"mensaje": "Usuarios creados exitosamente"}), 201
    else:
        # Caso en el que se envía un solo usuario como JSON
        nuevo_usuario = {
            "nombre": datos.get("nombre"),
            "apellido": datos.get("apellido"),
            "mail": datos.get("mail")
        }
        usuarios.append(nuevo_usuario)
        return jsonify(nuevo_usuario), 201


# Endpoint para obtener un usuario por email
@app.route('/usuarios/<string:mail>', methods=['GET'])
def obtener_usuario_por_email(mail):
    usuario = next((u for u in usuarios if u["mail"] == mail), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

# Ejecuta la aplicación en modo de desarrollo
if __name__ == '__main__':
    app.run(debug=True)
