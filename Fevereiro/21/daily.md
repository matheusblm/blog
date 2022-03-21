### Atualizando dados com o SQLAlchemy

Utilizamos o setattr para atualizar os dados. 
Recebe três argumentos, obj, name, value.

exemplo:
def atualizar_salgado(id):
    data = request.get_json()

    # Capturamos o objeto desejado a partir do id
    salgado = SalgadoModel.query.get(id)

    # Iteramos sobre as chaves e valores da nossa request
    # recebida, atualizando os atributos do objeto
    # capturado um a um.
    for key, value in data.items():
        setattr(salgado, key, value)
    
    
    current_app.db.session.add(salgado)
    current_app.db.session.commit()

    return {
        "id": salgado.id,
        "nome": salgado.nome,
        "preco": salgado.preco
    }
    
    ### Deletando itens pela primary key
    
    Retornar 204 quando não tem retorno e 200 quando tem.
    
    exemplo:
    def deletar_salgado(id):
    query = SalgadoModel.query.get(id)

    current_app.db.session.delete(query)
    current_app.db.session.commit()

    return "", 204
    
    
    def deletar_salgado_preco(preco):
    salgados = SalgadoModel.query.filter_by(preco=preco)

    salgados_deletados = [
        {"id": salgado.id, "nome": salgado.nome, "preco": salgado.preco}
        for salgado in salgados.all()
    ]

    salgados.delete()
    current_app.db.session.commit()

    return {
        "salgados_deletados": salgados_deletados
    }, 200
