import pandas as pd
df = pd.read_csv('data.csv')
print(df)
names = ['Artline',  'Dell',  'Asus',  'Lenovo',   'HP',  'IT-Blok']
def fun(row,name):
    return row['Вага']*row[name]
list_=[]
for i in range(len(names)):
    list_.append(round(sum(df.apply(fun,name=names[i], axis = 1)),2))
result = list(zip(names,list_))
result_df = pd.DataFrame(result,columns=['Виробник','Оцінка'])
print(result_df)
print()
print('Найкращим є:')
print(result_df.iloc[result_df['Оцінка'].idxmax()])