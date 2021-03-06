#Ne pas oublier de changer le module à importer
module="Les_conditions/Conversion_Celsius_Fahrenheit"

import sys
import io
from ma_bao import *
tester("from Conversion_Celsius_Fahrenheit import mon_programme ",globals())

#liste des couples input/output
input_output=[\
((0,0),32.0),\
((100,0),212.0),\
((0,1),-17.778),\
((100,1),37.778),\
((37,0),98.6),\
((-273.15,0),-459.67)\
]


#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"

#Afficher la correction
def afficher_correction():
    try:
        with open(module+"_Correction.py", "r") as correction :
            ligne="Voici un ou des exemples de corrections possibles"
            send_msg("Exemple(s) de correction", ligne)
            ligne="-------------------------------------------------"
            send_msg("Exemple(s) de correction", ligne)
            lignes=correction.read().split("\n")
            for ligne in lignes:
                send_msg("Exemple(s) de correction", ligne)
    except:
        pass

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    send_msg("Tests validés","Bravo !")
    afficher_correction()
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for inp,outp in input_output:
        sauvegarde_stdout=sys.stdout
        sys.stdout=io.StringIO()
        mon_programme(*inp)
        count1 = sys.stdout.getvalue()[:-1]
        sys.stdout=sauvegarde_stdout
        assert str(count1) == str(outp), "En testant les valeurs {} le résultat obtenu est {} au lieu de {}".format(str(inp),str(count1),str(outp))
        send_msg("Tests validés",("La température {}°"+"C"*(inp[1]==0)+"F"*(inp[1]==1)+" correspond bien à {}°"+"C"*(inp[1]==1)+"F"*(inp[1]==0)).format(str(inp[0]),str(count1)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()

