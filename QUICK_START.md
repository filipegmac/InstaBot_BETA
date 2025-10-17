# 🚀 Guia Rápido - Começando com o Bot

## 📥 Instalação

1. **Clone o repositório**
```bash
git clone <repo_url>
cd Instabot
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure suas credenciais**
Edite o arquivo `.env`:
```env
INSTAGRAM_USERNAME=seu_usuario
INSTAGRAM_PASSWORD=sua_senha
```

4. **Execute o bot**
```bash
python main.py
```

---

## 🎯 Casos de Uso Comuns

### 1️⃣ Extrair Seguidores de um Influencer

**Objetivo:** Coletar seguidores de um perfil para análise

```
Escolha: 1.1
Nome de usuário: influencer_exemplo
Máximo de seguidores: 200

✅ Arquivo salvo em: data/influencer_exemplo_followers.json
```

---

### 2️⃣ Seguir Seguidores de um Concorrente

**Objetivo:** Crescer sua base seguindo o público do concorrente

```
Escolha: 2.3
Usuário alvo: concorrente_exemplo
Máximo de seguidores: 50

⚙️ O bot irá:
1. Extrair seguidores do concorrente
2. Filtrar quem você já segue
3. Seguir até 50 pessoas automaticamente
```

**Proteções automáticas:**
- ✅ Não segue quem você já segue
- ✅ Delay aleatório entre 3-8s
- ✅ Limite de 150 follows/dia

---

### 3️⃣ Engajamento com Hashtag

**Objetivo:** Ganhar visibilidade curtindo/comentando em hashtags do seu nicho

```
Escolha: 2.6
Hashtag: marketingdigital
Máximo de posts: 20
Curtir? s
Comentar? s

🎯 O bot irá:
- Curtir 20 posts da hashtag
- Comentar automaticamente
- Usar delay aleatório
```

---

### 4️⃣ Enviar DM de Boas-Vindas para Novos Seguidores

**Objetivo:** Engajar automaticamente quem te seguiu

```
Escolha: 3.3
Máximo de DMs: 10
Mensagem: Obrigado por me seguir, {username}! 🎉
Personalizar: s

📨 Enviará:
- Para @joao: "Obrigado por me seguir, joao! 🎉"
- Para @maria: "Obrigado por me seguir, maria! 🎉"
```

**Limites de segurança:**
- ✅ Máximo 50 DMs/dia
- ✅ Máximo 10 DMs/hora
- ✅ Delay de 30-90s entre mensagens

---

### 5️⃣ Campanha de DM para Seguidores de Influencer

**Objetivo:** Alcançar público qualificado com mensagem personalizada

```
Escolha: 3.2
Usuário alvo: influencer_exemplo
Máximo de DMs: 20
Mensagem: Oi {username}! Vi que você segue @influencer_exemplo e achei que iria gostar do meu conteúdo 😊
Personalizar: s

💌 Estratégia:
1. Extrai seguidores do influencer
2. Personaliza a mensagem
3. Envia de forma natural com delays
```

---

### 6️⃣ Assistir Stories Automaticamente

**Objetivo:** Aumentar engajamento assistindo stories de seguidores

```
Escolha: 4.2
Usuários: usuario1, usuario2, usuario3

👀 O bot:
- Assiste todos os stories disponíveis
- Registra como visualização
- Aumenta sua presença
```

---

### 7️⃣ Extrair Posts de um Usuário

**Objetivo:** Analisar conteúdo de um perfil

```
Escolha: 1.3
Nome de usuário: exemplo_perfil
Máximo de posts: 50

📄 Dados extraídos:
- Media ID
- Caption
- Likes e comentários
- Data de publicação
- URL do post

✅ Salvo em: data/exemplo_perfil_posts.json
```

---

### 8️⃣ Buscar Perfis por Nome

**Objetivo:** Encontrar perfis de empresas/pessoas

```
Escolha: 1.9
Nomes: Nike, Adidas, Puma

