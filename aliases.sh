#!/bin/bash
# Aliases para facilitar o uso do Zettelkasten
# Adicione ao seu ~/.zshrc ou ~/.bashrc

# Diretório base do Zettelkasten
export ZK_DIR="$HOME/Projetos/blog"

# Criar nota rápida
alias zk-quick='cd $ZK_DIR && python3 quick_note.py quick'

# Criar nota permanente
alias zk-permanent='cd $ZK_DIR && python3 quick_note.py permanent'

# Criar anotação literária
alias zk-literature='cd $ZK_DIR && python3 quick_note.py literature'

# Criar daily note
alias zk-daily='cd $ZK_DIR && python3 quick_note.py daily'

# Ver estatísticas
alias zk-stats='cd $ZK_DIR && python3 zettelkasten_utils.py'

# Organizar Zettelkasten
alias zk-organize='cd $ZK_DIR && python3 organize_zettelkasten.py'

# Buscar notas
zk-search() {
    cd $ZK_DIR
    python3 zettelkasten_utils.py
}

# Limpar arquivos vazios
alias zk-clean='cd $ZK_DIR && python3 delete_empty_md.py'

# Ir para o diretório do Zettelkasten
alias zk='cd $ZK_DIR'

# Listar notas recentes
alias zk-recent='cd $ZK_DIR && find Zettelkasten -name "*.md" -type f -not -name "README.md" -printf "%T@ %p\n" | sort -rn | head -10 | cut -d" " -f2-'

# Ver notas do dia
alias zk-today='cd $ZK_DIR && ls -lh Zettelkasten/03-Daily-Notes/$(date +%Y-%m-%d).md 2>/dev/null || echo "Nenhuma nota hoje ainda"'

# Abrir nota do dia
alias zk-open-today='cd $ZK_DIR && code Zettelkasten/03-Daily-Notes/$(date +%Y-%m-%d).md 2>/dev/null || zk-daily'

# Contar notas
alias zk-count='cd $ZK_DIR && echo "Total de notas:" && find Zettelkasten -name "*.md" -type f -not -name "README.md" | wc -l'

# Ver ajuda
zk-help() {
    echo "=========================================="
    echo "ZETTELKASTEN - Comandos Disponíveis"
    echo "=========================================="
    echo ""
    echo "Criar Notas:"
    echo "  zk-quick       - Nota rápida (Inbox)"
    echo "  zk-permanent   - Nota permanente"
    echo "  zk-literature  - Anotação literária"
    echo "  zk-daily       - Daily note"
    echo ""
    echo "Gerenciamento:"
    echo "  zk-stats       - Ver estatísticas"
    echo "  zk-organize    - Organizar sistema"
    echo "  zk-search      - Buscar notas"
    echo "  zk-clean       - Limpar arquivos vazios"
    echo ""
    echo "Navegação:"
    echo "  zk             - Ir para diretório"
    echo "  zk-recent      - Notas recentes"
    echo "  zk-today       - Ver nota do dia"
    echo "  zk-open-today  - Abrir/editar nota do dia"
    echo "  zk-count       - Contar notas"
    echo ""
    echo "Ajuda:"
    echo "  zk-help        - Mostrar esta ajuda"
    echo ""
    echo "=========================================="
}

echo "Zettelkasten aliases carregados!"
echo "Execute 'zk-help' para ver todos os comandos disponíveis"

