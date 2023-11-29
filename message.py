def message(topic, slide_length):

    message = f"""Crie um esboço para uma apresentação de slides sobre o tópico de {topic} que possua {slide_length} slides. Certifique-se de que tenha {slide_length} slides apenas.

    Você tem permissão para usar os seguintes tipos de slide:
    Slide de título - (título, subtítulo)
    Slide de conteúdo - (título, conteúdo)
    Slide de imagem - (título, conteúdo, imagem)
    Slide de agradecimento - (Título)

    Coloque esta tag antes do slide de título: [L_TS]
    Coloque esta tag antes do slide de conteúdo: [L_CS]
    Coloque esta tag antes do slide da imagem: [L_IS]
    Coloque esta tag antes do slide de agradecimento: [L_THS]

    Coloque esta tag antes do título: [TITLE]
    Coloque esta tag após o título: [/TITLE]
    Coloque esta tag antes do subtítulo: [SUBTITLE]
    Coloque esta tag após o subtítulo: [/SUBTITLE]
    Coloque esta tag antes do Conteúdo: [CONTENT]
    Coloque esta tag após o Conteúdo: [/CONTENT]
    Coloque esta tag antes da imagem: [IMAGE]
    Coloque esta tag depois da imagem: [/IMAGE]

    Coloque "[SLIDEBREAK]" após cada slide

    Por exemplo:
    [L_TS]
    [TITLE]Entre nós[/TITLE]

    [SLIDEBREAK]

    [L_CS]
    [TITLE]O que há entre nós?[/TITLE]
    [CONTENTE]
    1. Among Us é um popular jogo multijogador online desenvolvido e publicado pela InnerSloth.
    2. O jogo se passa em um cenário com tema espacial onde os jogadores assumem os papéis de tripulantes e impostores.
    3. O objetivo dos Crewmates é completar tarefas e identificar os Impostores entre eles, enquanto o objetivo dos Impostores é sabotar a nave e eliminar os Crewmates sem serem pegos.
    [/CONTENTE]

    [SLIDEBREAK]

    Elabore o conteúdo, forneça o máximo de informações possível.
    LEMBRE-SE DE COLOCAR [/CONTENT] no final do Conteúdo.
    Não inclua caracteres especiais (?, !, ., :, ) no título.
    Não inclua nenhuma informação adicional em sua resposta e siga o formato."""

    return message