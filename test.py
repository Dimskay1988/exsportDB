import pandas as pd

df = pd.read_excel('file/skany.xlsx')
f = df.Uzytkownik.nunique()
print(f)
