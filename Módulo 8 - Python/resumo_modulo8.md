# Resumo — Módulo 8: Python

## 1. Introdução ao Python e Jupyter Notebooks

**Google Colab** é a plataforma usada no curso — não requer instalação, roda no navegador. Arquivos de notebook têm extensão `.ipynb` e são divididos em células que podem ser executadas independentemente.

- **Executar célula:** `CTRL + ENTER` (executa atual) ou `SHIFT + ENTER` (executa e cria célula abaixo)
- **print()** — exibe mensagens, variáveis, tipos; essencial para debug
- **Comentários** — iniciam com `#`; tudo à frente é ignorado pelo interpretador
- **Colab** não exige `print()` para exibir valores — última expressão da célula já é exibida

## 2. Tipos primitivos e uso do type

| Tipo | Nome | Exemplo |
|---|---|---|
| **int** | Inteiro | `108` |
| **float** | Decimal | `1.08` (separador é **ponto**, não vírgula) |
| **str** | Texto | `'Analise de Dados'` |
| **bool** | Booleano | `True` / `False` |

- `type(variavel)` retorna o tipo
- **f-string**: `f'O valor e {variavel}'` — interpolação com `{}` dentro de aspas
- **Regra de aspas:** não pode aspas duplas dentro de duplas (mesmo para simples); use alternado

## 3. Operadores

| Categoria | Operadores |
|---|---|
| **Aritméticos** | `+` `-` `*` `/` `//` (divisão inteira) `%` (resto) `**` (exp) |
| **Atribuição** | `=` `+=` `-=` `*=` `/=` `%=` |
| **Comparação** | `>` `<` `==` `!=` `>=` `<=` |
| **Lógicos** | `and` `or` `not` |
| **Identidade** | `is` `is not` (mesmo objeto na memória) |
| **Associação** | `in` `not in` (pertence à sequência) |

**Pegadinha:** `=` é atribuição; `==` é comparação.

## 4. Listas

Variáveis que armazenam múltiplos valores. Índices começam em **zero**.

```python
lista = []              # ou list()
lista = [1, 'texto', True]
lista[0]                # acessa primeiro elemento
```

| Função | Descrição |
|---|---|
| `.append(x)` | Adiciona ao final |
| `.remove(x)` | Remove primeira ocorrência (erro se não existir) |
| `.insert(i, x)` | Insere na posição i |
| `.pop(i)` | Remove da posição i (ou último se omitido) |
| `.index(x)` | Retorna índice da primeira ocorrência |
| `.count(x)` | Conta ocorrências |
| `.sort(reverse=True)` | Ordena (reverse para decrescente) |

## 5. Dicionários

Coleção com **chaves editáveis** (não índices fixos). Parâmetro `chave: valor`.

```python
dicionario = {'inteiro': 108, 'texto': 'Indicium'}
dicionario['texto']          # acessa valor
dicionario['nova'] = valor   # cria/atualiza chave (chaves são ÚNICAS)
```

| Função | Descrição |
|---|---|
| `.keys()` | Retorna chaves |
| `.values()` | Retorna valores |
| `.items()` | Retorna pares (chave, valor) |
| `.pop(chave)` | Remove chave especificada |

## 6. Estruturas de decisão

```python
if condicao:
    # codigo
elif outra_condicao:
    # codigo
else:
    # codigo
```

**Pegadinha if vs elif:**
- `if` sempre é verificado independentemente
- `elif` só é verificado se as condições anteriores foram falsas
- Use `elif` quando as condições são mutuamente exclusivas

## 7. Estruturas de repetição

**while** — executa enquanto condição for verdadeira:
```python
while condicao:
    # codigo
    break    # interrompe o loop
```

**for** — itera sobre coleção ou faixa de valores:
```python
for elemento in colecao:
    # codigo

for i, valor in enumerate(colecao):    # retorna índice e valor
```

**`len()`** — retorna tamanho de listas, dicionários etc.

## 8. Funções

Blocos reutilizáveis com propósito específico.

