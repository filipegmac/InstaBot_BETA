# 🤖 Bot do Instagram - Automação Segura

Bot completo do Instagram com todas as funcionalidades de automação implementadas de forma segura para evitar banimentos.

## 📋 Menu Organizado

O bot possui um **menu hierárquico organizado em 5 categorias**:

- **1.x - Extração de Dados** (9 opções)
- **2.x - Ações de Engajamento** (7 opções)
- **3.x - Mensagens Diretas** (4 opções)
- **4.x - Stories** (4 opções)
- **5.x - Sistema** (2 opções)

📖 Veja [MENU_STRUCTURE.md](MENU_STRUCTURE.md) para detalhes completos da estrutura.

## 🌟 Funcionalidades

### 👥 Gerenciamento de Seguidores
- ✅ Extrair seguidores de uma conta
- ✅ Extrair contas seguidas por um usuário
- ✅ Seguir automaticamente usuários de uma lista
- ✅ Deixar de seguir automaticamente usuários de uma lista
- ✅ Seguir automaticamente os seguidores de uma conta específica

### 💬 Interações
- ✅ Curtir automaticamente posts de uma lista
- ✅ Comentar automaticamente em posts
- ✅ Interagir com hashtags (curtir e comentar)
- ✅ Engajamento automático diário com hashtags do seu nicho
- ✅ Extrair usuários que curtiram um post
- ✅ Extrair comentários de um post com informações dos usuários

### 📨 Mensagens Diretas
- ✅ Enviar DMs em massa para lista de usuários
- ✅ Enviar DMs para seguidores de uma conta
- ✅ Enviar DMs para seus novos seguidores
- ✅ Enviar DMs a partir de arquivo
- ✅ Personalização de mensagens com {username}
- ✅ Limites de segurança: 50 DMs/dia, 10 DMs/hora
- 📖 Veja [DMS_README.md](DMS_README.md) para guia completo

### 📊 Extração de Dados
- ✅ Extrair posts de usuários
- ✅ Extrair posts de hashtags (recentes ou top)
- ✅ Extrair posts de localizações
- ✅ Extrair informações completas de perfis
- ✅ Extrair posts marcados de uma conta
- ✅ Extrair todos os dados disponíveis de posts
- ✅ Buscar perfis por nome completo ou empresa

### 📖 Stories
- ✅ Extrair stories atuais de usuários
- ✅ Assistir automaticamente stories de uma lista
- ✅ Assistir stories do feed automaticamente
- ✅ Extrair visualizadores das suas stories
- ✅ Extrair notificações do Instagram

## 🛡️ Proteção Anti-Ban

O bot implementa várias técnicas para evitar detecção e banimento:

### ⏱️ Rate Limiting
- Delays aleatórios entre ações (3-8 segundos por padrão)
- Limites diários configuráveis para cada tipo de ação
- Limite de ações por hora
- Tracking de ações realizadas

### 🔒 Limites Padrão Seguros
- **Follow**: 150 por dia
- **Unfollow**: 150 por dia
- **Curtidas**: 200 por dia
- **Comentários**: 50 por dia
- **Visualizações de stories**: 300 por dia
- **Ações por hora**: 30

### 🎭 Comportamento Humano
- Delays aleatórios entre ações
- Comentários variados e naturais
- Simulação de dispositivo real
- Suporte a proxy
- Sessões persistentes

## 📦 Instalação

### Requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone ou baixe o projeto**
```bash
cd Instabot
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure as credenciais**

Copie o arquivo `.env.example` para `.env`:
```bash
copy .env.example .env
```

Edite o arquivo `.env` e adicione suas credenciais:
```env
INSTAGRAM_USERNAME=seu_usuario
INSTAGRAM_PASSWORD=sua_senha
```

## 🚀 Uso

### Executar o Bot

```bash
python main.py
```

### Menu Interativo

O bot possui um menu interativo com todas as funcionalidades:

```
═══════════════ MENU PRINCIPAL ═══════════════
1.  Extrair seguidores de uma conta
2.  Extrair contas seguidas por um usuário
3.  Seguir usuários de uma lista
4.  Deixar de seguir usuários de uma lista
5.  Seguir seguidores de uma conta
6.  Curtir posts de uma lista
7.  Comentar em posts
8.  Interagir com hashtag (curtir e comentar)
9.  Engajamento automático diário com hashtags
10. Extrair posts de um usuário
11. Extrair posts de uma hashtag
12. Extrair informações de perfil
13. Extrair usuários que curtiram um post
14. Extrair comentários de um post
15. Extrair posts marcados de uma conta
16. Buscar perfis por nome
17. Extrair stories de usuários
18. Assistir stories automaticamente
19. Assistir stories do feed
20. Extrair visualizadores das suas stories
21. Extrair notificações
22. Ver estatísticas de uso
0.  Sair
```

## ⚙️ Configuração Avançada

### Ajustar Limites

Edite o arquivo `.env` para personalizar os limites:

```env
# Delays entre ações (segundos)
MIN_DELAY=3
MAX_DELAY=8

