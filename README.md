# Meu primeiro projeto solo

### Resumo
Sou sócia de uma loja e decidi utilizar o relatório de vendas realizadas de 01/07/2023 até 24/05/2024 para fazer um projeto de tratamento e apresentação de dados.
Como o relatório (ReportPedidosItens.csv) contém informações internas, como nome completo dos clientes, não vou disponibilizá-lo aqui, mas você ainda pode se basear no script e fazer a análise com o CSV que você quiser :wink:

### Detalhes
Aqui vai uma explicação passo a passo do que o script faz:

1. Importa as bibliotecas necessárias: 
    - Pandas (para manipulação de dados) 
    - Matplotlib (para visualização dos dados)
2. Lê o CSV (ReportPedidosItens.csv) pulando as 2 primeiras linhas que não tinham informações relevantes
    > Lembrando que o arquivo CSV está no mesmo diretório que o script, por isso foi usado apenas o nome, e não o caminho do arquivo 
3. Apaga colunas vazias e colunas desnecessárias à análise
4. Filtra o dataframe para trabalhar apenas com os pedidos faturados
5. Formata o nome dos clientes para mostrar no gráfico apenas o primeiro nome + primeira letra do último nome e todas as letras em maiúsculo (ex: Beatriz Pereira agora é exibido como BEATRIZ P)
6. Usando df.info() sabemos os tipos de cada coluna. Tirando a primeira, as outras eram todas do tipo 'object', então o script formata:
    - Colunas 'Descrição' e 'Cliente' para tipo _string_
    - Coluna 'Data' para tipo _data_
    - Colunas restantes para tipo _float_
7. Remove clientes PJ que estavam atrapalhando os valores totais dos gráficos
8. Agrupa o dataframe por 'Cliente' e soma o valor gasto por cada cliente nesse período. O resultado é exibido em um gráfico de barras horizontais
9. Agrupa o dataframe por 'Descrição' (de cada produto) e soma a quantidade vendida nesse período. O resultado é exibido em um gráfico de barras horizontais