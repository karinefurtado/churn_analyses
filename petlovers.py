#!/usr/bin/env python
# coding: utf-8

# In[180]:


# Bibliotecas para tratamento dos dados
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# In[181]:


# 2. Importando a base de dados
tabela = pd.read_csv("data-test-analytics_5.csv")


# In[182]:


# 3. Visualizando a base de dados
display(tabela)


# In[183]:


print(tabela.info())


# In[184]:


# excluindo colunas desnecessárias
tabela = tabela.drop("id", axis=1)
tabela = tabela.drop("email_hash", axis=1)
tabela = tabela.drop("address_hash", axis=1)
tabela = tabela.drop("name_hash", axis=1)
tabela = tabela.drop("birth_date", axis=1)
tabela = tabela.drop("city", axis=1)
tabela = tabela.drop("neighborhood", axis=1)
tabela = tabela.drop("recency", axis=1)


# In[185]:


print(tabela["status"].value_counts())
print(tabela["status"].value_counts(normalize=True).map("{:.2%}".format))


# In[186]:


tabela['updated_at'] = pd.to_datetime(tabela['updated_at'], format='%m/%d/%y %I:%M %p')

# Extract date and year information
#tabela['date'] = tabela['updated_at'].dt.date
#tabela['year'] = tabela['updated_at'].dt.year


# In[187]:


# Convert the column to datetime format with explicit format specification
tabela['created_at'] = pd.to_datetime(tabela['created_at'], format='%m/%d/%y %I:%M %p')


# Extract date and year information
#tabela['date'] = tabela['created_at'].dt.date
#tabela['year'] = tabela['created_at'].dt.year


# In[188]:


tabela['last_date_purchase'] = pd.to_datetime(tabela['last_date_purchase'], format='%m/%d/%y %I:%M %p')


# In[189]:


# Filtrar os dados para o ano de 2020 e criar uma cópia
tabela_2020 = tabela.loc[tabela['created_at'].dt.year == 2020].copy()

# Extrair o mês da coluna 'created_at'
tabela_2020['month'] = tabela_2020['created_at'].dt.month

# Criar histograma para a coluna 'month'
grafico = px.histogram(tabela_2020, x='month', color="status", text_auto=True)
grafico.update_layout(title="Relação de status por mês (ANO 2020)")
grafico.show()


# In[190]:


# Convert 'deleted_at' column to datetime
tabela['deleted_at'] = pd.to_datetime(tabela['deleted_at'], errors='coerce')

# Filter rows where "status" is equal to "canceled" and limited to the year 2021
filtered_data = tabela[(tabela["status"] == "canceled") & (tabela["deleted_at"].dt.year == 2021)]

# Count the occurrence of each unique value in the "marketing_source" column
count_by_source = filtered_data["marketing_source"].value_counts()

# Create the bar chart
plt.bar(count_by_source.index, count_by_source.values)

# Customize the chart
plt.title("Distribution of Cancelations by Marketing Source (Year 2021)")
plt.xlabel("Marketing Source")
plt.ylabel("Number of Cancelations")

# Rotate x-axis labels for better readability if needed
plt.xticks(rotation=45)

# Display the chart
plt.show()


# In[191]:


# Convert 'deleted_at' column to datetime
tabela['deleted_at'] = pd.to_datetime(tabela['deleted_at'], errors='coerce')

# Filter rows where "status" is equal to "canceled" and limited to the year 2021
filtered_data = tabela[(tabela["status"] == "canceled") & (tabela["deleted_at"].dt.year == 2020)]

# Count the occurrence of each unique value in the "marketing_source" column
count_by_source = filtered_data["state"].value_counts()

# Create the bar chart
plt.bar(count_by_source.index, count_by_source.values)

# Customize the chart
plt.title("Distribuição de cancelamento por estado (ANO 2021)")
plt.xlabel("Estados")
plt.ylabel("Número de cancelamentos")

# Rotate x-axis labels for better readability if needed
plt.xticks(rotation=45)

# Display the chart
plt.show()


# In[192]:


tabela.dropna(subset=['deleted_at'], inplace=True)


# In[193]:


# Filtrar os dados para o ano de 2020 e criar uma cópia
tabela_2020 = tabela.loc[tabela['deleted_at'].dt.year == 2020].copy()

# Extrair o mês da coluna 'created_at'
tabela_2020['month'] = tabela_2020['deleted_at'].dt.month

# Criar histograma para a coluna 'month'
grafico = px.histogram(tabela_2020, x='month', color="status", text_auto=True)
grafico.update_layout(title="Cancelamentos por mês (ANO 2020)")
grafico.show()


# In[ ]:




