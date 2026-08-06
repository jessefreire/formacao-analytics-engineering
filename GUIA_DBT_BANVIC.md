# Guia rápido: o que é esse repositório e como rodar o dbt

## O que é esse repositório

Este é um projeto de **dbt** (data build tool) feito para o curso de Analytics Engineering da
Indicium Academy. Ele usa dados fictícios de um banco chamado **Banvic**.

Hoje o repositório tem:

- **`seeds/banvic/`** — as tabelas cruas do Banvic em CSV (clientes, contas, agências, transações,
  propostas de crédito, colaboradores). É a matéria-prima, ainda sem tratamento.
- **`models/`** — onde a modelagem de dados de verdade é escrita, em SQL. Hoje só tem os exemplos
  padrão que o próprio dbt cria (`my_first_dbt_model`, `my_second_dbt_model`) — a modelagem do Banvic
  em si ainda precisa ser construída.
- **`macros/`** — um arquivo que define como os nomes de schema (as "gavetas" onde as tabelas ficam
  guardadas) são montados.

## O que é modelagem de dados (de forma simples)

Imagina que o banco tem várias planilhas soltas: uma de clientes, uma de contas, uma de transações,
etc. Elas estão cruas, bagunçadas, do jeito que saíram do sistema.

**Modelar dados** é o trabalho de pegar essas planilhas cruas e organizar/limpar/cruzar tudo isso até
virar informação útil — por exemplo, "quanto cada cliente tem de saldo total", cruzando a tabela de
contas com a de transações.

## Por que o dbt existe / serve pra quê

Sem o dbt, você teria que escrever um monte de script de SQL solto, sem organização, sem histórico e
sem garantia de que os dados estão certos. O dbt organiza esse trabalho:

- Você escreve arquivos `.sql` chamados **models**, cada um representando uma etapa da transformação
  (ex: "limpar tabela de clientes", "juntar clientes com contas", "calcular saldo por cliente").
- Um model pode usar o resultado de outro model — como uma esteira de produção, em etapas.
- O dbt roda tudo isso na ordem certa e cria as tabelas/views no banco de dados de verdade.
- Dá pra escrever **testes** (ex: "essa coluna nunca pode ser nula", "esse código é único") para
  garantir que os dados não quebraram no meio do caminho.

## dbt Cloud x dbt Core (isso confunde bastante gente)

Existem duas formas de usar o dbt, com o mesmo nome:

1. **dbt Cloud** — serviço online, hospedado, com IDE no navegador. Você loga numa conta. É
   provavelmente o que foi usado durante o curso originalmente — já vem com a conexão ao banco de
   dados pronta, então ninguém precisa configurar nada.
2. **dbt Core** — versão instalada localmente no computador (via Python), rodada pelo terminal.
   **Não precisa de nenhuma conta.** É o jeito que a maioria das empresas usa de verdade no dia a dia
   (fora de ambiente de curso).

Este repositório funciona com qualquer um dos dois. A diferença é que, no dbt Core local, é a gente
quem precisa fazer a "ponte" de conexão com o banco de dados — no dbt Cloud, essa ponte já vem pronta
pelo curso/empresa.

## O que dá pra fazer local (sem rodar nada) x o que precisa de conexão real

- **Escrever a modelagem** (os arquivos `.sql` em `models/`, os testes em `schema.yml`) dá pra fazer
  100% local, só editando texto — não precisa de nenhuma conexão.
- **Rodar de fato** (`dbt seed`, `dbt run`, `dbt test` — os comandos que carregam e processam os
  dados de verdade) precisa de:
  1. dbt Core instalado + o adaptador do Databricks (`dbt-databricks`);
  2. Um arquivo `profiles.yml` (fica fora do repositório, por guardar credenciais) com os dados de
     conexão do Databricks — host, caminho do cluster, token de acesso;
  3. Um acesso/workspace no Databricks de verdade — pode ser o do curso (se ainda existir) ou uma
     conta gratuita (Databricks tem "Community Edition").

## Comandos básicos do dbt

- `dbt seed` — carrega todas as tabelas cruas do Banvic (estão desabilitadas por padrão no projeto,
  então precisam ser habilitadas/selecionadas).
- `dbt seed -s <nome_do_csv>` — carrega só uma tabela específica (ex: `dbt seed -s clientes`).
- `dbt run` — roda os models (a modelagem escrita em SQL).
- `dbt run -s <nome_do_model>` — roda só um model específico.
- `dbt test` — roda os testes de qualidade dos dados.

## Situação em aberto

Ainda é preciso verificar se o acesso ao Databricks usado no curso (via dbt Cloud, na época) continua
válido, ou se será necessário criar um novo acesso (ex: conta gratuita do Databricks) para rodar este
projeto localmente.
