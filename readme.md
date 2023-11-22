# Ponderada 4

## Introdução

Está é a quarta ponderada do curso de engenharia da computação do Inteli ela é sobre desenvolvimento de um chatbot utilizando LLM. Nela foi desenvolvido um chatbot que responde perguntas sobre o videogame League of Legends.

## Setup

Sera necessário instalar o ollama para rodar o projeto, para isso basta executar o comando abaixo:

```bash
curl https://ollama.ai/install.sh | sh
```

Além disso é necessário instalar as dependências do projeto, para isso basta executar o comando abaixo:

```bash
pip install gradio 
```

É necessário também gerar o modelo do chatbot, para isso basta executar o comando abaixo:

```bash
ollama create lolzero -f Modelfile
```

## Execução

Para executar o projeto basta executar o comando abaixo:

```bash
python3 cli.py
```

## Vídeo

[![Vídeo](https://youtu.be/OAqZxcjnYzg)](https://youtu.be/OAqZxcjnYzg)

<!-- ollama create lolzero -f Modelfile
ollama run lolzero
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "dexter",
  "prompt":"Why is the sky blue?",
  "stream":false
}'

pip install gradio
curl https://ollama.ai/install.sh | sh
ollama run dolphin2.2-mistral -->