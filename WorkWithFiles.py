file_read=open('TextFile1.txt','r',encoding='utf-8-sig')
text=file_read.read()

print(text)
file_read.close()

file_write=open('TextFile1.txt','a',encoding='utf-8-sig')
text=input('Mis text on vaja lisada: ')
file_write.write('\n'+text)
file_write.close()
with open('TextFile1.txt','r',encoding='utf-8-sig') as reader:
    print(reader.read())

with open('TextFile5.txt','x',encoding='utf-8-sig') as whateverYouWant:
    for line in range(3):
        text=input('Mis text on vaja lisada: ')
        whateverYouWant.write('\n'+text)
with open('TextFile5.txt','r',encoding='utf-8-sig') as whateverYouWant:
    print(whateverYouWant.read())
