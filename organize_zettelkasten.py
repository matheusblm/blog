#!/usr/bin/env python3
"""
Script para organizar o sistema Zettelkasten
"""

import os
import shutil
from datetime import datetime
from pathlib import Path
import re


def create_zettelkasten_structure(base_dir='.'):
    """
    Cria a estrutura de pastas para o Zettelkasten
    """
    base_path = Path(base_dir)
    
    # Estrutura do Zettelkasten
    structure = {
        'Zettelkasten': {
            '00-Inbox': 'Notas rápidas e temporárias',
            '01-Permanent-Notes': 'Notas permanentes (núcleo do sistema)',
            '02-Literature-Notes': 'Anotações de leitura',
            '03-Daily-Notes': 'Notas diárias e reflexões',
            '04-MOCs': 'Maps of Content (índices temáticos)',
            '05-Archive': 'Notas arquivadas ou menos relevantes'
        }
    }
    
    print("=" * 60)
    print("Criando estrutura Zettelkasten")
    print("=" * 60)
    print()
    
    for folder, description in structure['Zettelkasten'].items():
        folder_path = base_path / folder
        folder_path.mkdir(exist_ok=True)
        
        # Criar README explicativo em cada pasta
        readme_path = folder_path / 'README.md'
        if not readme_path.exists():
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(f"# {folder}\n\n")
                f.write(f"{description}\n\n")
                f.write("## Como usar\n\n")
                
                if 'Inbox' in folder:
                    f.write("- Anote rapidamente qualquer ideia\n")
                    f.write("- Não se preocupe com organização aqui\n")
                    f.write("- Revise diariamente e mova para notas permanentes\n")
                elif 'Permanent' in folder:
                    f.write("- Notas atômicas (uma ideia por nota)\n")
                    f.write("- Use IDs únicos (timestamp)\n")
                    f.write("- Conecte com outras notas usando [[links]]\n")
                elif 'Literature' in folder:
                    f.write("- Anotações sobre livros, artigos, vídeos\n")
                    f.write("- Use suas próprias palavras\n")
                    f.write("- Referencie a fonte original\n")
                elif 'Daily' in folder:
                    f.write("- Notas diárias e reflexões\n")
                    f.write("- Formato: YYYY-MM-DD.md\n")
                elif 'MOC' in folder:
                    f.write("- Mapas de conteúdo por tema\n")
                    f.write("- Índices para navegação\n")
        
        print(f"✓ Criado: {folder}")
        print(f"  {description}")
    
    print()
    print("=" * 60)
    print("Estrutura criada com sucesso!")
    print("=" * 60)


def migrate_journal_to_daily_notes(journal_dir='Journal', target_dir='Zettelkasten/03-Daily-Notes'):
    """
    Migra notas do Journal para o formato de daily notes do Zettelkasten
    """
    journal_path = Path(journal_dir)
    target_path = Path(target_dir)
    
    if not journal_path.exists():
        print(f"Pasta {journal_dir} não encontrada.")
        return
    
    print()
    print("=" * 60)
    print("Migrando Journal para Daily Notes")
    print("=" * 60)
    print()
    
    migrated_count = 0
    
    # Encontrar todos os arquivos .md no Journal
    for md_file in journal_path.rglob('*.md'):
        if md_file.is_file():
            # Ler conteúdo
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                
                # Só migrar se tiver conteúdo
                if content:
                    # Criar nome no formato YYYY-MM-DD.md
                    # Extrair data do caminho
                    parts = md_file.parts
                    
                    # Tentar extrair ano, mês e dia do caminho
                    year = None
                    month = None
                    day = None
                    
                    for part in parts:
                        if part.isdigit() and len(part) == 4:
                            year = part
                        elif part in ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
                                     'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']:
                            month_map = {
                                'Janeiro': '01', 'Fevereiro': '02', 'Março': '03',
                                'Abril': '04', 'Maio': '05', 'Junho': '06',
                                'Julho': '07', 'Agosto': '08', 'Setembro': '09',
                                'Outubro': '10', 'Novembro': '11', 'Dezembro': '12'
                            }
                            month = month_map.get(part)
                    
                    # Extrair dia do nome do arquivo
                    day_match = re.match(r'(\d+)\.md', md_file.name)
                    if day_match:
                        day = day_match.group(1).zfill(2)
                    
                    if year and month and day:
                        new_filename = f"{year}-{month}-{day}.md"
                        new_path = target_path / new_filename
                        
                        # Se já existe, adicionar conteúdo
                        if new_path.exists():
                            with open(new_path, 'a', encoding='utf-8') as f:
                                f.write(f"\n\n---\n\n")
                                f.write(content)
                        else:
                            with open(new_path, 'w', encoding='utf-8') as f:
                                f.write(f"# {year}-{month}-{day}\n\n")
                                f.write(content)
                        
                        migrated_count += 1
                        print(f"✓ Migrado: {md_file} -> {new_filename}")
            
            except Exception as e:
                print(f"✗ Erro ao migrar {md_file}: {e}")
    
    print()
    print(f"Total de notas migradas: {migrated_count}")
    print("=" * 60)


def create_moc_template(topic_name, output_dir='Zettelkasten/04-MOCs'):
    """
    Cria um template de MOC (Map of Content) para um tema
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Criar nome do arquivo (slug)
    slug = topic_name.lower().replace(' ', '-')
    moc_file = output_path / f"{slug}.md"
    
    if moc_file.exists():
        print(f"MOC '{topic_name}' já existe!")
        return
    
    template = f"""# {topic_name}

## Visão Geral
Breve descrição do tema e sua importância.

## Notas Permanentes
<!-- Adicione links para notas relacionadas usando [[nome-da-nota]] -->

## Literatura
<!-- Anotações de leitura relacionadas -->

## Conexões
<!-- Outros MOCs ou temas relacionados -->

## Desenvolvimento
<!-- Ideias em desenvolvimento, perguntas a explorar -->

---
*Criado em: {datetime.now().strftime('%Y-%m-%d')}*
"""
    
    with open(moc_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"✓ MOC criado: {moc_file}")


def create_note_template(note_type='permanent'):
    """
    Cria um template de nota
    """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    
    if note_type == 'permanent':
        template = f"""# Nota Permanente - {timestamp}

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
        template = f"""# Anotação Literária - {timestamp}

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
    else:
        template = f"""# Nota Rápida - {timestamp}

## Conteúdo
<!-- Anote rapidamente sua ideia -->

---
*Criado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""
    
    return template


def main():
    """
    Menu principal
    """
    print("=" * 60)
    print("Organizador de Zettelkasten")
    print("=" * 60)
    print()
    print("Escolha uma opção:")
    print("1. Criar estrutura de pastas")
    print("2. Migrar Journal para Daily Notes")
    print("3. Criar MOC (Map of Content)")
    print("4. Criar template de nota")
    print("5. Fazer tudo (criar estrutura + migrar)")
    print()
    
    choice = input("Digite sua escolha (1-5): ").strip()
    
    if choice == '1':
        create_zettelkasten_structure()
    
    elif choice == '2':
        migrate_journal_to_daily_notes()
    
    elif choice == '3':
        topic = input("Nome do tema para o MOC: ").strip()
        if topic:
            create_moc_template(topic)
    
    elif choice == '4':
        print("\nTipo de nota:")
        print("1. Nota Permanente")
        print("2. Anotação Literária")
        print("3. Nota Rápida")
        note_type = input("Escolha (1-3): ").strip()
        
        type_map = {'1': 'permanent', '2': 'literature', '3': 'quick'}
        selected_type = type_map.get(note_type, 'permanent')
        
        template = create_note_template(selected_type)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        
        # Determinar pasta de destino
        if selected_type == 'permanent':
            folder = 'Zettelkasten/01-Permanent-Notes'
        elif selected_type == 'literature':
            folder = 'Zettelkasten/02-Literature-Notes'
        else:
            folder = 'Zettelkasten/00-Inbox'
        
        Path(folder).mkdir(exist_ok=True)
        filename = f"{folder}/{timestamp}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template)
        
        print(f"\n✓ Template criado: {filename}")
    
    elif choice == '5':
        create_zettelkasten_structure()
        migrate_journal_to_daily_notes()
        print("\n✓ Processo completo finalizado!")
    
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()

