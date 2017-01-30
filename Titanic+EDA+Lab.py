
# coding: utf-8

# In[11]:

import pandas as pd
get_ipython().magic('pylab inline')


# In[3]:

df = pd.read_csv("train.csv")


# In[4]:

df


# In[5]:

df.shape


# In[6]:

df.Survived.value_counts()


# In[7]:

342/891.0


# In[8]:

342.0/891


# In[9]:

342.0/891.0


# ##EDA (Exploratory Data Analytics)
# 
# Learn about the data
# 
# For each variable:
# <li> Is it categorical?
# <li> If not, what are the Min, Max, and Average values?
# <li> If it is, what are the categories?
# <li> Are there missing values?
# <li> Something about the distribution of the variable
# 

# In[10]:

df.Sex.value_counts()


# In[12]:

df.Sex.value_counts().plot(kind='bar')


# In[16]:

df.Sex.value_counts()


# In[17]:

df[df.Sex=='female']


# In[18]:

df


# In[19]:

df[df.Sex.isnull()]


# In[20]:

df.Fare.value_counts()


# In[21]:

df.Fare.values


# In[22]:

df.describe()


# In[23]:

df.Fare.mean


# In[24]:

df.Fare.mean()


# In[25]:

df.Fare.hist(bins=5)


# In[26]:

df[df.Fare.isnull()]


# In[30]:

df[df.Fare==0]


# In[31]:

df[df.Cabin.isnull()]


# In[32]:

#Women and children first?

df[df.Sex=='male'].Survived.value_counts().plot(kind='barh')


# In[33]:

df[df.Sex=='female'].Survived.value_counts().plot(kind='barh')


# In[43]:

#Women and children first?

fig, axs = plt.subplots(1,2)
df[df.Sex=='male'].Survived.value_counts().plot(kind='barh' ,ax=axs[0], title ="Male Survivorship")
df[df.Sex=='female'].Survived.value_counts().plot(kind='barh' ,ax=axs[1], title ="Female Survivorship")


# In[44]:

df[df.Age<15].Survived.value_counts().plot(kind='barh')


# In[45]:

df[(df.Age<15)&(df.Sex=='female')].Survived.value_counts().plot(kind='barh')


# In[46]:

df[(df.Age<15)&(df.Sex=='male')].Survived.value_counts().plot(kind='barh')


# In[47]:

df


# In[52]:

#Is the variable categorical or continuous
#Min, Max, Mean, and Standard Deviation of the continuous variables.
df.describe()


# In[49]:

df.describe


# In[51]:

#Are there missing value for Pclass?

df[df.Pclass.isnull()]


# In[55]:

#Are there missing value for PassengerId?

df[df.PassengerId.isnull()]


# In[57]:

#Are there missing value for Survived?
df[df.Survived.isnull()]


# In[56]:

#Are there missing value for Sex?
df[df.Sex.isnull()]


# In[58]:

#Are there missing value for Age?
df[df.Age.isnull()]


# In[59]:

#Are there missing value for SibSp?
df[df.SibSp.isnull()]


# In[60]:

#Are there missing value for Parch?
df[df.Parch.isnull()]


# In[61]:

#Are there missing value for Ticket?
df[df.Ticket.isnull()]


# In[62]:

#Are there missing value for Fare?
df[df.Fare.isnull()]


# In[63]:

#Are there missing value for Cabin?
df[df.Cabin.isnull()]


# In[64]:

#Are there missing value for Embarked?
df[df.Embarked.isnull()]


# In[66]:

#Histogram: PassengerId?
df.PassengerId.hist(bins=5)


# In[67]:

#Histogram: Survived?
df.Survived.hist(bins=5)



# In[68]:

#Histogram: Pclass?
df.Pclass.hist(bins=5)


# In[71]:

#bar: Sex?
df.Sex.value_counts().plot(kind='bar')


# In[72]:

#Histogram: Age?
df.Age.hist(bins=5)


# In[73]:

#Histogram: SibSp?
df.SibSp.hist(bins=5)


# In[74]:

#Histogram: Parch?
df.Parch.hist(bins=5)


# In[77]:

#bar: Ticket?
df.Ticket.value_counts().plot(kind='bar')


# In[78]:

#Ticket values
df.Ticket.value_counts()


# In[79]:

#Histogram: Fare?
df.Fare.hist(bins=5)


# In[81]:

#bar: Cabin?
df.Cabin.value_counts().plot(kind='bar')


# In[82]:

#Cabin values

df.Cabin.value_counts()


# In[84]:

#bar: Embarked?
df.Embarked.value_counts().plot(kind='bar')


# In[90]:

df[(df.Sex=='female')&(df.Age<=15)&(df.Pclass ==3)].Survived.value_counts().plot(kind='bar')


# In[91]:

df[(df.Sex=='male')&(df.Age<=15)&(df.Pclass ==3)].Survived.value_counts().plot(kind='bar')


# In[ ]:



