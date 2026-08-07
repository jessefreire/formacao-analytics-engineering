# Resumo — Módulo 7: Estatística aplicada à análise de dados

## 1. Introdução e fundamentos

A **estatística** é o elo entre o rigor matemático e a complexidade do mundo real. Surgiu dos jogos de azar (séc. XVII–XVIII) e permite descrever o "que foi", prever o "que será" e estimar o "que poderia ter sido".

**Lei dos Grandes Números:** com repetições suficientes, a frequência relativa de um evento converge para sua probabilidade real. É a base de cassinos, seguradoras e modelos de risco.

**Precisão ≠ Acurácia:** um resultado pode ser preciso (reprodutível) mas errado (viesado). Ex: usar distribuição normal quando os dados não satisfazem essa premissa gera estimativas precisas mas incorretas.

**Pensar probabilisticamente:** toda afirmação deve vir acompanhada de uma medida de confiança. 2+2 nem sempre é 4 quando há incerteza.

## 2. Análise descritiva

**Análise descritiva** resume e descreve características dos dados sem fazer inferências sobre a população. É a porta de entrada para análises mais complexas.

**Vantagens:** objetividade, imparcialidade, visão ampla, permite criar hipóteses.
**Limitações:** não generaliza para outras populações, não testa hipóteses, não estabelece causalidade.

## 3. Medidas de tendência central

| Medida | Fórmula | Quando usar |
|---|---|---|
| **Média** | $\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$ | Dados simétricos, sem outliers fortes |
| **Mediana** | valor central (ordenado) | Dados assimétricos, com outliers |
| **Moda** | valor mais frequente | Dados categóricos ou picos de frequência |

**Exemplo BanVic:** média de transação débito foi ~5x maior que a mediana → distribuição assimétrica com cauda longa (poucos valores altos puxam a média).

**Regra prática:** quanto mais assimétricos os dados, maior a diferença entre média, mediana e moda.

## 4. Medidas de dispersão

| Medida | Fórmula | Interpretação |
|---|---|---|
| **Amplitude** | $max - min$ | Diferença entre extremos |
| **Desvio médio** | $\frac{\sum |x_i - \bar{x}|}{n}$ | Média dos desvios absolutos |
| **Variância** | $\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n}$ | Média dos quadrados dos desvios |
| **Desvio padrão** | $\sigma = \sqrt{\sigma^2}$ | Raiz da variância (mesma unidade dos dados) |
| **Coef. variação** | $CV = \frac{\sigma}{\bar{x}}$ | Adimensional, compara conjuntos distintos |

**Exemplo BanVic (altura):** desvio padrão = 0,097m ≈ 9,7cm.

## 5. Medidas de associação

**Coeficiente de correlação (ρ ou r):** mede a força e direção da relação linear entre duas variáveis.

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}$$

- Valor entre **-1 e 1**
- Próximo de 0 = sem associação linear
- Próximo de 1 = correlação positiva forte
- Próximo de -1 = correlação negativa forte

**Correlação NÃO é causalidade:** duas variáveis podem estar correlacionadas por coincidência (correlação espúria). Ex: consumo de mussarela x doutores em engenharia civil (r=0,95).

## 6. Visualização de dados

| Gráfico | Tipo de dado | O que mostra |
|---|---|---|
| **Histograma** | Uma variável contínua | Distribuição de frequência (classes × frequência) |
| **Dispersão** | Duas variáveis contínuas | Relação/padrão entre variáveis |
| **Boxplot** | Uma variável + grupos | Mediana, quartis, outliers (IQR × 1,5) |

**Elementos do boxplot:** mínimo (Q1 - 1,5×IQR), Q1, mediana (Q2), Q3, máximo (Q3 + 1,5×IQR), outliers.

## 7. Probabilidade

**Espaço amostral (Ω):** conjunto de todos os resultados possíveis.
**Evento:** subconjunto do espaço amostral.
**Probabilidade:** frequência relativa de ocorrência após muitas repetições.

**Regras fundamentais:**
- **Adição:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Condicional:** $P(A|B) = \frac{P(A \cap B)}{P(B)}$
- **Eventos independentes:** $P(A \cap B) = P(A) \cdot P(B)$

**Exemplo Monty Hall:** trocar a porta dá ⅔ de chance de ganhar (não ½).

## 8. Variáveis aleatórias e distribuições discretas

| Tipo | Exemplos |
|---|---|
| **Discreta** | Lançamento de dado, número de filhos, fraude/não-fraude |
| **Contínua** | Tempo, valor de transação, altura |

**Distribuições discretas:**

