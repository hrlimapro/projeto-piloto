# 🤝 Guia de Fluxo Git & GitHub (Trabalho em Dupla)

Este guia documenta o passo a passo prático para o trabalho colaborativo durante os 7 dias de desenvolvimento, garantindo que o código da dupla seja integrado sem conflitos e com histórico organizado.

---

## 🌳 1. A Estratégia de Branches

A branch `main` representa o código final, estável e testado.  
**Regra de Ouro:** **Nunca faça commits ou pushes diretamente na branch `main`**.

```text
main (código estável)
 │
 ├── feature/dia2-timer-logic   (Pessoa A) ──> Abre PR ──> Review ──> Merge na main
 └── feature/dia2-timer-ui      (Pessoa B) ──> Abre PR ──> Review ──> Merge na main
```

### Padrão de Nomenclatura das Branches:
- `feature/dia<X>-<descricao>` (para novas funcionalidades)
- `fix/dia<X>-<descricao>` (para correções de bugs)

*Exemplos:*
- `feature/dia2-logica-timer`
- `feature/dia2-layout-flet`
- `feature/dia3-maquina-estados`

---

## 🚀 2. Ciclo de Trabalho Diário Passo a Passo

### Passo 1: Comece sempre com a `main` atualizada
Antes de iniciar qualquer código do dia:
```bash
git checkout main
git pull origin main
```

### Passo 2: Crie e entre na sua branch de trabalho
```bash
git checkout -b feature/dia2-logica-timer
```

### Passo 3: Escreva o código e faça commits atômicos
Faça commits pequenos e frequentes à medida que avança:
```bash
# Verifique os arquivos alterados
git status

# Adicione as alterações
git add .

# Crie a mensagem seguindo os padrões de commit
git commit -m "feat: adiciona classe Pomodoro e metodo tick"
```

#### 🏷️ Padrões de Mensagens de Commit:
- `feat:` Nova funcionalidade implementada
- `fix:` Correção de bug
- `refactor:` Melhoria de código sem alterar funcionamento
- `docs:` Alterações em documentações/README
- `style:` Ajustes visuais ou de formatação

---

### Passo 4: Envie sua branch para o GitHub
Ao terminar a tarefa do dia (ou uma parte importante dela):
```bash
git push -u origin feature/dia2-logica-timer
```
*(Nas próximas vezes na mesma branch, basta executar apenas `git push`).*

---

## 🔀 3. Abrindo e Aprovando o Pull Request (PR)

### Como Abrir o PR no GitHub:
1. Acesse o repositório no navegador: [github.com/hrlimapro/projeto-piloto](https://github.com/hrlimapro/projeto-piloto).
2. O GitHub mostrará uma barra amarela no topo com o botão verde: **"Compare & pull request"**. Clique nele.
3. **Título:** Dê um título claro (ex: `feat: lógica do timer e decremento (Dia 2)`).
4. **Descrição (Template Automático):** Preencha o checklist marcando com `[x]` as etapas concluídas e testadas na sua máquina.
5. **Reviewers:** No painel lateral direito, adicione seu colega de dupla como revisor.
6. Clique em **"Create pull request"**.

---

### Como Revisar e Fazer o Merge:
1. O parceiro entra na aba **"Pull Requests"** do repositório.
2. Clica na aba **"Files changed"** para ver as linhas adicionadas (verde) e removidas (vermelho).
3. Testa o código na própria máquina se necessário.
4. Se tudo estiver correto, clica em **"Merge pull request"** e depois em **"Confirm merge"**.
5. Opcional: Clicar em **"Delete branch"** no GitHub para manter o repositório limpo.

---

### Passo 5: Atualizando o ambiente local após o Merge
Assim que um PR for mergeado na `main`, **ambos** devem atualizar seus computadores:
```bash
git checkout main
git pull origin main
```

---

## 🛡️ 4. Como Lidar com Conflitos (Sem Pânico!)

Se duas pessoas editarem o mesmo arquivo na mesma linha:
1. Ao fazer `git pull origin main` ou tentar o merge, o Git avisará de um conflito.
2. Abra o arquivo no **VS Code**: ele destacará as opções:
   - *Accept Current Change* (manter sua alteração local)
   - *Accept Incoming Change* (aceitar a alteração que veio do parceiro)
   - *Accept Both Changes* (manter ambas)
3. Escolha a opção correta, salve o arquivo e finalize com:
   ```bash
   git add .
   git commit -m "fix: resolve conflito de merge"
   git push
   ```
