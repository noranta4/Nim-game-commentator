from graphics import *
from random import *
# -*- coding: utf-42 -*-

def main():
    def inside(punto, figura):
        if punto.getX() > figura.getP1().getX() and punto.getY() > figura.getP1().getY() and punto.getX() < figura.getP2().getX() and punto.getY() < figura.getP2().getY():
            return True
        else:
            return False
    def count(linea):
        gruppi=[0,0,0,0,0]
        counter=0
        for j in range(5):
            for i in range(5-j):
                counter+=linea[j][i]
                if linea[j][i]==0 and counter!=0:
                    gruppi[counter-1]+=1
                    counter=0
                elif linea[j][i]==1 and 4-j==i:
                    gruppi[counter-1]+=1
                    counter=0
            counter=0
        return gruppi
    def commento(t, turno, linea):
        gruppi=count(linea)
        single=gruppi[0]
        gruppi[0]=0
        vinc1=[[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
        vinc2=[[0,1,0,1,0],[0,1,0,0,1],[0,3,0,0,0],[0,2,1,0,0],[0,2,0,1,0],[0,2,0,0,1]]
        vinc3=[[0,0,1,1,0],[0,0,1,0,1],[0,1,2,0,0],[0,1,1,1,0],[0,1,1,0,1],[0,3,0,1,0],[0,3,0,0,1]]
        vinc4=[[0,0,3,0,0]]
        vincd1=[[0,1,1,0,0],[0,3,1,0,0]]
        vincd2=[[0,0,0,2,0]]
        perdd=[[0,0,2,0,0],[0,4,0,0,0],[0,2,2,0,0],[0,2,0,0,0]]
        #vtext1r=vtext2r=vtext3r=vtext4r=['vince rosso']
        #vtext1b=vtext2b=vtext3b=vtext4b=['vince blu']
        vtext1r=['Io sinceramente non so perché state giocando ancora, ha vinto Rosso','Blu pensaci bene, hai una tattica vincente... ahah scherzo','Rosso se ci pensi più di 3 secondi ti dichiaro sconfitto!','Ecco che Rosso si appresta a chiudere la partita'] 
        vtext1b=['Io sinceramente non so perché state giocando ancora, ha vinto Blu','Rosso pensaci bene, hai una tattica vincente... ahah scherzo','Blu se ci pensi più di 3 secondi ti dichiaro sconfitto!','Ecco che Blu si appresta a chiudere la partita']
        vtext2r=['Rosso hai vinto, vedi di non deludermi adesso',"Ed è proprio in questi casi che Rosso manda tutto all'aria",'Rosso hai fatto una grande partita, non mi sbagliare adesso',"Blu lo so che stai sperando intensamente in un errore dell'avversario"]
        vtext2b=['Blu hai vinto, vedi di non deludermi adesso',"Ed è proprio in questi casi che Blu manda tutto all'aria",'Blu hai fatto una grande partita, non mi sbagliare adesso',"Rosso lo so che stai sperando intensamente in un errore dell'avversario"]
        vtext3r=['Non è banale, ma Rosso può portarla a casa','Rosso fermati e concentrati, da ora se non sbagli la porti a casa',"Fin'ora la partita era in bilico, adesso invece è in vantaggio Rosso","Errore di Blu! Rosso puoi portarla a casa","Blu ma che mi combini!"]
        vtext3b=['Non è banale, ma Blu può portarla a casa','Blu fermati e concentrati, da ora se non sbagli la porti a casa',"Fin'ora la partita era in bilico, adesso invece è in vantaggio Blu","Errore di Rosso! Blu puoi portarla a casa","Rosso ma che mi combini!"]
        vtext4r=["La situazione è delicata ma se Rosso gioca bene la partita è sua","Le sorti della partita potrebbero cambiare da un momento all'altro, ma ora è di Rosso","Sembra pari, ma ora Rosso se non sbaglia vince","Rosso fermati e respira con calma, hai una strategia vincente"]
        vtext4b=["La situazione è delicata ma se Blu gioca bene la partita è sua","Le sorti della partita potrebbero cambiare da un momento all'altro, ma ora è di Blu","Sembra pari, ma ora Blu se non sbaglia vince","Blu fermati e respira con calma, hai una strategia vincente"]
        itext=['A dire il vero gi� si sa chi � in vantaggio, ma sto zitto per non mettere ansie',"Non saprei davvero dire chi vince",'Rosso lo do a 2,10 e Blu a 1,90... ma giusto così per simpatia','Vabbè mi vado a fare un sonno','Richiamatemi quando si fa più interessante','Blu mi sta più simpatico, tifo per lui','Paura di sbagliare eh??? Per ora non mi sbilancio','Non molto interessante finora questa partita']
        if (gruppi in vinc1):
            t.setText(choice(vtext1r))
            if turno%2==1:
                t.setText(choice(vtext1b))
        elif (gruppi in vinc2):
            t.setText(choice(vtext2r))
            if turno%2==1:
                t.setText(choice(vtext1b))
        elif (gruppi in (vinc3+vinc4)):
            t.setText(choice(vtext3r))
            if turno%2==1:
                t.setText(choice(vtext3b))
        elif (gruppi in vincd1) and (((single%2==0) and turno%2==0) or ((single%2==1) and turno%2==1)):
            t.setText(choice(vtext4r))
        elif(gruppi in vincd1) and (((single%2==1) and turno%2==0) or ((single%2==0) and turno%2==1)):
            t.setText(choice(vtext4b))
        elif ((gruppi in vincd2) and (((single%2==0) and turno%2==0) or ((single%2==1) and turno%2==1)) or ((gruppi in perdd) and (((single%2==1) and turno%2==0) or ((single%2==0) and turno%2==1)))):
            t.setText(choice(vtext4r))
        elif ((gruppi in vincd2) and (((single%2==1) and turno%2==0) or ((single%2==0) and turno%2==1)) or ((gruppi in perdd) and (((single%2==0) and turno%2==0) or ((single%2==1) and turno%2==1)))):
            t.setText(choice(vtext4b))
        elif single!=0 and gruppi==[0,0,0,0,0]:
            t.setText('Ooooooooooooooooooooooooooooooooooooh...')
        else:
            t.setText(choice(itext))


    #settaggio finestra
    win = GraphWin("Nim Bot", 700, 800)
    win.setBackground('white')
    win.setCoords(0.0, 0.0, 10.0, 6.0)



    #selezione modalita
    play=1
    while play==1:
        play=0
        nocomm=Rectangle(Point(1,0.25),Point(4,0.75))
        comments=Rectangle(Point(6,0.25),Point(9,0.75))
        nocomm.setFill('grey')
        comments.setFill('grey')
        nocomm.draw(win)
        comments.draw(win)
        title=Text(Point(5,4),'N I M\n\nBot')
        title.setSize(36)
        title.setFace('courier')
        title.setStyle('bold')
        title.setOutline('blue')
        title.draw(win)
        quote=Text(Point(5,2.5),'"Vince la partita chi fa il penultimo errore"')
        quote1=Text(Point(5,2),"Savelij Grigor'evic' Tartakover, scacchista polacco (ma vale anche per Nim!)")
        quote.setStyle('italic')
        quote.draw(win)
        quote1.draw(win)
        t1=Text(nocomm.getCenter(), 'Sto zitto e vi lascio\ngiocare in pace')
        t2=Text(comments.getCenter(), 'Faccio qualche commento,\nniente di personale')
        t1.draw(win)
        t2.draw(win)
        sel=Point(0,0)
        while (inside(sel, nocomm) or inside(sel, comments)) == False:
            sel=win.getMouse()
            if inside(sel, nocomm):
                mode='nocomm'
                nocomm.undraw()
                comments.undraw()
                t1.undraw()
                t2.undraw()
            elif inside(sel, comments):
                mode='comments'
                nocomm.undraw()
                comments.undraw()
                t1.undraw()
                t2.undraw()
        pt=Point(5,0.5)
        t=Text(pt,'Bene, allora vi auguro una buona partita!\nComincia il rosso, clic per continuare')
        t.draw(win)
        win.getMouse()
        title.undraw()
        quote.undraw()
        quote1.undraw()
        t.setText('')
        if mode=='nocomm':
            t.setOutline('white')

        #Disegno griglia e inizializzazione
        linea=[[1],[1],[1],[1],[1]]
        griglia=[]
        for j in range (5):
            for i in range(5-j):
                l=Line(Point(2*i+j+1,j+1.25),Point(2*i+j+1,j+1.75))
                l.setWidth(3)
                l.draw(win)
            linea[4-j]*=(j+1)
            griglia+=[Rectangle(Point(j,j+1),Point(10-j,j+2))]

        turn=0
        newgame=Rectangle(Point(0.1,5.5),Point(3.1,5.9))
        newgame.setFill('grey')
        tnewgame=Text(Point(1.6,5.7),'Nuova partita')
        newgame.draw(win)
        tnewgame.draw(win)
        #elaborazione input
        while max(linea)!=[0,0,0,0,0]:
            turn+=1
            p1=win.getMouse()
            if inside(p1,newgame):
                linea=[[0,0,0,0,0]]
                play=1
                white=Rectangle(Point(0,0),Point(10,6))
                white.setFill('white')
                white.draw(win)
                nextp2=Text(Point(5,3),'doppio clic per continuare')
                nextp2.draw(win)
            p2=win.getMouse()
            if linea==[[0,0,0,0,0]]:
                nextp2.undraw()
            if (inside(p1,griglia[0]) or inside(p1,griglia[1]) or inside(p1,griglia[2]) or inside(p1,griglia[3]) or inside(p1,griglia[4])) and (inside(p2,griglia[0]) or inside(p2,griglia[1]) or inside(p2,griglia[2]) or inside(p2,griglia[3]) or inside(p2,griglia[4])):
                tratto=Line(p1,p2)
                tratto.setWidth(2)
                if turn%2==1:
                    tratto.setOutline('red')
                else:
                    tratto.setOutline('blue')
                tratto.draw(win)
                
                if int(p1.getY())%2==1 and int(p2.getY())==int(p1.getY()):
                    crdsx=min((int(p1.getX())-(int(p1.getY())-1))/2,(int(p2.getX())-(int(p1.getY())-1))/2)
                    crddx=max((int(p1.getX())-(int(p1.getY())-1))/2,(int(p2.getX())-(int(p1.getY())-1))/2)+1
                    for i in range(crdsx,crddx):
                        linea[int(p1.getY())-1][i]=0

                elif int(p1.getY())%2==0 and int(p2.getY())==int(p1.getY()):
                    crdsx=min((int(round(p1.getX()))-(int(p1.getY())-1))/2,(int(round(p2.getX()))-(int(p1.getY())-1))/2)
                    crddx=max((int(round(p1.getX()))-(int(p1.getY())-1))/2,(int(round(p2.getX()))-(int(p1.getY())-1))/2)+1
                    for i in range(crdsx,crddx):
                        linea[int(p1.getY())-1][i]=0
                    
                else:
                    t.setOutline('black')
                    t.setText('ti sei sbagliato, clicca per continuare')
                    win.getMouse()
                    if mode=='nocomm':
                        t.setOutline('white')
                    tratto.undraw()
                    turn-=1
                commento(t, turn, linea)        
            else:
                t.setOutline('black')
                t.setText('ti sei sbagliato, clicca per continuare')
                win.getMouse()
                if mode=='nocomm':
                    t.setOutline('white')
                turn-=1
        t.setText('Ha vinto Rosso!')
        t.setSize(20)
        if turn%2==1:
            t.setText('Ha vinto Blu!')
    newgame.undraw()
    tnewgame.undraw()
    esc=Text(Point(5,0.2), 'Clicca per uscire')
    esc.setSize(10)
    esc.draw(win)
    win.getMouse()
    win.close()
main()

