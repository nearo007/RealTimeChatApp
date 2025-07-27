# **Nearochat.my**

**Nearochat.my** é uma aplicação web de **chat em tempo real com múltiplas salas**, desenvolvida com Django, HTML, JavaScript e AJAX. Os usuários podem criar salas, enviar mensagens instantaneamente e visualizar salas ativas sem precisar atualizar a página.

---

## **Funcionalidades**

- **Criação e entrada em salas de chat**
- **Lista dinâmica de salas disponíveis**
- **Salvamento do nome de usuário no navegador com `localStorage`**
- **Envio e recebimento de mensagens em tempo real via AJAX**
- **Interface amigável e responsiva**
- **Exclusão de salas inativas automaticamente**
- **Botão para sair da sala e voltar à página principal**

---

## **Tecnologias Utilizadas**

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, JavaScript (jQuery)
- **Banco de dados:** SQLite (padrão do Django)
- **Templates:** Django Template Language (DTL)
- **AJAX:** para comunicação assíncrona sem recarregar a página

---

## **Estrutura do Projeto**

### **Views principais (`views.py`):**

- `index`: Renderiza a página inicial com as salas disponíveis.
- `checkview`: Cria uma sala ou redireciona para uma já existente.
- `room`: Renderiza a página da sala.
- `send`: Salva mensagens enviadas no banco de dados.
- `get_messages`: Retorna mensagens da sala em formato JSON.
- `get_available_rooms`: Retorna todas as salas ativas em formato JSON.
- `delete_room`: Exclui uma sala específica.
- `clear_empty_rooms`: Remove automaticamente salas inativas por mais de 30 minutos.

### **Templates:**

- **`index.html`**: Tela inicial onde o usuário insere o nome e o nome da sala.
- **`room.html`**: Interface da sala com mensagens em tempo real e opção de voltar/excluir sala.

---

## **Detalhes adicionais**

- O nome de usuário é armazenado com `localStorage`, permitindo persistência entre sessões.
- A lista de salas é atualizada automaticamente a cada 3 segundos.
- As mensagens são atualizadas a cada 2 segundos com AJAX.
- As salas inativas por mais de 30 minutos são automaticamente removidas da base de dados.
