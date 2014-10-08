import tokenizer as im
import pickle
import string
from functools import  reduce
import shelve
import pickle
import os
import sys
import math


class MAIN:
     Querytoken=list()
     querysplit=list()

     invertedindex=dict()
     newdict=dict()     
     termlist=list()
     def main(self):     
          path="C:/Users/ANISH/Desktop/IR"              
          block=im.Tokenize()           #Fucntion which is  responsible for reading all the .smg files from the directory .
         
          for filename in os.listdir(path):
               if filename.endswith(".sgm"):
                    block.bytes_from_file(filename)    
          self.invertedindex=block.tokenize()
          self.termlist=block.collection
          Query="Drug company bankruptcies"
         
          self.querysplit=Query.split(" ")
##          termlist1=list()
          for doc in self.querysplit:
               docid1=self.querysplit.index(doc)
               doc=doc.lower()
               for char in string.punctuation:
                    doc=doc.replace(char,"")               #pre processing the input query.
               for abc in "\n\t":
                    doc=doc.replace(abc," ")
               for token in doc.split(" "):
                    self.Querytoken.append(token)
          
          for token in self.Querytoken:
               for key in self.invertedindex.keys():
                    if key==token:                           #matching and creating a new or mini dictionary to store common term and term frequency between  
                         print("iam here")                  #queryterm  and inverted index term 
                         self.newdict[key]=self.invertedindex[key]
          compare=dict()

          for doc2 in self.newdict:
               print doc2
               xtemp=self.newdict.get(doc2)
               for docid in xtemp:
                    if docid in compare.keys():
                         score=compare.get(docid)
                         score=score+xtemp.get(docid)    #####LOGIC that calculates and stores the rank for documetn based on term frequency only
                         compare[docid]=score
                    #print (docid)
                    else:
                         compare[docid]=xtemp.get(docid)
          d=sorted(compare,key=compare.get,reverse=True)
          five=d[:5]
          print five                                     ## prints the  top 5 ranked  documents.
          five=d[:5]
          for l in five:
               print (l,compare[l])
               
               for abc in "\n\t":
                doc=self.termlist[l].replace(abc," ")
               print((doc))
     def IDFokapibm25(self,k):                           
          N=len(self.termlist)
          print(N)
          nq=dict()
          idf=dict()
          b=0.75
          #k=1.2
          lenD=len(self.termlist)
          sumoflenghts=0
          for document in self.termlist:
               for abc in "\n\t":
                doc=document.replace(abc," ")
               sumoflenghts=sumoflenghts+len(doc)     
          print sumoflenghts
          avgdl=sumoflenghts/len(self.termlist)                      ##averge document length 
          print avgdl
     
          for token in self.Querytoken:
               temp=self.newdict.get(token)
               nq[token]=len(temp)
          for t in nq:
               num=(N-nq.get(t)+0.5)
               denom=nq.get(t)+0.5
               x=math.log(num/denom)
               idf[t]=x                  ##Logic to calculate the IDF
          score=dict()
          for ta  in self.newdict:
          
               temp=self.newdict.get(ta)
               for docid in temp:
                    tf=temp.get(docid)
                    numerator=tf*(k+1)
               
                    denominator=tf+k*(1-b+(b*(len(self.termlist[docid])/avgdl)))

                    qscore=idf[ta]*(numerator/denominator)  #Logic to calculate the value of OKapiBM25
                    if docid not in score.keys():
                         score[docid]=qscore
                    
                    else:
                         tempscore=score.get(docid)
                         score[docid]=tempscore+qscore

       
          d=sorted(score,key=score.get,reverse=True)
          five=d[:5]
          for l in five:
               print (l,score[l])
               for abc in "\n\t":
                doc=self.termlist[l].replace(abc," ")       #will print the top 5 documents based on okapiBM25
                
               print((doc))
               
               
               
if __name__ == '__main__':
     flag=True
     m=MAIN()
     m.main()
     while flag!=False:
          print("please enter value of k")
          print("0 to exit ")

          var =input()
          if var==0:
               flag=False
          else:
               
               m.IDFokapibm25(var)
               
