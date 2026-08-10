# 🍅 Pomodoro Timer com Flet

> **Projeto prático desenvolvido em dupla utilizando Python e Flet.**  
> Foco em aprendizado prático, código autoral construído linha por linha ("na mão"), versionamento colaborativo via Git/GitHub e entrega acelerada em 5 dias (Segunda a Sexta).

---

## 📌 1. Visão Geral & Filosofia do Projeto

Este projeto tem como meta a criação de um aplicativo desktop para gerenciamento de tempo baseado na metodologia Pomodoro, entregue em um ciclo rápido de 5 dias.

> [!IMPORTANT]
> **Nota sobre Design e Decisões Estéticas:**  
> O desenvolvimento segue a abordagem *Function First* (funcionalidade primeiro).  
> **Todas as decisões visuais e refinamentos estéticos (paleta de cores, tipografia, espaçamentos, ícones e modo escuro) serão tomadas na quinta-feira (Dia 4).**  
> De segunda a quarta-feira, a interface servirá estritamente como esqueleto funcional para suportar o timer, estados e persistência.

---

## 📁 2. Estrutura do Repositório

```text
projeto-piloto/
│
├── assets/                  # Recursos estáticos (áudios, ícones, imagens)
│   └── audio/               # Arquivos sonoros de alarme e notificação
│
├── data/                    # Armazenamento de dados locais
│   └── log.json             # Histórico de ciclos pomodoro finalizados
│
├── tests/                   # Testes unitários da lógica
│   └── test_placeholder.py # Teste base inicial
│
├── .github/                 # Templates do GitHub (Pull Requests)
│   └── PULL_REQUEST_TEMPLATE.md
│
├── .gitignore               # Arquivos ignorados pelo Git (venv, bytecode, temporários)
├── CONTRIBUTING.md          # Guia prático de Git e fluxo de PRs da dupla
├── main.py                  # Ponto de entrada da aplicação Flet
├── README.md                # Documentação oficial do projeto
├── requirements.txt         # Lista de dependências Python
└── TEST_PLAN.md             # Matriz de testes dia a dia e cenários de estresse
```

---

## ⚙️ 3. Guia de Instalação e Execução

### Pré-requisitos
- **Python 3.10+** instalado ([python.org](https://www.python.org/))
- **Git** configurado com SSH no GitHub

### Passo a Passo

1. **Clonar o Repositório:**
   ```bash
   git clone git@github.com:hrlimapro/projeto-piloto.git
   cd projeto-piloto
   ```

2. **Criar e Ativar o Ambiente Virtual (`venv`):**
   - **No Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **No Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar a Aplicação:**
   ```bash
   python main.py
   ```

---

## 📅 4. Cronograma de 5 Dias (Segunda a Sexta-feira)

| Dia | Foco & Objetivo | Tarefas - Pessoa A | Tarefas - Pessoa B | Conexão & Integração |
| :--- | :--- | :--- | :--- | :--- |
| **Dia 1 (Seg)** | **Setup, Git & Timer Básico** | Setup de Git e classe Pomodoro (`tempo_atual`, `tick()`) | Layout Flet inicial com botão "Iniciar" | Botão dispara o timer e atualiza a tela com `page.update()` |
| **Dia 2 (Ter)** | **Máquina de Estados & Controles** | Lógica de ciclos (`Foco 25m`, `Pausa 5m`, `Pausa Longa 15m`) | Botões de Pausar, Retomar e Resetar + Indicador de estado | Timer transiciona de ciclo e responde aos comandos de controle |
| **Dia 3 (Qua)** | **Persistência, Áudio & Histórico** | Módulo de leitura/gravação em `data/log.json` | Disparo de som (`flet.Audio`/`pygame`) ao zerar + Modal de histórico | Ao zerar o foco, toca o alarme, salva o ciclo e exibe no modal |
| **Dia 4 (Qui)** | **🎨 Design, UI/UX & Refinamento** | Cores contextuais por estado (tom foco vs pausa) e atalhos | **Decisões estéticas:** Tema escuro, tipografia, ícones (`ft.icons`) e bordas | O app ganha a identidade visual completa e polida |
| **Dia 5 (Sex)** | **Testes de Estresse & Entrega** | Testes de estresse (múltiplos cliques, pausa no zero, JSON) | Revisão final de PRs, documentação e merge na `main` | **Entrega final do projeto concluída!** |

---

## 🤝 5. Boas Práticas e Fluxo Git & GitHub

> [!TIP]
> O passo a passo completo de branches, abertura de PRs, revisão de código e resolução de conflitos está documentado no **[CONTRIBUTING.md](file:///c:/projetos-pessoais/projeto-piloto/CONTRIBUTING.md)**.

### Resumo do Fluxo Diário
1. Atualize sua `main`: `git checkout main && git pull origin main`
2. Crie sua branch: `git checkout -b feature/diaX-nome-da-tarefa`
3. Codifique, teste localmente e comite: `git commit -m "feat: descricao"`
4. Envie para o GitHub: `git push -u origin feature/diaX-nome-da-tarefa`
5. Abra o **Pull Request** no GitHub para aprovação do parceiro.

---

## 🧪 6. Plano de Testes & Qualidade

- **Matriz de Testes Completa:** Consulte o arquivo **[TEST_PLAN.md](file:///c:/projetos-pessoais/projeto-piloto/TEST_PLAN.md)** para os critérios de aceitação e testes de estresse antes de aprovar cada Pull Request.
- **Execução dos Testes Unitários:**
  ```bash
  pytest
  ```

---

## 📝 7. Regras e Convenções do Código

- **Código Limpo:** Manter o `main.py` organizado e modular.
- **Separação de Responsabilidades:** Lógica matemática e gravação de arquivos separadas dos componentes visuais Flet.
- **Manipulação de Dados:** O arquivo `log.json` deve ser manipulado exclusivamente via funções utilitárias seguras.
