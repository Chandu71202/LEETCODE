class Solution:
    def entityParser(self, text: str) -> str:
        d={"&quot;":'\"',"&apos;":"'","&gt;":">","&lt;":"<","&frasl;":"/","&amp;":"&"}
        for key,value in d.items():
            text = text.replace(key,value)
        return text
