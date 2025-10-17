"""
Bot do Instagram - Sistema completo de automação segura
Autor: Instagram Bot
Versão: 1.0.0
"""
import sys
import io
import logging
from pathlib import Path
from colorama import init, Fore, Style

# Configurar saída UTF-8 para Windows (suporte a emojis)
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Adicionar diretório src ao path
sys.path.insert(0, str(Path(__file__).parent))

from src.config import Config
from src.auth import InstagramAuth
from src.followers import FollowersManager
from src.interactions import InteractionsManager
from src.data_extractor import DataExtractor
from src.stories import StoriesManager
from src.direct_messages import DirectMessagesManager

# Inicializar colorama para cores no terminal
init(autoreset=True)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOGS_DIR / 'bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def print_banner():
    """Exibe banner do bot"""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          {Fore.YELLOW}🤖 BOT DO INSTAGRAM - AUTOMAÇÃO SEGURA 🤖{Fore.CYAN}           ║
║                                                              ║
║  {Fore.GREEN}✓ Extração de seguidores e seguidos{Fore.CYAN}                        ║
║  {Fore.GREEN}✓ Follow/Unfollow automático{Fore.CYAN}                               ║
║  {Fore.GREEN}✓ Curtidas e comentários automáticos{Fore.CYAN}                       ║
║  {Fore.GREEN}✓ Extração de dados de posts e perfis{Fore.CYAN}                      ║
║  {Fore.GREEN}✓ Gerenciamento de stories{Fore.CYAN}                                 ║
║  {Fore.GREEN}✓ Envio de DMs em massa{Fore.CYAN}                                    ║
║  {Fore.GREEN}✓ Proteção anti-ban com rate limiting{Fore.CYAN}                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """
    print(banner)


def print_menu():
    """Exibe menu principal"""
    print(f"\n{Fore.YELLOW}╔═══════════════════════════════════════════════════════════╗")
    print(f"║              {Fore.WHITE}MENU PRINCIPAL - CATEGORIAS{Fore.YELLOW}                  ║")
    print(f"╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    print(f"\n{Fore.MAGENTA}┌─ 1. EXTRAÇÃO DE DADOS{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  1.1{Style.RESET_ALL} - Extrair seguidores de uma conta")
    print(f"{Fore.CYAN}  1.2{Style.RESET_ALL} - Extrair contas seguidas por um usuário")
    print(f"{Fore.CYAN}  1.3{Style.RESET_ALL} - Extrair posts de um usuário")
    print(f"{Fore.CYAN}  1.4{Style.RESET_ALL} - Extrair posts de uma hashtag")
    print(f"{Fore.CYAN}  1.5{Style.RESET_ALL} - Extrair informações de perfil")
    print(f"{Fore.CYAN}  1.6{Style.RESET_ALL} - Extrair usuários que curtiram um post")
    print(f"{Fore.CYAN}  1.7{Style.RESET_ALL} - Extrair comentários de um post")
    print(f"{Fore.CYAN}  1.8{Style.RESET_ALL} - Extrair posts marcados de uma conta")
    print(f"{Fore.CYAN}  1.9{Style.RESET_ALL} - Buscar perfis por nome")
    
    print(f"\n{Fore.MAGENTA}┌─ 2. AÇÕES DE ENGAJAMENTO{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  2.1{Style.RESET_ALL} - Seguir usuários de uma lista")
    print(f"{Fore.CYAN}  2.2{Style.RESET_ALL} - Deixar de seguir usuários de uma lista")
    print(f"{Fore.CYAN}  2.3{Style.RESET_ALL} - Seguir seguidores de uma conta")
    print(f"{Fore.CYAN}  2.4{Style.RESET_ALL} - Curtir posts de uma lista")
    print(f"{Fore.CYAN}  2.5{Style.RESET_ALL} - Comentar em posts")
    print(f"{Fore.CYAN}  2.6{Style.RESET_ALL} - Interagir com hashtag (curtir e comentar)")
    print(f"{Fore.CYAN}  2.7{Style.RESET_ALL} - Engajamento automático diário com hashtags")
    
    print(f"\n{Fore.MAGENTA}┌─ 3. MENSAGENS DIRETAS{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  3.1{Style.RESET_ALL} - Enviar DMs para lista de usuários")
    print(f"{Fore.CYAN}  3.2{Style.RESET_ALL} - Enviar DMs para seguidores de uma conta")
    print(f"{Fore.CYAN}  3.3{Style.RESET_ALL} - Enviar DMs para seus novos seguidores")
    print(f"{Fore.CYAN}  3.4{Style.RESET_ALL} - Enviar DMs a partir de arquivo")
    
    print(f"\n{Fore.MAGENTA}┌─ 4. STORIES{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  4.1{Style.RESET_ALL} - Extrair stories de usuários")
    print(f"{Fore.CYAN}  4.2{Style.RESET_ALL} - Assistir stories automaticamente")
    print(f"{Fore.CYAN}  4.3{Style.RESET_ALL} - Assistir stories do feed")
    print(f"{Fore.CYAN}  4.4{Style.RESET_ALL} - Extrair visualizadores das suas stories")
    
    print(f"\n{Fore.MAGENTA}┌─ 5. SISTEMA{Style.RESET_ALL}")
    print(f"{Fore.CYAN}  5.1{Style.RESET_ALL} - Extrair notificações")
    print(f"{Fore.CYAN}  5.2{Style.RESET_ALL} - Ver estatísticas de uso")
    
    print(f"\n{Fore.RED}  0{Style.RESET_ALL}   - Sair")
    print(f"{Fore.YELLOW}{'─' * 63}{Style.RESET_ALL}")


def main():
    """Função principal"""
    print_banner()
    
    # Validar configurações
    try:
        Config.validate()
    except ValueError as e:
        logger.error(f"❌ Erro de configuração: {e}")
        logger.info("Por favor, configure suas credenciais no arquivo .env")
        return
    
    # Fazer login
    logger.info("Iniciando autenticação...")
    auth = InstagramAuth()
    
    if not auth.login():
        logger.error("❌ Falha na autenticação. Verifique suas credenciais.")
        return
    
    client = auth.get_client()
    rate_limiter = auth.rate_limiter
    
    # Inicializar gerenciadores
    followers_mgr = FollowersManager(client, rate_limiter, auth)
    interactions_mgr = InteractionsManager(client, rate_limiter)
    data_extractor = DataExtractor(client)
    stories_mgr = StoriesManager(client, rate_limiter)
    dm_mgr = DirectMessagesManager(client, rate_limiter)
    
    logger.info(f"✅ Autenticado como @{Config.USERNAME}")
    
    # Loop principal
    while True:
        try:
            print_menu()
            choice = input(f"\n{Fore.GREEN}Escolha uma opção: {Style.RESET_ALL}").strip()
            
            if choice == "0":
                logger.info("Saindo...")
                auth.logout()
                break
            
            # ========== 1. EXTRAÇÃO DE DADOS ==========
            elif choice == "1.1":
                username = input("Nome de usuário: ").strip()
                max_amount = input("Máximo de seguidores (0 = todos): ").strip()
                max_amount = int(max_amount) if max_amount else 0
                followers_mgr.extract_followers(username, max_amount)
            
            elif choice == "1.2":
                username = input("Nome de usuário: ").strip()
                max_amount = input("Máximo de seguidos (0 = todos): ").strip()
                max_amount = int(max_amount) if max_amount else 0
                followers_mgr.extract_following(username, max_amount)
            
            elif choice == "1.3":
                username = input("Nome de usuário: ").strip()
                max_posts = int(input("Máximo de posts: ").strip())
                data_extractor.extract_user_posts(username, max_posts)
            
            elif choice == "1.4":
                hashtag = input("Hashtag (sem #): ").strip()
                max_posts = int(input("Máximo de posts: ").strip())
                recent = input("Posts recentes? (s/n): ").strip().lower() == 's'
                data_extractor.extract_hashtag_posts(hashtag, max_posts, recent)
            
            elif choice == "1.5":
                username = input("Nome de usuário: ").strip()
                data_extractor.extract_user_info(username)
            
            elif choice == "1.6":
                media_id = input("ID do post: ").strip()
                interactions_mgr.get_media_likers(media_id)
            
            elif choice == "1.7":
                media_id = input("ID do post: ").strip()
                interactions_mgr.get_media_comments(media_id)
            
            elif choice == "1.8":
                username = input("Nome de usuário: ").strip()
                max_posts = int(input("Máximo de posts: ").strip())
                data_extractor.extract_tagged_posts(username, max_posts)
            
            elif choice == "1.9":
                names_input = input("Nomes para buscar (separados por vírgula): ").strip()
                names = [n.strip() for n in names_input.split(',')]
                data_extractor.search_users_by_name(names)
            
            # ========== 2. AÇÕES DE ENGAJAMENTO ==========
            elif choice == "2.1":
                usernames = input("Lista de usuários (separados por vírgula): ").strip().split(',')
                usernames = [u.strip() for u in usernames]
                followers_mgr.follow_users(usernames)
            
            elif choice == "2.2":
                usernames = input("Lista de usuários (separados por vírgula): ").strip().split(',')
                usernames = [u.strip() for u in usernames]
                followers_mgr.unfollow_users(usernames)
            
            elif choice == "2.3":
                target_username = input("Usuário alvo: ").strip()
                max_follows = int(input("Máximo de seguidores para seguir: ").strip())
                followers_mgr.follow_account_followers(target_username, max_follows)
            
            elif choice == "2.4":
                media_ids = input("IDs de posts (separados por vírgula): ").strip().split(',')
                media_ids = [m.strip() for m in media_ids]
                interactions_mgr.like_posts(media_ids)
            
            elif choice == "2.5":
                media_ids = input("IDs de posts (separados por vírgula): ").strip().split(',')
                media_ids = [m.strip() for m in media_ids]
                use_custom = input("Usar comentários personalizados? (s/n): ").strip().lower()
                comments = None
                if use_custom == 's':
                    comments_input = input("Comentários (separados por vírgula): ").strip()
                    comments = [c.strip() for c in comments_input.split(',')]
                interactions_mgr.comment_on_posts(media_ids, comments)
            
            elif choice == "2.6":
                hashtag = input("Hashtag (sem #): ").strip()
                max_interactions = int(input("Máximo de posts: ").strip())
                like = input("Curtir? (s/n): ").strip().lower() == 's'
                comment = input("Comentar? (s/n): ").strip().lower() == 's'
                interactions_mgr.interact_with_hashtag(hashtag, max_interactions, like, comment)
            
            elif choice == "2.7":
                hashtags_input = input("Hashtags do nicho (separadas por vírgula): ").strip()
                hashtags = [h.strip() for h in hashtags_input.split(',')]
                max_per = int(input("Máximo de posts por hashtag: ").strip())
                interactions_mgr.auto_engage_daily(hashtags, max_per)
            
            # ========== 3. MENSAGENS DIRETAS ==========
            elif choice == "3.1":
                usernames_input = input("Lista de usuários (separados por vírgula): ").strip()
                usernames = [u.strip() for u in usernames_input.split(',')]
                message = input("Mensagem a enviar: ").strip()
                personalize = input("Personalizar com {username}? (s/n): ").strip().lower() == 's'
                dm_mgr.send_bulk_dms(usernames, message, personalize)
            
            elif choice == "3.2":
                target_username = input("Usuário alvo (para pegar seguidores): ").strip()
                max_dms = int(input("Máximo de DMs para enviar: ").strip())
                message = input("Mensagem a enviar: ").strip()
                personalize = input("Personalizar com {username}? (s/n): ").strip().lower() == 's'
                dm_mgr.send_dms_to_followers(target_username, message, max_dms, personalize)
            
            elif choice == "3.3":
                max_dms = int(input("Máximo de DMs para enviar: ").strip())
                message = input("Mensagem a enviar: ").strip()
                personalize = input("Personalizar com {username}? (s/n): ").strip().lower() == 's'
                dm_mgr.send_dms_to_new_followers(message, max_dms, personalize)
            
            elif choice == "3.4":
                file_path = input("Caminho do arquivo com usernames: ").strip()
                message = input("Mensagem a enviar: ").strip()
                personalize = input("Personalizar com {username}? (s/n): ").strip().lower() == 's'
                dm_mgr.send_dms_from_file(file_path, message, personalize)
            
            # ========== 4. STORIES ==========
            elif choice == "4.1":
                usernames_input = input("Usuários (separados por vírgula): ").strip()
                usernames = [u.strip() for u in usernames_input.split(',')]
                stories_mgr.extract_multiple_user_stories(usernames)
            
            elif choice == "4.2":
                usernames_input = input("Usuários (separados por vírgula): ").strip()
                usernames = [u.strip() for u in usernames_input.split(',')]
                stories_mgr.watch_stories(usernames)
            
            elif choice == "4.3":
                max_users = int(input("Máximo de usuários: ").strip())
                stories_mgr.watch_feed_stories(max_users)
            
            elif choice == "4.4":
                stories_mgr.get_story_viewers()
            
            # ========== 5. SISTEMA ==========
            elif choice == "5.1":
                stories_mgr.extract_notifications()
            
            elif choice == "5.2":
                stats = rate_limiter.get_statistics()
                print(f"\n{Fore.YELLOW}═══ ESTATÍSTICAS DE USO ═══{Style.RESET_ALL}")
                for action_type, data in stats.items():
                    print(f"{Fore.CYAN}{action_type.upper()}:{Style.RESET_ALL}")
                    print(f"  Últimas 24h: {data['last_24h']}")
                    print(f"  Última hora: {data['last_hour']}")
            
            else:
                print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
            
            input(f"\n{Fore.YELLOW}Pressione Enter para continuar...{Style.RESET_ALL}")
            
        except KeyboardInterrupt:
            logger.info("\n⚠️ Operação cancelada pelo usuário")
            break
        except Exception as e:
            logger.error(f"❌ Erro: {e}")
            input(f"\n{Fore.YELLOW}Pressione Enter para continuar...{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
