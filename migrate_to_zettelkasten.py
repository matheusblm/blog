#!/usr/bin/env python3
"""
Script de migração para o Zettelkasten.

Journal/* → 03-Daily-Notes
AWS, Books, CS, CyberSecurity, DataCamp, Data Science - UTFPR,
Estacio, FullCycle, Graphql, How to Leaner, JiuJitsu → 02-Literature-Notes

Nomenclatura: YYYYMMDDHHmm.md (com resolução de conflitos via sufixo _01, _02...)
Pastas originais e vazias deletadas ao final.
"""

import os
import re
import shutil
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent

DAILY_NOTES_DIR = BASE_DIR / "03-Daily-Notes"
LITERATURE_NOTES_DIR = BASE_DIR / "02-Literature-Notes"

MONTH_MAP = {
    "janeiro": "01", "fevereiro": "02", "março": "03", "marco": "03",
    "abril": "04", "maio": "05", "junho": "06",
    "julho": "07", "agosto": "08", "setembro": "09", "set": "09",
    "outubro": "10", "out": "10", "novembro": "11", "dezembro": "12",
}

STUDY_FOLDERS = [
    "AWS", "Books", "CS", "CyberSecurity", "DataCamp",
    "Data Science - UTFPR", "Estacio", "FullCycle", "Graphql",
    "How to Leaner", "JiuJitsu",
]

EMPTY_FOLDERS = ["AprendendoAaprender", "Interview"]

# Track used timestamps to resolve conflicts
used_timestamps: set[str] = set()


def generate_unique_timestamp(ts: str) -> str:
    """Return ts unchanged if unused, otherwise ts_01, ts_02, etc."""
    if ts not in used_timestamps:
        used_timestamps.add(ts)
        return ts
    counter = 1
    while True:
        candidate = f"{ts}_{counter:02d}"
        if candidate not in used_timestamps:
            used_timestamps.add(candidate)
            return candidate
        counter += 1


def add_frontmatter(content: str, frontmatter: str) -> str:
    """Prepend frontmatter to content, skipping if already present."""
    if content.startswith("---"):
        return content
    return frontmatter + "\n" + content


def mtime_to_timestamp(path: Path) -> str:
    """Convert file mtime to YYYYMMDDHHmm string."""
    dt = datetime.fromtimestamp(path.stat().st_mtime)
    return dt.strftime("%Y%m%d%H%M")


# ─── Journal migration ────────────────────────────────────────────────────────

