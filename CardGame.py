import random

def basic_trap(noumera,symbols):
    '''
    Συνάρτηση που κατασκευάζει την τράπουλα για το παιχνίδι και γυρνάει μια 
    λίστα που περιέχει σε μορφή string τις κάρτες
    
    noumera-- λίστα που περιέχει το νούμερο η την φιγούρα της κάρτας
    symbols-- λίστα που περιέχει την κατηγορία της κάρτας όπως κούπα σπαθί κ.ο.κ.:
    
    >>> noumera=['1','2','3','4']
    >>> symbols=['\u2660','\u2663','\u2665','\u2666']
    >>> d=basic_trap(noumera,symbols)
    >>> print(d)
    ['1♠', '2♠', '3♠', '4♠', '1♣', '2♣', '3♣', '4♣', '1♥', '2♥', '3♥', '4♥', '1♦', '2♦', '3♦', '4♦']
    '''
    cards=[]
    for i in range(len(symbols)):
        for x in range(len(noumera)):
            cards.append(noumera[x]+symbols[i])
    return cards


def joker_placer(row,col):
    '''
    Συνάρτηση που κατασκευάζει το ταμπλό του παιχνιδιού σε μορφή λεξικού
    
    row-- Πόσες σειρές θέλουμε να εχει το ταμπλό σε μορφή λίστας
    col-- Πόσες στήλες θέλουμε να έχει το ταμπλό σε μορφή λίστας
    
    Μέσα το λεξικό περιέχει συντεταγμένες σε μορφή tuple όπως πχ (2,1),(1,2) κλπ:
    
    >>> row=[1,2,3,4]
    >>> col=[1,2,3,4]
    >>> e=joker_placer(row,col)
    >>> print(e)
    {(1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False}
    '''
    oxforddict={}
    for single in range(1,len(row)+1):
        for pringle in range(1,len(col)+1):
            truffle=(single,pringle)
            oxforddict.update({truffle:False})
    return oxforddict  


def showman_joker(joker,col,row,cards):
    '''
    Συνάρτηση που εμφανίζει το ταμπλό του παιχνιδιού
    
    row-- Πόσες σειρές θέλουμε να εχει το ταμπλό σε μορφή λίστας
    col-- Πόσες στήλες θέλουμε να έχει το ταμπλό σε μορφή λίστας
    joker-- Ένα λεξικό που προκύπτει από την συνάρτηση  joker_placer (ή μπορεί να είναι λεξικό της επιλογής μας)
    cards-- Λίστα που περιέχει της κάρτες της τράπουλας που δημιουργήσαμε:

    #Η συνάρτηση αυτή φαίνεται όσο παίζουμε το παιχωίδι ότι λειτουργεί#
    #Όσο έτρεχα το παιχνίδι δοκιμάζοντας το (γράφωντας ένα doctest) για κάποιο λόγο ενώ γύρναγε το ίδιο αποτέλεσμα το έπιανε ως λάθος#
    '''
    misery=''
    counter=0
    for iamblue in range(1,len(col)+1):
        misery+='|'+str(iamblue)
    print('',misery)
    for kokkinhgrammh in range(1,len(row)+1):
        hope=''
        for iamblue in range(1,len(col)+1):
            hope+=(cards[counter] if joker[(kokkinhgrammh,iamblue)]==True else ' ?')
            counter+=1
        print(str(kokkinhgrammh),hope)


    
def sleeve_card(joker,bless):
    '''
    Συνάρτηση που ανοίγει μία κάρτα της επιλογής μας πάνω στο ταμπλό
    
    joker-- Ένα λεξικό που προκύπτει από την συνάρτηση  joker_placer (ή μπορεί να είναι λεξικό της επιλογής μας)
    bless-- Οι συντεταγμένες που θέλουμε σε μορφή tuple:
    
    >>> joker={(1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False}
    >>> bless=(2,1)
    >>> sleeve_card(joker,bless)
    >>> print(joker)
    {(1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (2, 1): True, (2, 2): False, (2, 3): False, (2, 4): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False}
    '''
    resurrection=joker.update({bless:True})
    return resurrection


