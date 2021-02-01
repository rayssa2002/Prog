from config import *
from modelo import Produtora, Filme, Elenco

@app.route("/")
def inicio():
    return 'Sistema para Cadastrar Filmes. '+\
        '<a href="/listar/Filme">Listar Filmes</a>'

@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "Produtora":
      dados = db.session.query(Produtora).all()
    elif classe == "Filme":
      dados = db.session.query(Filme).all()
    elif classe == "Elenco":
      dados = db.session.query(Elenco).all()
    lista_jsons = [ x.json() for x in dados ]
    resposta = jsonify(lista_jsons)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/incluir_filme", methods=['post'])
def incluir_filme():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try:
        nova =Filme(**dados)
        db.session.add(nova)
        db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/excluir_filme/<int:filme_id>", methods=["delete"])
def excluir_filme(filme_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Filme.query.filter(Filme.id == filme_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)