# Guia de Apresentação do WinMind

> Slides: https://www.canva.com/design/DAGZYZspJIY/oklmQeol3FR3ev468I-Zgw/edit?ui=eyJFIjp7IkE_IjoiTiIsIlMiOiJBQUZTM2R6a0NVVSIsIlQiOjd9fQ

---

---
### Slide 05, 06, 07, 08 (6 minutos)

**Comunicação entre dois Agentes**: a forma mais simples de padrão de conversação onde dois agentes conversam entre si.<br>

**Chat Sequencial**: uma sequência de bate-papos entre dois agentes, encadeados por um mecanismo de transferência, que traz o resumo do bate-papo anterior para o contexto do próximo bate-papo.

**Grupo**: um único chat envolvendo mais de dois agentes. Uma pergunta importante no chat em grupo é: Qual agente deve ser o próximo a falar? Para dar suporte a diferentes cenários, fornecemos diferentes maneiras de organizar agentes em um chat em grupo:
Damos suporte a várias estratégias para selecionar o próximo agente: round_robin, aleatório, manual (seleção humana) e automático (padrão, usando um LLM para decidir).
Fornecemos uma maneira de restringir a seleção do próximo palestrante (veja os exemplos abaixo).

---

