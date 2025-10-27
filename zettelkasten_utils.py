#!/usr/bin/env python3
"""
Utilitários para o Sistema Zettelkasten
"""

import os
import re
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict
import json


class ZettelkastenUtils:
    """
    Classe com utilitários para gerenciar o Zettelkasten
    """
    
    def __init__(self, base_dir='Zettelkasten'):
        self.base_dir = Path(base_dir)
        self.folders = {
            'inbox': self.base_dir / '00-Inbox',
            'permanent': self.base_dir / '01-Permanent-Notes',
            'literature': self.base_dir / '02-Literature-Notes',
            'daily': self.base_dir / '03-Daily-Notes',
            'mocs': self.base_dir / '04-MOCs',
            'archive': self.base_dir / '05-Archive'
        }
    
    def get_statistics(self):
        """
        Retorna estatísticas do Zettelkasten
        """
        stats = {
            'total_notes': 0,
            'notes_by_folder': {},
            'total_links': 0,
            'total_tags': 0,
            'unique_tags': set(),
            'notes_with_links': 0,
            'notes_with_tags': 0,
            'orphan_notes': 0,  # Notas sem links
            'most_linked_notes': [],
            'most_used_tags': []
        }
        
        all_notes = []
        
        # Contar notas por pasta
        for folder_name, folder_path in self.folders.items():
            if folder_path.exists():
                md_files = list(folder_path.glob('*.md'))
                # Excluir README.md
                md_files = [f for f in md_files if f.name != 'README.md']
                count = len(md_files)
                stats['notes_by_folder'][folder_name] = count
                stats['total_notes'] += count
                all_notes.extend(md_files)
        
        # Analisar conteúdo das notas
        link_pattern = r'\[\[([^\]]+)\]\]'
        tag_pattern = r'#(\w+)'
        
        note_links = defaultdict(int)
        
        for note_file in all_notes:
            try:
                with open(note_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Contar links
                links = re.findall(link_pattern, content)
                if links:
                    stats['notes_with_links'] += 1
                    stats['total_links'] += len(links)
                    for link in links:
                        note_links[link] += 1
                
                # Contar tags
                tags = re.findall(tag_pattern, content)
                if tags:
                    stats['notes_with_tags'] += 1
                    stats['total_tags'] += len(tags)
                    stats['unique_tags'].update(tags)
                
            except Exception as e:
                print(f"Erro ao ler {note_file}: {e}")
        
        # Identificar notas órfãs
        stats['orphan_notes'] = stats['total_notes'] - stats['notes_with_links']
        
        # Top 10 notas mais linkadas
        stats['most_linked_notes'] = sorted(
            note_links.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:10]
        
        # Top 10 tags mais usadas
        stats['most_used_tags'] = Counter(stats['unique_tags']).most_common(10)
        
        return stats
    
    def print_statistics(self):
        """
        Imprime estatísticas formatadas
        """
        stats = self.get_statistics()
        
        print("=" * 60)
        print("ESTATÍSTICAS DO ZETTELKASTEN")
        print("=" * 60)
        print()
        
        print(f"📊 Total de notas: {stats['total_notes']}")
        print()
        
        print("📁 Notas por pasta:")
        for folder, count in stats['notes_by_folder'].items():
            print(f"   {folder}: {count}")
        print()
        
        print(f"🔗 Total de links: {stats['total_links']}")
        print(f"   Notas com links: {stats['notes_with_links']}")
        print(f"   Notas órfãs: {stats['orphan_notes']}")
        print()
        
        print(f"🏷️  Total de tags: {stats['total_tags']}")
        print(f"   Tags únicas: {len(stats['unique_tags'])}")
        print(f"   Notas com tags: {stats['notes_with_tags']}")
        print()
        
        if stats['most_linked_notes']:
            print("⭐ Notas mais linkadas:")
            for note, count in stats['most_linked_notes']:
                print(f"   [[{note}]]: {count} links")
            print()
        
        if stats['most_used_tags']:
            print("🏷️  Tags mais usadas:")
            for tag, count in stats['most_used_tags']:
                print(f"   #{tag}: {count} vezes")
            print()
        
        print("=" * 60)
    
    def search_notes(self, query, folder=None):
        """
        Busca notas por texto
        """
        search_folder = self.folders.get(folder, self.base_dir) if folder else self.base_dir
        
        results = []
        
        for md_file in search_folder.rglob('*.md'):
            if md_file.name == 'README.md':
                continue
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if query.lower() in content.lower():
                    # Encontrar linha com o termo
                    lines = content.split('\n')
                    for i, line in enumerate(lines, 1):
                        if query.lower() in line.lower():
                            results.append({
                                'file': md_file,
                                'line': i,
                                'context': line.strip()
                            })
                            break
            
            except Exception as e:
                print(f"Erro ao ler {md_file}: {e}")
        
        return results
    
    def print_search_results(self, query, folder=None):
        """
        Imprime resultados de busca
        """
        results = self.search_notes(query, folder)
        
        print("=" * 60)
        print(f"RESULTADOS DA BUSCA: '{query}'")
        print("=" * 60)
        print()
        
        if not results:
            print("Nenhum resultado encontrado.")
            return
        
        print(f"Total de resultados: {len(results)}\n")
        
        for result in results:
            print(f"📄 {result['file']}")
            print(f"   Linha {result['line']}: {result['context'][:80]}...")
            print()
        
        print("=" * 60)
    
    def find_orphan_notes(self):
        """
        Encontra notas sem links (órfãs)
        """
        orphan_notes = []
        
        for folder_name, folder_path in self.folders.items():
            if not folder_path.exists():
                continue
            
            for md_file in folder_path.glob('*.md'):
                if md_file.name == 'README.md':
                    continue
                
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Verificar se tem links
                    if not re.search(r'\[\[[^\]]+\]\]', content):
                        orphan_notes.append(md_file)
                
                except Exception as e:
                    print(f"Erro ao ler {md_file}: {e}")
        
        return orphan_notes
    
    def print_orphan_notes(self):
        """
        Imprime notas órfãs
        """
        orphans = self.find_orphan_notes()
        
        print("=" * 60)
        print("NOTAS ÓRFÃS (sem links)")
        print("=" * 60)
        print()
        
        if not orphans:
            print("✓ Nenhuma nota órfã encontrada!")
            return
        
        print(f"Total de notas órfãs: {len(orphans)}\n")
        
        for note in orphans:
            print(f"📄 {note}")
        
        print()
        print("💡 Dica: Conecte essas notas com outras para criar uma rede de conhecimento!")
        print("=" * 60)
    
    def find_backlinks(self, note_name):
        """
        Encontra todas as notas que linkam para uma nota específica
        """
        backlinks = []
        
        for folder_name, folder_path in self.folders.items():
            if not folder_path.exists():
                continue
            
            for md_file in folder_path.glob('*.md'):
                if md_file.name == 'README.md':
                    continue
                
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Verificar se contém link para a nota
                    if f'[[{note_name}]]' in content:
                        backlinks.append(md_file)
                
                except Exception as e:
                    print(f"Erro ao ler {md_file}: {e}")
        
        return backlinks
    
    def print_backlinks(self, note_name):
        """
        Imprime backlinks de uma nota
        """
        backlinks = self.find_backlinks(note_name)
        
        print("=" * 60)
        print(f"BACKLINKS DE: {note_name}")
        print("=" * 60)
        print()
        
        if not backlinks:
            print(f"Nenhuma nota linka para '{note_name}'")
            return
        
        print(f"Total de backlinks: {len(backlinks)}\n")
        
        for backlink in backlinks:
            print(f"📄 {backlink}")
        
        print()
        print("=" * 60)
    
    def export_graph(self, output_file='zettelkasten_graph.json'):
        """
        Exporta grafo de conexões das notas
        """
        graph = {
            'nodes': [],
            'edges': []
        }
        
        note_ids = {}
        node_id = 0
        
        # Criar nós
        for folder_name, folder_path in self.folders.items():
            if not folder_path.exists():
                continue
            
            for md_file in folder_path.glob('*.md'):
                if md_file.name == 'README.md':
                    continue
                
                note_name = md_file.stem
                note_ids[note_name] = node_id
                
                graph['nodes'].append({
                    'id': node_id,
                    'label': note_name,
                    'group': folder_name,
                    'file': str(md_file)
                })
                
                node_id += 1
        
        # Criar arestas (links)
        for folder_name, folder_path in self.folders.items():
            if not folder_path.exists():
                continue
            
            for md_file in folder_path.glob('*.md'):
                if md_file.name == 'README.md':
                    continue
                
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Encontrar links
                    links = re.findall(r'\[\[([^\]]+)\]\]', content)
                    
                    source_id = note_ids.get(md_file.stem)
                    
                    for link in links:
                        target_id = note_ids.get(link)
                        if target_id is not None and source_id is not None:
                            graph['edges'].append({
                                'source': source_id,
                                'target': target_id
                            })
                
                except Exception as e:
                    print(f"Erro ao ler {md_file}: {e}")
        
        # Salvar JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(graph, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Grafo exportado para: {output_file}")
        print(f"  Nós: {len(graph['nodes'])}")
        print(f"  Arestas: {len(graph['edges'])}")


def main():
    """
    Menu principal
    """
    utils = ZettelkastenUtils()
    
    print("=" * 60)
    print("UTILITÁRIOS DO ZETTELKASTEN")
    print("=" * 60)
    print()
    print("Escolha uma opção:")
    print("1. Ver estatísticas")
    print("2. Buscar notas")
    print("3. Encontrar notas órfãs")
    print("4. Ver backlinks de uma nota")
    print("5. Exportar grafo de conexões")
    print()
    
    choice = input("Digite sua escolha (1-5): ").strip()
    
    if choice == '1':
        utils.print_statistics()
    
    elif choice == '2':
        query = input("Digite o termo de busca: ").strip()
        folder = input("Pasta específica (Enter para todas): ").strip()
        folder = folder if folder else None
        utils.print_search_results(query, folder)
    
    elif choice == '3':
        utils.print_orphan_notes()
    
    elif choice == '4':
        note_name = input("Nome da nota: ").strip()
        utils.print_backlinks(note_name)
    
    elif choice == '5':
        output = input("Nome do arquivo (Enter para padrão): ").strip()
        output = output if output else 'zettelkasten_graph.json'
        utils.export_graph(output)
    
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()

