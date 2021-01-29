def mor(a):
    if a in dictionary1 or a in dictionary2:
        if vol == "do":
            #Přeloží znak do morseovštiny - VERY HARD - a přídá custom oddělovač (weirdchamp pokud to není mezera)
            return dictionary1[a] + sep
        elif vol == "z":
            #Vrátí překlad ze slovníku - easy peasy
            return dictionary2[a]
    else:
        #Velice důležitá část kódu - co nejvíce se vysmát člověku za to, že neumí zadat morseovku
        exit("Neumíš morsevku LMAOOOO - špatný symbol: " + a)
        
#Na následujících 4 řádcích celý kód stojí - v žádném případě NEODSTRAŇOVAT!!
print("Projekťák WOOOO WOOOO WOOOO")
print("Zdravíčko elitní týme plný expertů na dané téma: Morseovka")
print("Převodník, který by bez 3 lidí NEFUNGOVAL")
print("zz")

#WIP slovníky
dictionary1 = {"A":".-", "B":"-...", "C":"-.-.","D":"-..", "E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
"CH":"----","Ä":".-.-","Ë":"..–..","Ö":"---.","Ü":"..--","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----",
"?":"..--..",",":"--..--",".":".-.-.-",";":"-.-.-.","/":"-..-.","=":"-...-","-":"-....-","'":".----.","(":"-.--.",")":"-.--.-","\"":".-..-.",":":"---...","_":"..--.-","+":".-.-.","@":".--.-."," ":"/","!":"-.-.--",
"Á":".-","É":".","Ě":".","Í":"..","Ó":"---","Ú":"..-","Ů":"..-","Ý":"-.--","Č":"-.-.","Ř":".-.","Š":"...","Ž":"--..","Ť":"-"}

dictionary2 = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",
"----":"CH",".-.-":"Ä","..–..":"Ë","---.":"Ö","..--":"Ü",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0",
"..--..":"?","--..--":",",".-.-.-":".","-.-.-.":";","-..-.":"/","-...-":"=","-....-":"-",".----.":"'","-.--.":"(","-.--.-":")",".-..-.":"\"","---...":":","..--.-":"_",".-.-.":"+",".--.-.":"@","/":" ","":" ","-.-.--":"!"}

#uživatele si necháme zvolit zda chce dekodovat či kodovat (nejsme jako ti, co vám ani nedají na výběr)
print("Zvolte zda budete chtít překládat do moseovky/ z morseovky:")

#Tohle uživatele donutí strefit se na klávesnici
while True:
    vol=input("Pro překlad do morseovky napiš: 'do', pro překlad z morseovky napiš 'z': ")

    #PŘEKLAD ZMOR
    if vol == "z":
        #opět necháme uživatele rozhodnout - může dokonce nahrát soubor z .dxd
        roz=input("Budete chtít nahrát kód ze souboru (.txt) - napiš: 's', pokud budeš kód napsat - napiš: 'n'")
        #rozhodl se používat klávesnici
        if roz == "n":
            #Pullneme klasický Facebook move, kdy z uživatelů vytáhneme všechna jejich data
            raw = input("Vložte morseovku k přeložení: ")
            print("Abychom vaší šifru mohli dekodovat musíte vložit oddělovač písmen. Oddělovč nesmí být: . - – − _ · *")
            sep = input("Vložte oddělovač písmen: ")
            #Tohle hopefully zajistí větší kompatibilitu s jinými překladači (a nakonec to rozdělí na písmena)
            text = raw.replace("–","-").replace("−","-").replace("_","-").replace("·",".").replace("*",".").split(sep)
            #Využijeme znalostí zeměpisu k rozluštění morseovky (Outstanding move right here!)
            #Prostě to na každé písmeno aplikuje funkci zmor, která písmeno v morseovce nahradí reálným písmenem
            res = map(mor, text)
            #Lepší způsob na převedení listu do stringu jsem nenašel, takže here we go
            print("".join(res))
            break
        #rozhodl se pro jednodušší cestu
        elif roz == "s":
            #tímto krokem nahlédneme do vašeho počítače
            txt = input("Vložte název a cestu k souboru:")
            #soubor si necháme bez vašeho povolení otevřít
            soubor = open(txt, "r")
            #TO-DO: při čtení váceřádků error, závest odstranění neviditelného enteru
            #a teď si ho nahráváme (PS. další krok nahrání na internet)
            raw=(soubor.read())
            #to už známe
            print("Abychom vaší šifru mohli dekodovat musíte vložit oddělovač písmen. Oddělovč nesmí být: . - – − _ · *")
            sep = input("Vložte oddělovač písmen: ")
            soubor.close()
            text = raw.replace("–","-").replace("−","-").replace("_","-").replace("·",".").replace("*",".").split(sep)
            res = map(mor, text)
            print("".join(res))
            break

    #PŘEKLAD DOMOR
    elif vol == "do":
        raw = input("Vložte text k přeložení: ")
        sep = input("Vložte oddělovač písmen: ")
        #MILUJU CAPS-LOCK
        text = raw.upper()
        #TO VÍME, TO ZNÁME
        res = map(mor, text)
        #TO VÍME, TO ZNÁME
        print("".join(res))
        break

    #TI CO CHTĚJÍ BÝT VÝJIMEČNÍ
    else:
        print("Zadali jste špatnou volbu!!!")