---
title: "Tekstitöötluse koolitus. Töö terminaliga, käsurida ja Unixi käsud"
author: "Kristel Uiboaed, Liina Lindström, Kadri Muischnek"
date: "25. jaanuar 2017"
output:
  html_document: default
  word_document: default
---

## Sisukord
1. [Sissejuhatus](#intro)
2. [Keskkond ja seadistused](#keskkond)
3. [Töö lihtsustamiseks](#shortcutid)
4. [Töö kataloogidega](#kataloogid)
5. [Töö failidega](#failid)
6. [Faili kasutusõigused](#oigused)
7. [Tekstitöötlus](#greptrsed)
    * [`grep`](#grep)
    * [`tr`](#tr)
    * [`sed`](#sed)
    * [`cut`](#cut)
8. [Sorteerimine](#sort)
9. [Erisümbolid](#erisymbolid)
10. [Grupeerimine](#grupid)
11. [Näiteid](#nt)
12. [Praktikum](#praktikum)
    * [Sagedusloendid](#sagedusloendid)
    * [Kollokatsioonid](#kollok)
13. [Lisamaterjale](#kirjandust)

## Sissejuhatus <a name="intro"></a>


Praktikumides kasutame [Bitvise’i](https://www.bitvise.com/download-area), aga TÜ arvutiklasside arvutites on olemas tavaliselt ka näiteks [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/) ning kasutada võib mis tahes endale meelepärast rakendust.
Suvalisest arvutist saab sisse logida ssh-terminaliakna abil ülikooli Linuxi-serverisse `adalberg.ut.ee` (täpitähtede kuvamiseks vt [siia](http://anti.teamidiot.de/nei/2007/02/irssi_putty_screen_unicode_utf/) ja ülikooli serverisse logimise kohta [siia](https://wiki.ut.ee/pages/viewpage.action?pageId=17105728)).

Linuxi graafilise keskkonna kasutamiseks (GNOME, KDE) installeerida arvutisse [NX Client](https://www.nomachine.com/download).

Kelle arvutis on Linuxi/Unixi opsüsteem,  ei vaja mingit lisvahendit. Windowsi kasutaja vajab praktikumi kaastagemiseks Bitvise'i, Putty't või mõnda muud ssh klienti.


Praktikumi materjalid on GitHubis 25. jaanuari kaustas.
...

## Keskkond ja seadistused <a name="keskkond"></a>

Kontrolli, millist shelli kasutad (oleneb ülikooli kasutajakonto seadistustest, mida ise püsivalt muuta ei saa).

``` bash
which $shell
which $SHELL
echo $0
```

Vaata olemasolevaid shelle.

``` bash
cat /etc/shells
```

Kui sinu masin kasutab midagi muud peale tcsh, siis saad seda ajutiselt muuta nii (iga kord peale sisse logimist):

``` bash
exec /bin/tcsh
```

Kõige lihtsam on aga kirjutada oma skriptid faili ja esimesel real defineerida, millist shelli peaks käivitatav skript kasutama ([mõned näited](https://github.com/kristel-/Corpus-Linguistics/tree/master/Unix)).

``` bash
#! /bin/bash
#! /bin/tcsh
#! /bin/sh
jne
```

`tcsh` kasutamine ei ole kohustuslik, aga praktikumides esitatud näited on `tcsh`-põhised.

Linke, millest võib seadistamisel abi olla:

[http://www.thegeekstuff.com/2009/10/change-login-shell-from-bash-to-sh-csh-ksh-tcsh/](http://www.thegeekstuff.com/2009/10/change-login-shell-from-bash-to-sh-csh-ksh-tcsh/)

[http://stackoverflow.com/questions/4132661/run-csh-scripts-from-bash-change-shell-temporary-via-command](http://stackoverflow.com/questions/4132661/run-csh-scripts-from-bash-change-shell-temporary-via-command)

[http://unix.stackexchange.com/questions/20629/how-to-change-from-csh-to-bash-as-default-shell](http://unix.stackexchange.com/questions/20629/how-to-change-from-csh-to-bash-as-default-shell)

Mõned `bashi` ja `tcsh` [erinevused](http://www.thegeekstuff.com/2009/10/change-login-shell-from-bash-to-sh-csh-ksh-tcsh/).

Täpitähtede seadistamine käsurealt

``` bash
setenv LANG et_EE.UTF-8

# või 

export LANG=et_EE.UTF-8


# Kui tekib probleeme, siis kasuta pigem

setenv LANG en_US.UTF-8
export LANG=en_US.UTF-8


# Kehtib ainult selles aknas kuni akna sulgemiseni.
# Parem seadistada kodeering kohe sisselogimisel.
```

Käsud töötavad põhimõttel:
`käsk  [-lipuke/täpsustav kriteerium] [argument]`

Rohkem infot iga käsu kohta:

``` bash
man käsuNimi
käsuNimi --h
```

## Töö lihtsustamiseks <a name="shortcutid"></a>
**Nooleklahv üles**: näita eelmist käsku, mille sisestasid.

**Ctrl + u**: kustuta käsurida

**Ctrl + a**: mine käsurea algusesse

**Ctrl + c**: katkesta protsess

**Ctrl + I** *või* **clear**: puhasta aken

**TAB**: lihtsustab trükkimist

**q**: välju teksti lehitsemisest (*quit*)

Masinast väljumine: `exit`.

## Töö kataloogidega/kaustadega <a name="kataloogid"></a>

Töökataloogi vahetamine (`cd` - ***c**hange **d**irectory*). Näiteks:

``` bash
cd kataloog1/kataloog2/…/soovitudKataloog
# tagasi kodukataloogi
cd
# üks samm töökataloogist tagasi
cd ..
```

Mis on töökataloogis (`ls` - *list*)?

``` bash
ls
ls kataloogiNimi
```

Detailsemalt kataloogis olevate failide ja alamkataloogide kohta:
``` bash
ls -l
ls -l kataloogiNimi
```

Näita ka n-ö peidetud faile:
``` bash
ls -a
```

Kataloogi sisu rekursiivselt:
``` bash
ls -R
```

Kus ma olen?
``` bash
pwd
```

Kes ma olen?
``` bash
who
whoami
```

Kuhu ma kuulun?
``` bash
groups kasutajaNimi
```

Kataloogide ja failide sisu sirvimine kitsendatult:

``` bash
less
more
head
tail
head -25
tail -25
```

Loo uus kataloog (`mkdir` - *make directory*)
``` bash
mkdir KataloogiNimi
cd KataloogiNimi
cd
```

Kustuta kataloog (`rmdir` - *remove directory*)
``` bash
rmdir kustutatavaKataloogiNimi
```

Kustuta fail (`rm` - *remove*)
``` bash
rm kustutatavaFailiNimi
```

Kustuta kataloog ja kõik tema alamkataloogid koos oma sisuga, r-rekursiivselt. **NB!** Selle käsu kasutamisel ole ettevaatlik ja veendu, et soovid tõepoolest kõike kustutada, sest sel viisil kustutatud pole enam võimalik taastada.

``` bash
rm -r kustutatavaKataloogiNimi
```

Küsi faili kustutamisel nõusolekut:
``` bash
rm -i
```

## Töö failidega <a name="failid"></a>

Mis on failis? Faili sisu vaatamine (`cat` - *concatenate, catenate*):

``` bash
cat failiNimi
cat failiNimi | less
cat failiNimi | head
cat failiNimi | tail
cat failiNimi | less
cat failiNimi | head -10
cat failiNimi | tail -3
```

Faili sisu ülevaade. Kui palju on failis ridu, sõnu, sümboleid (`wc` - *word count*). **NB!** sõna on see, mis on eraldatud tühikute või muude "nähtamatute sümbolitega", st et tegemist ei ole ilmtingimata lingvistilise sõnaga.

``` bash
cat failiNimi | wc
```

Kopeeri faile (`cp` - *copy*):

``` bash
cp kopeeritafaFailiNimiVõiTeekond kuhuKopeeridaTeekond
```

Liiguta/teisalda faile, nimeta fail ümber (`mv` - *move*):

``` bash
mv vanaFailiNimi uueFailiNimi
mv vanaFailiNimi uueFailiNimiKoosTeekonnaga
```

Vaata kõiki faile, mis lõpevad, sisaldavad, algavad etteantud ühisosaga failinimes.

``` bash
ls | ühisosa*
ls | *ühisosa*
ls | *ühisosa
```

## Faili õiguste muutmine <a name="oigused"></a>

`chmod` - *change mode*

``` bash
chmod
```

chmod
`u` = **u**ser, `g` = **g**roup, `o` = **o**thers, `a` = **a**ll

\+	anna õigused

\-	võta õigused ära

**r**  lugemisõigused (*read*)

**w** kirjutamisõigused (*write*)

**x** käivitamisõigused (*execute*)

Näiteks:

``` bash
chmod o+x failiNimi
chmod u-w failiNimi
chmod ugo-rw failiNimi
jne
```

Väljundi suunamine uude faili (või n-ö salvestamine).

\> ja \>\>

``` bash
# uus fail kirjutatakse ümber/üle
cat failiNimi > uueFailiNimi
# faili sisu lisatakse olemasoleva faili lõppu
cat failiNimi >> väljundFailiNimi
```

## Failist otsimine, asendamine, kustutamine. `grep, tr, sed` <a name="greptrsed"></a>

### `grep`  <a name="grep"></a>

`grep` otsib ridu etteantud mustri järgi. **NB!** rida, mida näed ekraanil ei ole ilmtingimata see rida, mida näed ekraanil. Arvuti jaoks on rida see, mis lõpeb reavahetuse sümboliga, "enteriga" (`\n` või `\012`). Näiteks:

``` bash
grep ’maja’
grep ’#’
```

Otsingule on võimalik lisada eritingimusi.  
**-i**  ei tee vahet suurtel ja väikestel tähtedel  
**-v** 	otsib ridu, mis ei sisalda mingit mustrit / viskab välja read, mis sisaldavad etteantud mustrit  
**-n**	näitab väljundis lisaks rea numbrit, kus otsitav märk või märgijada leiti  
**-c**	väljastab otsingule vastavate ridade arvu  
**-2**	lisab konteksti otsingule vastava rea ümber kaks rida ette ja taha  
  
Võib kasutada mitut lipukeste korraga, näiteks

``` bash
grep –vc ’maja’
```
 	
Vaata ka **`egrep`** ja **`fgrep`**.

### `tr`  <a name="tr"></a>
`tr` (***tr**anslate*)

Näiteks muuda kõik suured tähed väikesteks.

Asenda numbrid suure A-tähega.

Asenda trellid @-märgiga.

Asenda reavahetused tühikuga.

``` bash
tr '[:upper:]' '[:lower:]'
tr '[A-Z]' [a-z]'

tr '[0-9]' 'A'
tr '#' '@'
tr '\012' ' '
```

Sümbolite kustutamine `-d` (***d**elete*). Mõned näited:
``` bash
tr -d '\012'
tr -d '@'
tr -d '[0-9]'
```

Korduvate sümbolite kustutamine `-s`. Näiteks kustuta kõik korduvad *a*-tähed (aa, aaa, aaaa … > a)
``` bash
tr -s 'a'
```

**NB!** `tr` "tõlgib" ühe baidi teiseks baidiks, aga utf8-s on mõned sümbolid esitatud mitme baidi abil, seega `tr` ja utf-8 kodeering ei ole päris hästi kooskõlas. Ühesõnaga: võib kasutada nt tühiku, reavahetuse asendamiseks, aga muul puhul olla ettevaatlik ja muude sümbolite asendamiseks kasutada pigem  käsku `sed 'y/asendatav/asendus/'`

### `sed`. Pikemate märgijadade asendamine ja kustutamine  <a name="sed"></a>

Pikemate märgijadade asendamiseks ja kustutamiseks (asendus mitte millegagi).

``` bash
sed 's/asendatav/asendus/'
sed 's/asendatav/asendus/g'
```
Esimene variant asendab ainult iga rea esimese tabamuse. Teine variant (`g` = ***g**lobal*) asendab kõik real leitud tabamused.

``` bash
sed '3 s/[0-9]*//'

sed '1,100 s/asendatav/asendus/'

sed '/start/,/stop/ s/#.*//'

sed '/start/ s/#.*//'

sed '/muster/d'

sed 'y/ÄÖÜ/äöü/'

sed 's/[a-z]*/(&)/'

sed 's/[a-z]*/(&)/g'

sed 's/[a-z]/ &/g'


# Proovi

echo "tere tere hommikust" | sed 's/tere/head/'
echo "tere tere hommikust" | sed 's/tere/head/g'
echo "tere hommikust" | sed 's/tere//'
echo "tere hommikust" | sed 's/ /\n/'
echo "tere hommikust" | sed 's/\([^ ]*\) \([^ ]*\)/\2 \1/'
echo "tere hommikust" | sed 's/^\([^ ]*\) .*$/\1/'
echo "ÕUEAIAÄÄR" | sed 'y/Õ/õ/'
echo "ÕUEAIAÄÄR" | sed 'y/ÕÄ/õä/'
echo "ÕUEAIAÄÄR" | sed 'y/ÕÄ/äõ/'
echo "ÕUEAIAÄÄR" | tr 'ÕÄ' 'äõ'
```

### `cut`  <a name="cut"></a>

Töötleb teksti kui tabelit, selleks peab olema tekstifailis veergudel üks kindel eraldaja.
`-d` selle käsu puhul märgib `d` (***d**elimiter*) välja eraldajat.
`-f` (***f**ield*) anna ette, mitmes väli "ära lõigata".

``` bash
# lõika failist välja kõik, mis algab kolmandast väljast (jäta alles ainult kaks esimest välja), välju eraldab %-märk
cat test.txt | cut -d % -f 1-2

# lõika failist välja kõik, mis algab kolmandast väljast (jäta alles ainult kaks esimest välja), välju eraldab tühik
cat test.txt | cut -d " " -f 1-2

# lõika failist välja osa, mis algab teisest väljast (eemalda esimene väli), välju eraldab tühik
cut -d " " -f 2-
```

### Sorteerimine  <a name="sort"></a>

Käsk `sort` järjestab read, vaikimisi tähestikulises järjekorras.

`sort –n` sorteerib ridu kui arve (***n**umeric*).

`sort –r` sorteerib vastupidises järjekorras (***r**everse*).

`uniq` jätab identsetest ridadest alles vaid ühe, fail peab enne olema sorteeritud.

`uniq –c` loeb identsed read ka kokku (***c**ount*)


## Erisümboleid <a name="erisymbolid"></a>

`\t`:	tabulaator

`\011`:	tabulaator

`\n`:	Linuxi reavahetus

`\012`:	Linuxi reavahetus

`\015`:	Windowsi reavahetus

## Grupeerimine  `\(\)` <a name="grupid"></a>

`sed`-ga on võimalik kasutada ka grupeerimist. Selleks kasutatakse sulge, mille ette on lisatud tagurpidi kaldkriipsud. Gruppidele on võimalik tagasi viidata (töötab samamoodi nagu kasutajaliidestes).

``` bash
# lisa kahe järjestikuse a-tähe ette ja taha alakriipsud
cat fail | sed 's/\(aa\)/_\1_/g'

# Ühe grupi puhul on samas funktsioonis võimalik aksutada ka &-märki
# sisuliselt sama, mis eelmine
cat fail | sed 's/aa/_&_/g'
```


## Näiteid  <a name="nt"></a>

Käske võib omavahel kombineerida, eraldades need |-ga.

Võta failist välja read, kus esineb sõna *maja*, ja suuna tulemus uude faili.

``` bash
cat algfail | grep 'maja' > väljundfail


# Võta failist välja read, kus esineb sõna maja.
# Asenda seejärel maja sõnaga hoone.
# Muuda tekst suurtäheliseks.
# Lisa tulemus juba olemasolevasse faili.

cat sisendfail | grep 'maja' | sed 's/maja/hoone/' | tr '[:lower:]' '[:upper:]' >> väljund

```

## Praktikum <a name="praktikum"></a>

Teeme praktikumi materjalide hoidmiseks oma kodukataloogi uue kausta `tekstiPraktikum`, milles hoiame kõik selle praktikumiga seotud faile. Peale uue kausta tekitamist, liigume sellesse käsuga `cd` ja kontrollime, kus me oma kataloogipuus paikneme `(pwd)` ja mis on töökataloogi sees `(ls)`.


``` bash
mkdir tekstiPraktikum
cd tekstiPraktikum
pwd
ls
```

Seejärel tõstame praktikumi failid oma lokaalsest arvutist ülikooli serverisse oma kodukataloogi, et igaüks saaks neid töödelda oma kodukataloogis ja nii nagu ise soovib. Teekonna oma kodukataloogi saad vaadata käsuga `pwd`, mida juba eelnevalt proovisime.

``` bash
cp source dest
```

Nüüd saame jälle `ls` käsuga vaadata, mis kodukataloogis muutunud on ja kas kõik failid on kopeeritud. Edasi töötame kahe portsu failidega. Ühed on failid n-ö normaalsel tekstikujul ja teine ports faile, on lemmatiseeritud ehk samades algfailides on kõik sõnad viidud tema algvormi/sõnaraamatu vormi kujule. Alustuseks töötame n-ö normaalsete tekstifailidega.


### Sagedusloendid <a name="sagedusloendid"></a>

Kui võtame ette mis tahes tekstifaili, siis selle töötlemiseks tuleb teha rida otsuseid: kas punktuatsioon on meie jaoks oluline või oleks see mõistlik eemaldada. Arvuti jaoks on erinevad sõnad `harjutan,` ja `harjutan` nagu on ka erinevad `harjutan` ja `Harjutan`, niisiis tuleks veel sõnad muuta ka väiketäheliseks, kui soovime, et sõnavormid `harjutan` ja `Harjutan` loetaks samaks sõnavormiks, mitte erinevateks. Siin tuleb meeles pidada, et sellisel juhul muutuvad väiketäheliseks ka näiteks kõik pärisnimed. Selle vältimiseks ongi meil vaja korpuse märgendust, millest oli juttu eelmisel korral. Praegu aga jätkame märgendamata tekstidega. Kuna arvuti töötab ka ridadega, siis on meil lõpuks kokkulugemiseks ka kogu faili sõnad "tõsta eraldi ridadele" ning sellisel kujul fail sorteerida ning unikaalsed read kokku lugeda. Lõpuks suuname väljundi eraldi faili.

``` bash
cat *soned* | tr '[:upper:]' '[:lower:]' | sed 'y/ÕÄÖÜ/õäöü/' | tr -d '[\.\?!,\":;\)\(]' | tr ' ' '\n' | grep -v '^$' | sort |  uniq -c | sort -nr | sed 's/ *\([0-9]*\) \(.*\)/\2;\1/' > sonavormide-sagedusloend.txt
```

``` bash
cat *.txt | tr -d '[\.\?!,\":;\)\(]' | tr ' ' '\n' | grep -v '^$' | sort |  uniq -c | sort -nr | sed 's/ *\([0-9]*\) \(.*\)/\2;\1/' > algvormide-sagedusloend.txt
```

### Kolllokatsioonid <a name="kollok"></a>

Järgnevalt esitame ühe väga lihtsa võimaluse kõrvuti asetsevate sõnade (nn kollokatsioonide) sagedusloendi tegemiseks. Praegu vaatame ainult kahesõnalisi kombinatsioone vasakult paremale. Eesti keele sõnajärg on varieeruv ja kokku kuuluvad sõnad ei paikne lauses ühesuunaliselt ja üksteisele vahetult järgnevana.

Näiteks.

*Nimelt **näeb** sel nädalal haridus- ja teadusministeeriumist valitsusse heakskiitmiseks saadetud gümnaasiumi riikliku õppekava määrus **ette**, et tuleb kolm riigieksamit, mis kõik on gümnaasiumiõpilasele kooli lõpetamiseks kohustuslikud.*

*Kes seda muidugi **ette nägi**, et veidi rohkem kui aasta ja meie mõtlemine hakkas minema hoopis teises suunas.*


``` bash
cat *lemma* | tr ' ' '\n' > sonaReal.txt
cat sonaReal.txt | tail -n +2 > sonaReal-1.txt
paste sonaReal.txt sonaReal-1.txt | grep -v "^\011" > paarid.txt
cat paarid.txt | grep -v "[\.,:;\?\!]" | sort | uniq -c | sort -nr > sorteeritudBigrammid.txt
```

## Lisamaterjale <a name="kirjandust"></a>
* [Regulaaravaldistest](http://korpuslingvistika.ut.ee/loengud/4-loeng/)
* [Bash Quick Reference](http://korpuslingvistika.ut.ee/wp-content/uploads/2016/09/Bash-Quick-Reference.pdf)
* Liina Lindströmi materjalid Unixi ja sagedusloendite kohta:[1](http://korpuslingvistika.ut.ee/wp-content/uploads/2016/09/UNIX_1_18_11_2013.pdf), [2](http://korpuslingvistika.ut.ee/wp-content/uploads/2016/09/unix2_parandatud_25_11_2013.pdf), [3](http://korpuslingvistika.ut.ee/wp-content/uploads/2016/09/Unix3.pdf).
* [Tere, terminaliaken!](https://drive.google.com/file/d/0BzzoDgAQIa9nY0JINXhlM0xuV0U/view)
* [Unix for corpus users: a beginner’s guide](http://www.port.ac.uk/media/Media,168754,en.pdf)
* [Unix for poets](https://web.stanford.edu/class/cs124/kwc-unix-for-poets.pdf)
* [UNIX Tutorial for Beginners](http://www.ee.surrey.ac.uk/Teaching/Unix/index.html)