🔍 Retorna:
- Username
- Nome completo
- Número de seguidores
- Se é verificado
- Se é privado
```

---

### 9️⃣ Monitorar suas Estatísticas

**Objetivo:** Ver quantas ações você realizou

```
Escolha: 5.2

📊 ESTATÍSTICAS DE USO
FOLLOWS:
  Últimas 24h: 45
  Última hora: 8
  
LIKES:
  Últimas 24h: 120
  Última hora: 15
  
DMS:
  Últimas 24h: 15
  Última hora: 3
```

---

## 🛡️ Dicas de Segurança

### ✅ Boas Práticas

1. **Comece devagar**
   - Teste com 5-10 ações primeiro
   - Aumente gradualmente

2. **Respeite os limites**
   - Não ultrapasse os limites diários
   - Aguarde o reset de 24h

3. **Varie as ações**
   - Não faça apenas follows
   - Misture likes, comentários, etc.

4. **Use delays realistas**
   - Mantenha os delays padrão (3-8s)
   - Não tente acelerar

5. **Monitore estatísticas**
   - Use opção 5.2 frequentemente
   - Fique atento aos limites

### ⚠️ Evite

- ❌ Executar múltiplas instâncias
- ❌ Usar em contas recém-criadas
- ❌ Ações massivas em curto período
- ❌ Mudar de IP constantemente
- ❌ Comentários genéricos/spam

---

## 📈 Estratégias de Crescimento

### Estratégia 1: Crescimento Orgânico
```
Dia 1-3:
- Extrair seguidores de 3 influencers (1.1)
- Seguir 30 pessoas/dia (2.3)
- Curtir 50 posts de hashtags (2.6)

Dia 4-7:
- Aumentar para 50 follows/dia
- Engajamento automático (2.7)
- DMs para novos seguidores (3.3)

Dia 8+:
- Manter ritmo consistente
- Deixar de seguir quem não seguiu de volta (2.2)
```

### Estratégia 2: Campanha de DM
```
1. Extrair seguidores do nicho (1.1)
2. Salvar lista em arquivo
3. Enviar DMs personalizadas (3.4)
4. Acompanhar resultados
```

### Estratégia 3: Engajamento com Hashtags
```
1. Identificar 10 hashtags do nicho
2. Engajamento diário automático (2.7)
3. Curtir e comentar consistentemente
4. Monitorar crescimento
```

---

## 🎨 Personalizações Avançadas

### Usar {username} em Mensagens
```
"Olá {username}! 👋"
"Ei {username}, tudo bem?"
"Obrigado {username}! 🙏"
```

### Comentários Personalizados
```
Opção 2.5:
- "Que foto incrível! 😍"
- "Amei o conteúdo! 🔥"
- "Inspirador demais! 💪"
```

---

## 🐛 Resolução de Problemas

### Erro: "Sessão expirada"
```
✅ Solução: O bot fará relogin automaticamente
⏳ Aguarde 5 segundos
```

### Erro: "Limite atingido"
```
✅ Solução: Aguarde o reset (24h ou 1h)
📊 Verifique estatísticas (5.2)
```

### Erro: "Credenciais inválidas"
```
✅ Solução: Verifique o arquivo .env
🔑 Confirme username e senha
```

### Erro: "Challenge necessário"
```
✅ Solução: 
1. Faça login no app oficial
2. Complete o challenge
3. Tente novamente
```

---

## 📚 Recursos Adicionais

- 📖 [MENU_STRUCTURE.md](MENU_STRUCTURE.md) - Estrutura completa do menu
- 📨 [DMS_README.md](DMS_README.md) - Guia de mensagens diretas
- ⚙️ [README.md](README.md) - Documentação completa

---

**Lembre-se: Use com responsabilidade e respeite os termos de serviço do Instagram! 🙏**
