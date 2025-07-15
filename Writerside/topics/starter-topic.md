# Casos de testes 
<topic title="Casos de Teste - verificar_aprovacao()" id="starter-topic">
  <p>
    Abaixo estão os casos de teste da função <code>verificar_aprovacao</code>, utilizando diferentes técnicas de teste.
  </p>

  <section title="Validação de Entrada (Técnicas: Partição de Equivalência, Valor Limite)">
    <subsection title="TC_APROV_001">
      <ul>
        <li><b>ID do Caso de Teste:</b> TC_APROV_001</li>
        <li><b>Técnica Utilizada:</b> Partição de Equivalência</li>
        <li><b>Notas de Entrada:</b> (1, 2, 3, 4) [Tupla, não lista]</li>
        <li><b>Resultado Esperado:</b> 'Erro: A entrada deve ser uma lista de notas.'</li>
      </ul>
    </subsection>

    <subsection title="TC_APROV_002">
      <ul>
        <li><b>ID do Caso de Teste:</b> TC_APROV_002</li>
        <li><b>Técnica Utilizada:</b> Análise de Valor Limite</li>
        <li><b>Notas de Entrada:</b> [8.0, 9.0, 7.5]</li>
        <li><b>Resultado Esperado:</b> 'Erro: A lista deve conter exatamente 4 notas.'</li>
      </ul>
    </subsection>

    <subsection title="TC_APROV_003">
      <ul>
        <li><b>ID do Caso de Teste:</b> TC_APROV_003</li>
        <li><b>Técnica Utilizada:</b> Partição de Equivalência</li>
        <li><b>Notas de Entrada:</b> ["8.0", "9.0", "7.5", "9.5"]</li>
        <li><b>Resultado Esperado:</b> 'Erro: A lista deve conter apenas números reais.'</li>
      </ul>
    </subsection>
  </section>

  <section title="Classificação da Média (Técnica: Análise de Valor Limite)">
    <subsection title="TC_APROV_004">
      <ul>
        <li><b>ID do Caso de Teste:</b> TC_APROV_004</li>
        <li><b>Técnica Utilizada:</b> Análise de Valor Limite</li>
        <li><b>Notas de Entrada:</b> [8.0, 9.0, 7.5, 9.5]</li>
        <li><b>Resultado Esperado:</b> 'Aprovado'</li>
      </ul>
    </subsection>

    <subsection title="TC_APROV_005">
      <ul>
        <li><b>ID do Caso de Teste:</b> TC_APROV_005</li>
        <li><b>Técnica Utilizada:</b> Análise de Valor Limite</li>
        <li><b>Notas de Entrada:</b> [6.0, 7.0, 8.0, 7.0]</li>
        <li><b>Resultado Esperado:</b> 'Recuperação'</li>
      </ul>
    </subsection>

    <subsection title="TC_APROV_006">
      <ul>
        <li><b>ID do Caso de Teste:</b> TC_APROV_006</li>
        <li><b>Técnica Utilizada:</b> Análise de Valor Limite</li>
        <li><b>Notas de Entrada:</b> [4.0, 5.0, 6.0, 5.0]</li>
        <li><b>Resultado Esperado:</b> 'Reprovado'</li>
      </ul>
    </subsection>
  </section>
</topic>
