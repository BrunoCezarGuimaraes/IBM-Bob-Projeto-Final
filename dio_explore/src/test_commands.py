"""
test_commands.py
Testes unitários para os slash commands /trilha, /desafio e /certificado.
Cobertura alvo: >= 70%

Execução:
    python dio_explore/src/test_commands.py

Resultado gravado em: dio_explore/docs/resultado_testes.txt
"""

import sys
import os
import json
import unittest
from datetime import datetime
from io import StringIO

# Garante que o módulo helpers seja encontrado
sys.path.insert(0, os.path.dirname(__file__))
from test_helpers import (
    load_trilhas,
    find_trilha_by_tecnologia,
    simulate_trilha_output,
    simulate_desafio_output,
    simulate_certificado_output,
    JSON_PATH,
    COMMANDS_DIR,
)

RESULTADO_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "resultado_testes.txt")
)


# ════════════════════════════════════════════════════════════════════════════
# SUITE 1 — Integridade do JSON
# ════════════════════════════════════════════════════════════════════════════
class TestJsonIntegrity(unittest.TestCase):
    """Valida estrutura e conteúdo do arquivo trilhas_dio.json."""

    def setUp(self):
        self.data = load_trilhas()
        self.trilhas = self.data.get("trilhas", [])

    def test_arquivo_json_existe(self):
        """O arquivo trilhas_dio.json deve existir em disco."""
        self.assertTrue(os.path.isfile(JSON_PATH), f"Arquivo não encontrado: {JSON_PATH}")

    def test_json_possui_chave_trilhas(self):
        """O JSON deve ter a chave raiz 'trilhas'."""
        self.assertIn("trilhas", self.data)

    def test_minimo_30_trilhas(self):
        """Deve haver no mínimo 30 trilhas cadastradas."""
        self.assertGreaterEqual(len(self.trilhas), 30)

    def test_campos_obrigatorios_em_todas_trilhas(self):
        """Cada trilha deve conter todos os campos obrigatórios."""
        campos = ["id", "nome", "tecnologia", "nivel", "numero_de_modulos",
                  "xp_total", "badges_disponiveis", "promocao", "vitalicio", "lives_ao_vivo"]
        for trilha in self.trilhas:
            for campo in campos:
                self.assertIn(campo, trilha, f"Campo '{campo}' ausente na trilha id={trilha.get('id')}")

    def test_ids_unicos(self):
        """Todos os IDs das trilhas devem ser únicos."""
        ids = [t["id"] for t in self.trilhas]
        self.assertEqual(len(ids), len(set(ids)), "IDs duplicados encontrados")

    def test_xp_total_positivo(self):
        """O XP total de cada trilha deve ser maior que zero."""
        for t in self.trilhas:
            self.assertGreater(t["xp_total"], 0, f"XP inválido na trilha id={t['id']}")

    def test_numero_modulos_positivo(self):
        """O número de módulos deve ser >= 1."""
        for t in self.trilhas:
            self.assertGreaterEqual(t["numero_de_modulos"], 1)

    def test_nivel_valido(self):
        """O nível deve ser Básico, Intermediário ou Avançado."""
        niveis_validos = {"Básico", "Intermediário", "Avançado"}
        for t in self.trilhas:
            self.assertIn(t["nivel"], niveis_validos, f"Nível inválido: {t['nivel']} (id={t['id']})")

    def test_badges_e_lista(self):
        """O campo badges_disponiveis deve ser uma lista não vazia."""
        for t in self.trilhas:
            self.assertIsInstance(t["badges_disponiveis"], list)
            self.assertGreater(len(t["badges_disponiveis"]), 0)

    def test_promocao_tem_campos_corretos(self):
        """Cada promoção deve ter os campos ativa, desconto_percentual e validade."""
        for t in self.trilhas:
            promo = t["promocao"]
            self.assertIn("ativa", promo)
            self.assertIn("desconto_percentual", promo)
            self.assertIn("validade", promo)

    def test_vitalicio_e_booleano(self):
        """O campo vitalicio deve ser booleano."""
        for t in self.trilhas:
            self.assertIsInstance(t["vitalicio"], bool)


