import string
import csv
import matplotlib.pyplot as plt

def cleaner(text):
    l_text=text.lower()
    clean_text=l_text.translate(str.maketrans('','',string.punctuation+'”'+'“'+"’"))
    return(clean_text.split())

def stop_words():
    f=open("stopwords.txt") 
    text=f.read()
    c_text=text.translate(str.maketrans('','',string.punctuation))
    stop_word_list=c_text.split()
    return(stop_word_list)

def action_words(tokens):
    stop_word_list=stop_words() 
    final_words=[]
    for word in tokens:
        if word not in stop_word_list:
            final_words.append(word)
    return(final_words)

def classification(final_words):
    senti={}
    j=0
    with open("NRC-Emotion.csv",'r') as emotion_file:
            csv_reader=csv.DictReader(emotion_file)
            for line in csv_reader:
                if (line['Word']) in final_words:
                    senti[j]=line
                    j=j+1                   
    j=0
    result={}
    for j in range(len(senti)):
        result['Positive']=int(result.get("Positive",0))+int(senti[j]['Positive'])
        result['Negative']=int(result.get("Negative",0))+int(senti[j]['Negative'])
        result['Anger']=int(result.get("Anger",0))+int(senti[j]['Anger'])
        result['Fear']=int(result.get("Fear",0))+int(senti[j]['Fear'])
        result['Joy']=int(result.get("Joy",0))+int(senti[j]['Joy'])
        result['Sadness']=int(result.get("Sadness",0))+int(senti[j]['Sadness'])
        result['Surprise']=int(result.get("Surprise",0))+int(senti[j]['Surprise'])
        j=j+1
    return(result)            

class Visualisation:
    def feeling(sentiments):
        emotion=['Positive','Negative']
        values=[sentiments['Positive'],sentiments['Negative']]
        plt.title("Overall Feeling")
        plt.ylabel("No. of words exhibiting sentiment")
        plt.bar(emotion, values)
        plt.show()
        return
    def emotions(sentiments):
        emotion=['Anger','Fear','Joy','Sadness','Surprise']
        values=[sentiments['Anger'],sentiments['Fear'],sentiments['Joy'],sentiments['Sadness'],sentiments['Surprise']]
        plt.title("Segregated Emotions")
        plt.ylabel("No. of words exhibiting sentiment")
        plt.bar(emotion, values)
        plt.show()
        return
    

sentiments=classification(action_words(cleaner(input("Enter your Text: "))))
Visualisation.feeling(sentiments)
Visualisation.emotions(sentiments)
