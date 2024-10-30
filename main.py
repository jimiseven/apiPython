from flask import Flask, jsonify, request

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
    nuevo_usuario = {
        "nombre": request.json.get("nombre"),
        "apellido": request.json.get("apellido"),
        "mail": request.json.get("mail")
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