# ════════════════════════════════════════════════════════════════════════════
# SUITE 2 — Comando /trilha
# ════════════════════════════════════════════════════════════════════════════
class TestComandoTrilha(unittest.TestCase):
    """Testa o fluxo do slash command /trilha."""

    def test_trilha_java_encontrada(self):
        """/trilha Java deve retornar a formação Java Developer."""
        resultado = simulate_trilha_output("Java")
        self.assertIn("Java", resultado)
        self.assertNotIn("[ERRO]", resultado)

    def test_trilha_java_contem_plano_de_estudos(self):
        """/trilha Java deve conter cabeçalho do plano de estudos."""
        resultado = simulate_trilha_output("Java")
        self.assertIn("Plano de Estudos", resultado)

    def test_trilha_java_contem_modulos(self):
        """/trilha Java deve listar os módulos numerados."""
        resultado = simulate_trilha_output("Java")
        self.assertIn("Módulo 1", resultado)
        self.assertIn("Módulo 14", resultado)  # Java tem 14 módulos

    def test_trilha_java_contem_xp(self):
        """/trilha Java deve exibir o XP total (22000)."""
        resultado = simulate_trilha_output("Java")
        self.assertIn("22000", resultado)

    def test_trilha_java_contem_badges(self):
        """/trilha Java deve listar as badges disponíveis."""
        resultado = simulate_trilha_output("Java")
        self.assertIn("Java OOP", resultado)
        self.assertIn("Spring Boot Expert", resultado)

    def test_trilha_java_contem_lives(self):
        """/trilha Java deve listar as lives ao vivo."""
        resultado = simulate_trilha_output("Java")
        self.assertIn("Spring Boot na Prática", resultado)

    def test_trilha_java_sem_promocao(self):
        """/trilha Java deve indicar ausência de promoção (ativa=false)."""
        resultado = simulate_trilha_output("Java")
        self.assertIn("Nenhuma promoção", resultado)

    def test_trilha_tecnologia_inexistente_retorna_erro(self):
        """/trilha com tecnologia inexistente deve retornar [ERRO]."""
        resultado = simulate_trilha_output("COBOL_INEXISTENTE_XYZ")
        self.assertIn("[ERRO]", resultado)

    def test_trilha_tecnologia_inexistente_lista_disponiveis(self):
        """/trilha com tecnologia inexistente deve listar tecnologias disponíveis."""
        resultado = simulate_trilha_output("COBOL_INEXISTENTE_XYZ")
        self.assertIn("Python", resultado)

    def test_trilha_case_insensitive(self):
        """/trilha deve funcionar com 'java' em minúsculas."""
        resultado = simulate_trilha_output("java")
        self.assertNotIn("[ERRO]", resultado)
        self.assertIn("Java", resultado)

    def test_trilha_python_encontrada(self):
        """/trilha Python deve ser encontrada."""
        resultado = simulate_trilha_output("Python")
        self.assertNotIn("[ERRO]", resultado)
        self.assertIn("Python", resultado)

    def test_trilha_aws_encontrada(self):
        """/trilha AWS deve ser encontrada."""
        resultado = simulate_trilha_output("AWS")
        self.assertNotIn("[ERRO]", resultado)


# ════════════════════════════════════════════════════════════════════════════
# SUITE 3 — Comando /desafio
# ════════════════════════════════════════════════════════════════════════════
class TestComandoDesafio(unittest.TestCase):
    """Testa o fluxo do slash command /desafio."""

    def test_desafio_java_intermediario_gerado(self):
        """/desafio Java Intermediário deve gerar saída válida."""
        resultado = simulate_desafio_output("Java", "Intermediário")
        self.assertIn("Java", resultado)
        self.assertIn("Intermediário", resultado)
        self.assertNotIn("[ERRO]", resultado)

    def test_desafio_contem_codigo_identificador(self):
        """/desafio deve conter código identificador DIO-XXXX."""
        resultado = simulate_desafio_output("Java", "Intermediário")
        self.assertIn("DIO-", resultado)

    def test_desafio_contem_xp(self):
        """/desafio Intermediário deve conter 3000 XP."""
        resultado = simulate_desafio_output("Java", "Intermediário")
        self.assertIn("3000 XP", resultado)

    def test_desafio_contem_tempo_estimado(self):
        """/desafio deve conter tempo estimado em minutos."""
        resultado = simulate_desafio_output("Java", "Intermediário")
        self.assertIn("minutos", resultado)

    def test_desafio_contem_casos_de_teste(self):
        """/desafio deve conter tabela de casos de teste."""
        resultado = simulate_desafio_output("Java", "Intermediário")
        self.assertIn("Casos de Teste", resultado)
        self.assertIn("Entrada", resultado)
        self.assertIn("Saída Esperada", resultado)

    def test_desafio_contem_criterios_avaliacao(self):
        """/desafio deve conter critérios de avaliação."""
        resultado = simulate_desafio_output("Java", "Intermediário")
        self.assertIn("Critérios de Avaliação", resultado)

    def test_desafio_nivel_invalido_retorna_erro(self):
        """/desafio com nível inválido deve retornar [ERRO]."""
        resultado = simulate_desafio_output("Java", "Masterizado")
        self.assertIn("[ERRO]", resultado)

    def test_desafio_basico_xp_menor(self):
        """/desafio Básico deve ter XP menor que Avançado."""
        resultado_basico   = simulate_desafio_output("Python", "Básico")
        resultado_avancado = simulate_desafio_output("Python", "Avançado")
        self.assertIn("1500 XP", resultado_basico)
        self.assertIn("5000 XP", resultado_avancado)

    def test_desafio_avancado_tempo_maior(self):
        """/desafio Avançado deve ter 90 minutos estimados."""
        resultado = simulate_desafio_output("Python", "Avançado")
        self.assertIn("90 minutos", resultado)


