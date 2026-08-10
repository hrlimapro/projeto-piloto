# 🧪 Plano de Testes - Pomodoro Timer

Documento de referência para garantir a qualidade, estabilidade e conformidade da aplicação durante o desenvolvimento em dupla nos 7 dias.

---

## 🎯 1. Estratégia de Testes

A aplicação é dividida em duas camadas de validação:

1. **Testes Unitários Automatizados (Lógica Pura):**
   - Executados via `pytest`.
   - Cobrem o decremento de tempo, troca de estados, contagem de ciclos e manipulação do arquivo `log.json`.
   - Executados automaticamente a cada Push / Pull Request pelo **GitHub Actions**.

2. **Testes Manuais de Interface & Integração (Flet UI & Áudio):**
   - Validados localmente pela dupla antes de abrir e aprovar Pull Requests.
   - Cobrem renderização visual, comportamento dos botões, reprodução de sons e ausência de travamentos.

---

## 📅 2. Matriz de Testes por Etapa (Dia a Dia)

### 🔹 Dia 1: Setup & Ambiente
- [ ] **T01 - Execução do App:** O comando `python main.py` abre a janela Flet sem erros no terminal.
- [ ] **T02 - Dependências:** `pip install -r requirements.txt` instala todos os pacotes com sucesso no `venv`.

### 🔹 Dia 2: Lógica do Timer & Conexão
- [ ] **T03 - Decremento (Unitário):** O método `tick()` reduz exatamente 1 segundo do tempo restante.
- [ ] **T04 - Formatação:** A função de tempo formata corretamente segundos em `MM:SS` (ex: `1500s` -> `25:00`, `59s` -> `00:59`).
- [ ] **T05 - Disparo na UI:** Ao clicar em "Iniciar", o texto do cronômetro atualiza a cada segundo via `page.update()`.

### 🔹 Dia 3: Máquina de Estados (Foco, Pausa Curta, Pausa Longa)
- [ ] **T06 - Transição Automática:** Ao atingir `00:00` no Foco (25 min), o estado muda para Pausa Curta (5 min).
- [ ] **T07 - Ciclo Completo:** Após 4 ciclos de Foco, o próximo estado de descanso é a Pausa Longa (15-20 min).
- [ ] **T08 - Indicador Visual:** O texto da interface exibe corretamente o nome e objetivo do estado ativo.

### 🔹 Dia 4: Notificação & Áudio
- [ ] **T09 - Alarme Sonoro:** O áudio toca no momento exato em que o timer atinge `00:00`.
- [ ] **T10 - Não Bloqueante:** A reprodução do som não congela a interface gráfica.
- [ ] **T11 - Troca de Cor:** A cor/tema de fundo altera visualmente entre foco e descanso.

### 🔹 Dia 5: Persistência de Dados (`log.json`)
- [ ] **T12 - Gravação do Ciclo:** Ao concluir um ciclo de foco, um novo registro com data e contagem é salvo em `data/log.json`.
- [ ] **T13 - Arquivo Inexistente:** Se `log.json` não existir, a função deve criá-lo automaticamente sem quebrar o app.
- [ ] **T14 - Leitura no Histórico:** O modal/aba de histórico reflete o número exato de ciclos salvos para o dia atual.

### 🔹 Dia 6: UI/UX, Pausa & Reinício
- [ ] **T15 - Pausar e Retomar:** O botão "Pausar" congela a contagem no segundo exato; "Retomar" continua sem saltos de tempo.
- [ ] **T16 - Reiniciar (Reset):** O botão "Reiniciar" reseta o timer para o tempo inicial do estado atual.
- [ ] **T17 - Responsividade:** A janela pode ser redimensionada sem quebrar os elementos na tela.

---

## ⚡ 3. Cenários de Testes de Estresse (Dia 7)

| ID | Cenário de Teste | Ação Executada | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **ST01** | Cliques repetidos no Iniciar | Clicar 10 vezes consecutivas no botão "Iniciar" | O timer não acelera a contagem (mantém 1 tick por segundo). |
| **ST02** | Alternância rápida Pause/Start | Clicar alternadamente em Pausar e Iniciar várias vezes | Estado permanece consistente sem travar a thread. |
| **ST03** | Fechamento durante contagem | Fechar a janela com o timer rodando | A aplicação encerra os processos sem deixar processos zumbis. |
| **ST04** | Arquivo `log.json` corrompido | Inserir texto inválido manualmente no `log.json` | O app trata a exceção com segurança e recupera o arquivo. |

---

## 🚀 4. Como Executar os Testes Automatizados Localmente

```bash
# Executar todos os testes
pytest

# Executar com relatório detalhado de saída
pytest -v
```