def isitwrong(bless,joker,row,col):
    '''
    Συνάρτηση που ελέγχει αν είναι ήδη ανοιχτή η κάρτα που επιλέξαμε και αν είναι μας βάζει να ξαναεπιλέξουμε κάρτα
    
    bless-- Οι συντεταγμένες που θέλουμε σε μορφή tuple
    joker-- Ένα λεξικό που προκύπτει από την συνάρτηση  joker_placer (ή μπορεί να είναι λεξικό της επιλογής μας)
    row-- Πόσες σειρές θέλουμε να εχει το ταμπλό σε μορφή λίστας
    col-- Πόσες στήλες θέλουμε να έχει το ταμπλό σε μορφή λίστας:
    
    #Σε αυτή την συνάρτηση δεν μπορώ να σκεφτώ κάποιο doctest αλλά μέσα από δοκιμές είδα πως δουλεύει#
    
    '''
    while joker[bless]==True:
        bless=epilogh(row,col)
        isitwrong(bless,joker,row,col)
    return bless

    
    
def repeat_res(sleeve_card,row,col,last_joker):
    '''
    Συνάρτηση που μετατρέπει όλο το ταμπλό από κλειστό σε ανοιχτό(από False όλα θα γίνουν True)
    
    last_joker-- Ένα λεξικό που προκύπτει από την συνάρτηση  joker_placer (ή μπορεί να είναι λεξικό της επιλογής μας)
    sleeve_card-- Συνάρτηση για να γυρίζουν οι κάρτες
    row-- Πόσες σειρές θέλουμε να εχει το ταμπλό σε μορφή λίστας
    col-- Πόσες στήλες θέλουμε να έχει το ταμπλό σε μορφή λίστας:
    
    >>> last_joker={(1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False}
    >>> row=[1,2,3,4]
    >>> col=[1,2,3,4]
    >>> last_joker=repeat_res(sleeve_card,row,col,last_joker)
    >>> print(last_joker)
    {(1, 1): True, (1, 2): True, (1, 3): True, (1, 4): True, (2, 1): True, (2, 2): True, (2, 3): True, (2, 4): True, (3, 1): True, (3, 2): True, (3, 3): True, (3, 4): True, (4, 1): True, (4, 2): True, (4, 3): True, (4, 4): True}
    '''
    for i in range(1,len(row)+1):
        for j in range(1,len(col)+1):
            sleeve_card(last_joker,(i,j))
    return last_joker


def dolphin_joker(joker):
    '''
    Συνάρτηση για να αντιγραφεί το ταμπλό του παιχνιδιού
    
    joker-- Ένα λεξικό που προκύπτει από την συνάρτηση  joker_placer (ή μπορεί να είναι λεξικό της επιλογής μας)
    
    #Αυτή η συνάρτηση είναι για πιο άνετη κατανόηση τον κινήσεων μέσα στο παιχνίδι οπότε δεν υπάρχει κατι να ελέγξουμε#
    '''
    flippy=joker.copy()
    return flippy


def startingpoint(players):
    '''
    Συνάρτηση για να φτιεχτεί μία λίστα που περίεχει τους πόντους των παικτών
    
    players-- Λίστα που περιέχει τα ονόματα των παικτών:
    
    '''
    innerstr=[]
    for i in range(len(players)):
        innerstr+=[0]
    return innerstr


def gainingpower(trapcard,scoreboard,gyros):
    '''
    Συνάρτηση που ανάλογα τις κάρτες που ανοίξαμε προσθέτει αντίστοιχα πόντους
    
    trapcard-- Λίστα που περιέχει τις κάρτες που ανοίξαμε
    scoreboard-- Λίστα που περιέχει τους πόντους των παικτών
    gyros-- Μία μεταβλητή που χρησιμοποίησα για να μετράω τους γύρους αλλά το σημαντικότερο να μπορώ να τοποθετώ τους πόντους στον σωστό παίκτη΄:
    
    >>> scoreboard=[0,0,0]
    >>> trapcard=['2p', '2d']
    >>> gyros=0
    >>> g=gainingpower(trapcard,scoreboard,gyros)
    >>> print(g)
    [2, 0, 0]
    '''
    if len(trapcard)==3:
        if trapcard[0][0]==trapcard[2][0]:
            scoreboard[gyros%len(scoreboard)]+=10
        elif trapcard[1][0]==trapcard[2][0]:
            scoreboard[gyros%len(scoreboard)]+=10
        else:
            pass
    else:
        if 'A'==trapcard[0][0]:
            if 'A'==trapcard[1][0]:
                scoreboard[gyros%len(scoreboard)]+=1
        elif 'K'==trapcard[0][0]:
            if 'K'==trapcard[1][0]:
                scoreboard[gyros%len(scoreboard)]+=10
        elif 'Q'==trapcard[0][0]:
            if 'Q'==trapcard[1][0]:        
                    scoreboard[gyros%len(scoreboard)]+=10
        elif 'J'==trapcard[0][0]:
            if 'J'==trapcard[1][0]:    
                scoreboard[gyros%len(scoreboard)]+=10
        elif '1'==trapcard[0][0]:
            if '1'==trapcard[1][0]:
                scoreboard[gyros%len(scoreboard)]+=10
        elif trapcard[0][0]==trapcard[1][0]:
            scoreboard[gyros%len(scoreboard)]+=int(trapcard[0][0])
        else:
            pass

    return scoreboard

            

