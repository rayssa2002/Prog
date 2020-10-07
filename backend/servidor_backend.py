from config import *
from modelo import Filme

@app.route("/")
def inicio():
    return 'Sistema para Cadastro para Filmes '+\
        '<a href="/listar_filmes">Listar Filmes</a>'

@app.route("/listar_filmes")
def listar_filmes():
    filmes = db.session.query(Filme).all()
    filme_em_json = [Filme.json() for Filme in filmes]
    
    return (jsonify(filme_em_json))


@app.route("/incluir_filmes", methods=['POST'])
def incluir_filmes():
    resposta = jsonify({"resultado":"ok","detalhes": "ok"})
    dados = request.get_json()
    try:   
        nova=Filme(**dados)
        db.session.add(nova)
        db.session.commit()
        
    except Exception as e: 
        resposta = jsonify({"resultado":"erro","detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin","*")
    
    return resposta

@app.route("/excluir_filmes/<int:filmes_id>", methods=['DELETE'])
def excluir_filmes(filmes_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Filme.query.filter(Filme.id == filmes_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta    

app.run(debug=True)