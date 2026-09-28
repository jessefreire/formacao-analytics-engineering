---
name: dbt-modelagem-dimensional
description: Decide e implementa o modelo dimensional de um projeto dbt — grão da fato, dimensões, ponte muitos-para-muitos com allocation_factor, membros sintéticos -1, atributo vs. métrica e dimensão degenerada. Use quando o usuário pedir "modela a fato", "qual o grão", "star schema", "como tratar muitos-para-muitos", "bridge table", "desenha o modelo conceitual", ou antes de escrever os modelos de marts.
---

# /dbt-modelagem-dimensional

Decisões de modelagem com evidência medida na base, antes de qualquer linha de SQL de marts.
Regra de ouro: **medir primeiro, decidir depois, registrar o porquê.** Nenhuma decisão entra
sem o número que a sustenta.

## Processo

1. **Levantar as perguntas de negócio** e, para cada uma, qual métrica e qual corte ela exige.
2. **Decidir o grão da fato** (passo mais importante — ver abaixo).
3. **Listar dimensões** a partir dos cortes; confirmar a chave de cada uma na origem.
4. **Classificar cada relacionamento**: 1:N direto na fato, ou N:N → ponte.
5. **Tratar ausência**: membro sintético `-1` em vez de FK nula.
6. **Classificar colunas**: métrica aditiva, atributo, ou degenerada.
7. **Registrar** em `docs/` a decisão + o número medido que a justificou.
8. **Implementar** em `int_` + `dim_`/`fact_` na mesma branch, com `.yml` (descrição + testes).

## Grão da fato

- Escolha o **grão mais fino que a métrica-chave exige**. Se a métrica nasce no item
  (`qtd × preço`), a fato é no item, mesmo que o briefing fale em "pedido".
- Teste: a métrica de aceite do negócio (ex.: receita bruta de um ano) **só fecha** no grão
  escolhido? Rode a soma nos dois grãos candidatos e compare.
- Campos do cabeçalho (frete, imposto, total do pedido) **não entram** numa fato de item — se
  somados por item, multiplicam. Ficam fora, ou numa fato própria se alguma pergunta pedir.
- Prefira **uma fato** quando o briefing fala no singular; duas fatos (cabeçalho + linha) só
  com justificativa, e cuidado com relacionamento circular no BI.

## Muitos-para-muitos → ponte com allocation_factor

Quando um registro da fato se liga a N valores de uma dimensão (ex.: pedido com até 3 motivos):

1. **Medir a distribuição**: quantos têm 0, 1, 2, 3... valores. Medir a cobertura por segmento
   (ex.: canal) — ausência sistemática muda a leitura.
2. **Ponte** `bridge_<fato>_<dim>` com a chave do registro + chave da dimensão.
3. **`allocation_factor = 1 / n_valores_do_registro`** — a soma do fator por registro é 1.
4. **Regra**: receita **mora na fato**; a ponte **filtra e fatia, nunca soma**. Somar receita
   atravessando a ponte sem o fator infla o total (medir e registrar o quanto: no desafio
   Adventure Works, +29%).
5. Cobrir **todos** os registros da fato na ponte (os sem valor apontam para o `-1`), senão
   filtrar pela dimensão apaga linhas.
6. Teste customizado: soma do `allocation_factor` por registro = 1.
7. Se só uma pergunta precisa de um "sim/não" (ex.: teve promoção?), acrescente um
   **sinalizador degenerado** na fato (`has_x`) em vez de forçar a ponte.

## Membros sintéticos -1

- Toda FK da fato é `not_null` **por desenho**. "Sem valor" vira a chave `-1` na dimensão
  ("Sem cartão", "Não informado", "Sem vendedor").
- Antes de criar, **meça**: quantos registros caem no `-1` e se isso coincide com um segmento
  (ex.: 88% dos pedidos sem vendedor = exatamente o canal online → não é dado faltante, é regra).
- Documente o significado do `-1` no `.yml` da dimensão.

## Atributo vs. métrica vs. degenerada

| Tipo | Exemplo | Regra |
|---|---|---|
| Métrica aditiva | `gross_revenue`, `order_quantity` | soma em qualquer corte |
| Atributo na fato | `unit_price`, `discount_rate` | **nunca somar** — marcar "ATRIBUTO, não métrica" no `.yml`; no BI, `summarizeBy: none` |
| Degenerada | `sales_order_id`, `channel`, `status` | fica na fato; sem atributos próprios, não merece dimensão |

Coluna constante (ex.: `status` = 5 em 100% das linhas): documentar e **não** oferecer como
filtro — ela não corta nada.

## Chaves

- Padrão: reaproveitar a chave natural da origem (`product_key = product_id`).
- Surrogate só quando a natural não existe ou colide (ex.: dimensão de datas gerada, dimensão
  composta).

## Testes mínimos por mart

- PK: `unique` + `not_null` em toda dimensão e na fato.
- `relationships` em toda FK da fato.
- Ponte: sem `unique` de coluna única (chave composta) — teste da soma do fator.
- Teste de aceite do negócio como teste singular (`tests/assert_<regra>.sql`), com tolerância
  explícita (ex.: 1 centavo) e o valor esperado no comentário.

## Armadilhas já pagas

- Comparar métricas **misturando segmentos** que são "dois negócios" (online vs. revenda)
  inverte conclusões. Defina um eixo de controle e documente.
- Dinheiro em `decimal(19,4)`, nunca `double` — a 4ª casa é o que fecha o valor de auditoria.
- Dimensão de território ≠ dimensão de geografia de cobrança: conceitos diferentes, não
  hierarquize.
