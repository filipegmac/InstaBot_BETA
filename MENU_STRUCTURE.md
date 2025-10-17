# 📋 Nova Estrutura do Menu - Hierárquica e Organizada

## 🎨 Estrutura Visual

O menu agora está organizado em **5 categorias principais** com numeração hierárquica:

```
╔═══════════════════════════════════════════════════════════╗
║              MENU PRINCIPAL - CATEGORIAS                  ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 📊 1. EXTRAÇÃO DE DADOS

Ferramentas para coletar informações do Instagram.

| Código | Funcionalidade |
|--------|----------------|
| **1.1** | Extrair seguidores de uma conta |
| **1.2** | Extrair contas seguidas por um usuário |
| **1.3** | Extrair posts de um usuário |
| **1.4** | Extrair posts de uma hashtag |
| **1.5** | Extrair informações de perfil |
| **1.6** | Extrair usuários que curtiram um post |
| **1.7** | Extrair comentários de um post |
| **1.8** | Extrair posts marcados de uma conta |
| **1.9** | Buscar perfis por nome |

---

## 🎯 2. AÇÕES DE ENGAJAMENTO

Automação de interações (follows, likes, comentários).

| Código | Funcionalidade |
|--------|----------------|
| **2.1** | Seguir usuários de uma lista |
| **2.2** | Deixar de seguir usuários de uma lista |
| **2.3** | Seguir seguidores de uma conta |
| **2.4** | Curtir posts de uma lista |
| **2.5** | Comentar em posts |
| **2.6** | Interagir com hashtag (curtir e comentar) |
| **2.7** | Engajamento automático diário com hashtags |

---

## 📨 3. MENSAGENS DIRETAS

Envio de DMs em massa com proteção anti-ban.

| Código | Funcionalidade |
|--------|----------------|
| **3.1** | Enviar DMs para lista de usuários |
| **3.2** | Enviar DMs para seguidores de uma conta |
| **3.3** | Enviar DMs para seus novos seguidores |
| **3.4** | Enviar DMs a partir de arquivo |

**Limites de Segurança:**
- Máximo 50 DMs/dia
- Máximo 10 DMs/hora
- Delay de 30-90s entre envios

---

## 📸 4. STORIES

Gerenciamento e automação de stories.

| Código | Funcionalidade |
|--------|----------------|
| **4.1** | Extrair stories de usuários |
| **4.2** | Assistir stories automaticamente |
| **4.3** | Assistir stories do feed |
| **4.4** | Extrair visualizadores das suas stories |

---

## ⚙️ 5. SISTEMA

Configurações e estatísticas do bot.

| Código | Funcionalidade |
|--------|----------------|
| **5.1** | Extrair notificações |
| **5.2** | Ver estatísticas de uso |

**Estatísticas incluem:**
- Follows, Unfollows
- Likes, Comments
- Story Views
- DMs enviadas
- Contagem por 24h e por hora

---

## 🚀 Como Usar

### Exemplo 1: Extrair seguidores
```
Escolha uma opção: 1.1
Nome de usuário: exemplo_usuario
Máximo de seguidores: 200
```

### Exemplo 2: Seguir seguidores de uma conta
```
Escolha uma opção: 2.3
Usuário alvo: influencer
Máximo de seguidores para seguir: 50
```

### Exemplo 3: Enviar DMs personalizadas
```
Escolha uma opção: 3.1
Lista de usuários: joao, maria, pedro
Mensagem: Olá {username}! Tudo bem?
Personalizar: s
```

### Exemplo 4: Ver estatísticas
```
Escolha uma opção: 5.2
═══ ESTATÍSTICAS DE USO ═══
FOLLOWS:
  Últimas 24h: 45
  Última hora: 8
DMS:
  Últimas 24h: 15
  Última hora: 3
```

---

## 🎯 Vantagens da Nova Estrutura

### ✅ **Organização Lógica**
- Funções agrupadas por categoria
- Fácil localização de recursos
- Menu mais limpo e profissional

### ✅ **Numeração Hierárquica**
- **1.x** = Extração
- **2.x** = Engajamento
- **3.x** = DMs
- **4.x** = Stories
- **5.x** = Sistema

### ✅ **Escalabilidade**
- Fácil adicionar novas opções (ex: 1.10, 2.8)
- Mantém organização mesmo com crescimento
- Subcategorias claras

### ✅ **Visual Aprimorado**
- Cores diferentes para cada categoria
- Símbolos e ícones informativos
- Interface mais intuitiva

---

## 🔄 Migração da Numeração Antiga

| Antiga | Nova | Funcionalidade |
|--------|------|----------------|
| 1 | 1.1 | Extrair seguidores |
| 2 | 1.2 | Extrair seguidos |
| 3 | 2.1 | Seguir usuários |
| 4 | 2.2 | Deixar de seguir |
| 5 | 2.3 | Seguir seguidores de conta |
| 6 | 2.4 | Curtir posts |
| 7 | 2.5 | Comentar posts |
| 8 | 2.6 | Interagir com hashtag |
| 9 | 2.7 | Engajamento diário |
| 10 | 1.3 | Extrair posts usuário |
| 11 | 1.4 | Extrair posts hashtag |
| 12 | 1.5 | Extrair info perfil |
| 13 | 1.6 | Extrair likers |
| 14 | 1.7 | Extrair comentários |
| 15 | 1.8 | Extrair posts marcados |
| 16 | 1.9 | Buscar perfis |
| 17 | 4.1 | Extrair stories |
| 18 | 4.2 | Assistir stories |
| 19 | 4.3 | Assistir stories feed |
| 20 | 4.4 | Visualizadores stories |
| 21 | 5.1 | Extrair notificações |
| 22 | 5.2 | Estatísticas |
| 23 | 3.1 | DMs lista usuários |
| 24 | 3.2 | DMs seguidores conta |
| 25 | 3.3 | DMs novos seguidores |
| 26 | 3.4 | DMs de arquivo |

---

## 💡 Dicas de Uso

1. **Comece pela categoria certa:** Se quer extrair dados, vá para 1.x
2. **Use as estatísticas:** Opção 5.2 para monitorar seu uso
3. **Explore cada categoria:** Cada bloco tem funções relacionadas
4. **Atalhos:** Digite diretamente o código (ex: 2.3) sem navegar

---

## 🛡️ Proteções Incluídas

Todas as opções incluem:
- ✅ Rate limiting inteligente
- ✅ Delays aleatórios
- ✅ Logs detalhados
- ✅ Tratamento de erros
- ✅ Proteção anti-ban

---

**Desenvolvido com foco em organização, usabilidade e segurança! 🚀**
