# itmp-repulesi-statisztika-4-1

Képek, ikonok átszínezése, átméretezése: Paint 3D programban
egyszerű kezelni
a Windows részeként telepítődik, frissítődik
egy alkalmazásban meg lehet csinálni az átszínezést, és a méretezést
könnyen menthető
Logók kigyűjtése: bármelyik internet böngésző gyors, pontos találatot ad.
a logók legtöbb helyen külön képként letölthetők
Logók méretezése: Paint 3D programmal

### Backed feladatok

**1.	A kapott csv állomány feldolgozása**

A flight.csv 22 779 sornyi adatot tartalmaz. Minden sorban 22 adat vesszővel elválasztva. Ezt a karaktert szeparátorként használva fel kellett darabolni a sorokat, hogy egyedi adatokat kapjunk. 
Ezt megnehezítő tényezők:
-	az repülőtér rövidítése és városa egy idézőjelben szerepelt a repülőtér nevével.
-	néhány sorban hiányzó adatok
-	egy-egy sorban még néhány szeparátor is hiányzott


**2.	Adatfeldolgozás módjának kiválasztása**

Mivel weben megjelenő alkalmazásról van szó, legcélszerűbbnek a MySQL + PHP megoldás tűnt. Ezek segítségével a feladatban kért eredmények egyetlen jól megírt SQL paranccsal hatékonyan és gyorsan megjelenthetők úgy, hogy az SQL lekérdezés eredménytáblája egy PHP mátrixba kerül. Ennek tartalma alapján pedig legeneráljuk a szükséges HTML kódot.

**3.	MySQL adatbázis létrehozása**

A feladat kérte több eredmény megjelenítését ezen adatok alapján. Célszerű volt ezért adatbázisba tenni azokat. Az adatbázisnak viszont 3. normálformában kell lennie. Ezért a redundáns értékeket tartalmazó oszlopokból külön táblák készültek. 

![adatbázis](images/database-view.png "adatbázis")


**4.	Adatbáziskapcsolat kialakítása**

A kapcsolat felállítása egy PHP osztály segítségével törtét a PDO osztály kiterjsztésével.
Neve: Database.php, tartalma megtekinthető a server mappában:


**5.	Feladatmegoldások**

Megoldandó feladatok:
-	minden légitarsaság felsorolása
-	egy kiválasztott légitársaság különféle adatainak megjelenítése
-	top 3 reptér fogadott járatok száma alapján
-	top 3 légitársaság késés alapján
Minden feladatra és az azokon belüli részeredmények lekérdezésére külön függvény készült. Ezek egy PHP osztályban kerültek kidolgozásra. Neve: Query.php, tartalma megtekinthető a server mappában:


**6.	PHP**

Az időközben elkészült html oldalak lecserélése php oldalakra, ahol a függvényhívások megtörténtek, majd a visszaadott eredmények a megtervezett arculatnak megfelelően dinamikusan megjelentek.
A PHP fájlok megtekinthetők a pages mappában


**7.	Kitelepítés**

Az elkészült weboldal nyilvános url címen való megjelenítéséhez ingyenes webtárhelyre volt szükség adatbázis szolgáltatással. A választás a www.000webhost.com oldalra esett.
Regisztráció után PhpMyAdmin és webes file upload szolgáltatást nyújt korlátozott méretben. Ide került fel az adatbázis és weboldalhoz tartozó állományok. 

A weboldalt így bárki megtekintheti a http://americanflights.000webhostapp.com/ címen


##Python

###Python-ról röviden
> A Python egy általános célú, nagyon magas szintű programozási nyelv, melyet Guido van Rossum holland programozó kezdett el fejleszteni 1989 végén, majd hozott nyilvánosságra 1991-ben. A nyelv tervezési filozófiája az olvashatóságot és a programozói munka megkönnyítését helyezi előtérbe a futási sebességgel szemben.

> A Python többek között a funkcionális, az objektumorientált, az imperatív és a procedurális programozási paradigmákat támogatja. Dinamikus típusokat és automatikus memóriakezelést használ, ilyen szempontból hasonlít a Scheme, Perl és Ruby nyelvekhez, emellett szigorú típusrendszerrel rendelkezik.

> A Python úgynevezett interpreteres nyelv, ami azt jelenti, hogy nincs különválasztva a forrás- és tárgykód, a megírt program máris futtatható, ha rendelkezünk a Python értelmezővel. A Python értelmezőt számos géptípusra és operációs rendszerre elkészítették, továbbá számtalan kiegészítő könyvtár készült hozzá, így rendkívül széles körben használhatóvá vált.
