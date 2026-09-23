# Skills e MCP — o kit de Analytics Engineer com IA

Mapa das ferramentas de IA usadas na formação e no desafio final Adventure Works: as **skills**
(instruções empacotadas que o Claude Code carrega quando a tarefa pede) e o **MCP** (o servidor
que dá à IA acesso direto ao modelo do Power BI).

> **Guardrail de dados** — só com dados fictícios/de treino ou com autorização explícita do
> cliente. Confirmar com a gestão antes de usar IA em projeto real.

---

## 1. O que é uma skill

Uma pasta com um `SKILL.md` (frontmatter `name` + `description`, e o corpo com o processo). A
`description` diz **quando** usar: o Claude Code lê as descrições de todas as skills e carrega
a que casa com o pedido, ou você chama pelo nome (`/pbi-dax-create`).

| Onde mora | Alcance |
|---|---|
| `.claude/skills/` deste repo (espelho em `skills/`) | só neste projeto, versionada |
| `~/.claude/skills/` | global, em qualquer projeto da máquina |

---

## 2. O fluxo de ponta a ponta, e qual skill entra em cada passo

```
Briefing ─▶ Ingestão ─▶ Modelagem ─▶ dbt ─▶ Mockup ─▶ Power BI ─▶ Conferência ─▶ Apresentação ─▶ Entrega
            databricks-  dbt-mod.    dbt-    pbi-      report-*    reconciliacao-  pbi-apresent.  entrega-a-
            ingestao     dimensional pack.   mockup-   pbi-dax-    numeros         indicium-      partir-do-
                                     tests   design    pbi-licoes                  slide-creator  briefing
                         └──────────── ae-fullflow (visão geral do fluxo inteiro) ────────────┘
```

---

## 3. Skills do projeto (versionadas aqui)

| Skill | O que faz |
|---|---|
| `ae-fullflow` | Fluxo completo do AE: Databricks → SQL → dbt → GitHub → Power BI → SVG → tema JSON |
| `dbt-packages-tests` | Packages (`dbt_utils`), testes genéricos e os erros comuns do dbt, com a correção de cada um |
| `ae_materials_app` | Sincroniza os materiais do curso com o `index.html` do visualizador local |

## 4. Skills de Power BI (globais, já existiam)

| Skill | O que faz |
|---|---|
| `powerbi-report-planning` | Requisitos → spec aprovada de um relatório novo (público, páginas, dependências) |
| `powerbi-report-design` | Direção visual: tom, layout, tipo de gráfico, tema, acessibilidade |
| `powerbi-report-authoring` | Edita PBIR/PBIP de verdade (páginas, visuais, filtros, slicers, temas) com validação e screenshot |
| `pbi-dax-create` | Cria medida DAX a partir de descrição em português, respeitando o modelo real |
| `pbi-doc` | Documenta um PBIP inteiro em markdown + HTML navegável |
| `pbi-modelo-review` | Audita o modelo e gera relatório com score e anti-patterns |
| `pbi-migra-fonte` | Reaponta datasets de uma fonte legada para Databricks, em lote |

Complementares usadas no desafio: `indicium-slide-creator` (decks na identidade Indicium AI).

## 5. Skills criadas a partir do desafio Adventure Works (globais, novas)

Cada uma nasceu de um problema que custou tempo de verdade no desafio.

