# Trip Management API

Uma API simples para gerenciamento de viagens, construída com Flask.

## Endpoints

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

