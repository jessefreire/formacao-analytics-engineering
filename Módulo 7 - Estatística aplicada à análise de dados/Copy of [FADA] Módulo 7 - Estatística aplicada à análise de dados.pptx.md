Training in: Data analysis Module 7 - Statistics applied to data analysis 







Hello! 

My name is Renata. Tech Lead for data analysis 

I have been at Indicium for three years, working as an analytics engineer, and I am currently part of the Data Analysis team. 





<!-- Start of picture text -->
gA\\<br><!-- End of picture text -->

#### **WELCOME!** 

3 



### **THE MODULE** 

This module is divided into three parts, each consisting of a varying number of lessons. At the end of this module, there is a quiz on the topics covered. 







**Part 1** Exploratory Data Analysis. 

**Part 2** Probability. 

**Part 3 Inference.** 

4 



<!-- Start of picture text -->
WON pee «OS<br>,<br>bs i Fe iy<br>og |<br><!-- End of picture text -->

###### **STATISTICS APPLIED TO DATA ANALYSIS** 

###### **<mark>PART 1</mark>** 

- Introduction to the Module 

- **Descriptive** analysis 

- Measures of **central tendency** 

- ● **Dispersion** measures 

- **Association** measures 

- Data visualization with **Histograms** and **Box plots** 



5 

###### **STATISTICS APPLIED TO DATA ANALYSIS** 

###### **<mark>PART 2</mark>** 

- **Random** phenomena 

- Introduction to **probability** 

- Mathematical **formalization** 

- **Conditional probability** 

- **Random variables** 

- **Discrete probability distributions** 

- **Normal distribution** 

- **Non-normal distribution** 





6 



<!-- Start of picture text -->
> oN >| Coens~<br>us ><br>|<br>Ah C4 " ”<br>aft N<br>indicium® \ pan / rin” yy<br>4 ‘ne | —<br>a3<br>f<br><!-- End of picture text -->

###### **STATISTICS APPLIED TO DATA ANALYSIS** 

###### **<mark>PART 3</mark>** 

- Introduction to inference 

- **Estimation** 

- **Sample distribution** 

- **Confidence intervals** 

- **Hypothesis testing** 

- Hypothesis testing with **unknown variance** 

- **Sampling** 

- **Experiments** 

- **Regression** 

- **Common errors** in regression 

7 

> <sup>(DN</sup> 8 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **INTRODUCTION** 

9 



###### **INTRODUCTION** 

- What is statistics? 



10 



###### **INTRODUCTION** 

- What is statistics? 

- Why statistics are important; 



11 



###### **INTRODUCTION** 

- What is statistics? 

- Why statistics are important; 

- Randomness all around us; 



<!-- Start of picture text -->
a DOV) OaelanS<br>Jeg<br><!-- End of picture text -->

12 



###### **INTRODUCTION** 

- What is statistics? 

- Why statistics are important; 

- Randomness all around us; 

- How to think probabilistically; 



13 



###### **INTRODUCTION** 

- What is statistics? 

- Why statistics are important; 

- Randomness all around us; 

- How to think probabilistically; 

- Precision vs. Accuracy; 



14 



###### **INTRODUCTION** 

- What is statistics? 

- Why statistics are important; 

- Randomness all around us; 

- How to think probabilistically; 

- Precision vs. Accuracy; 

- Use of formulas and Greek letters; 



15 



###### **INTRODUCTION** 

- What is statistics? 

- Why statistics are important; 

- Randomness all around us; 

- How to think probabilistically; 

- Precision vs. Accuracy; 

- Use of formulas and Greek letters; 

- Python statistical packages and examples. 



16 

