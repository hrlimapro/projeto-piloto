# 🍅 Pomodoro Timer com Flet

> **Projeto prático desenvolvido em dupla utilizando Python e Flet.**  
> Foco em aprendizado prático, código autoral construído linha por linha ("na mão"), versionamento colaborativo via Git/GitHub e arquitetura modular.

---

## 📌 1. Visão Geral & Filosofia do Projeto

Este projeto tem como meta a criação de um aplicativo desktop para gerenciamento de tempo baseado na metodologia Pomodoro.

> [!IMPORTANT]
> **Nota sobre Design e Decisões Estéticas:**  
> O desenvolvimento segue uma abordagem *Function First* (funcionalidade primeiro).  
> **Todas as decisões visuais e refinamentos estéticos (paleta de cores, tipografia, espaçamentos, ícones avançados e modo escuro) serão definidos exclusivamente na fase de UI/UX (Dia 6).**  
> Durante os primeiros dias, o layout servirá estritamente como esqueleto para suportar a lógica do timer, controle de estados e persistência.

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
├── .gitignore               # Arquivos ignorados pelo Git (venv, bytecode, temporários)
├── main.py                  # Ponto de entrada da aplicação Flet
├── README.md                # Documentação oficial do projeto
└── requirements.txt         # Lista de dependências Python
```

---

## ⚙️ 3. Guia de Instalação e Execução

### Pré-requisitos
- **Python 3.10+** instalado no sistema ([python.org](https://www.python.org/))
- **Git** configurado com chave SSH vinculada ao GitHub

### Passo a Passo

1. **Clonar o Repositório:**
   ```bash
   git clone git@github.com:hrlimapro/projeto-piloto.git
   cd projeto-piloto
   ```

2. **Criar o Ambiente Virtual (`venv`):**
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

## 📅 4. Cronograma Detalhado de 7 Dias (Trabalho em Dupla)

| Dia | Foco & Objetivo | Tarefas - Pessoa A | Tarefas - Pessoa B | Conexão & Integração |
| :--- | :--- | :--- | :--- | :--- |
| **Dia 1** | **Setup e Hello World** | Configurar repositório, branchs e `.gitignore` | Configurar ambiente local e rodar primeiro `main.py` | Validar fluxo de `pull`/`push` da dupla |
| **Dia 2** | **Lógica do Timer** | Classe de contagem regressiva, `tempo_atual` e método `tick()` | Layout funcional com botão de disparo | Conectar botão ao `tick()` e atualizar tela com `page.update()` |
| **Dia 3** | **Máquina de Estados** | Modelagem de estados (`Foco`, `Pausa Curta`, `Pausa Longa`) | Elementos visuais informativos de estado | O timer transiciona de estado automaticamente ao zerar |
| **Dia 4** | **Notificação & Áudio** | Lógica de disparo sonoro (`flet.Audio` / `pygame`) | Feedback de mudança de tela ao trocar de ciclo | Sincronizar término do tempo com áudio e troca de tela |
| **Dia 5** | **Persistência de Dados** | Módulo de leitura/escrita em `data/log.json` | Componente de UI para exibir histórico/ciclos do dia | Salvar ciclo concluído e atualizar a listagem |
| **Dia 6** | **🎨 Design, Estilo e UI/UX** | Lógica de pausar, retomar, reiniciar e atalhos | **Decisões estéticas:** Tema escuro, tipografia, bordas, ícones e espaçamentos | O produto ganha a identidade visual final |
| **Dia 7** | **Testes e Entrega** | Testes de estresse (múltiplos cliques, gravação contínua) | Documentação final, revisão de Pull Requests e merge na `main` | Tag de versão e entrega final do projeto |

---

## 🤝 5. Boas Práticas e Fluxo de Colaboração no Git

### Padrão de Branching
Nunca envie código diretamente para a branch `main`. Crie uma branch para a tarefa do dia:
```bash
# Exemplo para a Pessoa A no Dia 2
git checkout -b feature/dia2-timer-logic

# Exemplo para a Pessoa B no Dia 2
git checkout -b feature/dia2-timer-ui
```

### Padrão de Commits
Escreva mensagens de commit claras e no padrão convencional:
- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `refactor:` Melhoria de código sem alterar comportamento
- `docs:` Alterações na documentação
- `style:` Formatação visual/estética

Exemplo:
```bash
git add .
git commit -m "feat: implementa metodo tick na classe Pomodoro"
```

### Submissão e Integração (Pull Request)
1. Envie sua branch para o GitHub:
   ```bash
   git push -u origin feature/dia2-timer-logic
   ```
2. Abra um **Pull Request (PR)** no GitHub direcionado à `main`.
3. O parceiro de dupla revisa o código antes do merge.
4. Após o merge, ambos atualizam suas cópias locais:
   ```bash
   git checkout main
   git pull origin main
   ```

---

## 📝 6. Regras e Convenções do Código

- **Código Limpo:** Manter o `main.py` organizado e enxuto.
- **Separação de Responsabilidades:** Lógica de negócio e dados separados da interface visual.
- **Dados:** O arquivo `log.json` deve ser manipulado exclusivamente via funções utilitárias.
