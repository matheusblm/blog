#!/usr/bin/env python3
"""
Configurações do Sistema Zettelkasten
"""

# Estrutura de pastas
FOLDER_STRUCTURE = {
    'inbox': '00-Inbox',
    'permanent': '01-Permanent-Notes',
    'literature': '02-Literature-Notes',
    'daily': '03-Daily-Notes',
    'mocs': '04-MOCs',
    'archive': '05-Archive'
}

# Configurações de nomenclatura
NOTE_NAMING = {
    'format': 'timestamp',  # 'timestamp' ou 'sequential'
    'separator': '-',
    'extension': '.md'
}

# Configurações de tags
TAG_SETTINGS = {
    'prefix': '#',
    'lowercase': True,
    'spaces_to_underscores': False
}

# Configurações de links
LINK_SETTINGS = {
    'format': 'wiki',  # 'wiki' [[link]] ou 'markdown' [link](file.md)
    'auto_create': False,  # Criar arquivo automaticamente ao linkar
    'case_sensitive': False
}

# Configurações de templates
TEMPLATES = {
    'permanent_note': {
        'include_date': True,
        'include_tags': True,
        'include_links': True,
        'sections': ['main_idea', 'context', 'connections', 'references']
    },
    'literature_note': {
        'include_date': True,
        'include_tags': True,
        'include_links': True,
        'sections': ['source', 'summary', 'quotes', 'reflections', 'connections']
    },
    'daily_note': {
        'include_date': True,
        'include_tags': True,
        'sections': ['reflections', 'tasks', 'ideas', 'connections']
    }
}

# Configurações de revisão
REVIEW_SETTINGS = {
    'inbox_review_frequency': 'daily',  # 'daily', 'weekly', 'monthly'
    'permanent_note_review_frequency': 'weekly',
    'old_notes_review_frequency': 'monthly'
}

# Configurações de backup
BACKUP_SETTINGS = {
    'enabled': True,
    'frequency': 'weekly',  # 'daily', 'weekly', 'monthly'
    'location': 'backups/',
    'compress': True
}

# Configurações de estatísticas
STATS_SETTINGS = {
    'track_notes_created': True,
    'track_links_made': True,
    'track_tags_used': True,
    'generate_reports': True
}

# Configurações de pesquisa
SEARCH_SETTINGS = {
    'search_in_content': True,
    'search_in_tags': True,
    'search_in_links': True,
    'case_sensitive': False,
    'fuzzy_matching': True
}

# Configurações de exportação
EXPORT_SETTINGS = {
    'formats': ['markdown', 'html', 'pdf'],
    'include_metadata': True,
    'include_backlinks': True
}

# Configurações de integração
INTEGRATION_SETTINGS = {
    'obsidian_compatible': True,
    'logseq_compatible': True,
    'roam_compatible': True
}

# Configurações de privacidade
PRIVACY_SETTINGS = {
    'encrypt_sensitive_notes': False,
    'exclude_from_search': [],
    'exclude_from_backup': []
}

# Configurações de sincronização
SYNC_SETTINGS = {
    'enabled': False,
    'service': None,  # 'git', 'dropbox', 'onedrive', etc.
    'auto_sync': False,
    'conflict_resolution': 'manual'  # 'manual', 'newest', 'oldest'
}

# Configurações de notificações
NOTIFICATION_SETTINGS = {
    'remind_inbox_review': True,
    'remind_permanent_note_review': True,
    'remind_old_notes_review': True,
    'notification_method': 'console'  # 'console', 'desktop', 'email'
}

# Configurações de desenvolvimento
DEVELOPMENT_SETTINGS = {
    'debug_mode': False,
    'verbose_logging': False,
    'log_file': 'zettelkasten.log'
}

def get_config():
    """
    Retorna todas as configurações
    """
    return {
        'folders': FOLDER_STRUCTURE,
        'naming': NOTE_NAMING,
        'tags': TAG_SETTINGS,
        'links': LINK_SETTINGS,
        'templates': TEMPLATES,
        'review': REVIEW_SETTINGS,
        'backup': BACKUP_SETTINGS,
        'stats': STATS_SETTINGS,
        'search': SEARCH_SETTINGS,
        'export': EXPORT_SETTINGS,
        'integration': INTEGRATION_SETTINGS,
        'privacy': PRIVACY_SETTINGS,
        'sync': SYNC_SETTINGS,
        'notifications': NOTIFICATION_SETTINGS,
        'development': DEVELOPMENT_SETTINGS
    }

def print_config():
    """
    Imprime todas as configurações
    """
    import json
    config = get_config()
    print(json.dumps(config, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    print_config()

