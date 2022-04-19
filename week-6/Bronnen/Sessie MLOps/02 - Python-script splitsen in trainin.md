# 02 - Python-script splitsen in training en eval

Splits het bestand nu in twee delen:

1. Een bestand dat de training doet (t/m pickle.dump)
2. Een bestand dat het model laadt en vervolgens evalueert, en de resultaten terugschrijft

Vervolgens voegen we hier een REST service aan toe die in de gaten houdt of er een nieuwe evaluatie moet gebeuren.

Nu breiden we het uit, en zorgen we ervoor dat de data van een storage af gaat komen.