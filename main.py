import numpy as np
import pandas as  pd

arr = np.array([1, 2, 3, 4, 5])
print(arr)

zeros = np.zeros((2, 3))
ones = np.ones((3, 2))

print(zeros)
print(ones)

range_arr = np.arange(1, 10, 2)
reshape = np.arange(12).reshape(3, 4)

print("Arange array", range_arr)
print("Reshape array", reshape)

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])
print(a + b)
print(a * b)

#pandas
s = pd.Series([10, 20, 30, 40], name="Numbers")
print(s)


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print(df)

print(df['Name'])
print(df.iloc[0])
print(df.loc[1, 'Age'])


print(df[df['Age'] > 28])


df['Tax'] = df['Salary'] * 0.1

print(df.describe())
print(df.mean())


df['Bonus'] = np.where(df['Age'] > 28, 5000, 3000)

