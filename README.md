# churn_analyses

# Análise de Churn 

## Sumário

* [Linguagens e tecnologias usadas](#linguagens-e-tecnologias-usadas)
* [Passo a passo da solução](#passo-a-passo-da-solução)
* [Gráficos](#gráficos)
* [Conclusões](#conclusões)

## Linguagens e tecnologias usadas

* [Jupyter Notebook](https://jupyter.org/)
* [Visual Studio Code](https://code.visualstudio.com/download)
* [Python 3.11](https://www.python.org/)
* [Markdown](https://www.markdownguide.org/)


## Passo a passo da solução

* Passo 1: Importar a base de dados
* Passo 2: Visualizar a base de dados
* Passo 3: Tratar os dados
    * 3.1 Verificar as variáveis de cada coluna
    * 3.2 Excluir colunas desnecessárias
* Passo 4: Analisar os dados
    * 4.1 Analisar Graficamente

## Gráficos 

Com o código, foram gerados 4 gráficos, em formato de histogramas, comparando a coluna de "Churn" com as outras da base de dados. Tais gráficos podem ser encontrados dentro da pasta "Gráficos", mas abaixo estão três exemplos, referentes às colunas de "Casado", "TipoContrato" e "MesesComoCliente", respectivamente. 

Em Azul, temos as pessoas que não continuam com os serviços e, em laranja, as que cancelaram. No eixo $y$ está escrito "count" o que representa a quantidade de pessoas.

![Casado](Gráficos/Casado.png)

![TipoContrato](Gráficos/TipoContrato.png)

![MesesComoCliente](Gráficos/MesesComoCliente.png)

## Conclusões

A partir da análise dos gráficos, podemos gerar algumas hipóteses interessantes, mas algumas delas dependem de ser testadas. Outras são suficientemente claras, supondo que a base de dados é representativa. Com isso, sugerimos novas práticas para a empresa conseguir aumentar a fidelidade dos clientes, direcionar investigações, bem como deixar os serviços mais atrativos. 

Por exemplo, pode-se usar promoções e planos para direcionar o cliente para métodos que tendem a fidelizá-lo, o que acaba sendo bom para o cliente e para a empresa. Os resultados em nossa análise fazem muito sentido com o que é observado nas grandes empresas de assinaturas de serviços, como as de telecomunicações e streaming.

$\phantom{a}$

### <b> Sobre as informações pessoais </b>

Nesse tópico, vemos que ter família é um ponto relevante, pois as pessoas casadas e com dependentes tendem a manter os serviços. Outras informações, como gênero e se a pessoa é aposentada, não deram resultados significativos.

**Sugestão:** Pode-se disponibilizar serviços com planos familiares, oferecendo mais serviços por preços melhores, como uma linha adicional ou o serviço de segurança online, por exemplo. Planos familiares são usados por inúmeras empresas grandes, como Netflix e Spotify. 

$\phantom{a}$

### <b> Sobre o tempo e dinheiro investido pelo cliente </b>

Observando as tabelas relacionadas ao tempo como cliente e o total de dinheiro gasto, é possível perceber que quanto mais tempo e quanto mais dinheiro gasto, menos clientes cancelam os serviços. Nos primeiros meses e nas menores quantidades de dinheiro investidas, a desistência dos serviços é absurdamente mais alta.

**Sugestão:** É possível que a primeira experiência dos clientes com os serviços estejam sendo ruins ou, também, que a captação de clientes esteja trazendo clientes desqualificados, sendo necessário mudar as estratégias de marketing. Para entender melhor os motivos, vale a pena enviar uma pesquisa de satisfação sempre que alguém cancelar os serviços. Uma ideia interessante é criar incentivos para o cliente ficar mais tempo e ser fidelizado, como, por exemplo, dar uma promoção para os primeiros meses ou primeiro ano de uso, o que também é uma estratégia usada por grandes empresas.

$\phantom{a}$

### <b> Sobre os serviços </b>

A partir das tabelas relacionadas aos serviços, como "ServicoTelefone", "MultiplasLinhas", "ServicoSegurancaOnline", entre outros, vemos que quanto mais serviços, menores as chances de acontecer o churn. A única exceção é o "ServicoInternet", que está com uma alta taxa de cancelamento.

**Sugestão:** Oferecer planos com múltiplos serviços, o que também é feito por grandes empresas, e pesquisa de satisfação para os usuários do serviço de internet.

$\phantom{a}$

### <b> Sobre o pagamento </b>

Ao observar as tabelas "TipoContrato", "FormaPagamento" e "FaturaDigital" identificar que os clientes com contrato mensal tem muito mais chance de cancelar, o mesmo acontece com quem pagar usando boleto e quem recebe a fatura digitalmente.

**Sugestão:** Aparentemente os métodos em que os clientes lembram recorrentemente de pagar os serviços ou que dão mais trabalho são os que trazem maiores números de Churn Rate. Dessa forma, é necessário deixar os métodos que dão menos trabalho mais atrativos, com promoções ou outras vantagens. É possível, também, ensinar a fazer o pagamento da fatura automaticamente.


