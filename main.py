import tkinter as tk
import string
import re
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Removing 'not' stop word as it can be useful in the training of data
sw=list(ENGLISH_STOP_WORDS)
sw.remove('not')

# Removing Punctuation from messages
def removePunc(doc):
	pc=string.punctuation
	clean_doc=re.sub(f'[{pc}]','',doc)
	return clean_doc

# Loading the data
df=pd.read_csv('Dataset\\sms.txt',delimiter='\t')
df.columns=['type','msg']
df['msg']=df.msg.apply(removePunc)

# Removing stop words and creating vocab of words with countVectorizer 
cv=CountVectorizer(stop_words=sw)
X=cv.fit_transform(df.msg).todense()

# Implementing Naive Bayes on dataset
gnb=MultinomialNB()
gnb.fit(X,df.type)	

# save the model to disk
filename = 'spamPredictionModel.sav'
pickle.dump(gnb, open(filename, 'wb'))
  


# Creating GUI of this project with tkinter
def mypredict():
	new_rvw=e.get()
	X_test=cv.transform([new_rvw]).todense()
	p=loaded_model.predict(X_test)
    
	if(p[0] == 'ham'):
		label=tk.Label(root,text="Ham ",font=('Book Antiqua' ,25 ,'bold'),bg='white',fg='green')
		label.place(x=400,y=450) 
	else:
		label=tk.Label(root,text="Spam",font=('Book Antiqua' ,25 ,'bold'),bg='white',fg='red')
		label.place(x=400,y=450)
        
# load the model from disk
filename = 'spamPredictionModel.sav'
loaded_model = pickle.load(open(filename, 'rb'))

root=tk.Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(background='grey')

l=tk.Label(root,text='Spam Detection',bg='grey',fg='black',font=('cambria',40,'bold'))
l.place(x=550,y=10)

l2=tk.Label(root,text='Enter Msg:',bg='grey',fg='black',font=('cambria',20,'bold'))
l2.place(x=100,y=200)

# l3=tk.Label(root,text='',bg='blue',fg='black',font=('cambria',20,'bold'))
# l3.place(x=300,y=50)

e=tk.Entry(root,font=('',20,'bold'))
e.place(x=300,y=200)

b=tk.Button(root,command=mypredict,text='Predict',font=('book antiqua',20,'bold'),bg='grey',fg='black')
b.place(x=300,y=300)

root.mainloop()
