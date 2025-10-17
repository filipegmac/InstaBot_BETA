# 📨 Funcionalidade de DMs em Massa

## Novas Opções Adicionadas

### Opção 23: Enviar DMs em massa para lista de usuários
Envia mensagens diretas para uma lista específica de usuários.

**Como usar:**
1. Digite os usernames separados por vírgula
2. Digite a mensagem a ser enviada
3. Escolha se quer personalizar com `{username}`

**Exemplo:**
```
Lista de usuários: usuario1, usuario2, usuario3
Mensagem: Olá {username}! Como vai?
Personalizar: s
```

---

### Opção 24: Enviar DMs para seguidores de uma conta
Extrai seguidores de uma conta e envia DMs para eles.

**Como usar:**
1. Digite o username da conta alvo
2. Defina o máximo de DMs a enviar
3. Digite a mensagem
4. Escolha personalização

**Exemplo:**
```
Usuário alvo: influencer_exemplo
Máximo de DMs: 20
Mensagem: Oi {username}, vi que você segue @influencer_exemplo!
```

---

### Opção 25: Enviar DMs para seus novos seguidores
Envia DMs de boas-vindas para seus novos seguidores.

**Como usar:**
1. Defina quantos seguidores recentes receberão a mensagem
2. Digite a mensagem de boas-vindas
3. Escolha personalização

**Exemplo:**
```
Máximo de DMs: 10
Mensagem: Obrigado por me seguir, {username}! 🎉
Personalizar: s
```

---

### Opção 26: Enviar DMs a partir de arquivo
Lê uma lista de usernames de um arquivo e envia DMs para todos.

**Como usar:**
1. Crie um arquivo .txt com um username por linha
2. Forneça o caminho do arquivo
3. Digite a mensagem
4. Escolha personalização

**Exemplo de arquivo (`dm_users.txt`):**
```
usuario1
usuario2
usuario3
```

**Uso:**
```
Caminho do arquivo: data/dm_users.txt
Mensagem: Olá {username}!
```

---

## ⚠️ Limites de Segurança

Para evitar banimento do Instagram, os seguintes limites são aplicados:

- **Máximo por dia:** 50 DMs
- **Máximo por hora:** 10 DMs
- **Delay entre DMs:** 30-90 segundos (aleatório)
- **Pausa automática:** Se atingir limite horário, aguarda 1 hora

## 🔒 Proteção Anti-Ban

O sistema de DMs inclui:

1. **Rate Limiting inteligente** - controla velocidade de envio
2. **Delays aleatórios** - simula comportamento humano
3. **Tracking de ações** - monitora uso diário/horário
4. **Pausa automática** - evita overload

## 💡 Dicas de Uso

1. **Comece devagar:** Teste com 5-10 DMs primeiro
2. **Personalize mensagens:** Use `{username}` para tornar mais natural
3. **Evite spam:** Não envie a mesma mensagem para muitas pessoas
4. **Seja relevante:** Envie apenas para público-alvo apropriado
5. **Respeite limites:** Não tente burlar os limites de segurança

## ⚡ Funcionalidades de Personalização

Use `{username}` na mensagem para inserir o nome do destinatário:

**Exemplo:**
- Input: `Olá {username}! Tudo bem?`
- Para @joao: `Olá joao! Tudo bem?`
- Para @maria: `Olá maria! Tudo bem?`

## 📊 Estatísticas

Use a opção 22 para ver quantas DMs você enviou nas últimas 24 horas e na última hora.
