# 🛡️ DIO Agent — Especialização em Análise de Vulnerabilidades (AppSec)

Projeto desenvolvido para o desafio prático da **DIO (Digital Innovation One)**, evoluindo o [dio-agent](https://github.com/digitalinnovationone/dio-agent) para atuar como um **Mentor de Cibersegurança e Analista de AppSec**.

---

## 📌 Visão Geral da Especialização

Em vez de fornecer respostas imediatas ou automáticas, o agente foi calibrado para conduzir análises de segurança como um profissional:
1. **Entende o contexto** antes de sugerir comandos ou correções.
2. **Avalia risco** baseado na fórmula clássica: `Risco = Impacto × Probabilidade`.
3. **Mapeia padrões** utilizando referências de mercado como **OWASP Top 10** e **MITRE ATT&CK**.
4. **Orienta a correção segura** através de exemplos refatorados e explicações conceituais.

---

## 📂 Arquivos Criados e Estrutura

```text
├── README.md                              # Documentação principal do projeto
├── AGENTS.md                              # Mapeamento e tabela de skills do agente
├── app.py                                 # Código de teste (Vulnerável vs. Mitigado)
├── agent/
│   ├── persona.md                         # Persona de Mentor de Cibersegurança
│   └── knowledge/
│       └── security-basics.md             # Base teórica (Tríade CIA, Risco, OWASP)
└── skills/
    └── vulnerability-analysis/
        ├── SKILL.md                       # Roteiro que o agente executa na análise
        └── README.md                      # Explicação da skill para humanos
```

---

## 🔬 Validação com Caso de Teste (`app.py`)

Foi implementado um cenário clássico de autenticação web com banco de dados SQLite:
* **Cenário Inseguro:** Concatenação direta de strings no comando SQL, permitindo SQL Injection clássico (`' OR '1'='1`).
* **Cenário Mitigado:** Utilização obrigatória de **consultas parametrizadas (Prepared Statements)** via marcadores `?`, neutralizando a injeção sem depender de sanitização manual.

---

## 🚀 Como Executar

1. Abra o terminal na raiz deste projeto:
   ```bash
   cd dio-agent-security
   ```
2. Inicie o harness do **Hermes**:
   ```bash
   hermes
   ```
3. Exemplo de prompt para testar a nova habilidade:
   > *"Analise o arquivo app.py e identifique se há problemas de segurança na autenticação."*
