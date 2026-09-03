# 📘 Documentação Completa — dio_explore

> **Projeto:** dio_explore — Plataforma de Exploração de Trilhas DIO  
> **Repositório:** IBM-Bob-Projeto-final  
> **Bootcamp:** IBM Bob: IA de Nível Empresarial para Desenvolvedores e Tech Leaders  
> **Ferramenta principal:** IBM Bob (IA assistente de desenvolvimento)  
> **Autor:** Bruno Cezar Guimarães  

---

## 📌 Índice

1. [Visão Geral do Projeto](#1-visão-geral-do-projeto)
2. [Estrutura de Arquivos](#2-estrutura-de-arquivos)
3. [Etapas de Construção e Prompts Utilizados](#3-etapas-de-construção-e-prompts-utilizados)
4. [Slash Commands — Referência Completa](#4-slash-commands--referência-completa)
5. [Dados — trilhas_dio.json](#5-dados--trilhas_diojson)
6. [Testes Unitários](#6-testes-unitários)
7. [Configurações do Projeto (.bobignore)](#7-configurações-do-projeto-bobignore)
8. [Modos de Uso do IBM Bob](#8-modos-de-uso-do-ibm-bob)
9. [Dicas de Uso Avançado](#9-dicas-de-uso-avançado)
10. [Insights para Futuros Profissionais](#10-insights-para-futuros-profissionais)
11. [Glossário](#11-glossário)

---

## 1. Visão Geral do Projeto

O **dio_explore** é uma plataforma fictícia de exploração de trilhas de aprendizagem da DIO (Digital Innovation One), construída inteiramente com apoio do IBM Bob durante o Bootcamp. O projeto demonstra como um assistente de IA pode ser usado como copiloto de desenvolvimento real — desde a criação da estrutura de pastas até testes unitários e documentação.

### Objetivos alcançados

| Objetivo | Status |
|---|---|
| Criar estrutura de projeto organizada | ✅ |
| Popular base de dados JSON com trilhas fictícias | ✅ |
| Criar slash commands reutilizáveis para o Bob | ✅ |
| Configurar regras de ignore do Bob | ✅ |
| Escrever e executar testes unitários (≥ 70%) | ✅ 100% |
| Documentar todo o projeto | ✅ |

---

## 2. Estrutura de Arquivos

```
IBM-Bob-Projeto-final/
│
├── .bobignore                          ← Regras de ignore do IBM Bob
├── Hello World.md                      ← Arquivo original do repositório clonado
├── LICENSE                             ← Licença do repositório
├── README.md                           ← Descrição geral do projeto
│
├── .bob/
│   └── commands/                       ← Slash commands locais (escopo do projeto)
│       ├── trilha.md                   → /trilha <tecnologia>
│       ├── desafio.md                  → /desafio <tecnologia> <nivel>
│       └── certificado.md             → /certificado <nome> <trilha>
│
└── dio_explore/
    ├── commands/                       ← (reservado para scripts futuros)
    ├── data/
    │   └── trilhas_dio.json            ← 32 trilhas fictícias da DIO
    ├── docs/
    │   ├── DOCUMENTACAO.md             ← Este arquivo
    │   └── resultado_testes.txt        ← Relatório de execução dos testes
    ├── mcp/                            ← (reservado para integrações MCP)
    └── src/
        ├── test_helpers.py             ← Simuladores e utilitários de teste
        └── test_commands.py            ← 48 testes unitários em 5 suites
```

---

## 3. Etapas de Construção e Prompts Utilizados

Esta seção documenta **cada prompt real utilizado** durante a construção do projeto, na ordem em que foram executados. Serve como guia de reprodução e aprendizado.

---

### Etapa 1 — Criar a estrutura de pastas

**Prompt utilizado:**
```
Bob, eu quero que você entre dentro da pasta recentemente clonada
("/Documents/IBM-Bob-Projeto-final) e crie a seguinte estrutura de projeto
"dio_explore" dentro vai ter que ter pastas como src, data, commands, mcp e docs.
```

**O que o Bob fez:**
- Identificou o repositório clonado em `C:\Users\bruno\Documents\IBM-Bob-Projeto-final`
- Criou a pasta raiz `dio_explore/` e as 5 subpastas (`src`, `data`, `commands`, `mcp`, `docs`) com um único comando PowerShell usando `New-Item`

**Comando gerado pelo Bob:**
```powershell
New-Item -ItemType Directory -Path "dio_explore\src", "dio_explore\data",
  "dio_explore\commands", "dio_explore\mcp", "dio_explore\docs" -Force
```

---

### Etapa 2 — Criar o arquivo de dados

**Prompt utilizado:**
```
dentro da pasta data, quero que crie um arquivo chamado trilhas_dio.json
```

**O que o Bob fez:**
- Criou `dio_explore/data/trilhas_dio.json` com conteúdo inicial `{}`

---

### Etapa 3 — Popular o JSON com trilhas fictícias

**Prompt utilizado:**
```
Bob, dentro do arquivo trilhas_dio.json crie uma lista extensa de pelo menos 30
trilhas fictícias da DIO (https://web.dio.me/) contendo nome, tecnologia, nivel,
numero de modulos, xp total, badges disponíveis, promoções, vitalício, e lives ao vivo.
```

**O que o Bob fez:**
- Criou 32 trilhas fictícias cobrindo tecnologias como Python, Java, React, AWS, Angular, Machine Learning, Docker, Vue.js, Data Science, Go, Cybersecurity, Flutter, Azure, TypeScript, Kotlin, SQL, Git, IBM Watson, .NET, Ruby, Rust, DevOps, Blockchain, Figma, PHP, Google Cloud, Next.js, Swift, IA Generativa, Multi-Cloud e QA
- Cada trilha contém todos os 9 campos solicitados com dados realistas e coerentes

**Estrutura de cada trilha no JSON:**
```json
{
  "id": 4,
  "nome": "Formação Java Developer",
  "tecnologia": "Java",
  "nivel": "Intermediário",
  "numero_de_modulos": 14,
  "xp_total": 22000,
  "badges_disponiveis": ["Java OOP", "Spring Boot Expert", "Java Developer"],
  "promocao": { "ativa": false, "desconto_percentual": 0, "validade": null },
  "vitalicio": true,
  "lives_ao_vivo": ["Spring Boot na Prática", "APIs REST com Java"]
}
```

---

### Etapa 4 — Criar o .bobignore

**Prompt utilizado:**
```
Bob crie agora um arquivo .bobignore na raiz do projeto. Dentro deste bobignore
quero que ele ignore as pastas node_modules, arquivos .env, pasta como
data/cache-progresso, e certificados gerados doc/certificados-emitidos e
quaisquer outros arquivos com extensão .tmp
```

**O que o Bob fez:**
- Criou `.bobignore` na raiz do repositório com 5 regras de ignore
- Incluiu variações de `.env` (`.env.*`) para cobrir `.env.local`, `.env.production`, etc.

---

### Etapa 5 — Criar os Slash Commands

**Prompt utilizado:**
```
Bob crie um slash command dentro do projeto que possa ser invocado pelo comando
/trilha [...] vai receber o nome de uma tecnologia e retornar, a partir do arquivo
data/trilhas.json, um plano de estudos formado com os módulos daquela trilha.
Depois crie o mesmo slash command que possa ser invocado a partir do comando
/desafio e ele ao ser invocado vai gerar um desafio de código aleatório baseado
no nível e tecnologia escolhido pelo usuário. Crie outro slash command a partir
do chamado /certificado que vai gerar um certificado fictício em markdown com
nome do usuário e a trilha que ele completou. Todos esses slash commands têm que
ficar armazenados de forma local, para serem executados apenas neste projeto.
```

**O que o Bob fez:**
- Consultou a documentação oficial do IBM Bob antes de criar os arquivos
- Criou os 3 arquivos `.md` em `.bob/commands/` com frontmatter correto (`description` + `argument-hint`)
- Cada comando usa `$1`, `$2` para referenciar os argumentos passados pelo usuário

---

### Etapa 6 — Criar testes unitários

**Prompt utilizado:**
```
Bob crie arquivos de testes unitários e teste este fluxo para atingir uma
cobertura de 70% de aprovação. Teste os comandos /trilha para consultar trilhas
de JAVA, gere um arquivo de /desafio para o aluno e um /certificado para o mesmo.
Grave os resultados em um arquivo txt para acompanhá-los.
```

**O que o Bob fez:**
- Criou `test_helpers.py` com simuladores Python dos três comandos
- Criou `test_commands.py` com 48 testes unitários distribuídos em 5 suites
- Identificou e corrigiu bug de ambiguidade na busca (Java vs JavaScript)
- Implementou runner customizado que grava relatório em `resultado_testes.txt`
- Resultado final: **100% de aprovação (48/48 testes)**

---

## 4. Slash Commands — Referência Completa

Os slash commands ficam em `.bob/commands/` e são **exclusivos deste projeto** (escopo local). Para comandos globais, use `~/.bob/commands/`.

---

### `/trilha <tecnologia>`

**Arquivo:** `.bob/commands/trilha.md`  
**Descrição:** Busca uma trilha pelo nome da tecnologia e exibe um plano de estudos completo.

**Como usar:**
```
/trilha Python
/trilha Java
/trilha Machine Learning
/trilha AWS
```

**O que retorna:**
- Nome e metadados da trilha (nível, módulos, XP, acesso vitalício)
- Lista numerada de módulos com XP estimado por módulo
- Badges disponíveis para conquistar
- Lives ao vivo cadastradas
- Status de promoção (desconto e validade)
- Mensagem motivacional

**Comportamento de busca:**
- Case-insensitive: `/trilha python` = `/trilha Python`
- Match exato tem prioridade sobre substring (evita "Java" retornar "JavaScript")
- Se a tecnologia não for encontrada, lista todas as disponíveis

---

### `/desafio <tecnologia> <nivel>`

**Arquivo:** `.bob/commands/desafio.md`  
**Descrição:** Gera um desafio de código aleatório e criativo com enunciado, casos de teste e critérios de avaliação.

**Como usar:**
```
/desafio Java Intermediário
/desafio Python Básico
/desafio React Avançado
/desafio TypeScript Intermediário
```

**Níveis aceitos:** `Básico` | `Intermediário` | `Avançado`

**O que retorna:**
- Código identificador único do desafio (ex: `DIO-4721`)
- Tempo estimado de resolução
- XP a ser ganho ao concluir
- Enunciado contextualizado com caso de negócio real
- Formato de entrada e saída esperados
- 3 casos de teste em tabela
- Checklist de critérios de avaliação

**XP por nível:**
| Nível | XP | Tempo |
|---|---|---|
| Básico | 1.500 XP | 30 min |
| Intermediário | 3.000 XP | 60 min |
| Avançado | 5.000 XP | 90 min |

---

### `/certificado <seu-nome> <trilha-concluida>`

**Arquivo:** `.bob/commands/certificado.md`  
**Descrição:** Gera um certificado fictício de conclusão em Markdown com todos os detalhes da conquista.

**Como usar:**
```
/certificado "Bruno Oliveira" Java
/certificado "Ana Silva" Python
/certificado "Carlos Souza" "Machine Learning"
```

**O que retorna:**
- Header ASCII artístico do certificado
- Nome do aluno em destaque
- Nome completo da trilha concluída
- Tabela de detalhes: tecnologia, nível, módulos, XP, data de emissão
- Código único de certificado (`DIO-CERT-XXXXXXXX`)
- Lista de badges conquistadas
- Mensagem motivacional personalizada
- Citação de Leonardo da Vinci

> ⚠️ **Aviso:** Este é um certificado fictício gerado para fins educacionais e demonstrativos.

---

## 5. Dados — trilhas_dio.json

**Localização:** `dio_explore/data/trilhas_dio.json`

### Estatísticas do dataset

| Métrica | Valor |
|---|---|
| Total de trilhas | 32 |
| Trilhas com promoção ativa | 16 |
| Trilhas com acesso vitalício | 22 |
| Nível Básico | 8 trilhas |
| Nível Intermediário | 15 trilhas |
| Nível Avançado | 9 trilhas |
| Maior XP | 32.000 XP (Multi-Cloud) |
| Menor XP | 7.500 XP (Git) |
| Maior desconto | 50% (AWS e IA Generativa) |

### Tecnologias cobertas

Python, JavaScript, React, Java, AWS, Angular, Machine Learning, DevOps (Docker/Kubernetes), Vue.js, Data Science, Go, Cybersecurity, Flutter, Azure, TypeScript, Kotlin, SQL, Git, IBM Watson/IA, .NET/C#, Ruby, Rust, CI/CD, Blockchain/Solidity, UX/UI Design, PHP/Laravel, Google Cloud, Next.js, Swift, IA Generativa/LLMs, Multi-Cloud, QA/Cypress.

### Schema completo

```typescript
interface Trilha {
  id: number;                      // Identificador único
  nome: string;                    // Nome completo da formação
  tecnologia: string;              // Tecnologia principal
  nivel: "Básico" | "Intermediário" | "Avançado";
  numero_de_modulos: number;       // Quantidade de módulos
  xp_total: number;                // XP total ao completar
  badges_disponiveis: string[];    // Badges que podem ser conquistadas
  promocao: {
    ativa: boolean;
    desconto_percentual: number;   // 0 se não ativa
    validade: string | null;       // Formato: "YYYY-MM-DD"
  };
  vitalicio: boolean;              // Acesso permanente ao conteúdo
  lives_ao_vivo: string[];         // Lives disponíveis na trilha
}
```

---

## 6. Testes Unitários

### Arquivos de teste

| Arquivo | Função |
|---|---|
| `src/test_helpers.py` | Simuladores dos comandos + utilitários de busca no JSON |
| `src/test_commands.py` | 48 testes em 5 suites + runner com geração de relatório |

### Como executar

```powershell
# Na raiz do repositório
$env:PYTHONIOENCODING = "utf-8"; python dio_explore/src/test_commands.py
```

### Resultado da última execução

```
Total de testes : 48
Aprovados       : 48
Falhas          : 0
Erros           : 0
Cobertura geral : 100.0%
Status          : ✅ META DE 70% ATINGIDA
```

### Suites de teste

| Suite | Testes | O que valida |
|---|---|---|
| `TestJsonIntegrity` | 11 | Estrutura e integridade do JSON (campos, tipos, unicidade de IDs) |
| `TestComandoTrilha` | 12 | Busca por Java, badges, lives, XP, promoção, case-insensitive, tecnologia inexistente |
| `TestComandoDesafio` | 9 | Geração do desafio, XP por nível, tempo, casos de teste, nível inválido |
| `TestComandoCertificado` | 10 | Nome do usuário, header, código único, data, XP, badges, unicidade por aluno |
| `TestArquivosDeComando` | 6 | Existência dos .md, frontmatter correto, argumentos nos 3 comandos |

### Bug encontrado e corrigido durante os testes

**Problema:** A busca por "Java" retornava "JavaScript" (que aparece antes no JSON) porque usava match por substring simples.

**Solução implementada em `test_helpers.py`:**
```python
# 1ª passagem: match exato (case-insensitive)
for trilha in data.get("trilhas", []):
    if trilha["tecnologia"].lower() == termo:
        return trilha
# 2ª passagem: fallback por substring
for trilha in data.get("trilhas", []):
    if termo in trilha["tecnologia"].lower():
        return trilha
```

---

## 7. Configurações do Projeto (.bobignore)

O arquivo `.bobignore` na raiz do repositório instrui o IBM Bob a **ignorar** certos caminhos ao analisar o projeto.

```gitignore
# Dependências
node_modules/

# Variáveis de ambiente
.env
.env.*

# Cache de progresso
data/cache-progresso/

# Certificados gerados
docs/certificados-emitidos/

# Arquivos temporários
*.tmp
```

**Por que cada regra existe:**

| Regra | Motivo |
|---|---|
| `node_modules/` | Evita que o Bob analise milhares de arquivos de dependências |
| `.env` e `.env.*` | Protege credenciais e segredos de ambiente |
| `data/cache-progresso/` | Evita análise de cache gerado automaticamente |
| `docs/certificados-emitidos/` | Certificados são output, não source code |
| `*.tmp` | Arquivos temporários não fazem parte da base de código |

---

## 8. Modos de Uso do IBM Bob

Durante a construção deste projeto, o IBM Bob foi utilizado em diferentes capacidades:

### Como Engenheiro de Infraestrutura
- Criação de estrutura de pastas via PowerShell
- Configuração de `.bobignore`

### Como Engenheiro de Dados
- Geração do dataset `trilhas_dio.json` com 32 registros realistas
- Design do schema com todos os campos necessários

### Como Arquiteto de Features
- Design e implementação dos 3 slash commands
- Consulta à documentação oficial do Bob antes de criar os arquivos

### Como Engenheiro de QA
- Criação de 48 testes unitários distribuídos em 5 suites
- Identificação e correção do bug de ambiguidade na busca
- Geração automática de relatório de cobertura

### Como Technical Writer
- Documentação completa do projeto
- Geração de one-pager HTML para compartilhamento

---

## 9. Dicas de Uso Avançado

### Dica 1 — Slash commands com argumentos compostos
Se o argumento contém espaços (ex: nome completo), use aspas:
```
/certificado "Maria Fernanda" "Machine Learning"
```

### Dica 2 — Testar a busca de tecnologias
O comando `/trilha` aceita partes do nome da tecnologia:
```
/trilha cloud    → pode retornar AWS, Azure, Google Cloud ou Multi-Cloud
/trilha devops   → retorna Docker/Kubernetes ou CI/CD
```

### Dica 3 — Re-executar testes após mudanças no JSON
Sempre que adicionar novas trilhas ao `trilhas_dio.json`, re-execute os testes:
```powershell
$env:PYTHONIOENCODING = "utf-8"; python dio_explore/src/test_commands.py
```

### Dica 4 — Escopo de slash commands
- **Local** (`.bob/commands/`): visível apenas neste projeto
- **Global** (`~/.bob/commands/`): visível em todos os projetos

Para promover um comando de local para global, basta copiar o `.md` para `~/.bob/commands/`.

### Dica 5 — Extender os slash commands
Para adicionar novos campos à resposta do `/trilha`, edite `trilha.md` e adicione instruções ao prompt. Exemplo: adicionar uma seção de "pré-requisitos recomendados".

### Dica 6 — Encadeamento de comandos
Use os três comandos em sequência para simular uma jornada completa:
```
1. /trilha Java           → veja o plano de estudos
2. /desafio Java Intermediário  → receba um desafio prático
3. /certificado "Seu Nome" Java → emita seu certificado
```

---

## 10. Insights para Futuros Profissionais

Esta seção reúne aprendizados e reflexões para quem vai estudar este projeto como referência.

---

### 💡 IA como Copiloto, não como Substituto

O IBM Bob foi usado como acelerador: ele gerou código, identificou bugs e escreveu documentação — mas todas as decisões de design, estrutura e requisitos vieram do desenvolvedor. A IA amplifica sua produtividade, não substitui seu pensamento crítico.

---

### 💡 Prompts precisos = resultados melhores

Compare:
- ❌ "Crie um arquivo de dados"
- ✅ "Crie um arquivo trilhas_dio.json com pelo menos 30 trilhas contendo os campos: nome, tecnologia, nivel, numero_de_modulos, xp_total, badges_disponiveis, promocao, vitalicio, lives_ao_vivo"

Quanto mais específico e estruturado for o prompt, mais próximo o resultado estará do esperado — e menos iterações você precisará fazer.

---

### 💡 Teste antes de confiar

O projeto atingiu 100% de cobertura, mas o caminho incluiu falhas reais. Os testes revelaram um bug de busca ambígua (Java vs JavaScript) que passaria despercebido em uso manual. **Testes automatizados são o contrato de confiança do seu código.**

---

### 💡 Estrutura de projeto importa desde o início

Criar a estrutura correta de pastas (`src`, `data`, `docs`, `commands`, `mcp`) antes de qualquer código economizou reorganizações futuras. Projetos bem estruturados são mais fáceis de manter, documentar e colaborar.

---

### 💡 Slash commands são ferramentas de padronização de time

Os slash commands do Bob não são apenas atalhos pessoais — são **padrões de processo documentados em código**. Uma equipe que usa `/trilha`, `/desafio` e `/certificado` garante que todos seguem o mesmo fluxo, independente do desenvolvedor.

---

### 💡 .bobignore é parte da segurança do projeto

Ignorar `.env` e `node_modules` não é só organização — é segurança. Credenciais nunca devem ser processadas pela IA. Crie sempre seu `.bobignore` antes de começar a trabalhar.

---

### 💡 Documentação é parte do produto

Este arquivo `DOCUMENTACAO.md` foi gerado com o mesmo cuidado que o código. Profissionais que documentam bem são mais valorizados porque permitem que outros (e eles mesmos no futuro) entendam e evoluam o trabalho.

---

### 💡 O erro é parte do processo

Na primeira execução dos testes, 6 de 48 falharam. Isso é normal e esperado. O processo de **executar → identificar → corrigir → re-executar** é o ciclo de qualidade de qualquer engenheiro de software sênior.

---

## 11. Glossário

| Termo | Definição |
|---|---|
| **IBM Bob** | Assistente de IA da IBM para desenvolvimento de software, integrado à IDE |
| **Slash Command** | Comando iniciado com `/` que executa uma instrução pré-definida no Bob |
| **Frontmatter** | Bloco YAML no topo de um arquivo Markdown delimitado por `---`, usado para metadados |
| **.bobignore** | Arquivo de configuração que instrui o Bob a ignorar certos arquivos/pastas |
| **dio_explore** | Nome do projeto criado neste bootcamp |
| **DIO** | Digital Innovation One — plataforma brasileira de educação em tecnologia |
| **XP** | Experience Points — pontuação de experiência ao completar conteúdos na DIO |
| **Badge** | Conquista/insígnia digital obtida ao completar etapas de uma trilha |
| **Suite de testes** | Grupo de testes relacionados que validam uma funcionalidade específica |
| **Cobertura de testes** | Percentual de funcionalidades cobertas por testes automatizados |
| **Match exato** | Comparação onde o texto deve ser idêntico (ex: "Java" = "Java") |
| **Match substring** | Comparação onde um texto é contido em outro (ex: "Java" em "JavaScript") |
| **MCP** | Model Context Protocol — protocolo para integrar ferramentas externas ao Bob |
| **Bootcamp** | Programa intensivo de aprendizagem prática em tecnologia |

---

*Documentação gerada com IBM Bob — dio_explore Project*  
*Bootcamp: IBM Bob: IA de Nível Empresarial para Desenvolvedores e Tech Leaders*
