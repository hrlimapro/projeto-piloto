# 🧪 Plano de Testes - Pomodoro Timer (5 Dias)

Documento de referência para garantir a qualidade, estabilidade e conformidade da aplicação durante o ciclo de 5 dias (Segunda a Sexta-feira).

---

## 🎯 1. Estratégia de Testes

1. **Testes Unitários Automatizados (Lógica Pura):**
   - Executados localmente com `pytest`.
   - Cobrem o decremento de tempo, troca de estados, contagem de ciclos e persistência em `log.json`.

2. **Testes Manuais de Interface & Integração (Flet UI & Áudio):**
   - Validados localmente pela dupla antes de abrir e aprovar Pull Requests.
   - Cobrem visualização, botões de controle, reprodução de sons e ausência de travamentos.

---

## 📅 2. Matriz de Testes por Etapa (5 Dias)

### 🔹 Dia 1 (Segunda): Setup & Timer Básico
- [ ] **T01 - Execução do App:** O comando `python main.py` abre a janela Flet sem erros no terminal.
- [ ] **T02 - Dependências:** `pip install -r requirements.txt` instala todos os pacotes no `venv`.
- [ ] **T03 - Decremento (Unitário):** O método `tick()` reduz exatamente 1 segundo do tempo restante.
- [ ] **T04 - Disparo na UI:** Ao clicar em "Iniciar", o texto do cronômetro decrementa a cada segundo via `page.update()`.

### 🔹 Dia 2 (Terça): Máquina de Estados & Controles (Pause/Reset)
- [ ] **T05 - Transição Automática:** Ao atingir `00:00` no Foco (25 min), o estado muda para Pausa Curta (5 min).
- [ ] **T06 - Ciclo Completo:** Após 4 ciclos de Foco, o próximo estado de descanso é a Pausa Longa (15 min).
- [ ] **T07 - Pausar e Retomar:** O botão "Pausar" congela a contagem no segundo exato; "Retomar" continua sem saltos.
- [ ] **T08 - Reiniciar (Reset):** O botão "Reiniciar" restaura o timer para o tempo inicial do ciclo atual.

### 🔹 Dia 3 (Quarta): Persistência de Dados & Áudio
- [ ] **T09 - Alarme Sonoro:** O áudio toca no momento exato em que o timer atinge `00:00`.
- [ ] **T10 - Não Bloqueante:** A reprodução do som não congela nem trava a interface gráfica.
- [ ] **T11 - Gravação do Ciclo:** Ao concluir um ciclo de foco, um novo registro é salvo em `data/log.json`.
- [ ] **T12 - Modal/Aba de Histórico:** A visualização na tela reflete os ciclos salvos no `log.json`.

### 🔹 Dia 4 (Quinta): Design, UI/UX & Refinamento Estético
- [ ] **T13 - Decisões Visuais:** Tema escuro (Dark Mode), tipografia e ícones (`ft.icons`) aplicados.
- [ ] **T14 - Troca de Cor por Estado:** A interface altera suas cores contextualmente conforme o estado (foco vs descanso).
- [ ] **T15 - Responsividade:** A janela pode ser redimensionada sem desalinhamento dos botões ou textos.

### 🔹 Dia 5 (Sexta): Testes de Estresse & Entrega Final
- [ ] **T16 - Testes de Estresse (ST01 a ST04):** Todos os testes de estresse abaixo foram executados com sucesso.
- [ ] **T17 - Limpeza de Código:** Sem logs temporários, código morto ou branches pendentes.
- [ ] **T18 - Merge na Main:** Todas as features integradas e documentação do README revisada.

---

## ⚡ 3. Cenários de Testes de Estresse (Dia 5 - Sexta)

| ID | Cenário de Teste | Ação Executada | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **ST01** | Cliques repetidos no Iniciar | Clicar 10 vezes consecutivas no botão "Iniciar" | O timer não acelera a contagem (mantém 1 tick por segundo). |
| **ST02** | Alternância rápida Pause/Start | Clicar alternadamente em Pausar e Iniciar várias vezes | Estado permanece consistente sem travar a thread. |
| **ST03** | Fechamento durante contagem | Fechar a janela com o timer rodando | A aplicação encerra os processos sem deixar travamentos em segundo plano. |
| **ST04** | Arquivo `log.json` corrompido | Inserir texto inválido manualmente no `log.json` | O app trata a exceção com segurança e recupera o arquivo. |

---

## 🚀 4. Como Executar os Testes Automatizados

```bash
# Executar todos os testes
pytest

# Executar com detalhes de saída
pytest -v
```