def migrate_journal():
    journal_dir = BASE_DIR / "Journal"
    if not journal_dir.exists():
        print("Journal: pasta não encontrada, pulando.")
        return

    print("\n=== Migrando Journal → 03-Daily-Notes ===")
    migrated = 0
    skipped = 0

    for md_file in sorted(journal_dir.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8").strip()
        if not content:
            skipped += 1
            continue

        parts = md_file.parts  # e.g. ('.../Journal', '2024', 'Março', '22.md')

        # Find year
        year = None
        month_num = None
        for part in parts:
            if part.isdigit() and len(part) == 4:
                year = part
            else:
                normalized = part.lower().strip()
                if normalized in MONTH_MAP:
                    month_num = MONTH_MAP[normalized]

        # Determine timestamp
        day_match = re.match(r"^(\d{1,2})$", md_file.stem)

        if year and month_num and day_match:
            # Numbered file like 22.md inside Journal/2024/Março/
            day = day_match.group(1).zfill(2)
            ts_base = f"{year}{month_num}{day}1200"
            date_str = f"{year}-{month_num}-{day}"
        elif year and month_num:
            # Topic-named file like Kubernetes.md inside Journal/2025/Set/
            dt = datetime.fromtimestamp(md_file.stat().st_mtime)
            ts_base = dt.strftime("%Y%m%d%H%M")
            date_str = dt.strftime("%Y-%m-%d")
        elif year and day_match:
            # File directly inside year folder like Journal/2024/1.md
            day = day_match.group(1).zfill(2)
            ts_base = f"{year}01{day}1200"
            date_str = f"{year}-01-{day}"
        else:
            # Fallback: use mtime
            dt = datetime.fromtimestamp(md_file.stat().st_mtime)
            ts_base = dt.strftime("%Y%m%d%H%M")
            date_str = dt.strftime("%Y-%m-%d")

        ts = generate_unique_timestamp(ts_base)

        frontmatter = f"---\nid: {ts}\ntype: daily\ndate: {date_str}\n---"
        new_content = add_frontmatter(content, frontmatter)

        dest = DAILY_NOTES_DIR / f"{ts}.md"
        dest.write_text(new_content, encoding="utf-8")
        print(f"  {md_file.relative_to(BASE_DIR)} → 03-Daily-Notes/{ts}.md")
        migrated += 1

    print(f"Journal: {migrated} migradas, {skipped} vazias ignoradas.")


# ─── Study folders migration ──────────────────────────────────────────────────

def migrate_study_folders():
    print("\n=== Migrando pastas de estudo → 02-Literature-Notes ===")
    total_migrated = 0
    total_skipped = 0

    for folder_name in STUDY_FOLDERS:
        folder = BASE_DIR / folder_name
        if not folder.exists():
            print(f"  {folder_name}: não encontrada, pulando.")
            continue

        migrated = 0
        skipped_non_md = 0

        for filepath in sorted(folder.rglob("*")):
            if not filepath.is_file():
                continue
            if filepath.suffix.lower() != ".md":
                skipped_non_md += 1
                continue

            content = filepath.read_text(encoding="utf-8").strip()
            if not content:
                continue

            ts_base = mtime_to_timestamp(filepath)
            ts = generate_unique_timestamp(ts_base)

            # tema = most-specific subfolder name, or root folder if file is directly inside
            rel = filepath.relative_to(folder)
            if len(rel.parts) > 1:
                tema = rel.parts[-2]  # immediate parent subfolder
            else:
                tema = folder_name

            source = str(filepath.relative_to(BASE_DIR))

            frontmatter = f"---\nid: {ts}\ntags:\ntema: {tema}\nsource: {source}\n---"
            new_content = add_frontmatter(content, frontmatter)

            dest = LITERATURE_NOTES_DIR / f"{ts}.md"
            dest.write_text(new_content, encoding="utf-8")
            print(f"  {source} → 02-Literature-Notes/{ts}.md")
            migrated += 1

        print(f"  {folder_name}: {migrated} migradas, {skipped_non_md} não-.md ignoradas.")
        total_migrated += migrated
        total_skipped += skipped_non_md

    print(f"Estudo: {total_migrated} migradas no total, {total_skipped} não-.md ignoradas.")


# ─── Cleanup ──────────────────────────────────────────────────────────────────

def delete_original_folders():
    print("\n=== Deletando pastas originais ===")

    to_delete = STUDY_FOLDERS + ["Journal"] + EMPTY_FOLDERS

    for folder_name in to_delete:
        folder = BASE_DIR / folder_name
        if folder.exists():
            shutil.rmtree(folder)
            print(f"  Deletado: {folder_name}/")
        else:
            print(f"  {folder_name}/: já não existe.")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Migração para Zettelkasten")
    print("=" * 60)

    DAILY_NOTES_DIR.mkdir(exist_ok=True)
    LITERATURE_NOTES_DIR.mkdir(exist_ok=True)

    migrate_journal()
    migrate_study_folders()
    delete_original_folders()

    print("\n" + "=" * 60)
    print("Migração concluída!")
    print("=" * 60)
    print("\nVerificação:")
    daily_count = len(list(DAILY_NOTES_DIR.glob("*.md")))
    lit_count = len(list(LITERATURE_NOTES_DIR.glob("*.md")))
    print(f"  03-Daily-Notes:    {daily_count} arquivo(s) .md")
    print(f"  02-Literature-Notes: {lit_count} arquivo(s) .md")


if __name__ == "__main__":
    main()
