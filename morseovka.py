def mor(a):
    #BIG BRAIN MOMEENT WARNING
    #Pokud zjistíme, že bude následovat nový řádek, rozdělíme string dle něj
    #A pak použijeme funkci mor uprostřed funkce mor !!!
    #Nakonec převedené části spojíme s novými řádky mezi nimi
    #Thank you for attending my Ted Talk
    if "\n" in a and vol == "z":
        noNewLinesText = a.split("\n")
        noNewLinesRes = map(mor, noNewLinesText)
        return "\n".join(noNewLinesRes)

    if a in dictionary1 or a in dictionary2:
        if vol == "do":
            #Pokud nový řádek, pak nový řádek, že ano?
            if a == "\n":
                return "\n"
            else:
                #Přeloží znak do morseovštiny - VERY HARD - a přídá custom oddělovač (WeirdChamp pokud to není mezera)
                return dictionary1[a] + sep
        elif vol == "z":
            #Vrátí překlad ze slovníku - easy peasy
            return dictionary2[a]
    else:
        #Velice důležitá část kódu - co nejvíce se vysmát člověku za to, že neumí zadat morseovku
        exit("Neumíš morsevku LMAOOOO - špatný symbol: " + a)

def prekladZ(raw):
    #Tohle hopefully zajistí větší kompatibilitu s jinými překladači (a nakonec to rozdělí na písmena)
    text = raw.replace("–","-").replace("−","-").replace("_","-").replace("·",".").replace("*",".").split(sep)
    #Využijeme znalostí zeměpisu k rozluštění morseovky (Outstanding move right here!)
    #Prostě to na každé písmeno aplikuje funkci zmor, která písmeno v morseovce nahradí reálným písmenem
    res = map(mor, text)
    #Lepší způsob na převedení listu do stringu jsem nenašel, takže here we go
    resultToFile("".join(res))

def cteniSouboru():
    #tímto krokem nahlédneme do vašeho počítače
    txt = input("Vložte název a cestu k souboru: ")
    #soubor si necháme bez vašeho povolení otevřít
    soubor = open(txt, "r")
    #a teď si ho nahráváme (PS. další krok nahrání na internet)
    raw = soubor.read()
    #zavíráme
    soubor.close()
    return raw

def prekladD(raw):
    #MILUJU CAPS-LOCK
    text = raw.upper()
    #TO VÍME, TO ZNÁME
    res = map(mor, text)
    final = "".join(res)
    #Odebere oddělovač úplně na konci (na funkcionalitě to nic nezměnilo, ale hrozně mě tam štval)
    if final[-1:] == sep:
        final = final[:-1]
    #Poslat výsledek souborové funkce
    resultToFile(final)

def getSep():
    #zjistíme, čím si uživatel přeje oddělovat znaky
    print("Abychom vaší šifru mohli dekódovat musíte vložit oddělovač písmen. Oddělovač nesmí být: . - – − _ · *")
    sep = input("Vložte oddělovač písmen: ")
    return sep

def resultToFile(r):
    #jak chce uživatel svůj překlad dostat: poštou, holubem, e-mailem
    resch=input("Váš překlad je připraven. Chcete ho vypsat do nového souboru: 'ns' nebo vám postačí ho vypsat zde: 'zde'? ")
    #získá ho hned v konzoli
    if resch =="zde":
        print(r)
    #budeme muset kvůli němu vytvořit celý nový soubor
    elif resch =="ns":
        f = open("preklad.txt", "w")
        f.write(r)
        f.close()
        print("Soubor preklad.txt vytvořen.")
        
#Na následujících 4 řádcích celý kód stojí - v žádném případě NEODSTRAŇOVAT!!
print("Projekťák WOOOO WOOOO WOOOO")
print("Zdravíčko elitní týme plný expertů na dané téma: Morseovka")
print("Převodník, který by bez 3 lidí NEFUNGOVAL")
print("zz")

#WIP slovníky
dictionary1 = {"A":".-", "B":"-...", "C":"-.-.","D":"-..", "E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
"CH":"----","Ä":".-.-","Ë":"..–..","Ö":"---.","Ü":"..--","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----",
"?":"..--..",",":"--..--",".":".-.-.-",";":"-.-.-.","/":"-..-.","=":"-...-","-":"-....-","'":".----.","(":"-.--.",")":"-.--.-","\"":".-..-.",":":"---...","_":"..--.-","+":".-.-.","@":".--.-."," ":"/","!":"-.-.--",
"Á":".-","Â":".-","É":".","Ě":".","Ę":".","Í":"..","Î":"..","Ó":"---","Ő":"---","Ô":"---","Ú":"..-","Ů":"..-","Ű":"..-","Ý":"-.--","Č":"-.-.","Ç":"-.-.","Ć":"-.-.","Ř":".-.","Š":"...","Ś":"...","Ž":"--..","Ź":"--..","Ť":"-","Ň":"-.","Ń":"-.","Ľ":".-..","Ĺ":".-..","Ł":".-..","Ď":"-..","\n":"\n"}

dictionary2 = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",
"----":"CH",".-.-":"Ä","..–..":"Ë","---.":"Ö","..--":"Ü",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0",
"..--..":"?","--..--":",",".-.-.-":".","-.-.-.":";","-..-.":"/","-...-":"=","-....-":"-",".----.":"'","-.--.":"(","-.--.-":")",".-..-.":"\"","---...":":","..--.-":"_",".-.-.":"+",".--.-.":"@","/":" ","":"","-.-.--":"!","\n":"\n"}

#uživatele si necháme zvolit zda chce dekodovat či kodovat (nejsme jako ti, co vám ani nedají na výběr)
print("Zvolte zda budete chtít překládat do moseovky/ z morseovky:")

#Tohle uživatele donutí strefit se na klávesnici
while True:
    vol=input("Pro překlad do morseovky napiš: 'do', pro překlad z morseovky napiš: 'z': ")

    #PŘEKLAD ZMOR
    if vol == "z":
        #opět necháme uživatele rozhodnout - může dokonce nahrát soubor z .dxd
        roz=input("Budete chtít nahrát kód ze souboru (.txt) - napište: 's', pokud budete chtít kód napsat ručně - napište: 'n': ")
        #rozhodl se používat klávesnici
        if roz == "n":
            #Pullneme klasický Facebook move, kdy z uživatelů vytáhneme všechna jejich data
            sep = getSep()
            raw = input("Vložte morseovku k přeložení: ")            
            prekladZ(raw)
            break
        #rozhodl se pro jednodušší cestu
        elif roz == "s":
            #TO už známe    
            sep = getSep()
            raw = cteniSouboru()                    
            prekladZ(raw)
            break

    #PŘEKLAD DOMOR
    elif vol == "do":
        roz=input("Budete chtít nahrát kód ze souboru (.txt) - napište: 's', pokud budete chtít kód napsat ručně - napište: 'n': ")
        if roz == "n":
            sep = getSep()
            raw = input("Vložte text k přeložení: ")            
            prekladD(raw)
            break
        elif roz == "s":
            sep = getSep()
            raw=cteniSouboru()            
            prekladD(raw)
            break
            
    #TI CO CHTĚJÍ BÝT VÝJIMEČNÍ
    else:
        print("Zadali jste špatnou volbu!!!")