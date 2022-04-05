import random

d = ["Brille", "Gnavpot", "Lystig", "Prosit", "Flovmand", "Søvnig", "Dumpe"]
sted = ["køkkenet", "garagen", "skuret", "hytten", "badeværelset", "vaskekælderen", "drivhuset"]
handling = ["sidder", "står", "befinder sig", "går rundt", "er til stede", "er", "opholder sig"]

alting = list(zip(sted, d, handling)) #saml alle lister 

random.shuffle(alting) #randomize
sted, d, handling = zip(*alting) #udpak tilbage til separate lister

print("___________________")

aktuelle_d = [d[0], d[1]] #definer hvilke dværge i lokalet
print(aktuelle_d)

intro_text = ("{} kommer ind ad døren til {}, hvor {} allerede {}.".format(d[1], sted[0], d[0], handling[0])) #intro
print(intro_text)


if d[0] == "Brille" and d[1] == "Gnavpot" or d[1] == "Brille" and d[0] == "Gnavpot":
    print("Med det samme kaster Brille en kniv i hjertet på Gnavpot, der dør på stedet.")
    print("Han pudser derefter sine briller: 'Fejl tog jeg. Ups! Død han er?'")
    aktuelle_d.remove("Gnavpot")
    print("{} træder ind i lokalet ved lyden af det voldsomme spektakel.". format(d[2]))
    aktuelle_d.append(d[2])
    print(aktuelle_d)
    if d[2] != "Dumpe":
        print("'Sikke et spektakel! Og så endda midt i {}.'". format(sted[0]))
    elif d[2] == "Dumpe":
        print("Han vælter forvirret rundt og kigger på Gnavpots døde krop.")

elif d[0] == "Brille" and d[1] == "Lystig" or d[1] == "Brille" and d[0] == "Lystig":
    print("Lystig griber om Brilles briller og griner, mens han stamper på dem: 'Haha!'")
    print("Ved lyden af brilleglas, der knækker dukker {} op.".format(d[2]))
    aktuelle_d.append(d[2])
    print(aktuelle_d)
    print("Brille snøfter og forlader {}, mens {} giver highfive til Lystig.".format(sted[0], d[2]))
    aktuelle_d.remove("Brille")
    print(aktuelle_d)

elif d[0] == "Prosit":
    if d[1] != "Dumpe":
        print("Prosit nyser kraftigt, og {} beder ham forlade {}, så der ikke opstår smitterisiko.".format(d[1], sted[0]))
    elif d[1] == "Dumpe":
        print("Prosit nyser kraftigt, og {} vælter klodset en genstand i nærheden som reaktion på den høje lyd.".format(d[1]))
        print("Prosit forlader {}, så der ikke er flere ting, der skal gå i stykker ved hans nys.".format(sted[0]))
    aktuelle_d.remove("Prosit")
    print("Ind kommer i stedet {}.".format(d[2]))
    aktuelle_d.append(d[2])
    print(aktuelle_d)
    if d[2] != "Dumpe":
        print("{} roser {} for at have fået {} til at forlade {}, så der udvises samfundssind.".format(d[2], d[1], d[0], sted[0]))
    elif d[2] == "Dumpe":
        print("Dumpe nikker anerkendende til {} for at have fået {} til at forlade {}, så der udvises samfundssind.".format(d[1], d[0], sted[0]))

elif d[0] == "Brille":
    print("'Jeg kan ikke finde mine briller!' siger Brille til {}. 'Vil du hjælpe med at lede?'".format(d[1]))
    if d[1] != "Dumpe":
        print("{} bakker med det samme ud af {}. 'Nej tak du. Men måske {} vil hjælpe.'".format(d[1], sted[0], d[2]))
    elif d[1] == "Dumpe":
        print("{} bakker med det samme ud af {} og vælter et par genstande undervejs. Han gør tegn til, at {} måske vil hjælpe i stedet.".format(d[1], sted[0], d[2]))
    aktuelle_d.pop()
    aktuelle_d.append(d[2])
    print(aktuelle_d)
    if d[2] != "Dumpe":
        print("{} finder hurtigt brillerne.".format(d[2]))
    elif d[2] == "Dumpe":
        print("{} finder ikke brillerne, men tramper i stedet på dem ved et uheld.".format(d[2]))