| Distribuição | Função | Uso |
|---|---|---|
| **Uniforme** | $P(X=x) = 1/n$ | Dados com probabilidade igual (dado) |
| **Bernoulli** | $P(X=x) = p^x(1-p)^{1-x}$ | Um evento sucesso/fracasso |
| **Binomial** | $P(X=k) = C(n,k) p^k(1-p)^{n-k}$ | n repetições de Bernoulli |
| **Geométrica** | $P(X=k) = p(1-p)^{k-1}$ | Tentativas até 1º sucesso |
| **Poisson** | $P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$ | Taxa de ocorrência em intervalo |

**Exemplo Poisson (BanVic):** λ=4,5 trans/s → P(X>6) = 1 - P(X≤6) ≈ 16,89%.

## 9. Distribuição normal

**Função densidade:** $f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

**Notação:** $X \sim N(\mu, \sigma^2)$

**Propriedades:**
- Simétrica em relação a μ
- Média = Mediana = Moda
- Tende a 0 nos extremos

**Normal padrão:** $Z = \frac{X - \mu}{\sigma}$ → $Z \sim N(0, 1)$

**Regra 68-95-99,7:**
| Z-score | Área acumulada |
|---|---|
| ±1 | 68,26% |
| ±2 | 95,44% |
| ±3 | 99,74% |

**Exemplo BanVic (altura):** P(1,90 ≤ X ≤ 2,10) com μ=1,75, σ=0,10 → Z=(1,9-1,75)/0,1=1,5; Z=(2,1-1,75)/0,1=3,5 → P = 0,9998 - 0,9332 ≈ 6,66%.

## 10. Distribuições não normais

**Quatro momentos para identificar não normalidade:**
1. **Localização:** média ≠ mediana ≠ moda
2. **Dispersão:** variância muito grande ou pequena
3. **Assimetria:** positivo (cauda à direita), negativo (cauda à esquerda)
4. **Curtose:** mesocúrtica (≈normal), leptocúrtica (afunilada, caudas longas), platicúrtica (achatada)

**Principais distribuições não normais:**

| Distribuição | Característica | Exemplo |
|---|---|---|
| **Exponencial** | Assimétrica positiva, decaimento | Tempo entre eventos |
| **Log-normal** | ln(X) ~ Normal | Renda, valores multiplicativos |
| **Gamma** | Assimétrica positiva, flexível | Tempo até k eventos |
| **Qui-quadrado** | Assimétrica, valores positivos | Testes de hipóteses |

**Testes de normalidade:**
- **Gráficos:** histograma, boxplot, Q-Q plot
- **Shapiro-Wilk:** estatística W (próximo de 1 = normal)
- **Kolmogorov-Smirnov:** estatística D (maior diferença entre CDFs)

**Tratamento:** transformações (log, Box-Cox) ou testes não paramétricos (Wilcoxon, Kruskal-Wallis).

## 11. Inferência estatística

**Objetivo:** tirar conclusões sobre uma população com base em uma amostra.

**Tipos de estimativa:**
- **Pontual:** um valor único (ex: média amostral)
- **Intervalar:** intervalo de confiança (ex: IC 95%)

**Parâmetros e estimadores:**

| Parâmetro (população) | Estimador (amostra) |
|---|---|
| μ (média) | $\bar{X} = \frac{\sum X_i}{n}$ |
| p (proporção) | $\hat{p} = \frac{freq}{n}$ |
| σ² (variância) | $S^2 = \frac{\sum(X_i - \bar{X})^2}{n-1}$ |

## 12. Teorema Central do Limite e distribuição amostral

**Teorema Central do Limite (TCL):** para n suficientemente grande, a distribuição da média amostral $\bar{X}$ se aproxima de uma distribuição normal, independentemente da distribuição original.

$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

**Erro padrão:** $SE = \frac{\sigma}{\sqrt{n}}$

Quanto maior n → menor erro padrão → média amostral mais próxima da populacional.

## 13. Intervalos de confiança

**Definição:** intervalo de valores que contém o verdadeiro parâmetro com probabilidade (1-α).

**Interpretação correta:** se repetirmos o experimento várias vezes, esperamos que (1-α)% dos intervalos contenham o verdadeiro parâmetro.

**Fórmulas:**

| Parâmetro | IC (variância conhecida) | IC (variância desconhecida) |
|---|---|---|
| μ | $[\bar{X} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}}; \bar{X} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}]$ | $[\bar{X} - t_{\alpha/2}\frac{s}{\sqrt{n}}; \bar{X} + t_{\alpha/2}\frac{s}{\sqrt{n}}]$ |
| p | $[\hat{p} - z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}; \hat{p} + z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}]$ | — |

**Valores críticos (z):**
| Grau de confiança | α | z |
|---|---|---|
| 90% | 0,10 | 1,645 |
| 95% | 0,05 | 1,96 |
| 99% | 0,01 | 2,575 |

**Relação:** maior confiança → maior amplitude → menor precisão.

## 14. Testes de hipóteses

