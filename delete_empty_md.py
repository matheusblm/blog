#!/usr/bin/env python3
"""
Script para encontrar e excluir arquivos Markdown vazios
"""

import os
from pathlib import Path


def is_file_empty(file_path):
    """
    Verifica se um arquivo está vazio ou contém apenas espaços em branco
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return len(content.strip()) == 0
    except Exception as e:
        print(f"Erro ao ler arquivo {file_path}: {e}")
        return False


def find_and_delete_empty_md_files(root_dir='.'):
    """
    Encontra e exclui todos os arquivos .md vazios no diretório especificado
    """
    root_path = Path(root_dir)
    deleted_files = []
    
    # Percorre recursivamente todos os arquivos .md
    for md_file in root_path.rglob('*.md'):
        if is_file_empty(md_file):
            try:
                print(f"Excluindo arquivo vazio: {md_file}")
                md_file.unlink()
                deleted_files.append(str(md_file))
            except Exception as e:
                print(f"Erro ao excluir {md_file}: {e}")
    
    return deleted_files


def main():
    """
    Função principal
    """
    print("=" * 60)
    print("Script para excluir arquivos Markdown vazios")
    print("=" * 60)
    print()
    
    # Diretório atual
    current_dir = os.getcwd()
    print(f"Procurando arquivos .md vazios em: {current_dir}")
    print()
    
    # Encontra e exclui arquivos vazios
    deleted_files = find_and_delete_empty_md_files(current_dir)
    
    # Mostra resumo
    print()
    print("=" * 60)
    print(f"Total de arquivos excluídos: {len(deleted_files)}")
    print("=" * 60)
    
    if deleted_files:
        print("\nArquivos excluídos:")
        for file in deleted_files:
            print(f"  - {file}")
    else:
        print("\nNenhum arquivo vazio encontrado.")


if __name__ == "__main__":
    main()