def passinggyros(gyros,trapcard):
    '''
    Συνάρτηση για να πραγματοποιούνται οι ικανότητες των ειδικών καρτών (του ρήγα και του βαλέ μόνο)
    
    trapcard-- Λίστα που περιέχει τις κάρτες που ανοίξαμε
    gyros-- Μία μεταβλητή που χρησιμοποίησα για να μετράω τους γύρους:
    
    >>> trapcard=['Kp', 'Kd']
    >>> gyros=0
    >>> w=passinggyros(gyros,trapcard)
    >>> print(w)
    1
    '''
    if 'K'==trapcard[0][0]:
        if 'K'==trapcard[1][0]:
            gyros+=1
    elif trapcard[0][0]==trapcard[1][0]:
        if 'J'==trapcard[0][0]:
            gyros+=(-1)
    return gyros



def saving_card(bless,trapcard,cards,col):
    '''
    Συνάρτηση που αποθηκεύει την τιμή της κάρτας που ανοίξαμε σε μία λίστα
    
    bless-- Οι συντεταγμένες που θέλουμε σε μορφή tuple
    cards-- Λίστα που περιέχει της κάρτες της τράπουλας που δημιουργήσαμε
    trapcard-- Λίστα που περιέχει τις κάρτες που ανοίξαμε (Σε αυτό το σημείο μπορεί να είναι και άδεια)
    col-- Πόσες στήλες θέλουμε να έχει το ταμπλό σε μορφή λίστας:
    
    >>> col=[1,2,3,4]
    >>> trapcard=[]
    >>> cards=['1♠', '2♠', '3♠', '4♠', '1♣', '2♣', '3♣', '4♣', '1♥', '2♥', '3♥', '4♥', '1♦', '2♦', '3♦', '4♦']
    >>> bless=(2,1)
    >>> l=saving_card(bless,trapcard,cards,col)
    >>> print(l)
    ['1♣']
    '''
    biscuit=bless[1]+len(col)*bless[0]-(len(col)+1)
    trapcard.append(cards[biscuit])
    return trapcard



def lovebirds(trapcard,joker,bless1,bless2,row,col,final_ace,cards):
    '''
    Συνάρτηση που ελέγχει την τρίτη ειδική περίπτωση (Αν ανοίξουμε ρήγα με ντάμα)
    
    trapcard-- Λίστα που περιέχει τις κάρτες που ανοίξαμε
    joker-- Ένα λεξικό που προκύπτει από την συνάρτηση  joker_placer (ή μπορεί να είναι λεξικό της επιλογής μας)
    bless1-- Οι συντεταγμένες που θέλουμε σε μορφή tuple #κάρτα1
    bless2-- Οι συντεταγμένες που θέλουμε σε μορφή tuple #κάρτα2
    row-- Πόσες σειρές θέλουμε να εχει το ταμπλό σε μορφή λίστας
    col-- Πόσες στήλες θέλουμε να έχει το ταμπλό σε μορφή λίστας
    final_ace-- Ένα αντίγραφο του αρχικού λεξικού που έχει ανοιχτές τις κάρτες στις συντεταγμένες bless1 bless2
    cards-- Λίστα που περιέχει της κάρτες της τράπουλας που δημιουργήσαμε

    #Επειδή ζητάει έπειτα τιμή για τρίτη κάρτα για αυτό τον λόγο δεν έβαλα doctest εδώ#
    
    '''
    if 'K' in trapcard[0][0]:
        if 'Q' in trapcard[1][0]:
            bless3=epilogh(row,col)
            epomena_bhmata(final_ace,row,col,cards,trapcard,bless3)
            if trapcard[0][0]==trapcard[2][0]:
                sleeve_card(joker,bless1)
                sleeve_card(joker,bless3)
            elif trapcard[1][0]==trapcard[2][0]:
                sleeve_card(joker,bless2)
                sleeve_card(joker,bless3)
    elif 'K' in trapcard[1][0]:
        if 'Q' in trapcard[0][0]:
            bless3=epilogh(row,col)
            epomena_bhmata(final_ace,row,col,cards,trapcard,bless3)
            if trapcard[0][0]==trapcard[2][0]:
                sleeve_card(joker,bless1)
                sleeve_card(joker,bless3)
            elif trapcard[1][0]==trapcard[2][0]:
                sleeve_card(joker,bless2)
                sleeve_card(joker,bless3)
    else:
        pass



