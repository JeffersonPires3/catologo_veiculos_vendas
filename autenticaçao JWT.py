from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'  # Defina uma chave secreta forte em um ambiente real

# Função para verificar se o usuário está autenticado antes de acessar rotas protegidas
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token de autenticação ausente!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token de autenticação inválido!'}), 401

        return f(*args, **kwargs)

    return decorated

# Rota de login para autenticar o usuário e gerar um token JWT
@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.username == 'usuario' and auth.password == 'senha':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return jsonify({'message': 'Falha na autenticação!'}), 401

# Rota protegida que requer autenticação por token
@app.route('/carros')
@token_required
def get_carros():
    carros = [
        {'marca': 'Toyota', 'modelo': 'Corolla'},
        {'marca': 'Honda', 'modelo': 'Civic'},
        {'marca': 'Ford', 'modelo': 'Mustang'}
    ]
    return jsonify(carros)

if __name__ == '__main__':
    app.run(debug=True)
