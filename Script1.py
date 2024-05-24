import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ReportPedidosItens.csv', sep=';', skiprows=2) #skiprows=2 para pular os cabeçalhos
df = df.dropna(axis=1, how='all') #remove colunas vazias (axis=1 significa coluna)
df = df.loc[df['Status'] == 'Pedido Faturado'] #filtra apenas os pedidos faturados
df = df.drop(columns=['Status', 'Validade', 'Empresa', 'Cód. NFe/NFSe', 'Data NFe', 'Data Faturamento Pedido', 'CNPJ/CPF', 'Cidade', 'Estado', 'Região', 'Forma Pagamento', 'Foi Pago?', 'Frete (R$)', 'NCM', 'Comissão Unitária (R$)', 'Comissão Total', 'Peso Bruto (KG)', 'Peso Líquido', 'Unidade Comercial', 'Gênero', 'Marca', 'Fornecedor', 'Nome Produto', 'Código Prod.']) #exclui colunas desnecessárias

def format_names(name):
    parts = name.split() #divide a string do nome em palavras separadas
    return parts[0] + ' ' + parts[-1][0] #retorna o primeiro nome (parts[0]) e a 1ª letra do último nome

df['Cliente'] = df['Cliente'].str.upper().apply(format_names) #aplica a função format_names à coluna Cliente
df['Data'] = pd.to_datetime(df['Data']) #converte a coluna Data para o formato de data
df[['Quantidade', 'Preço Venda (R$)', 'Preço Venda Total (R$)', 'Lucro %', 'Custo R$']] = df[['Quantidade', 'Preço Venda (R$)', 'Preço Venda Total (R$)', 'Lucro %', 'Custo R$']].apply(lambda x: x.str.replace(',', '.').astype(float)) #substitui vírgulas por pontos e converte as colunas para float
df[['Descrição', 'Cliente']] = df[['Descrição', 'Cliente']].astype(str) 


clientes_ignorados = ['FLIPPER L', 'FLIPPER D', 'FOUR C', 'SEM N']
df_filtrado = df[~df['Cliente'].isin(clientes_ignorados)] #remove os clientes ignorados

#agrupando os pedidos por cliente e somando os valores totais:
clientes = df_filtrado.groupby('Cliente')['Preço Venda Total (R$)'].sum().sort_values(ascending=False) 
plt.figure(figsize=(6, 3))
clientes[:20].plot(kind='barh')
plt.title('Top 20 Clientes por Valor Total de Compras')
plt.ylabel('Valor Total (R$)')
plt.tight_layout() #ajusta o layout para não cortar os rótulos
plt.show()

#agrupando os produtos mais vendidos:
produtos = df_filtrado.groupby('Descrição')['Quantidade'].sum().sort_values(ascending=False)
plt.figure(figsize=(6, 3))
produtos[:20].plot(kind='barh')
plt.title('Top 20 Produtos Mais Vendidos')
plt.ylabel('Quantidades')
plt.tight_layout()
plt.show()

#print(df.info())