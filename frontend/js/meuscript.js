$(function() { 
    
    function exibir_filmes() {
        $.ajax({
            url: 'http://localhost:5000/listar_filmes',
            method: 'GET',
            dataType: 'json',
            success: listar,
            error: function() {
            alert("erro ao ler dados, verifique o backend");
            }
        });

        function listar (filmes) {
            // esvaziar o corpo da tabela
            $('#corpoTabelaFilmes').empty();
            // tornar a tabela visível
            mostrar_conteudo("TabelaFilmes");

            // Percorre a lista
            for (fil of filmes) { //i vale a posição no vetor
                lin = '<tr id="linha_'+fil.id+'">' + 
                '<td>' + fil.id + '</td>' + 
                '<td>' + fil.nome + '</td>' + 
                '<td>' + fil.genero + '</td>' +
                '<td>' + fil.ano_de_lancamento + '</td>' +
                '<td>' + fil.diretor + '</td>' +
                '<td>' + fil.premio + '</td>' +
                '<td><a href=# id="excluir_' + fil.id + '" ' + 
                  'class="excluir_filmes"><img src="../img/excluir.png" '+
                  'alt="Excluir Filmes" title="Excluir Filmes"></a>' + 
                '</td>' + 
                '</tr>';

                console.log(lin);
                // adiciona a linha no corpo da tabela
                console.log(fil.nome,fil.diretor);
                $('#corpoTabelaFilmes').append(lin);
            }
            
        }
    }
    
    function mostrar_conteudo(identificador) {
        $("#TabelaFilmes").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        $("#"+identificador).removeClass('invisible');
    }

    $(document).on("click", "#linkListarFilmes", function(e) {
        e.preventDefault();
        exibir_filmes();
        
    });

    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoInicial");
    });

    $(document).on("click", "#btIncluirFilmes", function(e) {
        //pegar dados da tela
        e.preventDefault();
        id = $("#campoId").val();
        nome = $("#campoNome").val();
        genero = $("#campoGenero").val();
        ano_de_lancamento = $("#campoAnodeLancamento").val();
        diretor = $("#campoDiretor").val();
        premio = $("#campoPremio").val();

        // preparar dados no formato json
        var dados = JSON.stringify({ id: id, nome: nome, genero: genero, ano_de_lancamento: ano_de_lancamento, diretor: diretor, premio: premio });
        // fazer requisição para o back-end
        console.log(dados);
        
        $.ajax({
            url: 'http://localhost:5000/incluir_filmes',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: filmeIncluido, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });

        function filmeIncluido (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Filme incluído com sucesso!");
                // limpar os campos
                $("#campoId").val("");
                $("#campoNome").val("");
                $("#campoGenero").val("");
                $("#campoAnodeLancamento").val("");
                $("#campoDiretor").val("");
                $("#campoPremio").val("");

            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
    

    $('#modalIncluirFilmes').on('hide.bs.modal', function (e) {
        // se a página de listagem não estiver invisível
        if (! $("#TabelaFilmes").hasClass('invisible')) {
            // atualizar a página de listagem
            exibir_filmes();
            
        }
    });

    // a função abaixo é executada quando a página abre
    mostrar_conteudo("conteudoInicial");

    $(document).on("click", ".excluir_filmes", function() {
        var componente_clicado = $(this).attr('id');
        var nome_icone = "excluir_";
        var id_filmes = componente_clicado.substring(nome_icone.length);
        $.ajax({
            url: 'http://localhost:5000/excluir_filmes/'+id_filmes,
            type: 'DELETE',
            dataType: 'json',
            success: filmesExcluido,
            error: erroAoExcluir
        });
        function filmesExcluido (retorno) {
            if (retorno.resultado == "ok") { 
                $("#linha_" + id_filmes).fadeOut(1000, function(){   
                    alert("Filme removido com sucesso!");
                });
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoExcluir (retorno) {
            alert("erro ao excluir dados, verifique o backend: ");
        }
    });    

});