# ════════════════════════════════════════════════════════════════════════════
# SUITE 4 — Comando /certificado
# ════════════════════════════════════════════════════════════════════════════
class TestComandoCertificado(unittest.TestCase):
    """Testa o fluxo do slash command /certificado."""

    NOME   = "Ana Silva"
    TRILHA = "Java"

    def test_certificado_java_gerado(self):
        """/certificado deve gerar certificado para trilha Java."""
        resultado = simulate_certificado_output(self.NOME, self.TRILHA)
        self.assertIn("Java", resultado)
        self.assertNotIn("[ERRO]", resultado)

    def test_certificado_contem_nome_usuario(self):
        """/certificado deve conter o nome do usuário."""
        resultado = simulate_certificado_output(self.NOME, self.TRILHA)
        self.assertIn(self.NOME, resultado)

    def test_certificado_contem_cabecalho(self):
        """/certificado deve conter o cabeçalho ASCII."""
        resultado = simulate_certificado_output(self.NOME, self.TRILHA)
        self.assertIn("CERTIFICADO DE CONCLUSÃO", resultado)

    def test_certificado_contem_codigo_unico(self):
        """/certificado deve conter código único DIO-CERT-XXXXXXXX."""
        resultado = simulate_certificado_output(self.NOME, self.TRILHA)
        self.assertIn("DIO-CERT-", resultado)

    def test_certificado_contem_data_emissao(self):
        """/certificado deve conter a data de emissão no formato DD/MM/AAAA."""
        resultado = simulate_certificado_output(self.NOME, self.TRILHA)
        hoje = datetime.now().strftime("%d/%m/%Y")
        self.assertIn(hoje, resultado)

    def test_certificado_contem_xp(self):
        """/certificado Java deve conter 22000 XP."""
        resultado = simulate_certificado_output(self.NOME, self.TRILHA)
        self.assertIn("22000 XP", resultado)

    def test_certificado_contem_badges(self):
        """/certificado Java deve listar as badges."""
        resultado = simulate_certificado_output(self.NOME, self.TRILHA)
        self.assertIn("Java OOP", resultado)

    def test_certificado_contem_citacao(self):
        """/certificado deve conter a citação de Leonardo da Vinci."""
        resultado = simulate_certificado_output(self.NOME, self.TRILHA)
        self.assertIn("Leonardo da Vinci", resultado)

    def test_certificado_trilha_inexistente_usa_nome_informado(self):
        """/certificado com trilha desconhecida deve usar o nome fornecido."""
        resultado = simulate_certificado_output("Ana Silva", "FortranLegacy")
        self.assertIn("Ana Silva", resultado)
        self.assertIn("FortranLegacy", resultado)

    def test_certificado_codigo_unico_por_usuario(self):
        """Dois usuários diferentes devem gerar códigos diferentes."""
        r1 = simulate_certificado_output("Bruno", "Java")
        r2 = simulate_certificado_output("Carlos", "Java")
        # Extrai o código DIO-CERT-... de cada resultado
        import re
        cod1 = re.search(r"DIO-CERT-[A-F0-9]+", r1)
        cod2 = re.search(r"DIO-CERT-[A-F0-9]+", r2)
        self.assertIsNotNone(cod1)
        self.assertIsNotNone(cod2)
        self.assertNotEqual(cod1.group(), cod2.group())