```python
def nome_funcao(parametros):
    # codigos
    return valor       # ou return None se não houver retorno
```

- **Parâmetros** — valores de entrada
- **return** — valor de saída (use `None` quando não retornar nada)
- Chamada: `resultado = nome_funcao(argumentos)`

## 9. Módulos vs Pacotes vs Bibliotecas

| Conceito | Definição |
|---|---|
| **Módulo** | Um arquivo `.py` com funções (ex: `sqlite3` — built-in) |
| **Pacote** | Conjunto de módulos em diretório (ex: `pandas`) |
| **Biblioteca** | Conjunto de pacotes, mais robusto (ex: `seaborn`, `matplotlib`) |

## 10. Pandas — manipulação de dados

Biblioteca open-source para manipulação de dados tabulares. Estrutura principal: **DataFrame** (linhas + colunas com índices).

### Tipos de dados do Pandas

| Tipo | Descrição |
|---|---|
| **int64** | Inteiros (viram float64 se tiver NaN) |
| **float64** | Decimais |
| **object** | Texto |
| **datetime[ns]** | Datas (pode precisar conversão manual) |

### Leitura e resumo

```python
import pandas as pd
df = pd.read_csv('caminho.csv')
```

| Função | Descrição |
|---|---|
| `.head(n)` | Primeiras n linhas (padrão 5) |
| `.tail(n)` | Últimas n linhas |
| `.dtypes` | Tipos das colunas |
| `.info()` | Linhas, colunas, non-null, tipos |
| `.shape` | Tupla (linhas, colunas) |

### Seleção/filtragem

| Função | Descrição |
|---|---|
| `.iloc[inicio:fim]` | Seleção por índice numérico (fatia) |
| `.loc[condicao]` | Seleção por condição booleana |
| `.query('expressão')` | Filtro por string de condição |

**Acessar coluna:** `df['coluna']`

### Operações e agregação

| Função | Descrição |
|---|---|
| `.sum()` | Soma |
| `.mean()` | Média |
| `.median()` | Mediana |
| `.var()` | Variância |
| `.std()` | Desvio padrão |
| `.value_counts(normalize=True)` | Contagem (ou proporção) |
| `.groupby('col')['col2'].função()` | Agrupa e agrega |

### Manipulação

| Função | Descrição |
|---|---|
| `.drop('col', axis=1)` | Remove coluna (axis=0 para linha) |
| `.rename({'antigo': 'novo'}, axis=1)` | Renomeia coluna |
| `.sort_values('col', ascending=False)` | Ordena |
| `.reset_index()` | Redefine índice |

**`inplace=True`** torna operação definitiva (senão precisa `df = df.drop(...)`)

### Operações com strings

