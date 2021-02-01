from modelo import *
import os

if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1 = Produtora(nome = "Soni Pictures Entertainment", pais = "Estados Unidos", ano = 1987)
    p2 = Produtora(nome = "Time Warner", pais = "Estados Unidos", ano = 1990)

    f1= Filme(nome="La La Land", genero="Musical", ano_de_lancamento="2016", diretor="Damien Chazelle", premio="Oscar de Melhor Diretor e Atriz", produtora_id = 1)
    f2= Filme(nome="Cisne Negro", genero="Drama/Suspense", ano_de_lancamento="2011", diretor="Darren Aronofsky", premio="Oscar de Melhor Atriz", produtora_id = 2)

    e1 = Elenco(nome = "Emma Stone", personagem = "Mia", categoria = "Protagonista", filme_id = 1)
    e2 = Elenco(nome = "Natalie Portman", personagem = "Nina Sayers", categoria = "Protagonista", filme_id = 2)

    db.session.add(p1)
    db.session.add(p2)

    db.session.add(f1)
    db.session.add(f2)

    db.session.add(e1)
    db.session.add(e2)
    
    db.session.commit()
    
    print(p1.json())
    print(p2.json())

    print(f1.json())
    print(f2.json())

    print(e1.json())
    print(e2.json())