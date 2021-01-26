# ML-Project---Spam-Detection

Text mining (deriving information from text) is a wide field which has gained popularity with the huge text data being 
generated. Automation of a number of applications like sentiment analysis, document classification, topic classification, 
text summarization, machine translation, etc has been done using machine learning models.
Spam filtering is a beginner’s example of document classification task which involves classifying a message as spam or 
non-spam(ham) mail. Spam box in your Gmail account is the best example of this.

 Before starting we must preprocess the messages. First of all, we shall make all the character lowercase. This is 
because ‘free’ and ‘FREE’ mean the same and we do not want to treat them as two different words.

Then we tokenize each message in the dataset. Tokenization is the task of splitting up a message into pieces and 
throwing away the punctuation characters. The words like ‘go’, ‘goes’, ‘going’ indicate the same activity. We can 
replace all these words by a single word ‘go’. We then move on to remove the stop words. Stop words are those words 
which occur extremely frequently in any text. For example words like ‘the’, ‘a’, ‘an’, ‘is’, ‘to’ etc. These words do not give 
us any information about the content of the text. Thus it should not matter if we remove these words for the text. You can 
also use n-grams to improve the accuracy. As of now, we only dealt with 1 word. But when two words are together the 
meaning totally changes.