def somecountdown(trapcard,joker,bless1,bless2):
    '''
    Συνάρτηση που ελεγχει αν οι κάρτες που ανοίξαμε έχουν τον ίδιο αριθμό η φιγούρα
    
    trapcard-- Λίστα που περιέχει τις κάρτες που ανοίξαμε
    joker-- Ένα λεξικό που προκύπτει από την συνάρτηση  joker_placer (ή μπορεί να είναι λεξικό της επιλογής μας)
    bless1-- Οι συντεταγμένες που θέλουμε σε μορφή tuple #κάρτα1
    bless2-- Οι συντεταγμένες που θέλουμε σε μορφή tuple #κάρτα2:
    
    >>> trapcard=['1♠','1♣']
    >>> joker={(1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False}
    >>> bless1=(1,1)
    >>> bless2=(1,2)
    >>> joker=somecountdown(trapcard,joker,bless1,bless2)
    >>> print(joker)
    {(1, 1): True, (1, 2): True, (1, 3): False, (1, 4): False, (2, 1): False, (2, 2): False, (2, 3): False, (2, 4): False, (3, 1): False, (3, 2): False, (3, 3): False, (3, 4): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False}
    '''
    if trapcard[0][0]==trapcard[1][0]:
        sleeve_card(joker,bless1)
        sleeve_card(joker,bless2)
    else:
        pass
    return joker

     
def wedidit(players,scoreboard):
    '''
    Συνάρτηση τελική συνάρτηση που τυπώνει το όνομα του παίκτη και τους βαθμούς που συγκέντρωσε
    
    players-- Λίστα που περιέχει τα ονόματα των παικτών
    scoreboard-- Λίστα που περιέχει τους πόντους των παικτών:
    
    >>> players=['A','B']
    >>> scoreboard=[10,5]
    >>> wedidit(players,scoreboard)
    Συγχαρητήρια  A  πήρες  10  πόντους!
    Συγχαρητήρια  B  πήρες  5  πόντους!
    '''  
    for i in range(len(players)):
        print('Συγχαρητήρια ',players[i],' πήρες ',scoreboard[i],' πόντους!')
   


         
def epilogh(row,col):
    '''
    Συνάρτηση που γυρίζει σε μορφή tuple τις συντεταγμένες που εισήγαγε ο χρήστης
    
    row-- Πόσες σειρές θέλουμε να εχει το ταμπλό σε μορφή λίστας
    col-- Πόσες στήλες θέλουμε να έχει το ταμπλό σε μορφή λίστας
    
    #Δεν μπορώ να βάλω doctest επειδή θέλει τιμές από χρήστη#
    
    '''
    a=int(input('Κάθετη συντεταγμένη: '))
    b=int(input('Οριζόντια συντεταγμένη: '))
    while a not in range(1,len(col)+1):
        print('Δώστε τιμή μέσα στα όρια')
        a=int(input('Κάθετη συντεταγμένη: '))
    while b not in range(1,len(row)+1):
        print('Δώστε τιμή μέσα στα όρια')
        b=int(input('Οριζόντια συντεταγμένη: '))
    return (b,a)



