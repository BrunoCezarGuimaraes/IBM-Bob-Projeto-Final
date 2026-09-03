---
name: certificado
description: >-
  Gera um certificado fictício em Markdown com o nome do usuário e a trilha
  concluída
metadata:
  user-invocable: true
  disable-model-invocation: true
  argument-hint: <seu-nome> <trilha-concluida>
---

Gere um **certificado fictício de conclusão** em Markdown para o usuário, com base nas informações abaixo:

- **Nome do usuário:** $1
- **Trilha concluída:** $2

Leia o arquivo `dio_explore/data/trilhas_dio.json` e tente encontrar uma trilha cujo campo `nome` ou `tecnologia` bata com "$2". Se encontrar, use os dados reais (xp_total, numero_de_modulos, badges_disponiveis) para enriquecer o certificado. Se não encontrar, use apenas as informações fornecidas.

Gere o certificado **exatamente** no formato abaixo:

---

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║                   🏆  CERTIFICADO DE CONCLUSÃO  🏆               ║
║                                                                  ║
║                  Digital Innovation One — DIO                   ║
║                       dio_explore Project                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

# 🎓 Certificado de Conclusão

**Certificamos que:**

## $1

concluiu com êxito a trilha de estudos:

## 🚀 {nome completo da trilha encontrada ou "$2"}

---

### 📋 Detalhes da Conquista

| Campo                  | Informação                          |
|------------------------|-------------------------------------|
| 🎯 Tecnologia          | {tecnologia}                        |
| 📊 Nível               | {nivel}                             |
| 🧩 Módulos Concluídos  | {numero_de_modulos}                 |
| ⭐ XP Conquistado      | {xp_total} XP                       |
| 📅 Data de Emissão     | {data atual no formato DD/MM/AAAA}  |
| 🔐 Código do Certificado | DIO-CERT-{hash_aleatorio_8_chars} |

---

### 🏅 Badges Conquistadas

{liste cada badge do array badges_disponiveis com 🎖️ na frente, uma por linha}

---

### 💬 Mensagem de Reconhecimento

Escreva uma mensagem motivacional e personalizada para $1, reconhecendo a conquista de ter concluído a trilha de $2. Seja inspirador e mencione o impacto dessa habilidade no mercado de trabalho. (3 a 4 linhas)

---

> _"O aprendizado é a única coisa que a mente nunca se cansa, nunca tem medo e nunca se arrepende."_  
> — Leonardo da Vinci

---

**Emitido por:** DIO — Digital Innovation One  
**Plataforma:** [https://web.dio.me](https://web.dio.me)  
**Projeto:** dio_explore | IBM Bob Project

---

> ⚠️ Este é um certificado fictício gerado para fins educacionais e demonstrativos pelo projeto dio_explore.
