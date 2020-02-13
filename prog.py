import random
def c():
    print("encours")
def py():
    print("encours")
def php():
    print("encours")
def java():
    #fichier1=input("Quel fichier voulez-vous modifier ? ")
    #f= open("test.txt","w+")
    #f=open("guru99.txt","a+")
   # for i in range(10):
         #f.write("This is line %d\r\n" % (i+1))
   # f.close()
    #Open the file back and read the contents
    f=open("java.txt", "r")
    #or, readlines reads the individual line into a list
    fl =f.readlines()
    lst = ["String", "int", "char", "short", "byte", "long", "double", "float", "boolean"]
    varuser=[]
    varnew=[]
    varindex=[]
    operation=["+","-","*","\n","/","(",")",";","="]
    for x in fl:
            x= x.split(" ")
            for y in x:
                if y in lst:
                            varuser.append(x[x.index(y)+1])
    
    for i in varuser:
        varnew.append(randmot())
    fwrite= open("java.txt","w+")
    for var1 in fl:
        var1= var1.split(" ")
        for var2 in var1:
            for i in varuser:
                if i in var2 and len(var2)==len(i):
                    print("ici")
                    print("var = "+var2)
                    print("replace by "+varnew[varuser.index(i)])
                    ligneFinale = var2.replace(var2,varnew[varuser.index(i)])
                    fwrite.write(" ")
                    fwrite.write(ligneFinale)
                    #var2.replace(var2,varnew[varuser.index(i)])
                    #if var1[var1.index(i)-1] ==" " and var1[var1.index(i)+1] ==" ":
                       # print(i)
                        #print(var1.index(i))
                       # print("ici")
            if var2 not in varuser:
                fwrite.write(" ")
                fwrite.write(var2)
            
    f.close()
    fwrite.close()
def reecriture():
    f=open("java.txt", "r")
    #or, readlines reads the individual line into a list
    fl =f.readlines()
    lst = ["String", "int", "char", "short", "byte", "long", "double", "float", "boolean"]
    varuser=[]
    varnew=[]
    compteur=0
    lettre=""
    varindex=[]
    verifvar=0
    operation=["+","-","*","\n","/","(",")",";","="]
    for x in fl:
            x= x.split(" ")
            for y in x:
                if y in lst:
                            print("found var")
                            print(x[x.index(y)+1])
                            varuser.append(x[x.index(y)+1])
    fwrite= open("java.txt","w+")
    for var1 in fl:
        var1= var1.split(" ")
        for var2 in var1:
            for i in varuser:
                    #(var2[var2.index(i)-1] or var2[var2.index(i)+1])
                if i in var2 and len(var2)==len(i):
                    fwrite.write(" ")
                    fwrite.write(var2)
                if i in var2:
                    if ((var2[var2.index(i)-1] or var2[var2.index(i)+1]) in operation):
                        print("find")
                        if (var2[-2] == "{" and var2[-1] == "\n") or (var2[-2] == "(" and var2[-1] == ")"):
                            break
                        varindex.append(var2)
                        for y in var2:
                            if y==i[compteur]:
                                lettre+=y
                                compteur=compteur+1
                                if (lettre==i and y==i[-1]): #and (var2[var2.index(i[compteur])+1] in operation):
                                    fwrite.write(" ")
                                    fwrite.write(lettre)
                                    fwrite.write(" ")
                                    lettre=""
                                    compteur=0
                            else:
                                fwrite.write(y)
                            """if y == i:
                                fwrite.write(" ")
                                fwrite.write(y)
                                fwrite.write(" ")
                            else:
                                fwrite.write(y)"""
            if (var2 not in varuser )and (var2 not in varindex):
                fwrite.write(" ")
                fwrite.write(var2)
    f.close()
    fwrite.close()

def randmot():
    caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789" #Tu peux en ajouter si tu veux
    longueur = 3 #10 est un exemple tu mets le nombre que tu veux.
    mdp = "" #Variable mot de passe
    compteur = 0 #Compteur de lettres
    while compteur < longueur:
        lettre = caracteres[random.randint(0, len(caracteres)-1)] #On tire au hasard une lettre
        mdp += lettre #Ona joute la lettre au mot de passe
        compteur += 1 #On incrémente le compteur de lettres
    return mdp
if __name__== "__main__":
    c=1
    while c ==1:
        print("1:java, 2:c, 3:python, 4:php")
        choice=input("En quel language est votre programme ? ")
        if choice == "java":
            reecriture()
            java()
            c=0
        if choice == "c":
            c()
            c=0
        if choice == "python":
            py()
            c=0
        if choice == "php":
            php()
            c=0
        