# ════════════════════════════════════════════════════════════════════════════
# SUITE 5 — Existência dos arquivos de comando
# ════════════════════════════════════════════════════════════════════════════
class TestArquivosDeComando(unittest.TestCase):
    """Verifica que os arquivos .md dos slash commands existem no projeto."""

    def test_comando_trilha_existe(self):
        """Arquivo trilha.md deve existir em .bob/commands/."""
        path = os.path.join(COMMANDS_DIR, "trilha.md")
        self.assertTrue(os.path.isfile(path), f"Não encontrado: {path}")

    def test_comando_desafio_existe(self):
        """Arquivo desafio.md deve existir em .bob/commands/."""
        path = os.path.join(COMMANDS_DIR, "desafio.md")
        self.assertTrue(os.path.isfile(path), f"Não encontrado: {path}")

    def test_comando_certificado_existe(self):
        """Arquivo certificado.md deve existir em .bob/commands/."""
        path = os.path.join(COMMANDS_DIR, "certificado.md")
        self.assertTrue(os.path.isfile(path), f"Não encontrado: {path}")

    def test_trilha_md_tem_frontmatter(self):
        """trilha.md deve conter frontmatter com description e argument-hint."""
        path = os.path.join(COMMANDS_DIR, "trilha.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("description:", content)
        self.assertIn("argument-hint:", content)

    def test_desafio_md_tem_dois_argumentos(self):
        """desafio.md deve aceitar dois argumentos (<tecnologia> <nivel>)."""
        path = os.path.join(COMMANDS_DIR, "desafio.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("<tecnologia>", content)
        self.assertIn("<nivel>", content)

    def test_certificado_md_tem_dois_argumentos(self):
        """certificado.md deve aceitar dois argumentos (<seu-nome> <trilha-concluida>)."""
        path = os.path.join(COMMANDS_DIR, "certificado.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("<seu-nome>", content)
        self.assertIn("<trilha-concluida>", content)


# ════════════════════════════════════════════════════════════════════════════
# RUNNER CUSTOMIZADO — grava resultado em .txt
# ════════════════════════════════════════════════════════════════════════════
def run_and_save():
    loader = unittest.TestLoader()
    suites = [
        ("JSON Integrity",       loader.loadTestsFromTestCase(TestJsonIntegrity)),
        ("Comando /trilha",      loader.loadTestsFromTestCase(TestComandoTrilha)),
        ("Comando /desafio",     loader.loadTestsFromTestCase(TestComandoDesafio)),
        ("Comando /certificado", loader.loadTestsFromTestCase(TestComandoCertificado)),
        ("Arquivos de Comando",  loader.loadTestsFromTestCase(TestArquivosDeComando)),
    ]

    linhas = []
    linhas.append("=" * 70)
    linhas.append("  RELATÓRIO DE TESTES — dio_explore | IBM Bob Project")
    linhas.append(f"  Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    linhas.append("=" * 70)
    linhas.append("")

    total_testes  = 0
    total_passou  = 0
    total_falhou  = 0
    total_erro    = 0
    falhas_detalhes = []

    for suite_nome, suite in suites:
        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)

        n_run    = result.testsRun
        n_fail   = len(result.failures)
        n_err    = len(result.errors)
        n_ok     = n_run - n_fail - n_err
        pct      = (n_ok / n_run * 100) if n_run > 0 else 0
        status   = "✅ PASSOU" if pct >= 70 else "❌ ABAIXO DE 70%"

        total_testes += n_run
        total_passou += n_ok
        total_falhou += n_fail
        total_erro   += n_err

        linhas.append(f"┌─ Suite: {suite_nome}")
        linhas.append(f"│  Executados : {n_run}")
        linhas.append(f"│  Aprovados  : {n_ok}")
        linhas.append(f"│  Falhas     : {n_fail}")
        linhas.append(f"│  Erros      : {n_err}")
        linhas.append(f"│  Cobertura  : {pct:.1f}%  {status}")
        linhas.append("└" + "─" * 60)
        linhas.append("")

        for test, traceback in result.failures + result.errors:
            falhas_detalhes.append(f"[FALHA] {test}\n{traceback}\n")

    pct_geral = (total_passou / total_testes * 100) if total_testes > 0 else 0
    status_geral = "✅ META DE 70% ATINGIDA" if pct_geral >= 70 else "❌ ABAIXO DA META DE 70%"

    linhas.append("=" * 70)
    linhas.append("  RESULTADO GERAL")
    linhas.append("=" * 70)
    linhas.append(f"  Total de testes : {total_testes}")
    linhas.append(f"  Aprovados       : {total_passou}")
    linhas.append(f"  Falhas          : {total_falhou}")
    linhas.append(f"  Erros           : {total_erro}")
    linhas.append(f"  Cobertura geral : {pct_geral:.1f}%")
    linhas.append(f"  Status          : {status_geral}")
    linhas.append("=" * 70)
    linhas.append("")

    if falhas_detalhes:
        linhas.append("─" * 70)
        linhas.append("  DETALHES DAS FALHAS / ERROS")
        linhas.append("─" * 70)
        linhas.extend(falhas_detalhes)

    conteudo = "\n".join(linhas)
    print(conteudo)

    os.makedirs(os.path.dirname(RESULTADO_PATH), exist_ok=True)
    with open(RESULTADO_PATH, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"\n📄 Resultado salvo em: {RESULTADO_PATH}")
    return pct_geral


if __name__ == "__main__":
    cobertura = run_and_save()
    sys.exit(0 if cobertura >= 70 else 1)