| Skill | Quando usar | O que ela resolve |
|---|---|---|
| `databricks-ingestao` | subir arquivos brutos a partir de um DDL | carga idempotente com `read_files` (sem duplicar), `nullValue`/`quote`/`FAILFAST`, dinheiro em `decimal(19,4)` e as 5 conferências antes de analisar |
| `dbt-modelagem-dimensional` | antes de escrever os marts | grão da fato, ponte N:N com `allocation_factor` (sem ela a receita inflava 29%), membros `-1`, atributo vs. métrica vs. degenerada, testes mínimos |
| `pbi-mockup-design` | desenhar o dashboard antes do Power BI | baixa → alta fidelidade no `/design`, 1280px com altura medida, artboards de fundo em SVG, cada interação já mapeada pro objeto real do PBI |
| `pbi-licoes-pbir` | algo "valida mas não funciona" | tabela sintoma → causa → correção: RANKX com linhas sem venda, `SELECTEDVALUE` em field parameter, caminho > 260 caracteres, formatação que não aplica |
| `reconciliacao-numeros` | "esse número tá certo?" / filtro vazio | bate o número em SQL, dbt e DAX; roteiro pra investigar vazio (catálogo maior que o usado ≠ bug) |
| `pbi-apresentacao` | gravar ou apresentar sem Power BI Service | abre o PBIP/PBIX no Desktop em tela cheia sem a interface de edição (app em `D:\Documentos\pbi-apresentacao`) |
| `entrega-a-partir-do-briefing` | fechar e submeter o projeto | tabela "o briefing pede × onde está", PDFs gerados dos `.md`, links testados sem login, ZIP no nome da plataforma |

---

## 6. MCP — `powerbi-modeling-mcp`

### O que é

O **Model Context Protocol** é o padrão que deixa a IA chamar ferramentas externas. O
`powerbi-modeling-mcp` (extensão da Microsoft, Analysis Services) conecta o Claude Code **ao
modelo semântico aberto no Power BI Desktop**: ler e editar tabelas, colunas, medidas e
relacionamentos, e **executar DAX de verdade** contra os dados carregados.

A diferença pra editar arquivo: com o MCP a IA **consulta o modelo vivo**. Em vez de supor que
uma medida está certa, ela roda a consulta e vê o número.

### Como está configurado

`.mcp.json` na raiz do repo aponta para o executável da extensão do VS Code Insiders:

```
C:\Users\<usuario>\.vscode-insiders\extensions\analysis-services.powerbi-modeling-mcp-<versao>-win32-x64\server\powerbi-modeling-mcp.exe --start
```

O número de versão faz parte do caminho — se parar de conectar depois de atualizar a
extensão, ajuste o caminho. Detalhes e template para outras IDEs em [`mcp/README.md`](mcp/README.md).

### Como se usa na prática

1. Abra o `.pbip` no Power BI Desktop.
2. `connection_operations` → `ListLocalInstances` → `Connect` (acha a porta do Desktop sozinho).
3. Trabalhe: `measure_operations`, `table_operations`, `dax_query_operations` → `Execute`…
4. **Salve no Desktop (Ctrl+S) depois de cada lote** — o MCP mexe na memória do Desktop, e
   fechar sem salvar perde tudo.

### Operações mais usadas no desafio

| Operação | Uso real |
|---|---|
| `dax_query_operations` (Execute) | conferir números: receita bruta de 2011 = 12.646.112,1607; descobrir que 3 dos 10 motivos de venda nunca aparecem em pedido |
| `measure_operations` | criar/corrigir as 45 medidas, com descrição `///` |
| `table_operations` (Delete, cascade) | remover a tabela de field parameter órfã, depois de confirmar que nada a usava |
| `connection_operations` | achar e conectar no Desktop aberto |

Lista completa das 17 operações em [`mcp/README.md`](mcp/README.md).

### CLIs que trabalham junto

Não são MCP, mas completam o ciclo de edição do relatório (usados pela `powerbi-report-authoring`):

| CLI | Papel |
|---|---|
| `powerbi-report-author` | metadados de visuais/formatação e `validate` do PBIR |
| `powerbi-desktop` | `status`, `reload` e `screenshot` do Desktop aberto |

**Divisão de trabalho:** MCP = modelo semântico (dados, medidas, relações); CLIs + PBIR =
relatório (páginas, visuais, formatação).

---

## 7. Guardrails que valem para tudo

- Fechar o Desktop sem salvar antes de editar JSON do PBIR por fora; salvar após cada lote MCP.
- Nunca remover backgrounds/SVGs sem pedido explícito.
- Toda consulta comentada: o que confere e qual o valor esperado.
- Prosa em português com acento; identificador e nome de arquivo em ASCII.
- Nenhum número é declarado certo (ou errado) sem ser recalculado em outra camada.