def paiktes():
    '''
    Συνάρτηση που δίνει τα ονόματα των παικτών σε μορφή λίστας
    
    Δέχεται τον αριθμό των παικτών ο οποίος πρέπει να είναι παραπάνω απο 1 και τους βάζει να ορίσουν το όνομα τους

    '''
    numplayers=int(input('Δώστε αριθμό παικτών: '))
    playernames=[]
    i=1
    while numplayers<2:
        print('Απαιτούνται παραπάνω παίκτες')
        numplayers=int(input('Δώστε αριθμό παικτών: '))
    while i<=numplayers:
        d=str( input('Δώστε όνομα παίκτη:'))
        playernames.insert((i-1),d)
        i+=1
    for i in range(0,len(playernames)):
        print(playernames[i])
    return playernames


def dikosas():
    '''
    Συνάρτηση που δέχεται την δυσκολία του παιχνιδιού
    
    Δέχεται τον αριθμό δυσκολίας εάν αυτός είναι έγκυρος
    
    '''
    difficultylevel=int(input('Επιλέψτε το επίπεδο δυσκολίας Εύκολο(1), Μέτριο(2), Δύσκολο(3): '))
    while difficultylevel not in range(1,4):
        print('Επιλέψτε υπαρκτή τιμή παρακαλώ')
        difficultylevel=int(input('Επιλέψτε το επίπεδο δυσκολίας Εύκολο(1), Μέτριο(2), Δύσκολο(3): '))
    return difficultylevel

    
def epomena_bhmata(joker,row,col,cards,trapcard,bless):
    '''
    Συνάρτηση που χρησιμοποίησα για να πραγματοποιούνται οι απαραίτητες ενέργειες για το άνοιγμα μίας κάρτας

    joker-- Ένα λεξικό που προκύπτει από την συνάρτηση  joker_placer (ή μπορεί να είναι λεξικό της επιλογής μας)
    row-- Πόσες σειρές θέλουμε να εχει το ταμπλό σε μορφή λίστας
    col-- Πόσες στήλες θέλουμε να έχει το ταμπλό σε μορφή λίστας
    trapcard-- Λίστα που περιέχει τις κάρτες που ανοίξαμε
    bless-- Οι συντεταγμένες που θέλουμε σε μορφή tuple
    cards-- Λίστα που περιέχει της κάρτες της τράπουλας που δημιουργήσαμε:

    #Το ίδιο πρόβλημα το οποίο είχε και η showman_joker (ενώ γύρνανε το ίδιο αποτέλεσμα το θεωρεί λαθος)#
    '''        
    middle_joker=dolphin_joker(joker)
        
    sleeve_card(middle_joker,bless)
        
    saving_card(bless,trapcard,cards,col)
        
    showman_joker(middle_joker,col,row,cards)
    
    return middle_joker



