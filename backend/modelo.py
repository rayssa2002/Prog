from config import *

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    genero = db.Column(db.String(254))
    ano_de_lancamento = db.Column(db.String(254))    
    diretor = db.Column(db.String(254))
    premio = db.Column(db.String(254))

    def __str__(self):
        return  str(self.id)+"," + self.nome + "," +\
            str(self.genero) + "," + str(self.ano_de_lancamento) + "," +\
                str(self.diretor) + "," + str(self.premio)

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "genero": self.genero,
            "ano_de_lancamento": self.ano_de_lancamento,
            "diretor": self.diretor,
            "premio": self.premio,
        }

if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    f1= Filme(nome="La La Land", genero="Musical", ano_de_lancamento="2016", diretor="Damien Chazelle", premio="Oscar de Melhor Diretor e Atriz")
    f2= Filme(nome="Cisne Negro", genero="Drama/Suspense", ano_de_lancamento="2011", diretor="Darren Aronofsky", premio="Oscar de Melhor Atriz")

    db.session.add(f1)
    db.session.add(f2)
    db.session.commit()
    
    print(f1.json())
    print(f2.json())
    