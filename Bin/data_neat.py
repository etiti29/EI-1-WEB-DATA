from Sentimental_analysis.Twitter.data.pre_traitement import *

tweets_words = read_saved_tweets('data.txt')

N=len(tweets_words)
l70, l20, l10 = partition_random(N-1)

def create_lists(l):
    tweets_list={}
    for k in l : 
        tweets_list[k]=tweets_words[k]
    return tweets_list

data70, data20, data10 = create_lists(l70), create_lists(l20), create_lists(l10)
        
with open('data10.txt', mode='w', encoding='utf-8') as file:
    json.dump(data10, file, ensure_ascii=False, indent=4)  
with open('data20.txt', mode='w', encoding='utf-8') as file:
    json.dump(data20, file, ensure_ascii=False, indent=4)  
with open('data70.txt', mode='w', encoding='utf-8') as file:
    json.dump(data70, file, ensure_ascii=False, indent=4)  