| Função | Descrição |
|---|---|
| `.str.lower()` | Minúsculas |
| `.str.upper()` | Maiúsculas |
| `.str.contains('texto') | Verifica substring |

### Exportação

- `.to_csv('arquivo.csv')` — exporta DataFrame

## 11. Visualização de dados — Seaborn e Matplotlib

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

| Gráfico | Função | Uso |
|---|---|---|
| **Barras** | `sns.barplot(data=, x=, y=)` | Comparar categorias (valores) |
| **Contagem** | `sns.countplot(data=, x= ou y=)` | Frequência de categorias |
| **Histograma** | `sns.histplot(data=, x=, kde=True)` | Distribuição de valores |
| **Boxplot** | `sns.boxplot(data=, x=, y=)` | Mediana, quartis, outliers |
| **Dispersão** | `sns.scatterplot(data=, x=, y=, hue=)` | Relação entre 2 variáveis |
| **Mapa de calor** | `sns.heatmap(data=, annot=True)` | Correlação entre variáveis |

**Customização:** `ax.set_title()`, `ax.set_xlabel()`, `ax.set_ylabel()`, `plt.xticks(rotation=90)`, `plt.show()`

**Pegadinha:** negativos = saída da conta; positivos = entrada. Filtrar outliers antes de plotar.

## 12. Testes de hipóteses (SciPy)

```python
from scipy.stats import normaltest, ttest_1samp, ttest_ind
```

| Teste | Função | Hipóteses |
|---|---|---|
| **Normalidade** | `normaltest(amostra)` | H0: segue normal / H1: não segue |
| **1 amostra** | `ttest_1samp(amostra, media, alternative='two-sided')` | H0: média igual à populacional |
| **2 amostras** | `ttest_ind(a, b, alternative='two-sided')` | H0: médias são iguais |

**Critério de decisão:** se `pvalor < alpha (0.05)` → rejeita H0.

**Quando usar t de Student:** amostra < 30 e desvio padrão populacional desconhecido.

## 13. Análise preditiva e Machine Learning

### Tipos de aprendizado

| Tipo | Característica | Exemplo |
|---|---|---|
| **Supervisionado** | Dados rotulados (features → target) | Regressão, Classificação |
| **Não supervisionado** | Sem target conhecido | Clusterização |

- **Regressão:** prevê valor contínuo (ex: preço do imóvel)
- **Classificação:** prevê categoria (ex: sim/não, churn)

### Treino vs Teste (Holdout)

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

- **Treino:** modelo aprende padrões
- **Teste:** avalia generalização (dados não vistos)
- **Overfitting:** modelo decora treino, ruim em teste (muito complexo)
- **Underfitting:** modelo simples demais, ruim em ambos

### Regressão Linear

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)          # treina
y_pred = model.predict(X_test)       # prediz
```

**Métricas:** R², MAE, MSE, RMSE (`np.sqrt(MSE)`)

### Regressão Logística (Classificação binária)

```python
from sklearn.linear_model import LogisticRegression
```

Modela probabilidade entre 0 e 1; **cutoff = 0.5** (≥ 0.5 classe 1, < 0.5 classe 0).

**Matriz de confusão:**
- VP (Verdadeiro Positivo), VN (Verdadeiro Negativo)
- FP (Falso Positivo), FN (Falso Negativo)

**Métricas:** Acurácia, Precisão, Revocação (Recall), F1-Score

### Clusterização com K-Means

```python
from sklearn.cluster import KMeans
```

1. Define K (número de clusters) via **método Elbow**
2. Inicializa centróides
3. Atribui observações ao centróide mais próximo
4. Recalcula centróides
5. Repete até convergir

**PCA** — reduz dimensionalidade para visualizar clusters (> 2 variáveis):
```python
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df)
```

---

## Pontos de reforço pessoal (quiz traps)

- **`=` vs `==`** — atribuição vs comparação; erro clássico dentro de `if`
- **`int64` vira `float64` com NaN** — NaN é float em Pandas
- **if vs elif** — `if` sempre executa; `elif` só se anteriores falsas (use para exclusão mútua)
- **`.drop()` não é inplace por padrão** — precisa `inplace=True` ou `df = df.drop(...)`
- **`shape[0]` vs `shape[1]`** — linhas (índice 0) e colunas (índice 1)
- **Cutoff da regressão logística** — é 0.5, não a probabilidade em si que decide
- **Overfitting** — bom em treino, ruim em teste (memorizou, não generalizou)
- **p-valor < alpha → rejeita H0** — não o contrário

---

## Conexões com o Desafio Final (dbt + Power BI)

- O notebook de Python serve para **análise exploratória** antes/depois da modelagem no dbt — entender distribuições, outliers, correlações das tabelas BanVic
- A **análise preditiva** (regressão logística, K-Means) complementa o dbt: enquanto o dbt modela dados para o dashboard, Python pode gerar insights preditivos que alimentam o Power BI
- O **export de dados tratados** (`to_csv`) é a ponte entre Python e Power BI — CSV tratado → dataset do Power BI
- Os **testes de hipóteses** validam estatisticamente insights antes de colocá-los no dashboard (evita mostrar correlação espúria)
- O padrão **treino/teste** do ML reforça a lógica de staging/marts do dbt: dados brutos (raw) → staging (limpeza) → marts (modelo final validado)