# Limites diários
DAILY_FOLLOW_LIMIT=150
DAILY_UNFOLLOW_LIMIT=150
DAILY_LIKE_LIMIT=200
DAILY_COMMENT_LIMIT=50
DAILY_STORY_VIEW_LIMIT=300

# Ações por hora
ACTIONS_PER_HOUR=30
```

### Usar Proxy (Opcional)

Para maior segurança, você pode usar um proxy:

```env
USE_PROXY=true
PROXY_URL=http://usuario:senha@ip:porta
```

### Comentários Personalizados

Os comentários padrão estão em `src/config.py`. Você pode personalizá-los editando a lista `COMMENT_TEMPLATES`.

## 📁 Estrutura do Projeto

```
Instabot/
├── main.py                 # Arquivo principal com menu
├── requirements.txt        # Dependências
├── .env.example           # Exemplo de configuração
├── .env                   # Suas credenciais (não commitar!)
├── src/
│   ├── auth.py           # Autenticação e login
│   ├── config.py         # Configurações
│   ├── rate_limiter.py   # Controle de taxa
│   ├── followers.py      # Gerenciamento de seguidores
│   ├── interactions.py   # Curtidas e comentários
│   ├── data_extractor.py # Extração de dados
│   └── stories.py        # Gerenciamento de stories
├── data/                  # Dados extraídos (JSON)
├── logs/                  # Logs de execução
└── sessions/             # Sessões salvas
```

## 📊 Dados Extraídos

Todos os dados extraídos são salvos em formato JSON na pasta `data/`:

- `{username}_followers.json` - Lista de seguidores
- `{username}_following.json` - Lista de seguidos
- `{username}_posts.json` - Posts de um usuário
- `hashtag_{hashtag}_posts.json` - Posts de uma hashtag
- `{username}_profile.json` - Informações de perfil
- `post_{id}_likers.json` - Usuários que curtiram
- `post_{id}_comments.json` - Comentários de um post
- `{username}_stories.json` - Stories de um usuário
- E muitos outros...

## 🔐 Segurança

### Autenticação
- ✅ Suporte a 2FA (autenticação de dois fatores)
- ✅ Tratamento de challenges
- ✅ Sessões persistentes (não precisa fazer login sempre)
- ✅ Detecção de "Please wait a few minutes"

### Proteção de Conta
- ✅ Rate limiting automático
- ✅ Delays aleatórios
- ✅ Limites diários respeitados
- ✅ Logging completo de ações
- ✅ Estatísticas de uso em tempo real

## ⚠️ Avisos Importantes

1. **Use com responsabilidade**: O uso excessivo pode resultar em banimento temporário ou permanente
2. **Comece devagar**: Teste com limites baixos antes de aumentar
3. **Não compartilhe suas credenciais**: Nunca commite o arquivo `.env`
4. **Respeite os ToS do Instagram**: Este bot é para fins educacionais
5. **Monitore sua conta**: Verifique regularmente se não há restrições

## 🐛 Troubleshooting

### Erro de Login
- Verifique suas credenciais no `.env`
- Se usar 2FA, tenha o código em mãos
- Tente fazer login pelo app oficial primeiro

### Challenge Required
- Faça login pelo app oficial
- Complete a verificação solicitada
- Tente novamente após algumas horas

### Limite Atingido
- Verifique as estatísticas (opção 22 do menu)
- Aguarde até o dia seguinte
- Reduza os limites no `.env`

### Import Errors
- Certifique-se de instalar todas as dependências:
```bash
pip install -r requirements.txt
```

## 📝 Logs

Os logs são salvos automaticamente em `logs/bot.log` e também exibidos no console.

## 🔄 Atualizações

Para atualizar o bot:
```bash
git pull
pip install -r requirements.txt --upgrade
```

## 📄 Licença

Este projeto é para fins educacionais. Use por sua conta e risco.

## 🤝 Suporte

Para dúvidas e suporte:
- Verifique os logs em `logs/bot.log`
- Consulte a documentação do [instagrapi](https://github.com/adw0rd/instagrapi)
- Reduza os limites se estiver tendo problemas

## 🎯 Melhores Práticas

1. **Comece devagar**: Use limites baixos nos primeiros dias
2. **Seja consistente**: Execute ações regularmente, não em rajadas
3. **Varie as ações**: Misture follows, likes e comentários
4. **Use horários variados**: Não execute sempre no mesmo horário
5. **Monitore os resultados**: Acompanhe as estatísticas e ajuste conforme necessário

---

**⚡ Desenvolvido com foco em segurança e eficiência!**
