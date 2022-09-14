from textblob import TextBlob
sen="""Hello,ths is sejal here.i loe to eat chclate"""
lst=sen.split(" ")
print("lst==",lst)
for i in lst:
    a=TextBlob(i)
    crt=a.correct()
    print(i,"correct words==",crt)
    sen.replace(i,str(crt))
