#!/usr/bin/env python3
"""
Script de acesso rápido para adicionar notas ao Zettelkasten
"""

import os
import sys
from datetime import datetime
from pathlib import Path


def create_quick_note(note_type='quick'):
    """
    Cria uma nota rápida
    """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    
    if note_type == 'quick':
        folder = 'Zettelkasten/00-Inbox'
        filename = f"{timestamp}.md"
        content = f"""# Nota Rápida - {timestamp}

## Conteúdo
<!-- Anote rapidamente sua ideia -->


---
*Criado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    elif note_type == 'permanent':
        folder = 'Zettelkasten/01-Permanent-Notes'
        filename = f"{timestamp}.md"
        content = f"""# Nota Permanente - {timestamp}

## Ideia Principal
<!-- Uma ideia atômica, clara e concisa -->


## Contexto
<!-- Onde essa ideia se encaixa -->


## Conexões
<!-- Links para outras notas relacionadas usando [[nome-da-nota]] -->


## Referências
<!-- Fontes, livros, artigos relacionados -->


## Tags
<!-- #tag1 #tag2 -->


---
*Criado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    elif note_type == 'literature':
        folder = 'Zettelkasten/02-Literature-Notes'
        filename = f"{timestamp}.md"
        content = f"""# Anotação Literária - {timestamp}

## Fonte
**Título:** 
**Autor:** 
**Ano:** 
**Tipo:** (livro/artigo/vídeo)


## Resumo
<!-- Em suas próprias palavras -->


## Citações Importantes
> 


## Minhas Reflexões
<!-- Como isso se conecta com outras ideias? -->


## Conexões
<!-- [[outras-notas]] -->


## Tags
<!-- #tag1 #tag2 -->


---
*Criado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    elif note_type == 'daily':
        folder = 'Zettelkasten/03-Daily-Notes'
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f"{date_str}.md"
        content = f"""# {date_str}

## Reflexões
<!-- Como foi o dia? -->


## Tarefas
- [ ] 
- [ ] 
- [ ] 


## Ideias
<!-- Ideias que surgiram hoje -->


## Conexões
<!-- [[outras-notas]] -->


## Tags
<!-- #tag1 #tag2 -->


---
*Criado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    else:
        print(f"Tipo de nota inválido: {note_type}")
        return None
    
    # Criar pasta se não existir
    Path(folder).mkdir(parents=True, exist_ok=True)
    
    # Caminho completo do arquivo
    filepath = os.path.join(folder, filename)
    
    # Salvar arquivo
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Nota criada: {filepath}")
    
    return filepath


def open_with_editor(filepath, editor=None):
    """
    Abre o arquivo com o editor preferido
    """
    if editor is None:
        # Tentar detectar editor preferido
        editors = ['code', 'vim', 'nano', 'gedit']
        for ed in editors:
            if os.system(f"which {ed} > /dev/null 2>&1") == 0:
                editor = ed
                break
        
        if editor is None:
            print("Nenhum editor encontrado. Abra manualmente:")
            print(f"  {filepath}")
            return
    
    # Abrir com editor
    os.system(f"{editor} {filepath}")


def main():
    """
    Menu principal
    """
    print("=" * 60)
    print("NOTA RÁPIDA - ZETTELKASTEN")
    print("=" * 60)
    print()
    
    # Verificar argumentos da linha de comando
    if len(sys.argv) > 1:
        note_type = sys.argv[1]
        if note_type not in ['quick', 'permanent', 'literature', 'daily']:
            print(f"Tipo inválido: {note_type}")
            print("Tipos válidos: quick, permanent, literature, daily")
            sys.exit(1)
    else:
        print("Escolha o tipo de nota:")
        print("1. Nota Rápida (Inbox)")
        print("2. Nota Permanente")
        print("3. Anotação Literária")
        print("4. Daily Note")
        print()
        
        choice = input("Digite sua escolha (1-4): ").strip()
        
        type_map = {
            '1': 'quick',
            '2': 'permanent',
            '3': 'literature',
            '4': 'daily'
        }
        
        note_type = type_map.get(choice, 'quick')
    
    # Criar nota
    filepath = create_quick_note(note_type)
    
    if filepath:
        # Perguntar se quer abrir com editor
        open_editor = input("\nAbrir com editor? (s/N): ").strip().lower()
        
        if open_editor in ['s', 'sim', 'y', 'yes']:
            editor = input("Editor (Enter para padrão): ").strip()
            editor = editor if editor else None
            open_with_editor(filepath, editor)
        
        print("\n✓ Pronto! Nota criada com sucesso.")


if __name__ == "__main__":
    main()