> <sup>(DN</sup> 17 





#### **PART 1: EXPLORATORY DATA ANALYSIS** 

18 





#### **DESCRIPTIVE ANALYSIS** 

19 



###### **What it is** 

Area of statistics that deals with the description and summary of numerical data. 

Describe the characteristics of the data to be analyzed. 

**Descriptiv e Analysis** 

###### **How it works** 

This is usually the first manipulation performed on the data. This can be done using frequency tables, graphs, and numerical summary measures. Does not make inferences about the population. 

20 



###### **DESCRIPTIVE ANALYSIS** 

|**Contributor**|**State**|**Education**|**Salary**|
|---|---|---|---|
|1|SP|Medium|R$ 1.400,00|
|2|SP|Complete Superior|R$ 3.800,00|
|3|SC|Master's Degree|R$ 5.000,00|
|4|MG|Complete Superior|R$ 2.500,00|
|5|SP|Medium|R$ 1.400,00|
|6|MG|Medium|R$ 1.400,00|
|7|SC|Complete Superior|R$ 2.500,00|
|8|RJ|Medium|R$ 1.400,00|
|9|SC|Complete Superior|R$ 2.500,00|
|10|SP|Master's Degree|R$ 3.800,00|



21 



###### **ANÁLISE DESCRITIVA** 

|**Contributor**|**State**|**Education**|**Salary**||
|---|---|---|---|---|
|1|SP|Medium|R$ 1.400,00||
|2|SP|Complete Superior|R$ 3.800,00|Média = R$ 2.570,00|
|3|SC|Master's Degree|R$ 5.000,00||
|4|MG|Complete Superior|R$ 2.500,00|Mediana = R$ 2.500,00|
|5|SP|Medium|R$ 1.400,00||
|6|MG|Medium|R$ 1.400,00|Moda = R$ 1.400,00|
|7|SC|Complete Superior|R$ 2.500,00|Desvio Padrão = R$ 1.200,87|
|8|RJ|Medium|R$ 1.400,00||
|9|SC|Complete Superior|R$ 2.500,00||
|10|SP|Master's Degree|R$ 3.800,00||



22 



<!-- Start of picture text -->
(aN<br><!-- End of picture text -->

###### **DESCRIPTIVE ANALYSIS** 



<!-- Start of picture text -->
Number of employees by level of education Salaries boxplot<br>3<br>.<br>g2?: a eee<br>::<br>1<br>; _<br>Medium Complete superior Master’s degree<br>Salarios (RS)<br><!-- End of picture text -->

23 



###### **DESCRIPTIVE ANALYSIS** 

###### **Advantages** 

- ✓ The results are objective and neutral; 

- ✓ Brings impartiality to the study; 

- ✓ It is considered expansive; 

- ✓ Provides a broad view of a phenomenon; 

- ✓ It allows you to create hypotheses based on the data. 

###### **Disadvantages** 

- ✓ Difficulty in generalizing the results; 

- ✓ It does not allow testing hypotheses or establishing causal relationships between variables; 

- ✓ It can be influenced by external factors; 

- ✓ It may be insufficient to explain complex phenomena. 

24 

> <sup>(DN</sup> 25 





#### **MEASURES OF CENTRAL TENDENCY** 

26 



###### **How we use** 

**Measures of central tendency** 

They represent, in some way, the center or "average" of a data set. They are used in statistics to summarize and describe data sets. 

**Who are they?** 

**Mean:** the sum of all data divided by the number of values; **Median:** the value that divides the data set in half; 

**Mode:** the value that occurs most frequently. 

27 



###### **MEASURES OF CENTRAL** 

###### **TENDENCY** 

|**Contributor**|**Height(xi)**|
|---|---|
|1|1,88|
|2|1,8|
|3|1,68|
|4|1,5|
|5|1,79|
|6|1,78|
|7|1,69|
|8|1,72|
|9|1,79|
|10|1,77|





<!-- Start of picture text -->
hn<br>xx.<br>OX<br>~ ~<br>H EX Haex, 2M<br>n n<br><!-- End of picture text -->

Média = 1,74m 

28 



###### **MEDIDAS DE TENDÊNCIA CENTRAL** 

|**Contributor**|**Height(xi)**|**Height(xi) ordered**|
|---|---|---|
|1|1,88|1,5|
|2|1,8|1,68|
|3|1,68|1,69|
|4|1,5|1,72|
|5|1,79|1,77|
|6|1,78|1,78|
|7|1,69|1,79|
|8|1,72|1,79|
|9|1,79|1,8|
|10|1,77|1,88|



###### Median: 

- Sort the height values from highest to lowest; 

- Select the central value; 

- If the number of values is even, take the 

average of the two middle values. 

Median = 1,77 + 1,78 

2 

Median = 1,775m 

29 



###### **MEASURES OF CENTRAL** 

###### **TENDENCY** 

|**Contributor**|**Height(xi)**|
|---|---|
|1|1,88|
|2|1,8|
|3|1,68|
|4|1,5|
|5|1,79|
|6|1,78|
|7|1,69|
|8|1,72|
|9|1,79|
|10|1,77|



###### Mode: 

- It is the most frequently occurring value in the data set; 

|1,88|1,8|1,68|1,5|1,79|1,78|1,69|1,72|1,77|
|---|---|---|---|---|---|---|---|---|
|1|1|1|1|2|1|1|1|1|



###### Mode = 1,79m 

30 



###### **MEASURES OF CENTRAL** 

###### **TENDENCY** 



<!-- Start of picture text -->
Mean= 1,74m<br><!-- End of picture text -->

31 



###### **MEDIDAS DE TENDÊNCIA CENTRAL** 



<!-- Start of picture text -->
Bar Chart of Heights<br>10<br>8<br>€<br>3 6<br>3<br><<br>4<br>2<br>0<br>150 155 160 165 170 175 180 185 1.90<br>Height (m)<br><!-- End of picture text -->



<!-- Start of picture text -->
Média = 1,74m<br>Mediana = 1,775m<br><!-- End of picture text -->

32 



###### **MEDIDAS DE TENDÊNCIA CENTRAL** 



<!-- Start of picture text -->
Bar Chart of Heights<br>10<br>8<br>=<br>3 6<br>=<br><<br>4<br>2<br>0<br>1.50 155 1.60 1.65 1.70 175 1.80 1.85 1.90<br>Height (m)<br><!-- End of picture text -->



<!-- Start of picture text -->
Média = 1,74m<br>Mediana = 1,775m<br>Moda = 1,79m<br><!-- End of picture text -->

33 



<!-- Start of picture text -->
(Fa<br><!-- End of picture text -->

###### **MEASURES OF CENTRAL** 

###### **TENDENCY** 

###### **Which measure should be used?** 

- ✓ Data characteristics 

- ✓ The more asymmetrical, the greater the difference between 

**Média: R$ 1353,00** <mark>{</mark> 98 (1100 6s 45 (-)125 31 56 56 47 45 (157 078 

**Mediano: R$ 810,00** 

measurements. 

- ✓ Outliers influence 

34 



###### **MEASURES OF CENTRAL TENDENCY - Example** 



<!-- Start of picture text -->
*<br>*<br><!-- End of picture text -->



<!-- Start of picture text -->
8000<br>7000<br>6000<br>5000<br>3000<br>2000<br>1000<br>0<br>—1000 —800 —600 —400 —200 Oo<br><!-- End of picture text -->



35 



###### **SUMMARIZING** 

The three main measures of central tendency are: 

- **Mean** : sum of all values in the data set divided by the number of values. 

- **Median** : value that divides the data set in half. 

- **Mode** : most frequent value. 



36 

> <sup>(DN</sup> 37 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **Dispersion measures** 

38 



###### **How we use** 

We use it to understand how our data is distributed in relation to measures of central tendency. 

They will make more sense when compared with other data sets. 

## **Dispersion measures** 

**Who are they?** 

**Range:** the difference between the highest and lowest values in the data set. 

**Simple deviation:** the distance of each height from the mean; 

**Variance:** is the square of the deviations; 

**Standard Deviation:** is the square root of the variance. 

**Coefficient of Variation:** it is the division between the standard deviation and the mean. 

39 



###### **Dispersion measures - Amplitude** 

|Contributor|Height (xi)|
|---|---|
|1|1,88|
|2|1,8|
|3|1,68|
|4|1,5|
|5|1,79|
|6|1,78|
|7|1,69|
|8|1,72|
|9|1,79|
|10|1,77|



Amplitude = 1,88cm - 1,50cm Amplitude = 38cm 

40 



###### **MEDIDAS DE DISPERSÃO - DESVIO SIMPLES** 

|Contributor|Height (xi)|_xi_-_̄x_||_xi_-_̄x_||
|---|---|---|---|
|1|1,88|0,14|0,14|
|2|1,8|0,06|0,06|
|3|1,68|-0,06|0,06|
|4|1,5|-0,24|0,24|
|5|1,79|0,05|0,05|
|6|1,78|0,04|0,04|
|7|1,69|-0,05|0,05|
|8|1,72|-0,02|0,02|
|9|1,79|0,05|0,05|
|10|1,77|0,03|0,03|



= Simple deviation mn x Ix, i=1 Simple Deviation = 0,06cm 

41 



###### **MEASURES OF DISPERSION - VARIANCE** 

|Contributor|Height (xi)|_xi_-_̄x_||_xi_-_̄x_||(_xi_-_x_)<sup>2</sup>|
|---|---|---|---|---|
|1|1,88|0,14|0,14|0,0196|
|2|1,8|0,06|0,06|0,0036|
|3|1,68|-0,06|0,06|0,0036|
|4|1,5|-0,24|0,24|0,0576|
|5|1,79|0,05|0,05|0,0025|
|6|1,78|0,04|0,04|0,0016|
|7|1,69|-0,05|0,05|0,0025|
|8|1,72|-0,02|0,02|0,0004|
|9|1,79|0,05|0,05|0,0025|
|10|1,77|0,03|0,03|0,0009|



Variance ==FZ,7 Variance = 0,0098cm<sup>2</sup> 

42 



###### **Dispersion measures - Standard deviation** 

|Contributor|Height (xi)|_xi_-_̄x_||_xi_-_̄x_||(_xi_-_x_)<sup>2</sup>|
|---|---|---|---|---|
|1|1,88|0,14|0,14|0,0196|
|2|1,8|0,06|0,06|0,0036|
|3|1,68|-0,06|0,06|0,0036|
|4|1,5|-0,24|0,24|0,0576|
|5|1,79|0,05|0,05|0,0025|
|6|1,78|0,04|0,04|0,0016|
|7|1,69|-0,05|0,05|0,0025|
|8|1,72|-0,02|0,02|0,0004|
|9|1,79|0,05|0,05|0,0025|
|10|1,77|0,03|0,03|0,0009|



Standard deviation 

Standard Deviation = 0,097cm 

43 



###### **MEASURES OF DISPERSION - COEFFICIENT OF** 

###### **VARIAT** **~~ION~~** 

|Contributor<br>|Height (xi)|_xi_-_̄x_||_xi_-_̄x_||(_xi_-_x_)<sup>2</sup>|
|---|---|---|---|---|
|1|1,88|0,14|0,14|0,0196|
|2|1,8|0,06|0,06|0,0036|
|3|1,68|-0,06|0,06|0,0036|
|4|1,5|-0,24|0,24|0,0576|
|5|1,79|0,05|0,05|0,0025|
|6|1,78|0,04|0,04|0,0016|
|7|1,69|-0,05|0,05|0,0025|
|8|1,72|-0,02|0,02|0,0004|
|9|1,79|0,05|0,05|0,0025|
|10|1,77|0,03|0,03|0,0009|





<!-- Start of picture text -->
: ay dp<br>coef.variacgao(cv) = ——<br>x<br><!-- End of picture text -->

cv = 5,57% 

44 



###### **Dispersion Measures - How to Interpret Them** 



Lower dispersion measures with values close to the mean/median/mode 



Higher dispersion measures with values far from the mean/median/mode 

45 



###### **SUMMARIZING** 

Dispersion measures indicate the variability of the observed data. 

The main dispersion measures are: 

- **Amplitude:** measures the difference between the largest and smallest values in a data set; 

- **Average Deviation:** calculates the average of the absolute deviations from the mean; 

- **Variance:** is one of the most important measures in statistics and is calculated by averaging the sum of the squares of the deviations from the mean; 

- **Standard Deviation:** is the square root of the variance; 

- **Coefficient of Variation:** has no dimension and is generally used to compare data sets with different measurements (e.g., weight and height). 

46 

> <sup>(DN</sup> 47 





#### **ASSOCIATION MEASURES** 

48 

###### **ASSOCIATION MEASURES** 



<!-- Start of picture text -->
= Q exame, FUTURE OF MONEY €<br>Future of Money<br>Home<br>> Futureof Money<br>Comportamento do prego do bitcoin atinge<br>maior correlagdo como ouro da historia<br>Criptomoeda teve melhor trimestre em dois anos, e analistas atribuem parte da sua alta ao<br>fortalecimento da tese de que ativo seria reserva de valor<br>ORB@av<ce Modo escuro<br><!-- End of picture text -->



**49** 

###### **ASSOCIATION MEASURES** 





<!-- Start of picture text -->
—— Bitcoin<br>—— Ouro<br>24000<br>19.5<br>23000<br>19.0<br>22000<br>21000 aa<br>20000 18.0<br>19000 175<br>18000 17.0<br>17000 ies<br>omyo om aca45aaar 4°>40°98 oe or95 ot 4°.<br>Da a a a ai ai Sia La<br><!-- End of picture text -->

**50** 

###### **ASSOCIATION MEASURES** 

|**Contributor**|**Height(x)**|**Weight(y)**|
|---|---|---|
|1|1,88|95|
|2|1,8|90|
|3|1,68|77|
|4|1,5|55|
|5|1,79|70|
|6|1,78|103|
|7|1,69|68|
|8|1,72|75|
|9|1,79|70|
|10|1,77|70|
|Mean<br>|**1,74**<br>|**77,3**<br>|
|Standard deviation<br>~~e~~|**0,097**<br>|**13,726**<br>~~e~~|







<!-- Start of picture text -->
s<br>e 7<br>eo te<br>e ee<br>17 18<br>Altura (x)<br><!-- End of picture text -->

**51** 

###### **ASSOCIATION MEASURES** 

###### **Positive Correlation** 

###### **Negative Correlation** 



**52** 

###### **ASSOCIATION MEASURES** 

|A|B|C|D|E|F|
|---|---|---|---|---|---|
|Contributor|Height (x)|Weight (y)||||
|1|1,88|95|1,44|1,29|1,85|
|2|1,8|90|0,62|0,93|0,57|
|3|1,68|77|-0,62|-0,02|0,01|
|4|1,5|55|-2,46|-1,62|4,00|
|5|1,79|70|0,51|-0,53|-0,27|
|6|1,78|103|0,41|1,87|0,77|
|7|1,69|68|-0,51|-0,68|0,35|
|8|1,72|75|-0,21|-0,17|0,03|
|9|1,79|70|0,51|-0,53|-0,27|
|10|1,77|70|0,31|-0,53|-0,16|
|**Mean**|**1,74**|**77,3**||**Total**|**6,88**|
|**Standard deviation**|**0,097**|**13,726**||**Correlation**|**0,688**|





**53** 

###### **ASSOCIATION MEASURES** 



<!-- Start of picture text -->
r@,-x)0,-y)<br>i=l<br>Pry —_ a<br><!-- End of picture text -->





<!-- Start of picture text -->
— x), —y)-<br><!-- End of picture text -->

**54** 

###### **CORRELATION IS NOT CAUSATION** 



<!-- Start of picture text -->
Sun makes the earth produce more<br>Earth produces more Sun A ‘<br><!-- End of picture text -->



**55** 

###### **SPURIOUS CORRELATION** 







**56** 

###### **SPURIOUS CORRELATION** 



<!-- Start of picture text -->
Per capita consumption of mozzarella cheese =<br>correlates with<br>Civil engineering doctorates awarded<br>Correlation: 95.86% (r=0.958648)<br>2000 2001 2002 2003 2004 2005 2006 2007 2008 2009<br>12lbs 1000 degrees<br>3<br>2lls 800 degrees g<br>5<br>Z0tte 600degrees 5<br>SIbs 400 dezrees<br>2000 2001 2002 2003 2004 2005 2006 2007 2008 2009<br>-@ Engineering doctorates -# Mozzarella cheese consumption<br><!-- End of picture text -->

Fonte: <u><mark>tylervigen.com</mark></u> 

**57** 

###### **CORRELATION** 



<!-- Start of picture text -->
—— Bitcoin<br>—— Ouro<br>45000 24<br>40000 22<br>35000<br>20<br>30000<br>1s<br>25000 i<br>6<br>20000<br>4<br>psOS P=5 epee1082 Sh01 a0% aeos) Oeio aye0? oaOe0) aah0!<br>9 Sh Shh ohh gph apt gh” 49?" 49?" at<br><!-- End of picture text -->



<!-- Start of picture text -->
=<br>24 ° é<br>*® e<br>o ©<br>22 °<br>2<br>- ><br>ee oot, e<br>e ee° %ee e e<br>18 ‘4 e e é e<br>® ° e<br>&<br>% °<br>wf} e . %°<br>e bad<br>° 3<br>eo<br>14 se<br>20000 25000 30000 35000 + 40000 +=. 45000<br><!-- End of picture text -->

**58** 

###### **SUMMARIZING** 

- ➢ Association measures help us understand how two variables relate to each other; 

- ➢ The correlation coefficient is a very popular measure of association; 

- ➢ The correlation coefficient value is always between -1 and 1. A correlation close to zero indicates no linear association between two variables. 

- ➢ Correlation does not imply causation; 

- ➢ There are many variables correlated for random reasons, known as spurious correlation. 



59 

> <sup>(DN</sup> 60 





#### **DATA VISUALIZATION** 

61 

###### **DATA VISUALIZATION** 

- Histograms 

   - ➢ Column charts; 

   - ➢ Built from a frequency table; 

   - ➢ Composed of: 

      - Class; 

      - Interval; 

      - Frequency/density. 





<!-- Start of picture text -->
1200<br>1000<br>>, 800<br>Fs2S= Frecuancy<br>600<br>& o Dewety<br>x<br>400<br>200 Class<br>t<br>0 o-<br>-200...,-v -1500 -1250 -1000 -750 -500 -250-' 0<br>Transaction Value<br><!-- End of picture text -->

62 

###### **DATA VISUALIZATION** 

- Scatter plots 

- ➢ Measures the association between two continuous variables; 

- ➢ Used to identify correlations between variables. 





<!-- Start of picture text -->
100<br>95<br>90<br>85<br>80<br>2 a 6 8 10 12 14 16<br><!-- End of picture text -->

63 

###### **DATA VISUALIZATION** 

###### Box plot 

- ➢ Used to visualize data distribution; 

- ➢ They are a representation of the main descriptive statistics. 





<!-- Start of picture text -->
Highest<br><—_ cteervec value tens than<br>: or equal to @3 +<br>: 1510<br>20th Quartile :<br>(Q3)<br>Median<br>Amplitude<br>Interquartil<br>(1a)<br>Oth Quartile<br>(on o-~—<br>H The smallest<br>° or equalto. 01-1.510<br>The Outlier<br><!-- End of picture text -->

64 

###### **DATA VISUALIZATION** 





<!-- Start of picture text -->
t)<br>-200<br>g<br>S -400<br>5<br>& -600<br>£<br>'<br>-800 { ry<br>.<br>1000 id ¢<br>Purchase Debit PurchaseTransactionCredit Realized Type Pix Sake<br><!-- End of picture text -->

Note: amounts greater than R$1,000 were filtered for ease of viewing. 

65 

> <sup>(DN</sup> 66 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **PART 2: PROBABILITY** 

67 





#### **INTRODUCTION TO PROBABILITY** 

68 

###### **RANDOM PHENOMENA** 

These are events or occurrences whose outcomes cannot be predicted with certainty. 





<!-- Start of picture text -->
=*<br>><br>,<br>- s °<br><!-- End of picture text -->

69 

###### **INTRODUCTION TO PROBABILITY** 

###### **Classical probability** 



<!-- Start of picture text -->
RRS:<br>roaoN >Pst.<br>Gar<br>ae<br><!-- End of picture text -->



<!-- Start of picture text -->
Jacob Bernoulli<br><!-- End of picture text -->



<!-- Start of picture text -->
<<br>:<br><!-- End of picture text -->



<!-- Start of picture text -->
Pascal<br><!-- End of picture text -->



<!-- Start of picture text -->
di<br>Whoe<br>i) A”<br><!-- End of picture text -->



<!-- Start of picture text -->
Laplace<br><!-- End of picture text -->

The probability of an event occurring is the frequency with which the event is expected to occur in relation to all possible events. 

70 

###### **INTRODUCTION TO PROBABILITY** 

###### **Classical probability** 



<!-- Start of picture text -->
1/6 1/6 1/6 1/6 1/6 1/6<br><!-- End of picture text -->

The probability of an event occurring is the frequency with which the event is expected to occur in relation to all possible events. 



71 

###### **INTRODUCTION TO PROBABILITY** 

###### **Classical probability** 



<!-- Start of picture text -->
1/6 1/6 1/6 1/6 1/6 1/6<br><!-- End of picture text -->

The probability of an event occurring is the frequency with which the event is expected to occur in relation to all possible events. 



72 

###### **INTRODUCTION TO PROBABILITY** 

# **Frequentist Probability** Sample Space =<sup>LICIC</sup> 



73 

###### **INTRODUCTION TO PROBABILITY** 

###### **Frequentist Probability** 

Event (1x3) = Event (2x3) = Event (odd) = 





<!-- Start of picture text -->
G2)<br><!-- End of picture text -->

74 



<!-- Start of picture text -->
INTRODUCTION TO PROBABILITY<br>Frequentist Probability<br>Games (experiments) Result Probability (Die = 3)<br>1 1/1 = 100%<br>2 1/2 = 50%<br>5 2/5 = 40%<br>1000 (...) 166/1000 => ⅙ =16,66%<br>75<br><!-- End of picture text -->

###### **SUMMARIZING** 

Probabilities depend on well-designed experiments; 

✔ Sample space: set of all possible outcomes; 

✔ Event: subset of the sample space; 

- ✔ Probability: relative frequency of occurrence of an event based on multiple repetitions of an experiment. 



76 

> <sup>(DN</sup> 77 





#### **MATHEMATICAL FORMALIZATION** 

78 



###### **MATHEMATICAL FORMALIZATION** 

##### P(A) = Count of "3" / Total number of entries 



79 

###### **MATHEMATICAL FORMALIZATION** 



<!-- Start of picture text -->
és P(AUB)<br><!-- End of picture text -->



<!-- Start of picture text -->
(Gara<br>+ P(B) — P(A B)<br><!-- End of picture text -->

80 

###### **MATHEMATICAL FORMALIZATION** 





<!-- Start of picture text -->
Espaco Amostral = Todas as pessoas<br>Mulher (40 — 50anos)<br>& & Q a) é<br>& & Mulher 2 (40 — 50anos) é é<br>, wl<br>g & f<br>& @ raf<br><!-- End of picture text -->

81 

> <sup>(DN</sup> 82 





#### **CONDITIONAL PROBABILITY** 

83 



<!-- Start of picture text -->
Gos<br>CONDITIONAL PROBABILITY<br>Door A<br>Door B Door C<br><!-- End of picture text -->

###### **CONDITIONAL PROBABILITY** 



84 



<!-- Start of picture text -->
CONDITIONAL PROBABILITY<br>1/3 X ½ = 1/6 Loss<br>1/2<br>Porta B<br>1/3<br>1/2<br>1/3 X ½ = 1/6 Loss<br>Porta A<br>Porta C<br>1<br>1/3<br>1/3 X 1 = 1/3 Win<br>Porta B Porta C<br>1<br>1/3 X 1 = 1/3 Win<br>1/3<br>Porta C<br>Porta B<br>85<br><!-- End of picture text -->

###### **CONDITIONAL PROBABILITY** 





<!-- Start of picture text -->
_ _P(ANB)<br><!-- End of picture text -->



<!-- Start of picture text -->
arc<br>1/6<br>Ee 17/3<br>Fp+ie 13  7 2/3<br><!-- End of picture text -->

86 

> <sup>(DN</sup> 87 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **RANDOM VARIABLES** 

88 

###### **RANDOM VARIABLES** 

It is a variable that assumes values with a certain probability; 

✓ Discrete: when it takes integer values; 

   - E.g.: rolling a die, number of children, whether or not fraud occurs; 

- ✓ Continuous: when it takes values within the set of real numbers; E.g.: time, value of a bank transaction, height. 



89 



###### **PROBABILITY FUNCTION** 



<!-- Start of picture text -->
>) =<br><!-- End of picture text -->



<!-- Start of picture text -->
P(X =x) =—=— 1 1 w 16,66%<br>i n 6<br><!-- End of picture text -->



<!-- Start of picture text -->
Probability in a Dice Game<br>0.200<br>0.175 °°°<br>'1 ' ' ' '<br>0.507" | H H H H H<br>.111<br>2=3 ars0: |<br>“7 ' 1 ' ' ' '<br>® 0.100 ! ' ' i ' !<br>{ { i H H i<br>0.0754: 1| 1H 'H H1 H1 '1<br>1 1 1 ' 1 1<br>0.0504 | H H H H H<br>'1'<br>'' ' ! ' '<br>0.0257 | i H H H '<br>'''<br>'1 ' i ' '<br>0.000<br>1 2 3 4 5 6<br>Result<br><!-- End of picture text -->

90 

###### **CUMULATIVE PROBABILITY FUNCTION** 



<!-- Start of picture text -->
F(X) = P(X <x)<br><!-- End of picture text -->

|Result|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|P(X=x)|1/6|1/6|1/6|1/6|1/6|1/6|
|P(X<x)|1/6|2/6|3/6|4/6|5/6|6/6=1|







<!-- Start of picture text -->
Cumulative Probability Distribution Function - Dice Game<br>Lo<br>0.8<br>;<br>c 0.4<br>0.2<br>0.0<br>1 2 34 5 6<br><!-- End of picture text -->

91 

###### **SUMMARIZING** 

- ✓ Random Variable: any quantity X that assumes values with a certain probability; 

- ✓ A discrete random variable is one that can only take on integer values, for example, the roll of a die or the number of children in a family. 

- ✓ A continuous random variable is one that can take any value in an interval; 

- ✓ To calculate the probability of a specific value, we use a probability function; 

- ✓ In addition to the probability that X has a specific value, it is also useful to calculate the sum of the cumulative probabilities of X, called the cumulative distribution function. 



92 

> <sup>(DN</sup> 93 





#### **DISTRIBUTION OF DISCRETE PROBABILITY** 

94 

###### **DISTRIBUTION OF DISCRETE PROBABILITY** 

These are probability distributions used for discrete random variables; 

**1. Uniform Distribution** : the results have the same probability of occurring 



<!-- Start of picture text -->
1<br>P(X =x) =><br>u eB<br><!-- End of picture text -->





<!-- Start of picture text -->
Uniform Distribution<br>0.14<br>0.12<br>sere Fee Fee ee<br>x'''''<br>><br>' 1 ' 1 ' ' ' 1 1 '<br>=25 0.08 eo'' '' @'' a'' @'' ‘a @¢' &' F' F&F'<br>e'1'''<br>a0.06 ' ' ' ' 1 ' ' ' '<br>'1'1'1<br>'' ' ' ' 1 ' ' ' '<br>0.047 a4'''''<br>'' ' ' ' ' ' ' ' '<br>a<br>0.0274 5PEt1 ' 1bod' 1gd 1do 1ppd1 1<br>' ' ' ' ' ' ' ' ' '<br>0.00<br>° 1 2 3 4 5 6 7 8 9<br>Result<br><!-- End of picture text -->

95 



<!-- Start of picture text -->
0,1,2,..,7<br><!-- End of picture text -->

###### **DISTRIBUTION OF DISCRETE PROBABILITY** 

**2. Bernoulli distribution** : single event of the success-failure 



<!-- Start of picture text -->
P(X =x) =p(1—p)<br><!-- End of picture text -->

**3. Binomial distribution** : number of repetitions of success-failure events 



<!-- Start of picture text -->
(i) = kin!<br><!-- End of picture text -->

Binomial coefficient: 



96 

###### **DISTRIBUTION OF DISCRETE PROBABILITY** 

**4. Geometric Distribution** : number of attempts until the first success occurs 



<!-- Start of picture text -->
P(X =x) = pl — p) k-1<br><!-- End of picture text -->



<!-- Start of picture text -->
p= 1-0,95 = 0,05e k=10<br><!-- End of picture text -->

**5. Poisson distribution** : average rate of occurrence of an event in a time or space interval 



<!-- Start of picture text -->
P(X=k) = +*,ew k=0,1,2..<br><!-- End of picture text -->



97 

###### **DISTRIBUTION OF DISCRETE PROBABILITY** 



<!-- Start of picture text -->
P(X=k) = +4, Aye k=0,1,2,.<br><!-- End of picture text -->

|k (number of<br>transactions)|0|1|2|3|4|5|6|k≤6|
|---|---|---|---|---|---|---|---|---|
|Probability(%)|1,11|5,0|11,25|16,87|18,98|17,08|12,81|83,10|



###### 𝝀 = 4.5 transactions per second 

P(k>6) = 1 - 83,10 = 16,89% 



98 

###### **SUMMARIZING** 

- ✓ Discrete Distribution: probability distributions used for random variables that only take **discrete values** such as <u><mark>number of occurrences, number of children,</mark></u> etc. 

- ✓ Uniform Distribution: used when any result has the <u><mark>same probability of occurrence,</mark></u> such as a dice game. 

- ✓ Bernoulli distribution: used to describe the outcome of a <u><mark>single success-failure event.</mark></u> 

- ✓ Binomial Distribution: used for <u><mark>repetitions of events</mark></u> of the success-failure type. 

- ✓ Geometric Distribution: used to calculate the <u><mark>number of attempts</mark></u> until the first occurrence of a successful event. 

- ✓ Poisson distribution: used to calculate the <u><mark>average occurrence rate</mark></u> of an event over a period of time or space. 



<!-- Start of picture text -->
space.<br><!-- End of picture text -->

99 

10<sup>(DN</sup> 0 





#### **NORMAL DISTRIBUTION** 

101 

###### **NORMAL DISTRIBUTION** 



<!-- Start of picture text -->
Se<br>\<br>\<br>Fae<br>a -<br>¢ =m ¥NGges f<br>a<br>4 4<br>‘ \<br><!-- End of picture text -->





<!-- Start of picture text -->
(Gat<br>n=10,p=0.5<br>6 7 8<br><!-- End of picture text -->

102 

###### **NORMAL DISTRIBUTION** 



<!-- Start of picture text -->
Ge<br>(S YJ<br>AN<br>C Foe<br>? = Nees<br>4<br>. cal<br><!-- End of picture text -->





<!-- Start of picture text -->
(Gat<br>n=100,p=0.5<br>50.0 52.5 55.0 57.5<br><!-- End of picture text -->

103 

###### **NORMAL DISTRIBUTION** 



<!-- Start of picture text -->
eS.)<br>i<br>\<br>< a ~\ ,<br>¢ ™ Nowy Ji<br>" a<br>‘<br>.<br><!-- End of picture text -->





<!-- Start of picture text -->
n=1000,p=0.5<br>520 540<br><!-- End of picture text -->

104 

###### **NORMAL DISTRIBUTION** 



<!-- Start of picture text -->
; —<br>\<br>Foe<br>? we NEGLI<br>"<br>y<br>. cal<br><!-- End of picture text -->





<!-- Start of picture text -->
(Gat<br>n=100000,p=0.5<br>50200 50400 50600 50800<br><!-- End of picture text -->

105 

###### **NORMAL DISTRIBUTION** 



<!-- Start of picture text -->
035 Distribuigao Binomial n=10,p=0.5<br>030<br>025<br>.<br># 020<br>2<br>r<br>3 os<br>—<br>020<br>0.05<br>0.00 3 4 3 6 1 8<br>Numero de Caras<br><!-- End of picture text -->



<!-- Start of picture text -->
Distribuicdo Binomial n=100,p=0.5<br>020<br>ig 0.08<br>3<br>zg<br>g 006<br>q<br>E<br>008<br>002<br>0.00 375 40.0 425 45.0 475 500 525 550 575<br>Numero de Caras,<br><!-- End of picture text -->





<!-- Start of picture text -->
(Gat<br>Distribuicao Binomial n=1000,p=0.5<br>0.030<br>0.025<br>‘<br>3 oo20<br>2<br>$<br>$ oo1s<br>&<br>oo10<br>0.005<br>50600 50800 0.000 460 48050052040<br>Numero de Caras<br><!-- End of picture text -->

106 



###### **NORMAL DISTRIBUTION** 





- ➢ Symmetric with respect to μ; 

- ➢ ƒ(x) tends to 0 in extreme cases; 

- ➢ The maximum density occurs when 𝑥 = 𝜇. 



107 

###### **STANDARD NORMAL DISTRIBUTION** 



<!-- Start of picture text -->
Z= X-<br>5<br><!-- End of picture text -->

The normal distribution with a mean of 0 and a standard deviation of 1 is called the Standard Normal. 





108 

###### **NORMAL DISTRIBUTION** 

- Suppose that the height of BanVic employees follows a normal distribution with a mean of 1.75 m and a standard deviation of 0.10 m. 𝖷 ~ 𝘕(𝜇 ＝1.75 , 𝜎² ＝0.1²) 

- What is the probability that an employee is between 1.90 and 2.10 meters tall? 

   - (1.90 ≤ 𝘟 ≤ 2.10) 



109 

###### **NORMAL DISTRIBUTION** 





<!-- Start of picture text -->
— 1,75)<br>)=P5 < Z < 3,5)<br><!-- End of picture text -->

110 

###### **NORMAL DISTRIBUTION** 

𝑃(1,5 ≤ 𝑍 ≤ 3,5)＝𝑃(𝑍 ≤ 3,5)﹣𝑃(1,5 ≤ 𝑍) 



<!-- Start of picture text -->
Probabilidade da Altura entre 1,9 e 2,1m<br>ag<br>803<br>3<br>3<br>Boz<br>'<br>oa<br>00 b<br>es ascore 1 2 3 4<br><!-- End of picture text -->



<!-- Start of picture text -->
Tabela da Distribui¢do Normal Padrao<br>P(Z<z)<br>|.0,0] 0,509] 0,5040| 0,5080] 0.5120] 0.5160] 0.5199] 0.5239] 0,5279| 0.5319] 0.5359<br>|0,1) 0.5398] 0.5436] 0.5478] 0.5517] 0.5557] 0.5596] 0.5636] 0,5675] 0,5714| 05753<br>| 0,2] 05793] 0,5832] 0.5871] 05910] 0.5948] 0,5987| 0,6026| 0.6064] 0,6103| 0.6141<br>| 0,3] 0,6179|_0,6217| 0,6255] 0,6293]_0,6331] 0.6368] 0.6406] 0,6443] 0,6480| 0.6517<br>| 0,4) 0,6554] 0,6591| 0,6628] 0,6664] 0,6700] 06736] 0,672 0,6808| 0,844] 0.6879<br>|0,5] 0.6915] 0.6950] 0,6985] 0,7019| 0.7054] 0.7088] 0.7123] 0,7157| 0,7190| 07224<br>| 0.6] 0,7257| 0,791] 0.7324] 0,7357| 0,7389| 0,7422| 0,7454| 0,7486| 0,7517| 0,7549<br>| 0.7] 0,7580|_0,7611] 0,7642| 0,7673| 0.7704] 07734] 0,764] 0.7794] 0.7823] 07852<br>| 0,8) 0.78811 0,7910| 0.7939] 0,7967| 0.7995] 0,8023|_0,8051| 0.8078] 0,8106| 0.8133<br>0,9] 0.8159] 0.8186] 0.8212] 0,8238| 0.8264] 0.8289] 0.8315] 0,8340] 0.8365] 08389<br>(1.0) 0.8413] 0,8436| 0.8461] 0,8485] 0,8508| 0.8531] 0.8554] 0,8577| 0,8599| 0.8621<br>| 4,1] 0,8643] 0,8665] 0.8686] 0.8708] 0.8729] 0,8749| 0,870] 0.8790] 0,810] 08830<br>| 1,2] 0.8849] 0,8869| 0.8888] 0,8907| 0,8925] 0,8944] 0.8962] 08980] 0.8997] 0.9015<br>| 1,3] 0.9032] 0,9049| 0.9066] 0.9082 0.9099] _0,9115[ 0.9131] 0,9147| 0.9162] 0.9177<br>| 1,4] 0,9192[ 0,9207] 0.9222] 0,9236| 0.9251] 0,9265| 0.9279] 0.9292] 0.9306] 0.9319<br>(1,5) 09332 09345| 0.9357] 09370] 0,9382| 0,9394] 0,9406| 0.9418] 0.9429] 0.9441<br><!-- End of picture text -->



<!-- Start of picture text -->
0,09<br>0,5359<br>0,5753<br><!-- End of picture text -->

###### **NORMAL DISTRIBUTION** 

|||Standard Nor|mal Distributio|n Table P(Z|< z)||
|---|---|---|---|---|---|---|
|z|0,00|0,01|0,02|0,03|(...)|0,09|
|0,0|0,50|0,5040|0,5080|0,5120||0,5359|
|0,1|0,5398|0,5438|0,5478|0,5517||0,5753|
|(...)|||||||
|1,5|**0,9332**||||||
|3,5|**0,99980**||||||



𝑃(𝑍 ≤ 3,5)﹣𝑃(1,5 ≤ 𝑍)＝0,9998 ﹣0,9332 ＝0,0666 

Probability ＝6,67% 



112 



<!-- Start of picture text -->
Concsasis<br><!-- End of picture text -->

###### **SUMMARIZING** 

- ✓ The normal distribution is the most popular of the statistical distributions. 



<!-- Start of picture text -->
os<br>04<br>#03<br>Boz<br>o1<br>aa zp<br>4 3 2 a. o tf 2 3 4<br>Zscore<br><!-- End of picture text -->

- ✓ The normal distribution allows us to approximate other unknown distributions. 



113 

11<sup>(DN</sup> 4 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

115 



<!-- Start of picture text -->
NON-NORMAL DISTRIBUTION<br>S\N ny v2 3<br>ES , sogess os gv.<br>NORMAL DISTRIBUTION zB aESS oars NON-NORMAL  Schneeeshicse&we,3 ¢ Fy<br>5, 408a Ses S50a 5A 2<br>ae22 DISTRIBUTIONS 3 -% Goals’ vonage = Control<br>Ste = {ressane Marketing Digital».<br>~ Total Quality Management >"<br>PFOCESS 'Y. & GO Analysis B38<br>Missiony cont Q SO Analysis =<br>manareeTask<& eg ESOeOcnTasks~<br>Finance? ES radio =x<br><!-- End of picture text -->



116 

###### **NON-NORMAL DISTRIBUTION** 



<!-- Start of picture text -->
NORMAL DISTRIBUTION<br>EES eee<br>PARANORMAL DISTRIBUTION<br><!-- End of picture text -->



<!-- Start of picture text -->
velocidades do vento<br><!-- End of picture text -->



<!-- Start of picture text -->
0.0030, 7<br>a<br><!-- End of picture text -->

117 

###### **NON-NORMAL DISTRIBUTION** 

###### Momentos 

**1. Location measures - Mean, Median, or Mode** 𝜇 = 0 𝜇 ≠ 0 





<!-- Start of picture text -->
YD vier<br>‘ACADEMY<br><!-- End of picture text -->

118 

###### **NON-NORMAL DISTRIBUTION** 

###### Moments 

1. Location measures 

**2. Dispersion measures** 

- Values far from the average 

- Very large variance 



Mode < Median < Mean 



Mean < Median < Mode 



119 

###### **NON-NORMAL DISTRIBUTION** 

###### Moments 

1. Location measures 

2. Dispersion measures 

**3. Measures of asymmetry** 

- Positive 



<!-- Start of picture text -->
ay<br>Q3<br><!-- End of picture text -->

- Negative 

- Zero 





<!-- Start of picture text -->
a a3<br><!-- End of picture text -->



<!-- Start of picture text -->
ee<br>Qi<br><!-- End of picture text -->

120 

###### **NON-NORMAL DISTRIBUTION** 

###### Moments 

1. Location measures 

2. Dispersion measures 

3. Measures of asymmetry 

**4. Curtosis** 





<!-- Start of picture text -->
Leptocurtica<br>— Platicirtica<br>—<br><!-- End of picture text -->

121 

###### **NON-NORMAL DISTRIBUTION - EXPONENTIAL** 

- ➢ Used to model the time between random events in a continuous and independent process. 





<!-- Start of picture text -->
Distribuigao Exponencial<br>0s Dal m=> Média<br>| ia sot Mediana<br>i |on "Moda<br>oa} | it il<br>i |<br>i ||<br>i Boal<br>293} | Pod<br>3 i oH<br>& i At<br>0.2 I i<br>| Ee<br>i Ea<br>014 j il<br>i en<br>i Po<br>oo} !} mu<br>° 2 a 6 8 10<br>Valores<br><!-- End of picture text -->

122 



<!-- Start of picture text -->
(Gat<br>Média<br>Mediana<br>Moda<br><!-- End of picture text -->

###### **NON-NORMAL DISTRIBUTION - BINOMIAL** 

- ➢ Used to describe the number of successes in a fixed number of attempts. 



<!-- Start of picture text -->
Distribuicao Binomial<br>0.30 ! <> Média<br>i === Mediana<br>i? === Moda<br>025 1B)<br>He<br>iG<br>La<br>0.20 Te<br>it<br>ta<br>8 ee<br>= He<br>8 it<br>tt<br>010 it<br>it<br>it<br>it<br>tb<br>it<br>0.05 itte<br>a<br>it<br>0.00 itVit<br>° 2 4 6 8 yo<br>Valores<br><!-- End of picture text -->



123 

###### **NON-NORMAL DISTRIBUTION - LOG-NORMAL** 

- ➢ Used to model variables that are the result of multiplying other positive random variables. 





<!-- Start of picture text -->
Distribuicdo Log-normal<br>06 1 1 1 --- Moda<br>Wy 4<br>05 iui111<br>i<br>a 1 '<br>as ,oiNg<br>8 1 DNS<br>rN<br>1<br>02 ia<br>oa Hoi<br>rob 4<br>|<br>0.0 yo a<br>3 2 3 3 3 ra<br>\alores<br><!-- End of picture text -->

124 

###### **NON-NORMAL DISTRIBUTION - GAMMA** 

- ➢ Used to model the time until a certain number of events occur in a stochastic process. 





<!-- Start of picture text -->
Distribuicdo Gamma<br>H tal =~ Média<br>027s H 1 a =~ Mediana<br>H Hed =~ Moda<br>H tba<br>0.50 HHH \ti\iH<br>Ht<br>Hi<br>0.125 { ‘ae |<br>3 H tt<br>0.100 i i<br>3 H res<br>2 H ied<br>8 H fed<br>oors H Pa<br>0.050 HH teie<br>H ed<br>0.025 HH tttt<br>i He<br>0.000 ! ie<br>° 2 4 6 8 yo 2 4<br>Valores<br><!-- End of picture text -->

125 

###### **NON-NORMAL DISTRIBUTION - POISSON** 

- ➢ Used to model the number of events that occur in a fixed interval of time or space. 





<!-- Start of picture text -->
Distribuicao de Poisson<br>025 H === Média<br>\I === Mediana<br>i === Moda<br>020 iti<br>it<br>it<br>it<br>it<br>g 015 1}<br>3 it<br>3 it<br>2i<br>3<br>i<br>0.10 it<br>it<br>it<br>it<br>0.05 it<br>it<br>0.00 it<br>3 2 4 6 8 10 2 14<br>Valores<br><!-- End of picture text -->

126 

###### **NON-NORMAL DISTRIBUTION - CHI-SQUARE** 

- ➢ Used to model the relationship between categorical variables or the fit to a statistical model. 





<!-- Start of picture text -->
Distribuigdo Qui-Quadrado<br>LTT === Média<br>0.175 PNG] "> Mediana<br>iN mods<br>0.450 ' ot<br>0.125 } ei<br>; ott<br>1 ot<br>’ ttt<br>3 0.100 to ott<br>2 rot<br>2 ae<br>|<br>0.050 rot<br>0.025 Hal<br>tHe<br>dal<br>0.000 rotrot<br>00 25 50 75 10.0 us 50 «5 200<br>Valores<br><!-- End of picture text -->

127 

###### **NON-NORMAL DISTRIBUTION - VISUAL ANALYSIS** 



<!-- Start of picture text -->
Histograma da Distbuigo Exponencil<br>&<br>»<br>ares<br><!-- End of picture text -->



<!-- Start of picture text -->
Q0-Plat da DistribuicSo Normal<br>2<br>2<br>3 A<br>3 0 4<br>rf<br>e<br>B-<br>2<br>a aTheoretical Quanties3 H 3<br><!-- End of picture text -->





<!-- Start of picture text -->
Concsasis<br>Exponencial<br>4<br>2<br>Exponencial<br><!-- End of picture text -->

128 

###### **NON-NORMAL DISTRIBUTION - NORMALITY TEST** 

- ➢ Shapiro-Wilk tests 



<!-- Start of picture text -->
n 2<br>W = n<br>5<br>X(%,- x)<br>i=t<br><!-- End of picture text -->

is the Shapiro-Wilk coefficient, which depends on the Cr sample size and is tabulated. 

is the i-th ordered value of the sample *o 𝑥̄ is the sample mean 

- ➢ Shapiro-Wilk tests 



FA) is the empirical cumulative distribution function (CDF) of the observed data F(x is the theoretical cumulative distribution function F@x)| - 𝐷 is the largest difference between the two functions. 

129 



###### **NON-NORMAL DISTRIBUTION - IMPLICATIONS** 

- ➢ Statistical tests assume normality as a premise; 

- ➢ Greater chance of type I or type II errors; 

- ➢ Non-normality can complicate model building, especially regression models; 

- ➢ Linear models often assume that residuals follow a normal distribution; 



130 

###### **NON-NORMAL DISTRIBUTION - ALTERNATIVES** 

- ➢ Logarithmic transformation is useful when data is skewed and has long tails; 

- ➢ The Box-Cox transformation allows us to find the best alternative to make the data more symmetrical; 

- ➢ Nonparametric tests such as Wilcoxon or Kruskal-Wallis 



131 

###### **SUMMARIZING** 

- ✓ Non-normality occurs when variables do not follow a normal distribution; 

- ✓ The four moments are measures of location (mean), dispersion (variance), skewness, and kurtosis. 

- ✓ The main non-normal distributions are exponential, binomial, log-normal, gamma, Poisson, and chi-square. 

- ✓ We can identify non-normality with the help of histograms, boxplots, and Q-Q plots; 

- ✓ We can use statistical tests to test normality; 

- ✓ Non-normality can call into question statistical tests that assume normality as a premise; 

- ✓ We can address non-normality with transformations, or we can apply nonparametric tests to the data. 



132 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **PART 3: INFERENCE** 

134 





#### **INFERENCE AND ESTIMATION** 

135 

###### **INFERENCE** 

- Used for: ➢ Point estimates: for example, average height; 

- ➢ Interval estimates: for example, a confidence interval for height. 





<!-- Start of picture text -->
6 &<br>goo<br>tf & &a<br>“5 Inferéncia @ r<br><!-- End of picture text -->

136 

###### **ESTIMATION** 

- ➢ Parameter: numerical measures that describe the characteristics of a population; 

- ➢ Estimators: statistical methods used to estimate population parameters based on samples. 





<!-- Start of picture text -->
Parameter Estimator<br>μ (mean)<br>p (proportion)<br>𝛔² (variance)<br>𝛔 (standard deviation)<br><!-- End of picture text -->

137 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **SAMPLE DISTRIBUTION** 

139 



<!-- Start of picture text -->
2<br><!-- End of picture text -->

###### **SAMPLE DISTRIBUTION** 



<!-- Start of picture text -->
X~N(u,0°)<br><!-- End of picture text -->



<!-- Start of picture text -->
x xX, wey xX<br><!-- End of picture text -->





140 

###### **SAMPLE DISTRIBUTION** 



<!-- Start of picture text -->
X<br><!-- End of picture text -->



<!-- Start of picture text -->
~N(u,~)<br><!-- End of picture text -->



<!-- Start of picture text -->
_— X=" NO, 1)<br>a= o/\in<br><!-- End of picture text -->

The **Central Limit Theorem** is an important result in statistics, and the proof of many other statistical theorems depends on it. In probability theory, this theorem states that as the sample size increases, the sample distribution of its mean approaches a normal distribution. 



141 



<!-- Start of picture text -->
EP = E<br>Standard error<br>¥<br><!-- End of picture text -->

###### **STANDARD ERROR** 



<!-- Start of picture text -->
EP = E<br>In the sample<br>t ¥<br><!-- End of picture text -->



142 

###### **Rule 68-95-99** 





<!-- Start of picture text -->
(Fai<br><!-- End of picture text -->



<!-- Start of picture text -->
H-30  p-26 p-o ute pt2o pt3o 2<br>1-— 68,26%—4<br>me 5% ——“<br>-—e— 1 99,7% ——____4<br><!-- End of picture text -->

143 

###### **Rule 68-95-99** 





<!-- Start of picture text -->
(Fai<br><!-- End of picture text -->



<!-- Start of picture text -->
H-30 -26 p-o pb wto pt2o pt3o 2<br>1— 68,26%—4<br>———_ 95% ——————4<br>-—e— 1 99,7% ——____4<br><!-- End of picture text -->

144 

###### **Rule 68-95-99** 





<!-- Start of picture text -->
(Fai<br><!-- End of picture text -->



<!-- Start of picture text -->
H-30 -26 p-o pb wto pt2o pt3o 2<br>+-— 68,26%—4<br>m—— 95% ———“<br>99, 7% 2 —— 7,<br><!-- End of picture text -->

145 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





#### **CONFIDENCE INTERVALS** 

147 

###### **CONFIDENCE INTERVAL** 

Sample 1 2 3 4 5 6 7 8 9 10 Mean <u>X</u> 1,70 1,75 1,73 1,71 1,71 1,72 1,72 1,71 1,79 1,82 1,73 

Summary: Xx_ = 1,73 𝜎 = 0,1 n = 10 



<!-- Start of picture text -->
-z <Z<2z,.> -2Zz est < Z<br>a/2 a/2 a/2 of\in a/2<br>7 oO 7 oO<br>X Lope © PS 2S Bop ce<br><!-- End of picture text -->



148 



<!-- Start of picture text -->
*2<br><!-- End of picture text -->

###### **CONFIDENCE INTERVAL** 



<!-- Start of picture text -->
1,73 — 0,032,,<H< 1,73 + 0,032,<br><!-- End of picture text -->



<!-- Start of picture text -->
1,73 — 0,03 *2 <u< 1,73 + 0,03 *2<br>1,73 — 0,06< u< 1,73 + 0,06<br>1,67 < p< 1,79<br><!-- End of picture text -->



<!-- Start of picture text -->
1C(u, 0,95) = [1, 67; 1,79]<br><!-- End of picture text -->



149 

###### **CONFIDENCE INTERVAL** 



<!-- Start of picture text -->
0m 3m<br>;<br>a/2fo a/2<br>xX.-—a /2 X a/2/<br><!-- End of picture text -->





<!-- Start of picture text -->
fro<br>Accuracy<br>Chance of<br>success<br>95% IC [1,67; 1,69]<br>99% IC [1,65; 1,81]<br><!-- End of picture text -->

150 

###### **SUMMARIZING** 

- ✓ Confidence intervals allow us to calculate the uncertainty in an estimate; 

- ✓ We use the Standard Normal to calculate the confidence level with a known variance; 

- ✓ The larger the sample size, the smaller the standard error and the closer the sample will be to the population; 

- ✓ The size of the "acceptable" uncertainty is given by the confidence level. The higher the confidence level, the wider the confidence interval. 



151 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **HYPOTHESIS TESTING** 

153 

###### **HYPOTHESIS TESTING** 



<!-- Start of picture text -->
Hemograma<br>Material: Sangue total com EDTA _(coletado em 27/06/2012)<br>Método: Automago - Micros 60 / ABX<br>ERITROGRAMA<br>Eritrécitos 5,2 milhéesimm* 45.05,9 mihoesimm?<br>HematOctto wccccccccnnnn 40% Wats we<br>VOM rscesssesennensntnene — 88,46 U 80 100"<br>HOM nooccccscscsnenensitstene — 23,08 pg 26.034 pg<br>cHCM 26,09 % 31.036 %<br>ObSErVagSES! .esneveneeerene<br>LEUCOGRAMA<br>Leucécitos 8.700 /mm? 4.500<br>comm (OT 96<br>Neutréfilos a 11.000 mm*<br>Metamiel6citos cnn 0% O/mm* 0.1% Ate 100 mm?<br>Bastonetes ccc 0% 0 /mm* 0.4% Até-400 mm?<br>Segmentados 67% 5.829 mm? 36 a.66% 2000.4 7500 imm*<br>Eosinéfilos 3% 261 Imm* 0.4% 100.400 imm*<br>Basofilos 0% O/mm* 0.01% Até 100 mm?<br>Linfécllos iincsstoncianen ZOOM 2.436 Imm? 20.040 .% 900 0.4400 mm?<br>MOn6CitOS ....cecccseuesenene 2% 474 Imm? 28% 200.2800 imm*<br>400.000 /p.<br>Plaquetas 280.000 /mm* 150,000<br><!-- End of picture text -->

1. Hemoglobin level is within range -> normal result 

2. Hemoglobin level is outside the range -> abnormal result 

- H₀ - Who is in the interval; a _equality_ H₁ - Who is outside the range; the _difference_ 

154 



<!-- Start of picture text -->
HYPOTHESIS TESTING<br>— sadias<br>| ! — Doentes<br>:<br>} H₀: the treatment is not effective |  =<br>18<br>'<br>| H₁: the treatment is effective | < 18<br>\<br>n = 30<br>\<br>𝜎 = 6 units/ml<br>ar *     = 14 units/mL<br>16 18<br><!-- End of picture text -->

###### **HYPOTHESIS TESTING** 



155 

**HYPOTHESIS TESTING** 



<!-- Start of picture text -->
—18<br>Ro?<br><!-- End of picture text -->



<!-- Start of picture text -->
a = P PatX-p <+—)=x —18 P(Z < x—~——18<br>Conn ~ ep? ~ PP! < epRo?<br><!-- End of picture text -->



<!-- Start of picture text -->
0,05 = P(Z <z)<br><!-- End of picture text -->



<!-- Start of picture text -->
PZ <z)<br><!-- End of picture text -->

= -1,64 



<!-- Start of picture text -->
2. Gnp0<br><!-- End of picture text -->



<!-- Start of picture text -->
ec + 2.0<br><!-- End of picture text -->



<!-- Start of picture text -->
x, = 18 ~ 1,64-& =(16,20<br><!-- End of picture text -->



156 

###### **HYPOTHESIS TESTING** 



<!-- Start of picture text -->
A H =H<br>A: H# HL<br><!-- End of picture text -->





<!-- Start of picture text -->
arc<br>a/2<br><!-- End of picture text -->

157 



<!-- Start of picture text -->
— Sadias<br>| | —— Doentes<br>\|<br>I |<br>1]<br>l<br>°<br>\ | vel<br>\ |<br>Pleo tipo“ I)(ar)\ P(erro: tipo 11)(8)<br>|<br><!-- End of picture text -->

###### **HYPOTHESIS TESTING** 

Types of errors: 

- I. Rejecting the null hypothesis when it is true, "false positive"; 

- II. Not rejecting the null hypothesis when it should be rejected, "false negative." 

H₀ True H₀ Falsa Reject H₀ Type I error (false No mistake positive) No reject H₀ No mistake Type II error (false negative) 



158 

###### **SUMMARIZING** 

- ✓ Hypothesis tests are used to make inferences about random variables. 

- ✓ We call the null hypothesis, or H₀, the hypothesis that the parameter of interest is within an expected range. 

- ✓ And alternative hypothesis, or H₁ when the parameter of interest is outside the range. 

- ✓ We reject the null hypothesis if the observed value is in the critical region. 

- ✓ The probability of rejecting the null hypothesis when it is true is called a Type I error. 

- ✓ The probability of accepting the null hypothesis when it should be rejected is called a Type II error. 



159 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





#### **HYPOTHESIS TESTING WITH UNKNOWN VARIANCE** 

161 

###### **HYPOTHESIS TESTING WITH UNKNOWN VARIANCE** 

Steps in hypothesis testing: 

1. Establish the null and alternative hypotheses 

2. Define how to calculate the critical region (e.g., unilateral vs. bilateral) 

3. Identify the distribution of the estimator and obtain its estimate (e.g., normality vs. non-normality) 

4. Fix  and obtain the critical region (e.g.,  = 5%) 

5. Conclude the test based on the estimate and critical region 



162 

###### **HYPOTHESIS TESTING WITH UNKNOWN VARIANCE** 

###### Distribution _t_ of student 



<!-- Start of picture text -->
BS<br>T Xx= uy<br>S/yn<br><!-- End of picture text -->



<!-- Start of picture text -->
n—-<br>T ~t  ( 1)<br><!-- End of picture text -->





<!-- Start of picture text -->
0.407 —— Normal Padréo ro<br>Distribuigao t (GL=5) Y<br>0.35 Distribuicdo t (GL=10)<br>—— Distribuicao t (GL=30)<br>\<br>0.30<br>0.25 /<br>g<br>»<br>3s3 0.20<br>Fs<br>a 0.15<br>0.10<br>0.05 Yy<br>0.00 = —<br>4-3-2 = t) 1 2 3 4<br>Valores<br><!-- End of picture text -->

163 

###### **HYPOTHESIS TESTING WITH UNKNOWN VARIANCE** 



<!-- Start of picture text -->
Hy: He anVic ~ He  -asil<br><!-- End of picture text -->



<!-- Start of picture text -->
Hi: He anVic - He -asil<br><!-- End of picture text -->

Average weight at BanVic is equal to Brazilian average Average weight at BanVic differs from Brazilian average 



<!-- Start of picture text -->
oe<br>2 1<br>S = 77 (LX, 2 — nX2 )<br>i=1<br><!-- End of picture text -->





<!-- Start of picture text -->
X-68<br>ao<br>s/j10 (9)<br><!-- End of picture text -->

𝛼 = 0,005 

164 

###### **HYPOTHESIS TESTING WITH UNKNOWN VARIANCE** 



<!-- Start of picture text -->
x. = 77,3<br>obs<br><!-- End of picture text -->



<!-- Start of picture text -->
t = 2,2622<br>c<br><!-- End of picture text -->





<!-- Start of picture text -->
209,35<br>2,033<br><!-- End of picture text -->

165 

###### **HYPOTHESIS TESTING WITH UNKNOWN VARIANCE** 





<!-- Start of picture text -->
-2,2622 e 2,2622<br><!-- End of picture text -->

166 

###### **HYPOTHESIS TESTING WITH UNKNOWN VARIANCE** 



<!-- Start of picture text -->
Parameter Estimator Test statistics<br>“ F z(sen>30)<br>t(sen< 30)<br>x² (chi-square)<br><!-- End of picture text -->



167 

###### **SUMMARIZING** 

- ✓ We use the standard normal distribution when we know the population variance. 

- ✓ When the variance is unknown, we use the T statistic that follows the Student's t distribution with n-1 degrees of freedom. 

- ✓ When we have samples with more than 30 elements, we can use the standard normal distribution. 



168 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **SAMPLING** 

170 

###### **SAMPLING** 

- ✓ **Population** is the complete set of individuals, objects, events, or measurements that have one or more characteristics in common and are of interest for analysis. 

- ✓ A **sample** is a <u><mark>subset o</mark></u> f individuals, objects, events, or measurements selected from a population so that information about the population as a whole can be inferred. 

- ✓ <u>The larger the sample, the greater the precision of the estimates and the smaller the margin of</u> error. 

- ✓ The **sample size** should be defined according to the population size, confidence level, and margin of error. 



171 

###### **SAMPLING - SAMPLING TECHNIQUES** 

**1. Simple random sampling** : this is the most common and easy-to-use technique, in which each element of the population has the same probability of being chosen for the sample. 





<!-- Start of picture text -->
__><br><!-- End of picture text -->

172 

###### **SAMPLING - SAMPLING TECHNIQUES** 

**1. Simple random sampling** 

**2. Stratified sampling:** a technique that divides the population into strata or groups with similar characteristics and randomly selects a sample from each stratum. 





<!-- Start of picture text -->
—<br><!-- End of picture text -->

173 

###### **SAMPLING - SAMPLING TECHNIQUES** 

**1. Simple random sampling** 

**2. Stratified sampling** 

**3. Cluster sampling:** a technique that divides the population into clusters or larger groups and randomly selects some of these clusters for the sample. 





<!-- Start of picture text -->
Pge —<br><!-- End of picture text -->

174 

###### **SAMPLING - SAMPLING TECHNIQUES** 

**1. Simple random sampling** 

**2. Stratified sampling** 

**3. Cluster sampling** 

**4. Systematic sampling:** a technique that selects elements from the population systematically, at predetermined intervals. 

1     2    3    4     5    6     7     8     9   10  11  12   13 14   15  16 ~~ee~~ 



175 

###### **SAMPLING - SAMPLING TECHNIQUES** 

**1. Simple random sampling** 

**2. Stratified sampling** 

**3. Cluster sampling** 

**4. Systematic sampling** 

**5. Quota sampling:** a technique that selects a sample based on pre-established quotas, such as age, gender, social class, etc. 









176 

###### **SAMPLING** 



𝑛 = sample size 

||**Confidence Level**|𝝰|**Value for**|
|---|---|---|---|
|= critical value with desired confidence level|90%|0,10|1,645|
|𝛔= population variance|95%|0,05|1,96|
||99%|0,01|2,575|



𝑒 = margin of error 



177 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **EXPERIMENTS** 

179 

###### **EXPERIMENTS** 

- ✓ Construction of two groups that are practically identical except for the application of the **treatment** 

- ✓ **Test group** receives treatment 

- ✓ **Control group** does not receive or receives a "placebo." 

- ✓ The most straightforward way to design experiments is to randomly assign participants to a treatment group and a control group, called **randomized experiments.** 



180 

###### **EXPERIMENTS** 

- ✓ Provide different websites to users at random; 

- ✓ Implement new marketing actions in a specific region; 

- ✓ Send messages at different times of the day 

- ✓ Offer a wider range of products to different customers 

- ✓ And so it goes... 





<!-- Start of picture text -->
YD vier<br>‘ACADEMY<br><!-- End of picture text -->

181 

###### **EXPERIMENTS** 





<!-- Start of picture text -->
iodieue<br>Crease<br>Ss<br>Women,40 to 50 years old<br>wee<br>Public Servants<br><!-- End of picture text -->

182 

###### **EXPERIMENTS** 







183 

**EXPERIMENTS** 





<!-- Start of picture text -->
KareQe ps oo) Hf | PuaPang - «ats GY<br>\ ; tel SO) Y. IN @=- |<br>feral ercich | ina x<br>Major Servo OR as Ne faels Aeneas<br>dade (i, Fra ae Ya ¢ oy yd = a<br>\ pitandhiont cia ‘A % BPrisnorsd<br>| east (<br>Salta Diener uted<br><!-- End of picture text -->





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





<!-- Start of picture text -->
\\<br>g-2<br><!-- End of picture text -->

#### **REGRESSION** 

186 

###### **REGRESSION** 

𝑦 = 𝑎 + 𝑏 × 𝑥 

##### 𝑦( _Weight_ ) = 𝑎 + 𝑏 × 𝑥( _Height_ ) 

𝑦 - dependent variable a -interception 𝑏 - angular coefficient 𝑥 - independent variable 





<!-- Start of picture text -->
2<br>e<br>ee<br><!-- End of picture text -->

187 

###### **REGRESSION** 



<!-- Start of picture text -->
125<br>100 2<br>s 75 ee<br>& 50<br>25<br>————E—E——————150 160 170 180<br>Altura (x)<br><!-- End of picture text -->



<!-- Start of picture text -->
125<br>100<br>5 75 @$ ° bgtJ Ero<br>2 50<br>25<br>9 150 160 170 180<br>Altura (x)<br><!-- End of picture text -->

###### **Ordinary Least Squares (OLS)** 

It is a technique that seeks to find the best fit for a set of data by trying to minimize the sum of the squares of the differences between the estimated value and the observed data (such differences are called residuals). 

188 

###### **REGRESSION** 



𝑦 = 𝑎 + 𝑏 × 𝑥 

𝑦( _Weight_ ) = 𝑎 + 𝑏 × 𝑥( _Height_ ) 



<!-- Start of picture text -->
 em  cm)<br><!-- End of picture text -->

189 



###### **REGESSION - R²** 

- ✓ Determines the "quality" of the regression line 

- ✓ Its value ranges from 0 to 1. 

- ✓ It is easily calculated by statistical software. 

- ✓ Should be interpreted with caution 



<!-- Start of picture text -->
R- _ 5Q ep _ 1 _ SQ. 0s<br>SQ hot SQiot<br><!-- End of picture text -->



- Children Income 

Age 

190 

###### **REGESSION - R²** 

✓ Children ✓ Income ✓ Age + 267 * Children + 0,05 * Income + 80* Age 





<!-- Start of picture text -->
,<br><!-- End of picture text -->



<!-- Start of picture text -->
A<A<br>cas<br><!-- End of picture text -->

R$ 267,00 R$ 0,05 

R$ 80,00 

191 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 





#### **COMMON ERRORS IN REGRESSION** 

193 



<!-- Start of picture text -->
Crease<br>NN<br>NN<br>0.474 ~<br>0.408<br>7.205<br>0.0277<br>-37.171<br>78.34<br>78.95<br>@.975]<br>53.729<br>1.804<br>2.226<br>0.664<br><!-- End of picture text -->

###### **COMMON ERRORS IN REGRESSION** 

✓ Interpreting the regression result; 



<!-- Start of picture text -->
OLS Regression Results<br>sesanscescssesscesescesesessesescessssesesssesessessssesessssessssesessesess<br>Dep. Variable: y  R-squared: 0.474<br>Model: OLS Adj. R-squared: 0.408<br>Method: Least Squares F-statistic: 7.205<br>Date: Tue, 2@ Jun 2023 Prob (F-statistic): 0.0277<br>Time: 19:16:13 Log-Likelihood: -37.171<br>No. Observations: 1@ AIC: 78.34<br>Df Residuals: 8 BIC: 78.95<br>DF Model: 1<br>Covariance Type: nonrobust<br>coef std err t P>|t| [2.025 @.975]<br>const -91.5608 63.85 71.453 0.184 | -236.851 53.729<br>e 2.9785 0.362 2.684 2.028 0.137 1.804<br>Omnibus: 1.888  Durbin-Watson: 2.226<br>Prob(Omnibus) : 2.405 Jarque-Bera (38): 0.664<br>skew: @.629  Prob(3B): 0.718<br>kurtosis: 2.988 Cond. No. 3.12e+83<br><!-- End of picture text -->



194 

###### **COMMON ERRORS IN REGRESSION** 

- ✓ Interpreting the regression result; 

- ✓ Regression when the relationship is nonlinear; 

- ✓ Adding too many variables; 

- ✓ Multicollinearity; 

- ✓ Correlation is not causation 





<!-- Start of picture text -->
YD vier<br>‘ACADEMY<br><!-- End of picture text -->

195 





<!-- Start of picture text -->
ages<br><!-- End of picture text -->

**THANK YOU** 



**JOIN OUR COMMUNITY** CT 