elif d[0] == "Gnavpot":
    print("'Jeg er ved at gøre rent herinde. Kan du vente lidt?' spørger Gnavpot til {}.".format(d[1]))
    if d[1] != "Dumpe":
        print("{} sukker. 'Jeg venter og kommer tilbage senere.'".format(d[1]))
    elif d[1] == "Dumpe":
        print("{} sukker, trækker på skuldrene og bevæger sig klodset tilbage ud ad døren.".format(d[1]))
    aktuelle_d.pop()
    print(aktuelle_d)
    if d[2] != "Dumpe":
        print("{} kommer ind i {}. 'Jeg skal nok hjælpe dig, {}, også selvom dit hjerte er så godt.'".format(d[2], sted[0], d[0]))
    elif d[2] == "Dumpe":
        print("{} kommer væltende ind i {}. Han gør mine til at ville hjælpe {}, også selvom hans hjerte er så godt.".format(d[2], sted[0], d[0]))
    print("Gnavpot ryster gnavent på hovedet.")
    aktuelle_d.append(d[2])
    print(aktuelle_d)

elif d[0] == "Lystig":
    if d[1] != "Dumpe":
        print("{} himler øjne over, hvor glad Lystig ser ud. 'Skrid væk med din muntre fremtoning.'".format(d[1]))
    elif d[1] == "Dumpe":
        print("{} himler øjne over, hvor glad Lystig ser ud. Hans dvaske blik synes at kommenetere, at Lystig skal skride væk med sin muntre fremtoning.".format(d[1]))
    print("Lystig hopper ved opfordringen muntert ud af lokalet, og ind træder i stedet {}.".format(d[2]))
    aktuelle_d.remove("Lystig")
    aktuelle_d.append(d[2])
    print(aktuelle_d)

elif d[0] == "Flovmand":
    print("Flovmand gemmer sig i sit skæg ved synet af {}. Hans kinder er helt røde.".format(d[1]))
    print("{} rødmer også. Er Flovmand mon forelsket i ham?".format(d[1]))
    print("Kærligheden i luften kan fornemmes på lang afstand, og {} træder ind i {} for at få stillet sin nysgerrighed.".format(d[2], sted[0]))
    aktuelle_d.append(d[2])
    print(aktuelle_d)
    print("Flovmand bliver endnu mere flov og stormer ud ad døren.")
    aktuelle_d.remove("Flovmand")
    print(aktuelle_d)

elif d[0] == "Søvnig":
    print("{} ser, at Søvnig har åbne øjne, men at han ikke ser ud til at være ved bevidsthed.".format(d[1]))
    if d[1] != "Dumpe":
        print("'Vågn op, Søvnig,' siger han. 'Det er ikke sundt at gå i søvne.'")
    elif d[1] == "Dumpe":
        print("Dumpe prøver at vække ham, fordi han har hørt, at det ikke er sundt at gå i søvne.")
    print("I stedet for at vågne går Søvnig ud af {}, mens han stadig sover.".format(sted[0]))
    print("Ind kommer i stedet {}. Han er synligt creeped out efter at have set Søvnig famle sig vej ud af {}.".format(d[2], sted[0]))
    aktuelle_d.remove("Søvnig")
    aktuelle_d.append(d[2])
    print(aktuelle_d)

elif d[0] == "Dumpe":
    print("{} klapper overbærende Dumpe på skulderen.".format(d[1]))
    print("Dumpe hader at blive klappet på skulderen og løber forvildet ud af {}.".format(sted[0]))
    aktuelle_d.remove("Dumpe")
    print(aktuelle_d)
    print("{} råber til {}: 'Så er der fri bane! Kom bare ind.'".format(d[1], d[2]))
    aktuelle_d.append(d[2])
    print(aktuelle_d)
    print("De to kysser hinanden passioneret.")

#reaktioner, sidste på listen af aktuelle dværge
if aktuelle_d[1] == "Brille":
    print("'Her i {}, for meget drama der er,' udbryder Brille, mens han retter på brillerne.".format(sted[0]))
elif aktuelle_d[1] == "Gnavpot":
    print("Gnavpot ser sur ud, men trækker alligevel overbærende på skuldrene af begivenhederne i {}.".format(sted[0]))
elif aktuelle_d[1] == "Lystig":
    print("Det er med et smørret grin, at Lystig begiver sig ud i en lille dans efter dagens begivenheder i {}.".format(sted[0]))
elif aktuelle_d[1] == "Prosit":
    print("Prosit nyser - som han altid gør.")
elif aktuelle_d[1] == "Flovmand":
    print("En kraftig rødmen breder sig over Flovmands ansigt, og han overvejer, om han nogensinde tør sætte fod i {} igen.".format(sted[0]))
elif aktuelle_d[1] == "Søvnig":
    print("Søvnig strækker sig træt. Situationen i {} er mere ophidsende, end han orker at forholde sig til.".format(sted[0]))
elif aktuelle_d[1] == "Dumpe":
    print("Dumpe klapper små-dumt i hænderne over situationen.")
else:
    print("Noget er gået galt.")