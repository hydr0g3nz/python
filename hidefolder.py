import os




path = os.getcwd()
print(f'path is {path}')

allfolder = os.listdir(path)
allcommand = ""


for i,f in enumerate(allfolder):
    #print(f'{i+1}.{f}')
    if len(f.split(".")) > 1 :
        print("Don't hide : "+ f)
    else:
        print(f'attrib +h "{f}"')
        allcommand = allcommand + 'attrib +h "{}"\n'.format(f)
        f = open('hide.bat', 'w')
        f.write(allcommand)
        
        f.close

print("-"*20)
print(allcommand)
