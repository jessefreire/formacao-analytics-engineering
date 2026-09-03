# Setup do Ambiente das Aulas Práticas — GitHub + Databricks + dbt Cloud

> Instruções oficiais do curso para preparar o ambiente das aulas práticas. As três peças: **GitHub** (versionar código), **Databricks** (compute + storage) e **dbt Cloud** (orquestração e execução dos modelos).

---

## Visão geral

| Ferramenta | Papel |
|---|---|
| **GitHub** | Versionar o código (fork do repo base) |
| **Databricks** | Compute engine e storage (SQL Warehouse roda as queries) |
| **dbt Cloud** | Orquestração e execução dos modelos (IDE no navegador) |

Fluxo: você edita models no dbt Cloud (ou local) → commit no **seu fork** no GitHub → dbt Cloud executa contra o **SQL Warehouse do Databricks**.

---

## Passo 1 — GitHub e Fork

### 1.1 Criar conta
- Acesse: <https://github.com>
- Crie sua conta (caso ainda não tenha)

### 1.2 Fazer o fork (NÃO criar repo vazio)

O curso exige **fork** deste repositório, pois ele contém as seeds usadas nas aulas:

👉 <https://github.com/techindicium/banvic-dbt>

**Passo a passo:**
1. Acesse o repositório original
2. No canto superior direito, clique em **Fork**
3. Na tela seguinte:
   - Confirme que o fork será criado na **sua conta pessoal**
   - Mantenha o nome `banvic-dbt`
   - Clique em **Create fork**
4. Resultado: `https://github.com/<seu-usuario>/banvic-dbt`

> ⚠️ **Nunca commite no repositório original da Indicium** — trabalhe sempre no seu fork.

### 1.3 Branch de aula

O repositório tem uma branch com os códigos mostrados na aula:

👉 <https://github.com/techindicium/banvic-dbt/tree/recursos>

Para acompanhar localmente:

```bash
git fetch origin
git checkout recursos   # consulta os códigos da aula
git checkout main       # volta pro seu trabalho
```

---

## Passo 2 — Databricks (Trial)

> Antes de configurar o dbt Cloud, deixe o Databricks funcional.

### 2.1 Criar conta
- Vá para: <https://www.databricks.com/try-databricks>
- Escolha **Community / Trial**
- Crie a conta e faça login no workspace

### 2.2 Configurar o ambiente — 3 elementos

#### (A) Checar o SQL Warehouse

O dbt Cloud executa queries via **SQL Warehouse**.

1. Menu lateral esquerdo → **SQL**
2. **SQL Warehouses**
3. No `Serverless Starter Warehouse`, abra **Connection details** e copie:
   - **Server Hostname** — ex.: `adb-1234567890123456.17.azuredatabricks.net`
   - **HTTP Path** — ex.: `/sql/1.0/warehouses/<warehouse-id>`

#### (B) Criar catálogo + schema (opcional, mas recomendado)

1. Menu lateral → **Catalog**
2. Crie um catálogo chamado: `dev` (ou o nome que preferir)

#### (C) Gerar Token de Acesso

O dbt Cloud se conecta ao Databricks via **token**.

1. Avatar (canto superior direito) → **User Settings**
2. Aba **Developer**
3. **Access Token** → **Manage**
4. Crie o token (ex.: nome `dbt-cloud`)
5. **Generate** → copie e guarde

> ⚠️ **O token só é exibido uma vez.** Se perder, gere um novo. Nunca commite o token em nenhum repositório.

### 2.3 Checklist — o que salvar antes do dbt Cloud

| Informação | Onde achar |
|---|---|
| **Server Hostname** | Barra do navegador (ex.: `https://adb-1234567.89.azuredatabricks.net`) |
| **HTTP Path** | SQL Warehouses → Connection details do seu warehouse |
| **Token** | User Settings → Developer → Access Tokens |
| **Catalog** | O catálogo que você criou (ex.: `dev`) |

---

## Passo 3 — Projeto no dbt Cloud

### 3.1 Acessar
- <https://cloud.getdbt.com>
- Faça login
- Primeira vez: o dbt abre o fluxo de criação automática
- Caso contrário: **Engrenagem** (canto superior direito) → **Account Settings** → **+ New Project**

### 3.2 Configuração

**1. Data platform:** selecione **Databricks**

**2. Credenciais** (as informações do Passo 2):

| Campo | Valor |
|---|---|
| Host | Server Hostname do Databricks |
| HTTP Path | path do seu warehouse |
| Token | o token `dbt-cloud` gerado |
| Catalog | `dev` (ou o que você criou) |
| Schema | ex.: `dbt_nome_sobrenome` |

**3. Conectar ao GitHub:**
- Selecione **GitHub**
- Autorize o dbt a acessar sua conta
- Selecione **o seu fork**: `<seu-usuario>/banvic-dbt`

> ⚠️ **Nunca selecione o repositório original da Indicium.**

**4. Finalização:** se tudo estiver correto: **"Your project is ready!"**

A partir daí você pode:
- Rodar modelos
- Carregar as seeds (`dbt seed`)
- Acompanhar as aulas pela branch `recursos`
- Editar modelos direto no IDE do dbt Cloud

---

## Estado atual (Jesse) — atualizado em 24/08/2026

- ✅ Fork criado: `jessefreireufc/banvic-dbt`
- ✅ Clone local em `banvic-dbt/` (repo aninhado, `main`)
- ✅ Branch `recursos` (baixada do upstream e enviada pro fork)
- ✅ Conta Databricks pessoal (free) + Server Starter Warehouse + catálogo `dev` + token `dbt-cloud`
- ✅ Projeto no dbt Cloud (`banvic-dbt`) conectado ao fork + ambiente Development (track `Latest` — Fusion não compatível com Databricks)
- ✅ IDE: dbt **Studio** (novo nome do Develop) — `dbt debug` All checks passed
- ✅ Seeds habilitadas via PR (`chore/habilita-seeds` → main) — `dbt seed` 8/8 Success
- ✅ 8 tabelas carregadas em `dev.erp_banvic` (conferido no Catalog)

### Aprendizados do setup (pegadinhas reais)

- Fork do GitHub não copia outras branches por padrão → `git fetch <url-upstream> recursos` + `git branch recursos FETCH_HEAD` + `git push -u origin recursos`
- Token Databricks: escopo **All APIs** (não só `sql`) pra evitar PERMISSION_DENIED no dbt
- dbt Cloud: ambiente **Development** (não Deployment) é onde vão as credenciais pessoais; token entra no **profile page** do usuário
- dbt version: **Latest** (Fusion ainda não suporta a conexão Databricks clássica)
- IDE se chama **Studio** (renomeado de "Develop"); `main` aparece travada 🔒 → criar branch pra editar
- Arquivo vermelho no explorer = modificado (git diff), não erro; erro real = contador `Error` no painel da execução

---

## Notas de segurança e boas práticas

1. **Token do Databricks** = senha. Nunca commitar; se vazar, revogue e gere outro
2. **dbt Cloud vs dbt Core:** estas instruções usam o **dbt Cloud** (IDE no navegador). O fluxo local (dbt Core) usa `~/.dbt/profiles.yml` com as mesmas credenciais — ver `GUIA_DBT_BANVIC.md`
3. **Community/Trial tem limites** (horas de cluster, tamanho) — planeje `dbt run` em horários de baixo uso
4. Trabalhe em branches (`feature/`, `fix/`) e faça merge na `main` do **seu** fork
