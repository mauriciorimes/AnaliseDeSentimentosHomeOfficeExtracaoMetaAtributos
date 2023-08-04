Continuando o tratamento de dados da Analise de Sentimentos relacionada a aceitação do trabalho Home Office, usando de coleta de dados tweets, para treinar um algoritmo que saiba identificar se novos tweets são positivos ou negativos nessa forma de trabalho.

Nessa abordagem, vão ser extraído os dados.

Além do pandas, usando a biblioteca de emojis, para assim separar em uma lista, quais emojis são positivos e quais emojis são negativos.

Foram definidas algumas funções:
- Verificação de emojis
- Contador de palavras
- Contador de palavras maiúsculas
- Contador de todas palavras maiúsculas
- Contar letras maiúsculas
- Contar pontos de interrogação
- Contar pontos de exclamação
- Media de caracteres por palavra

Cria um novo DataFrame com as colunas desejas, onde:
--> Vai percorrer cada linha do dataset original
    - Verifica os atributos de cada linha
    - Verifica a quantidade de letras repetidas em sequência no tweet
    - Verifica emojis positivos e negativos
    - Define os emojis positivos e negativos

Cria uma nova linha no novo dataset com os valores dos atributos:
- Converte as colunas de atributos para inteiros

Para assim salvar em um novo arquivo CSV.

Testes e demais informações em: https://colab.research.google.com/drive/1nbUIaVrrGOBFLwzXh5mWrUePKsf77Q-X?usp=sharing
