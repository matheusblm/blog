import pandas as pd

DataFrame and the Series.

DataFrame = Table

Example: pd.DataFrame({"Yes": [50,21], "No": [131,2]})

When we build the table, on the left will be the count from 0, if we want to change:

pd.DataFrama({"Yes": [20,21],"No": [10,23], index=["AnswersOne","AnswersTwo"]})


Series - Sequence of data values = List

pd.Series([1,2,3,4,5])
output= 
0    1
1    2
2    3
3    4
4    5

Series will be a sing column in a dataFrame

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

2015 Sales    30
2016 Sales    35
2017 Sales    40
Name: Product A,


Most times we will read data from CSV not creating our own data

wine_reviews = pd.read_csv("../path")

To attribute check how large 

wine_reviews.shape

To see the first five rows

wine_review.head()


fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])