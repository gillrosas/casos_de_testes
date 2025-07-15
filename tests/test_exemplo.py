from calcula_media import verificar_aprovacao

"Teste 01 - Erro: entrada deve ser uma lista de nota "
def test_valor_limite_001():
    assert verificar_aprovacao((1,2,3,4)) == 'Erro: A entrada deve ser uma lista de notas.'

"Teste 02- Erro: a lista tem exatamente 4 notas"
def test_valor_limite_002():
    assert verificar_aprovacao([8.0, 9.0, 7.5]) == 'Erro: A lista deve conter exatamente 4 notas.'


"Teste 03- Erro: A lista deve conter apenas números reais. a entrada são strings"
def test_valor_limite_003():
    assert verificar_aprovacao(["8.0", "9.0", "7.5", "9.5"]) == 'Erro: A lista deve conter apenas números reais.'

"Teste 04- Aprovado - valor limite - média = 8,5"
def test_valor_limite_004():
    assert verificar_aprovacao([8.0, 9.0, 7.5, 9.5]) == 'Aprovado'

"Teste 05- Recuperação - valor limite - média = 7"
def test_valor_limite_005():
    assert verificar_aprovacao([6.0, 7.0, 8.0, 7.0]) == 'Recuperação'

"Teste 06- Reprovado - valor limite - média = 5"
def test_valor_limite_006():
    assert verificar_aprovacao([4.0, 5.0, 6.0, 5.0]) == 'Reprovado'