def game(): 
    '''
    Συνάρτηση του παιχνιδιού. Αυτή την συνάρτηση καλούμαι ώστε να παάξουμε
    
    Μέσα από αυτή την συνάρτηση τρέχει το παιχνίδι. Περιέχει όλα τα απαιτούμενα βήματα όπως έλεγχος 
    αν έχει ανοίξει όλο το ταμπλό, τις επιλογές των καρτών και τέλος καλεί τις προηγούμενες συναρτήσεις
    
    #Δεν μπορώ να βάλω doctest καθώς καλείται η random#
    '''
    players=paiktes()
    soft=dikosas()
    if soft==1:
        noumera=['10','J','Q','K']
        symbols=['\u2660','\u2663','\u2665','\u2666']
        row=[1,2,3,4]
        col=[1,2,3,4]
    
        scoreboard=startingpoint(players)
        
        gyros=0
        
        cards=basic_trap(noumera,symbols)
        
        random.shuffle(cards)
        
        trapcard=[]
        
        joker=joker_placer(row,col)
        
        last_joker=dolphin_joker(joker)
        
        repeat_res(sleeve_card,row,col,last_joker)
        
        print('Καλώς ήλθατε στο παιχνίδι')
        
        showman_joker(last_joker,col,row,cards)
        
        print()
        
        showman_joker(joker,col,row,cards)
        
        while joker!=last_joker:
        
            bless1=epilogh(row,col)
        
            bless1=isitwrong(bless1,joker,row,col)
        
            middle_joker=epomena_bhmata(joker,row,col,cards,trapcard,bless1)  
            
            bless2=epilogh(row,col)
        
            bless2=isitwrong(bless2,middle_joker,row,col)    
        
            final_ace=epomena_bhmata(middle_joker,row,col,cards,trapcard,bless2)
            
            lovebirds(trapcard,joker,bless1,bless2,row,col,final_ace,cards)
        
            joker=somecountdown(trapcard,joker,bless1,bless2)
            
            gainingpower(trapcard,scoreboard,gyros)
            
            gyros=passinggyros(gyros,trapcard)
            
            gyros+=1
            
            print('Το σκορ είναι',scoreboard)
            
            print('Μπαίνουμε στον γύρο',gyros)
            
            print('Είναι η σειρά του παίκτη',players[gyros%len(players)])
            
            trapcard=[]
        
        wedidit(players,scoreboard)
    
    elif soft==2:
        noumera=['A','2','3','4','5','6','7','8','9','10']
        symbols=['\u2660','\u2663','\u2665','\u2666']
        row=[1,2,3,4]
        col=[1,2,3,4,5,6,7,8,9,10]
        
        scoreboard=startingpoint(players)
        
        gyros=0
        
        cards=basic_trap(noumera,symbols)
        
        random.shuffle(cards)
        
        trapcard=[]
        
        joker=joker_placer(row,col)
        
        last_joker=dolphin_joker(joker)
        
        repeat_res(sleeve_card,row,col,last_joker)
        
        print('Καλώς ήλθατε στο παιχνίδι')
        
        showman_joker(last_joker,col,row,cards)
        
        print()
        
        showman_joker(joker,col,row,cards)
        
        while joker!=last_joker:
        
            bless1=epilogh(row,col)
        
            bless1=isitwrong(bless1,joker,row,col)
        
            middle_joker=epomena_bhmata(joker,row,col,cards,trapcard,bless1)
            
            bless2=epilogh(row,col)
        
            bless2=isitwrong(bless2,middle_joker,row,col)    
        
            final_ace=epomena_bhmata(middle_joker,row,col,cards,trapcard,bless2)
            
            lovebirds(trapcard,joker,bless1,bless2,row,col,final_ace,cards)
        
            joker=somecountdown(trapcard,joker,bless1,bless2)
            
            gainingpower(trapcard,scoreboard,gyros)
            
            gyros=passinggyros(gyros,trapcard)
            
            gyros+=1
            
            print('Το σκορ είναι',scoreboard)
            
            print('Μπαίνουμε στον γύρο',gyros)
            
            print('Είναι η σειρά του παίκτη',players[gyros%len(players)])
            
            trapcard=[]
        
        wedidit(players,scoreboard)
    
    
    elif soft==3:
        noumera=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        symbols=['\u2660','\u2663','\u2665','\u2666']
        row=[1,2,3,4]
        col=[1,2,3,4,5,6,7,8,9,10,11,12,13]
        
        scoreboard=startingpoint(players)
        
        gyros=0
        
        cards=basic_trap(noumera,symbols)
        
        random.shuffle(cards)
        
        trapcard=[]
        
        joker=joker_placer(row,col)
        
        last_joker=dolphin_joker(joker)
        
        repeat_res(sleeve_card,row,col,last_joker)
        
        print('Καλώς ήλθατε στο παιχνίδι')
        
        showman_joker(last_joker,col,row,cards)
        
        print()
        
        showman_joker(joker,col,row,cards)
        
        while joker!=last_joker:
        
            bless1=epilogh(row,col)
        
            bless1=isitwrong(bless1,joker,row,col)
        
            middle_joker=epomena_bhmata(joker,row,col,cards,trapcard,bless1)  
            
            bless2=epilogh(row,col)
        
            bless2=isitwrong(bless2,middle_joker,row,col)    
        
            final_ace=epomena_bhmata(middle_joker,row,col,cards,trapcard,bless2)
            
            lovebirds(trapcard,joker,bless1,bless2,row,col,final_ace,cards)
        
            joker=somecountdown(trapcard,joker,bless1,bless2)
            
            gainingpower(trapcard,scoreboard,gyros)
            
            gyros=passinggyros(gyros,trapcard)
            
            gyros+=1
            
            print('Το σκορ είναι',scoreboard)
            
            print('Μπαίνουμε στον γύρο',gyros)
            
            print('Είναι η σειρά του παίκτη',players[gyros%len(players)])
            
            trapcard=[]
        
        wedidit(players,scoreboard)
        


