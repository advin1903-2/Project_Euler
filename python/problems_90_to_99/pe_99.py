import pandas as pd
import math

filename="pe_99_data.csv"

# Download file
df=pd.read_csv(filename,header=None,delimiter=",")

# Name columns,create log of the value, create line
df.columns=['Base','Expoente']
df['linha']=df.index+1
df['Log_value']=df['Expoente']*df['Base'].apply(math.log)

# Drop columns and select the max 
max_val=df['Log_value'].max()
df=df[df['Log_value']==max_val]
df.drop(columns=['Base','Expoente','Log_value'],inplace=True)


# Print results
print(df)