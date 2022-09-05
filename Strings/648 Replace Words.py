class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()        
        for root in dictionary:
            for i,word in list(enumerate(sentence)):
                if word[:len(root)]==root:
                    sentence[i] = root        
        return " ".join(c for c in sentence) 
        
            
