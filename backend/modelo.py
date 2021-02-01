from config import *
import enum

class Produtora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    pais = db.Column(db.String(254))
    ano = db.Column(db.Integer)

    def __str__(self):
        return str(self.id)+", " + self.nome + ", " +\
            self.pais + ", " + str(self.ano)

    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "pais": self.pais,
            "ano": self.ano,
        })

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    genero = db.Column(db.String(254))
    ano_de_lancamento = db.Column(db.String(254))
    diretor = db.Column(db.String(254))
    premio = db.Column(db.String(254))
    produtora_id = db.Column(db.Integer, db.ForeignKey(Produtora.id))
    produtora = db.relationship("Produtora")

    def __str__(self):
        f = f"Filme {self.nome}"
        if self.produtora_id != None:
            f += f"exibida originalmente por {self.nome} localizada em {self.pais}"
            return f

    def json(self):
        if self.produtora_id is None:
            return {
                "id": self.id,
                "nome": self.nome,
                "genero": self.genero,
                "ano_de_lancamento": self.ano_de_lancamento,
                "diretor": self.diretor,
                "premio": self.premio,
        }

        else:
            return {
                "id": self.id,
                "nome": self.nome,
                "genero": self.genero,
                "ano_de_lancamento": self.ano_de_lancamento,
                "diretor": self.diretor,
                "premio": self.premio,
                "produtora": self.produtora.json()
            }

class Elenco(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    personagem = db.Column(db.String(254))
    categoria = db.Column(db.String(254))
    filme_id = db.Column(db.Integer, db.ForeignKey(Filme.id), nullable=False)
    filme = db.relationship("Filme")

    def __str__(self):
        return str(self.id)+", " + self.nome + ", " +\
            self.personagem + ", " + self.categoria

    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "personagem": self.personagem,
            "categoria": self.categoria,
            "filme": self.filme.json()
        })