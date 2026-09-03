---
name: trilha
description: >-
  Busca uma trilha da DIO pelo nome da tecnologia e exibe o plano de estudos
  formatado
metadata:
  user-invocable: true
  disable-model-invocation: true
  argument-hint: <tecnologia>
---

Leia o arquivo `dio_explore/data/trilhas_dio.json` deste projeto.

Busque a trilha cujo campo `tecnologia` contenha (busca case-insensitive) o valor "$1".

Se não encontrar nenhuma trilha com essa tecnologia, informe educadamente que a tecnologia "$1" não foi encontrada no arquivo e liste todas as tecnologias disponíveis no JSON.

Se encontrar, exiba o plano de estudos formatado em Markdown da seguinte forma:

---

# 📚 Plano de Estudos — {nome da trilha}

**🎯 Tecnologia:** {tecnologia}  
**📊 Nível:** {nivel}  
**🧩 Total de Módulos:** {numero_de_modulos}  
**⭐ XP Total:** {xp_total} XP  
**♾️ Acesso Vitalício:** Sim / Não  

---

## 🗂️ Módulos da Trilha

Liste os módulos numerados de 1 até {numero_de_modulos}, com títulos criativos e coerentes com a tecnologia. Cada módulo deve ter:
- Um título descritivo
- Uma breve descrição (1 linha) do que será aprendido
- A XP estimada para aquele módulo (divida o xp_total igualmente entre os módulos)

---

## 🏅 Badges Disponíveis

Liste cada badge do array `badges_disponiveis` com o emoji 🎖️ na frente.

---

## 🎥 Lives ao Vivo

Liste cada live do array `lives_ao_vivo` com o emoji 📡 na frente.

---

## 🏷️ Promoção

Se `promocao.ativa` for true, exiba:
> 🔥 **Promoção ativa!** {desconto_percentual}% de desconto até {validade}.

Se for false, exiba:
> ℹ️ Nenhuma promoção ativa no momento.

---

Ao final, encoraje o usuário a iniciar a trilha com uma mensagem motivacional curta.
