'''import pandas as pd
import numpy as np

commute = pd.read_excel("9.1 commute.xlsx",sheet_name="Sales",index_col='Date')
commute.replace(["Yes","No"],[1,0],inplace=True)
array1 = np.array(commute)
array2 = np.array([8,3,0.5,12])

daily_expenses= array1.dot(array2)###

print(daily_expenses)
rupees = "⟨₹⟩"
lady = "Himani Tyagi"
print(f'The total expenses of the {lady} is :{rupees}{daily_expenses.sum()}')
x= commute.index[daily_expenses.argmax()].strftime("%Y-%M-%d")####
print(f'The maximum spent money was on date : {x}')'''

import pandas as pd
import numpy as np

commute = pd.read_excel("9.1 commute.xlsx",sheet_name="Sales",index_col="Date")
price_data = pd.read_excel("9.1 commute.xlsx",sheet_name="Price")
commute.replace(["Yes","No"],[1,0],inplace=True)

sales_array = np.array(commute)
price_array = np.array([8,3,0.5,12])

daily_expense=sales_array.dot(price_array)
print(daily_expense)
rupees = "⟨₹⟩"
lady = "Himani Tyagi"
x= daily_expense.sum()
print(f'The total expenses of the {lady} is :{rupees}"{daily_expense.sum()}"')

x= commute.index[daily_expense.argmax()].strftime("%d-%m-%Y")
print(f'The maximum spent money was on date : {x}')






