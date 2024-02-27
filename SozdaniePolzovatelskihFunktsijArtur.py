def korrutis(arv1:float, arv2:float,arv2:float,arv3:float,float,arv4=1,0)->float... 
def suurid.element(arvud1:list,arvud2:list):

#(1)
def arithmetic(arv1:float, arv2:float,sumb:str)->any:
    """Funktsion tagastab aritmeetiliste tehteda tulemused.
    + - liitumine
    - - Lahutamine
    * - korrutamine
    / - jagamine
    :param float arv1: ujukomaarv mis sisetab kasutaja
    :param float arv2: ujukomaarv mis sisetab kasutaja
    :param str sumb:sõne/tehe , mis sisetab kasutaja
    """
 if sumb=="+":
     vastus=arv1+arv2
 elif sumb=="-":
     vastus=arv1-arv2
 elif sumb=="*":
     vastus==arv1*arv2
 elif sumb=="/":
     if arv2==0:
         vastus="Div/0"
     else:
        vastus=arv1/arv2
 else:
     vastus="Tundmatu operatsioon"
 return vastus

#(2)

