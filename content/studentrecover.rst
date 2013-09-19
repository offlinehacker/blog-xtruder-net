S pomočjo nizko cenovne delovne sile do poljubnega gesla študenta
#################################################################

:date: 2013-09-19 17:00
:tags: univerza, ljubljana, estudent, eštudent, id, ponastavitev, resetiranje,
       captcha
:category: hacks
:slug: do_poljubnega_gesla_studenta
:summary: Ali lahko s pomočjo nizko cenovne delovne sile pridemo do gesla
          poljubnega uporabnika, če sistem ni ustrezno zaščiten.

Opozorilo:

    V tem članku ni bil zlorabljen noben uporabniški račun, vsi testi so bili
    opravljeni na naših lastnih uporabniških računih.

Uvod
----

Luka Pušić je napisal `članek o ranljivosti e-identitete univerze v Ljubljani
<http://pusic.si/post/pomankljiva-zascita-e-identitete-univerze-v-ljubljani/>`_
in tudi demonstriral, kako lahko
kateremukoli študentu brez večjih težav ponastaviti geslo, ki se uporablja na več
spletnih portalih za študente, ki so kritičnega pomena za njihov študij.
Za uspešno uporabo njegove metode si potreboval ime študenta, priimek,
rojstni datum, vpisno številko in ime fakultete - podatke, ki si jih zlahka pridobil.
Edina ovira je bilo uporabniško ime, ki ga je bilo treba ugotoviti z avtomatiziranim
ugibanjem (do 10.000 poizkusov). Nekaj časa po objavi članka so na Univerzi formo
za ponastavitev gesla zaščitili s t.i. `CAPTCHA <http://en.wikipedia.org/wiki/CAPTCHA>`_
sistemom, ki preveri, ali so poizkusi človeški, ali pa nek program.

Ali je taka zaščita res dovolj dobra? Kaj če je nekdo pripravljen vložiti še več
truda in celo nekaj denarja, da nekomu ponastavi geslo?

Demonstracija
-------------

Edina večja ovira, ki nam v tem trenutku preprečuje ponastavitev gesla, je CAPTCHA.
Ampak tudi taka zaščita se da zaobiti. V Aziji obstaja veliko podjetij, ki za smešne
cene ponujajo reševanje CAPTCHA besed. Za manj kot 1$ za 1000 poizvedb.
Dober članek o takih storitvah najdete na:
http://www.troyhunt.com/2012/01/breaking-captcha-with-automated-humans.html

Za uspešno izveden napad bomo potrebovali približno 10$ (10.000x Captcha) in `naš
namenski program <https://github.com/offlinehacker/studentrecover>`_.
Le ta naloži ustrezne podatke iz https://id.uni-lj.si/index.php?action=resetpass
in potem poizkuša vsa mogoča uporabniška imena, dokler geslo ni zamenjano in
uporabniško ime ugotovljeno. Tako preprosto!

.. image:: |filename|/images/iduni_crack_demo.png

**Kot vidimo smo imeli srečo in že po približno 1500 uspešnih poizkusih smo uspešno
pridobili uporabniško ime, še edini manjkajoči podatek, ki je potreben za ponastavitev gesla.**

.. image:: |filename|/images/avantgate_panel.png

**Storitev, ki smo jo uporabili za razbijanje CAPTCHA omogoča interaktivni pregled
in tako lažji razvoj aplikacije**

Izkaže se, da so nekatere CAPTCHA tako zakomplicirane, da je stopnja uspeha
le okoli 50%, vendar če upoštevamo, da geslo v povprečju ugotovimo že mnogo prej,
potrebna cena za poskušanje v povprečju ostane ista.
Če bi vedeli kako so uporabniška imena generirana, bi lahko bila naša napoved mnogo
boljša, morda celo perfektna.

Ugotovitev
----------

Kot lahko vidimo, zaščita s CAPTCHA ni vedno primerna. Kot boljšo alternativo
predlagamo resetiranje gesla preko elektronske pošte.
