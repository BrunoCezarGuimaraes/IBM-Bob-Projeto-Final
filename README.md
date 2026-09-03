# 🚀 dio_explore — Projeto Final do Bootcamp IBM Bob

> Projeto final do **Bootcamp IBM Bob: IA de Nível Empresarial para Desenvolvedores e Tech Leaders**.
> 
> Desenvolvido com o IBM Bob como copiloto de desenvolvimento, explorando seu uso na implementação, testes e documentação do projeto.

---

## 📌 Sobre o Projeto

O **dio_explore** é uma plataforma fictícia de exploração de trilhas de aprendizagem da [DIO (Digital Innovation One)](https://web.dio.me/), construída inteiramente com auxílio do **IBM Bob** durante o **Bootcamp IBM Bob: IA de Nível Empresarial para Desenvolvedores e Tech Leaders**. O projeto demonstra como uma IA pode atuar como copiloto ao longo do desenvolvimento — desde a estruturação do projeto até a implementação, escrita de testes e documentação.

A plataforma permite consultar trilhas por tecnologia, gerar desafios de código personalizados e emitir certificados fictícios de conclusão, tudo via **slash commands** do IBM Bob.

---

## 🛠️ Tecnologias e Métodos Utilizados

| Categoria | Tecnologia / Método |
|---|---|
| Linguagem | Python 3.x |
| Dados | JSON (`trilhas_dio.json` — 32 trilhas fictícias) |
| IA / Copiloto | IBM Bob (slash commands, geração de código, testes e documentação) |
| Testes | Python `unittest` — 48 testes em 5 suites (cobertura 100%) |
| Versionamento | Git + GitHub |
| Configuração | `.bobignore` para escopo de análise da IA |
| Documentação | Markdown (`DOCUMENTACAO.md`) |

---

## ⚡ Slash Commands

Comandos disponíveis diretamente no chat do IBM Bob (escopo local do projeto):

| Comando | Exemplo de uso | Descrição |
|---|---|---|
| `/trilha` | `/trilha Java` | Exibe o plano de estudos completo de uma trilha |
| `/desafio` | `/desafio Java Intermediário` | Gera um desafio de código com casos de teste |
| `/certificado` | `/certificado "Seu Nome" Java` | Emite um certificado fictício de conclusão |

---

## 📁 Estrutura do Projeto

```
IBM-Bob-Projeto-final/
├── .bobignore
├── .bob/
│   └── commands/               ← Slash commands locais do IBM Bob
│       ├── trilha.md           → /trilha
│       ├── desafio.md          → /desafio
│       └── certificado.md      → /certificado
└── dio_explore/
    ├── data/
    │   └── trilhas_dio.json    ← 32 trilhas fictícias da DIO
    ├── docs/
    │   ├── DOCUMENTACAO.md     ← Documentação completa do projeto
    │   └── resultado_testes.txt
    └── src/
        ├── test_helpers.py
        └── test_commands.py    ← 48 testes unitários
```

---

## ▶️ Como Rodar Localmente

```powershell
# Clone o repositório
git clone https://github.com/BrunoCezarGuimaraes/IBM-Bob-Projeto-Final.git
cd IBM-Bob-Projeto-Final

# Execute os testes unitários
$env:PYTHONIOENCODING = "utf-8"; python dio_explore/src/test_commands.py
```

> Não há dependências externas — apenas Python 3.x instalado é suficiente.

---

## 📊 Resultados dos Testes

```
Total de testes : 48
Aprovados       : 48
Cobertura geral : 100%  ✅ META DE 70% ATINGIDA
```

---

## 📘 Documentação Completa

Consulte [`dio_explore/docs/DOCUMENTACAO.md`](dio_explore/docs/DOCUMENTACAO.md) para a documentação detalhada com todos os prompts utilizados, modos de uso, dicas avançadas e insights para futuros profissionais.
