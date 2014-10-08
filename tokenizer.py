import string
import newparser as p
import sys





            
######################## Preprocessing of tokens############################
class Tokenize:
    #tookenstream=list()
    
    dictionary=dict()
    collection=list()
    #termlist1=list()
    def bytes_from_file(self,filename1):
        with open (filename1) as f:
            Read=f.read()
            self.Parser(Read)
##            TokenStream=send.Parser(Read)
##            self.TokenStream1.append(TokenStream)
           

            #print"here"
            
            #print TokenStream[0]
            #self.tokenize(TokenStream)
    def Parser(self,chunk):
        #print ("iam here")
##        self.collection=list()
        terms=list()
        while True:
            try:
                i=chunk.index("<BODY>")+6
                try:
                    j=chunk.index("</BODY>")
                    self.collection.append(chunk[i:j])
                    chunk=chunk[j+7:]
                except:
                    self.collection.append(chunk[i:])
                    #return collection
                    break
            except :
                try:
                    k=chunk.index("</BODY>")
                    self.collection.append(chunk[:k])
                    #return collection
                    break
                except:
                    #return collection
                    break
    
    def tokenize(self):
        tookenstream=self.collection
        
        
        for doc in tookenstream:
            termlist1=list()
##            print doc
##            print("========================ENDOF ONE LOOP=========")
            doc_id=tookenstream.index(doc)
##            print doc_id
            doc=doc.lower()
            for char in string.punctuation:
                doc=doc.replace(char,"")
            for abc in "\n\t":
                doc=doc.replace(abc," ")
            for token in doc.split(" "):
                termlist1.append(token)
            for token in termlist1:
####                print token
####                print("========================token=========")
                
                if not token in self.dictionary:
##                    print token
                    self.ADDToDictionary(token,doc_id)
##                    print ("i am in new term")
                else:
##                    print token
                    self.newdict=self.dictionary.get(token,{})
##                    print self.newdict
                    
                    if not doc_id in self.newdict:
                        freq=1
                        self.newdict[doc_id]=freq
                        self.dictionary[token]=self.newdict
                    else:
                        
                        freq=self.newdict.get(doc_id)
                        freq=freq+1
                        self.newdict[doc_id]=freq
                        self.dictionary[token]=self.newdict
        return self.dictionary
##        
    def ADDToDictionary(self,term,doc_id):
        termfrequency=0
        self.termfrequency=1
        newpostinglist=list()
        #self.postinglist=self.dictionary.get(term,[])
        self.info=dict()

        self.info[doc_id]=self.termfrequency
        
        self.dictionary[term]=self.info
    
    


if __name__ == '__main__':
    bmw=Tokenize()
    test=list()
    test.append("anish chavan std 6421180")
    test.append("std 6421180")
##    print test[0]
    bmw.tokenize(test)
    
    
    
