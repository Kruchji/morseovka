def zmor(a):
    if a in dictionary[0]:
        #Velice big brain řádek
        #Najde index kódu ve slovníku a pak ho vyhledá ve slovníku písmen
        return dictionary[1][dictionary[0].index(a)]
    else:
        #Velice důležitá část kódu - co nejvíce se vysmát člověku za to, že neumí zadat morseovku
        exit("Neumíš morsevku LMAOOOO - špatný symbol: " + a)
    
#Na následujících 4 řádcích celý kód stojí - v žádném případě NEODSTRAŇOVAT!!
print("Projekťák WOOOO WOOOO WOOOO")
print("Zdravíčko elitní týme plný expertů na dané téma: Morseovka")
print("Převodník, který by bez 3 lidí NEFUNGOVAL")
print("zz")

#WIP slovník
#TO-DO: Předělat slovník z listu na dictionary (bude to přehlednější)
dictionary = {"A":".-", "B":"-...", "C":"-.-.","D":"-..", "E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..",
"CH":"----","Ä":".-.-","Ë":"..–..","Ö":"---.","Ü":"..--","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----",
"?":"..--..",",":"--..--",".":".-.-.-",";":"-.-.-.","/":"-..-.","=":"-...-","-":"-....-","'":".----.","(":"-.--.",")":"-.--.-","\"":".-..-.",":":"---...","_":"..--.-","+":".-.-.","@":".--.-."," ":"/"," ":"","!":"-.-.--"}

ditionary2 = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",
"----":"CH",".-.-":"Ä","..–..":"Ë","---.":"Ö","..--":"Ü",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0",
"..--..":"?","--..--":",",".-.-.-":".","-.-.-.":";","-..-.":"/","-...-":"=","-....-":"-",".----.":"'","-.--.":"(","-.--.-":")",".-..-.":"\"","---...":":","..--.-":"_",".-.-.":"+",".--.-.":"@","/":" ","":" ","-.-.--":"!"}
#Pullneme klasický Facebook move, kdy z uživatelů vytáhneme všechna jejich data
raw = input("Vložte morseovku k přeložení: ")
sep = input("Vložte oddělovač písmen: ")
#TO-DO: Upozornit uživatele, jaké oddělovače nemůže vložit (.-–−_·*)

#Tohle hopefully zajistí větší kompatibilitu s jinými překladači (a nakonec to rozdělí na písmena)
text = raw.replace("–","-").replace("−","-").replace("_","-").replace("·",".").replace("*",".").split(sep)

#Využijeme znalostí zeměpisu k rozluštění morseovky (Outstanding move right here!)
#Prostě to na každé písmeno aplikuje funkci zmor, která písmeno v morseovce nahradí reálným písmenem
res = map(zmor, text)
final = ""
#Lepší způsob na převedení listu do stringu jsem nenašel, takže here we go
print(final.join(res))