**Etapas:**
1. Definir H₀ (nula) e H₁ (alternativa)
2. Definir forma (unilateral ou bilateral)
3. Identificar distribuição do estimador
4. Fixar α e obter região crítica
5. Concluir

**Tipos de teste:**
- **Unilateral:** H₁: μ < μ₀ ou H₁: μ > μ₀
- **Bilateral:** H₁: μ ≠ μ₀

**Erros:**

|  | H₀ verdadeira | H₀ falsa |
|---|---|---|
| **Rejeitar H₀** | Erro Tipo I (α, falso positivo) | Acerto (1-β) |
| **Não rejeitar H₀** | Acerto (1-α) | Erro Tipo II (β, falso negativo) |

**Distribuição do teste:**
- **n > 30:** usar z (normal padrão)
- **n < 30:** usar t de Student (n-1 graus de liberdade)

**Estatísticas de teste:**

| Parâmetro | Estatística |
|---|---|
| μ | z (n>30) ou t (n<30) |
| p | z |
| σ² | χ² (qui-quadrado) |

## 15. Amostragem

| Técnica | Quando usar |
|---|---|
| **Aleatória simples** | População homogênea |
| **Estratificada** | População heterogênea com estratos |
| **Por conglomerados** | População grande/dispersa |
| **Sistemática** | População ordenável |
| **Por quotas** | Subgrupos específicos |

**Tamanho da amostra (população infinita):**

$$n = \frac{Z_{\alpha/2}^2 \cdot \sigma^2}{e^2}$$

Para proporções (pessimista, p=0,5): $n = \frac{Z_{\alpha/2}^2}{4e^2}$

## 16. Experimentos

**Teste A/B:** comparação entre grupo teste (recebe tratamento) e grupo controle (não recebe).

**Princípios:**
- Grupos o mais similares possível
- Um tratamento por vez
- Aleatorização

**Tipos:**
- **Experimento aleatório controlado:** alocação aleatória
- **Experimento natural:** circunstâncias externas criam grupos similares
- **Quase-experimento:** sem controle total, mas com técnicas de pareamento

## 17. Regressão linear

**Modelo:** $\hat{y} = a + bx$

- **y:** variável dependente (prevista)
- **x:** variável independente (explicativa)
- **a:** intercepto
- **b:** coeficiente angular

**Método:** Mínimos Quadrados Ordinários (MQO) — minimiza a soma dos quadrados dos erros.

**R²:** qualidade do ajuste (0 a 1). Problema: sempre aumenta ao adicionar variáveis.

**p-valor:** teste de hipótese para cada coeficiente. H₀: coef = 0. Se p < α, rejeita-se H₀ (variável é significativa).

**Erros comuns:**
- Usar quando relação é não-linear
- Adicionar variáveis sem critério (infla R²)
- **Multicolinearidade:** variáveis explicativas altamente correlacionadas
- Confundir correlação com causalidade

---

## Pontos de reforço pessoal

- **Média vs Mediana:** em distribuições assimétricas com cauda longa (renda, valor de transação), a média é puxada pelos valores extremos. A mediana é mais robusta.
- **Variância:** a fórmula da variância amostral usa **n-1** (correção de Bessel), não n.
- **Correlação:** r=0 significa ausência de relação **linear**, não independência. Relações não-lineares podem existir.
- **Condicional:** P(A|B) ≠ P(B|A). A ordem importa.
- **Erros I e II:** diminuir α aumenta β. O erro que se busca minimizar é o Tipo I.
- **t de Student:** para n>30 converge para normal. Use t quando variância desconhecida e amostra pequena.
- **IC:** quanto maior a confiança, maior (mais amplo) o intervalo.
- **R²:** sempre aumenta com mais variáveis. Use R² ajustado ou conhecimento de negócio.

---

## Conexões com o Desafio Final (dbt + Power BI)

- As **medidas de tendência central e dispersão** (média, mediana, desvio padrão) são a base para KPIs no Power BI — usar a medida certa depende da distribuição dos dados.
- **Correlação** entre variáveis transacionais (ex: valor × frequência) ajuda a definir features nos models intermediate do dbt.
- **Normalidade:** modelos de regressão e alguns testes estatísticos assumem normalidade. Verificar antes de aplicar.
- **Amostragem e inferência:** o dbt transforma dados populacionais; entender erro padrão ajuda a avaliar se diferenças em KPIs (ex: ticket médio entre agências) são estatisticamente significativas ou ruído.
- **Testes de hipóteses:** úteis para comparar métricas entre grupos no Power BI (ex: agência Digital vs Física).
- **Boxplot no Power BI:** visualiza outliers de transações que podem indicar fraudes — cruzar com modelo staging do dbt.
- **Regressão:** entender o conceito ajuda a interpretar tendências em séries temporais no dashboard final.
