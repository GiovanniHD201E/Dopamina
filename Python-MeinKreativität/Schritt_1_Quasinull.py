#Wenn zwei Elemente sind näher, welche Wechseln tritten zwischenbeiden ein?

import random

Klasse = ['Umgebung', 'C-H-O-N-P-S'] # Environment and 'Pseudo Chemical Elements, Carbon, Hydrogeny, etc..
Reihe = ['A','n','a']

print(Reihe)
print(Klasse)

par1 = 3

Sternen = 'x-o-' * par1, 'x-o- ' * par1, '-x-' * par1, 'x-x ' * par1, 'x-x- ' * par1

Stern = random.choice(Sternen)

Neue_Abschnitt = '\n' + Stern + " New Section " + Stern + " Novo Tópico " + Stern + '\n'

print(Neue_Abschnitt)

print #<built-in function print>

help(print)

dir()	#['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']


S = """\
... [1] Eigentlich sind Funktionsdefinitionen auch ‘Anweisungen’, die ‘ausgeführt’ werden; die Ausführung einer Funktionsdefinition auf Modulebene fügt den Funktionsnamen in die globale Symboltabelle des Moduls ein."""
type(S)
print(S)
len(S) # 211
# S.reverse() falhou, pois 'str' object has no attribute 'reverse'

Zk = str(S)

Zk.strip() # Um erro de grafia, mas experimente!

print(Neue_Abschnitt)

S1 = "Oft will man mehr Kontrolle über die Formatierung der Ausgabe haben als nur Leerzeichen-getrennte Werte auszugeben. Es gibt zwei Arten die Ausgabe zu formatieren: Die erste Möglichkeit ist, dass man die gesamte Verarbeitung der Zeichenketten selbst übernimmt; indem man Slicing- und Verknüpfungsoperationen benutzt, kann man jede denkbare Anordnung zusammenstellen. Der Typ string hat einige Methoden, die ein paar nützliche Operationen ausführen, um Zeichenketten auf eine bestimmte Länge aufzufüllen; diese werden wir in Kürze behandeln. Die zweite Möglichkeit ist die Benutzung der format() -Methode."

print(S1)
