"""
test_helpers.py
Utilitários compartilhados pelos testes do dio_explore.
"""

import json
import os
import re
from datetime import datetime

# ── Caminhos base ────────────────────────────────────────────────────────────
ROOT_DIR     = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR     = os.path.join(ROOT_DIR, "data")
COMMANDS_DIR = os.path.abspath(os.path.join(ROOT_DIR, "..", ".bob", "commands"))
JSON_PATH    = os.path.join(DATA_DIR, "trilhas_dio.json")


# ── Carregador de JSON ────────────────────────────────────────────────────────
def load_trilhas() -> dict:
    """Carrega e retorna o conteúdo de trilhas_dio.json."""
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def find_trilha_by_tecnologia(tecnologia: str) -> dict | None:
    """Busca uma trilha pelo campo tecnologia.
    Prioridade: match exato (case-insensitive) → match por substring.
    """
    data = load_trilhas()
    termo = tecnologia.lower()
    # 1ª passagem: match exato
    for trilha in data.get("trilhas", []):
        if trilha["tecnologia"].lower() == termo:
            return trilha
    # 2ª passagem: match por substring
    for trilha in data.get("trilhas", []):
        if termo in trilha["tecnologia"].lower():
            return trilha
    return None


# ── Simuladores de saída dos slash commands ──────────────────────────────────
def simulate_trilha_output(tecnologia: str) -> str:
    """Simula a saída do comando /trilha <tecnologia>."""
    trilha = find_trilha_by_tecnologia(tecnologia)
    if not trilha:
        techs = [t["tecnologia"] for t in load_trilhas()["trilhas"]]
        return f"[ERRO] Tecnologia '{tecnologia}' não encontrada.\nDisponíveis: {', '.join(techs)}"

    xp_por_modulo = trilha["xp_total"] // trilha["numero_de_modulos"]
    modulos = "\n".join(
        f"  Módulo {i+1}: Tópico {i+1} de {trilha['tecnologia']} — {xp_por_modulo} XP"
        for i in range(trilha["numero_de_modulos"])
    )
    badges  = "\n".join(f"  🎖️ {b}" for b in trilha["badges_disponiveis"])
    lives   = "\n".join(f"  📡 {l}" for l in trilha["lives_ao_vivo"])
    promo   = (
        f"🔥 Promoção ativa! {trilha['promocao']['desconto_percentual']}% até {trilha['promocao']['validade']}"
        if trilha["promocao"]["ativa"]
        else "ℹ️ Nenhuma promoção ativa."
    )
    vitalicio = "Sim" if trilha["vitalicio"] else "Não"

    return (
        f"# 📚 Plano de Estudos — {trilha['nome']}\n\n"
        f"🎯 Tecnologia: {trilha['tecnologia']}\n"
        f"📊 Nível: {trilha['nivel']}\n"
        f"🧩 Módulos: {trilha['numero_de_modulos']}\n"
        f"⭐ XP Total: {trilha['xp_total']} XP\n"
        f"♾️ Vitalício: {vitalicio}\n\n"
        f"## Módulos\n{modulos}\n\n"
        f"## Badges\n{badges}\n\n"
        f"## Lives\n{lives}\n\n"
        f"## Promoção\n{promo}"
    )


def simulate_desafio_output(tecnologia: str, nivel: str) -> str:
    """Simula a saída do comando /desafio <tecnologia> <nivel>."""
    niveis_validos = ["básico", "intermediário", "avançado"]
    if nivel.lower() not in niveis_validos:
        return f"[ERRO] Nível '{nivel}' inválido. Use: Básico, Intermediário ou Avançado."

    xp_map = {"básico": 1500, "intermediário": 3000, "avançado": 5000}
    tempo_map = {"básico": 30, "intermediário": 60, "avançado": 90}
    xp   = xp_map[nivel.lower()]
    tempo = tempo_map[nivel.lower()]
    codigo_desafio = f"DIO-{abs(hash(tecnologia + nivel)) % 9000 + 1000}"

    return (
        f"# ⚔️ Desafio DIO — {tecnologia} | Nível: {nivel}\n\n"
        f"🆔 Desafio: {codigo_desafio}\n"
        f"⏱️ Tempo estimado: {tempo} minutos\n"
        f"⭐ XP ao concluir: {xp} XP\n\n"
        f"## Enunciado\n"
        f"Implemente uma solução em {tecnologia} para o nível {nivel}.\n\n"
        f"## Entrada Esperada\nUma string ou conjunto de dados relevantes.\n\n"
        f"## Saída Esperada\nResultado processado conforme especificação.\n\n"
        f"## Casos de Teste\n"
        f"| # | Entrada   | Saída Esperada |\n"
        f"|---|-----------|----------------|\n"
        f"| 1 | Exemplo A | Resultado A    |\n"
        f"| 2 | Exemplo B | Resultado B    |\n"
        f"| 3 | Exemplo C | Resultado C    |\n\n"
        f"## Critérios de Avaliação\n"
        f"- [ ] Compila sem erros\n"
        f"- [ ] Casos de teste passam\n"
        f"- [ ] Código legível\n"
        f"- [ ] Boas práticas aplicadas"
    )


def simulate_certificado_output(nome: str, trilha_nome: str) -> str:
    """Simula a saída do comando /certificado <nome> <trilha>."""
    trilha = find_trilha_by_tecnologia(trilha_nome)
    hoje   = datetime.now().strftime("%d/%m/%Y")
    codigo = f"DIO-CERT-{abs(hash(nome + trilha_nome)) % 90000000 + 10000000:08X}"

    if trilha:
        badges  = "\n".join(f"🎖️ {b}" for b in trilha["badges_disponiveis"])
        detalhes = (
            f"Tecnologia: {trilha['tecnologia']}\n"
            f"Nível: {trilha['nivel']}\n"
            f"Módulos: {trilha['numero_de_modulos']}\n"
            f"XP: {trilha['xp_total']} XP\n"
        )
        nome_trilha = trilha["nome"]
    else:
        badges   = "🎖️ Conclusão de Trilha"
        detalhes = f"Trilha: {trilha_nome}\n"
        nome_trilha = trilha_nome

    return (
        f"╔══════════════════════════════════════╗\n"
        f"║   🏆 CERTIFICADO DE CONCLUSÃO 🏆     ║\n"
        f"║   Digital Innovation One — DIO       ║\n"
        f"╚══════════════════════════════════════╝\n\n"
        f"# 🎓 Certificado de Conclusão\n\n"
        f"Certificamos que **{nome}** concluiu:\n\n"
        f"## 🚀 {nome_trilha}\n\n"
        f"### Detalhes\n{detalhes}"
        f"Data de Emissão: {hoje}\n"
        f"Código: {codigo}\n\n"
        f"### Badges\n{badges}\n\n"
        f"> 'O aprendizado é a única coisa que a mente nunca se cansa.'\n"
        f"> — Leonardo da Vinci\n\n"
        f"Emitido por: DIO — Digital Innovation One"
    )
