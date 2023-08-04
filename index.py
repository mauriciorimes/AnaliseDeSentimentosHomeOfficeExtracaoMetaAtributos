#pip install emoji

import pandas as pd
import emoji
import re

def verificar_emojis(string):
    emojis_positivos = [emoji for emoji in re.findall(r'\:[a-zA-Z_]+\:', string) if emoji in emoji.emojize(':thumbs_up:')]
    emojis_negativos = [emoji for emoji in re.findall(r'\:[a-zA-Z_]+\:', string) if emoji in emoji.emojize(':thumbs_down:')]
    return len(emojis_positivos) > 0, len(emojis_negativos) > 0


def contar_palavras(string):
    palavras = string.split()
    quantidade_palavras = len(palavras)
    return quantidade_palavras


def contar_palavras_maiusculas(string):
    palavras = string.split()
    quantidade_palavras_maiusculas = 0
    for palavra in palavras:
        if palavra[0].isupper():
            quantidade_palavras_maiusculas += 1
    return quantidade_palavras_maiusculas

def contar_palavras_todas_maiusculas(string):
    palavras = string.split()
    quantidade_palavras_todas_maiusculas = 0
    for palavra in palavras:
        if palavra.isupper():
            quantidade_palavras_todas_maiusculas += 1
    return quantidade_palavras_todas_maiusculas

def contar_letras_maiusculas(string):
    quantidade_maiusculas = 0
    for caractere in string:
        if caractere.isupper():
            quantidade_maiusculas += 1
    return quantidade_maiusculas

def contar_pontos_interrogacao(string):
    quantidade_interrogacao = 0
    for caractere in string:
        if caractere == '?':
            quantidade_interrogacao += 1
    return quantidade_interrogacao

def contar_pontos_exclamacao(string):
    quantidade_exclamacao = 0
    for caractere in string:
        if caractere == '!':
            quantidade_exclamacao += 1
    return quantidade_exclamacao

def media_caracteres_por_palavra(string):
    palavras = string.split()
    quantidade_palavras = len(palavras)
    total_caracteres = sum(len(palavra) for palavra in palavras)
    media = total_caracteres / quantidade_palavras
    return media

dataset = pd.read_csv("home-office.csv")

novo_dataset = pd.DataFrame()

# Criar um novo DataFrame com as colunas desejadas
novo_dataset = pd.DataFrame()

# Percorrer cada linha do dataset original
for index, row in dataset.iterrows():
    # Verificar os atributos em cada linha
    tem_RT = 1 if "RT" in row["tweet"] else 0
    tem_hashtag = 1 if "#" in row["tweet"] else 0
    tem_user = 1 if "@" in row["tweet"] else 0  # Alteração aqui para verificar "@"
    tem_url = 1 if "http" in row["tweet"] else 0

    # Verificar a quantidade de letras repetidas em sequência no tweet
    tweet = row["tweet"]
    letras_repetidas = sum(1 for i in range(1, len(tweet)) if tweet[i] == tweet[i-1])

    tem_letra_repetida = 1 if letras_repetidas > 2 else 0
    tem_ponto_interrogacao = 1 if "?" in row["tweet"] else 0
    tem_ponto_exclamacao = 1 if "!" in row["tweet"] else 0

    # Verificar emojis positivos e negativos
    tem_emoji_positivo = 0
    tem_emoji_negativo = 0

    # Lista de emojis positivos e negativos
    emojis_positivos = ["😃", "😄", "😊", "🙂", "😁", "😆", "😍", "🤩", "😎", "🥳", "😎", "🤓", "😺", "😸", "❤️"]
    emojis_negativos = ["😞", "😔", "😢", "😭", "😣", "😩", "😡", "🤬", "😠", "😓", "🤧", "🤢", "☠", "💀", "👿"]

    # Verificar a presença de emojis positivos e negativos no tweet
    quantidade_emoji_positivo = 0
    for emoji in emojis_positivos:
        quantidade_emoji_positivo += tweet.count(emoji)
        if quantidade_emoji_positivo > 0:
            tem_emoji_positivo = 1
            break

    quantidade_emoji_negativo = 0
    for emoji in emojis_negativos:
        quantidade_emoji_negativo += tweet.count(emoji)
        if quantidade_emoji_negativo > 0:
            tem_emoji_negativo = 1
            break


    # Criar uma nova linha no novo dataset com os valores dos atributos
    novo_dataset.loc[index, "temRT"] = int(tem_RT)
    novo_dataset.loc[index, "temHashtag"] = int(tem_hashtag)
    novo_dataset.loc[index, "temUser"] = int(tem_user)
    novo_dataset.loc[index, "temURL"] = int(tem_url)
    novo_dataset.loc[index, "temLetraRepetid"] = int(tem_letra_repetida)
    novo_dataset.loc[index, "numeroLetrasRepetidas"] = int(letras_repetidas) if letras_repetidas > 2 else 0
    novo_dataset.loc[index, "temPontoInterrogacao"] = int(tem_ponto_interrogacao)
    novo_dataset.loc[index, "temPontoExclamaco"] = int(tem_ponto_exclamacao)
    novo_dataset.loc[index, "EmojisPositivo"] = int(1 if quantidade_emoji_positivo > 0 else 0)
    novo_dataset.loc[index, "EmojisNegativo"] = int(1 if quantidade_emoji_negativo > 0 else 0)

    novo_dataset.loc[index, "quantidadePalavras"] = int(contar_palavras(tweet))
    novo_dataset.loc[index, "quantidadePalavrasQueIniciamMaiusculas"] = int(contar_palavras_maiusculas(tweet))
    novo_dataset.loc[index, "quantidadePalavrastodasAsLetrasMaiusculas"] = int(contar_palavras_todas_maiusculas(tweet))
    novo_dataset.loc[index, "quantidadeLetrasMaiusculas"] = int(contar_letras_maiusculas(tweet))
    novo_dataset.loc[index, "quantidadePontosInterogacao"] = int(contar_pontos_interrogacao(tweet))
    novo_dataset.loc[index, "quantidadePontosExclamacao"] = int(contar_pontos_exclamacao(tweet))

    novo_dataset.loc[index, "quantidadeEmojisPositivos"] = int(quantidade_emoji_positivo)#alterar
    novo_dataset.loc[index, "quantidadeEmojisNegativos"] = int(quantidade_emoji_negativo)#alterar

    novo_dataset.loc[index, "mediaCharacteresPorPalavra"] = int(media_caracteres_por_palavra(tweet))


    novo_dataset.loc[index, "tweet"] = row["tweet"]
    novo_dataset.loc[index, "classe"] = row["classe"]

# Converter as colunas de atributos para inteiros
novo_dataset = novo_dataset.astype({"temRT": int, "temHashtag": int, "temUser": int,
                                    "temURL": int,
                                    "temLetraRepetid": int, "numeroLetrasRepetidas": int,
                                    "temPontoInterrogacao": int, "temPontoExclamaco": int})

# Salvar o novo dataset em um arquivo CSV
novo_dataset.to_csv("novo_dataset_completo.csv", index=False)




