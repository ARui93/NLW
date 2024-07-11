# Trip Management API

Uma API simples para gerenciamento de viagens, construída com Flask.

## Descrição do Projeto

Este projeto foi desenvolvido como parte do evento NLW Journey da Rocketseat em Python. Durante o evento, construímos uma aplicação para ajudar a organizar viagens, tanto a trabalho quanto lazer. Utilizamos o DBeaver para gerenciar o banco de dados e outras ferramentas para testar e integrar funcionalidades essenciais.

## Endpoints da API

### Criar Viagem
- **Rota**: `/trips`
- **Método**: `POST`
- **Descrição**: Cria uma nova viagem.

### Buscar Viagem
- **Rota**: `/trips/<tripId>`
- **Método**: `GET`
- **Descrição**: Retorna os detalhes de uma viagem específica.

### Confirmar Viagem
- **Rota**: `/trips/<tripId>/confirm`
- **Método**: `GET`
- **Descrição**: Confirma uma viagem.

### Criar Link de Viagem
- **Rota**: `/trips/<tripId>/links`
- **Método**: `POST`
- **Descrição**: Cria um link associado a uma viagem.

### Buscar Link de Viagem
- **Rota**: `/trips/<tripId>/links`
- **Método**: `GET`
- **Descrição**: Retorna o link associado a uma viagem.

### Convidar Participante para Viagem
- **Rota**: `/trips/<tripId>/invites`
- **Método**: `POST`
- **Descrição**: Convida um participante para uma viagem.

### Criar Atividade
- **Rota**: `/trips/<tripId>/activities`
- **Método**: `POST`
- **Descrição**: Cria uma atividade associada a uma viagem.

### Buscar Participantes de uma Viagem
- **Rota**: `/trips/<tripId>/participants`
- **Método**: `GET`
- **Descrição**: Retorna os participantes de uma viagem.

### Buscar Atividades de uma Viagem
- **Rota**: `/trips/<tripId>/activities`
- **Método**: `GET`
- **Descrição**: Retorna as atividades associadas a uma viagem.

### Confirmar Participante
- **Rota**: `/participants/<participantId>/confirm`
- **Método**: `PATCH`
- **Descrição**: Confirma um participante.

## Desenvolvimento

Durante o desenvolvimento deste projeto, passamos por três etapas principais:

1. **Configuração Inicial e Modelagem de Dados**:
   - Utilizamos o DBeaver para gerenciar o banco de dados.
   - Modelamos a estrutura de dados necessária para suportar viagens, links, participantes e atividades.

2. **Construção das Rotas da API**:
   - Implementamos as rotas necessárias para criar, buscar e confirmar viagens, gerenciar links, convidar participantes e criar atividades.

3. **Integração e Testes**:
   - Utilizamos o Postman para testar as APIs desenvolvidas.
   - Configuramos e utilizamos o Ethereal para criar um serviço de e-mail genérico e receber confirmações via e-mail.

Este projeto continua em desenvolvimento e novas funcionalidades podem ser adicionadas no futuro.
