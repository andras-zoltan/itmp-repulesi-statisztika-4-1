# itmp-repulesi-statisztika-4-1

#### Backed feladatok

**1.	A kapott csv állomány feldolgozása**

A flight.csv 22 779 sornyi adatot tartalmaz. Minden sorban 22 adat vesszõvel elválasztva. Ezt a karaktert szeparátorként használva fel kellett darabolni a sorokat, hogy egyedi adatokat kapjunk. 

Ezt megnehezítõ tényezõk:

.*	az repülõtér rövidítése és városa egy idézõjelben szerepelt a repülõtér nevével.
.*	néhány sorban hiányzó adatok
.*	egy-egy sorban még néhány szeparátor is hiányzott

**2.	Adatfeldolgozás módjának kiválasztása**

Mivel weben megjelenõ alkalmazásról van szó, legcélszerûbbnek a MySQL + PHP megoldás tûnt. Ezek segítségével a feladatban kért eredmények egyetlen jól megírt SQL paranccsal hatékonyan és gyorsan megjelenthetõk úgy, hogy az SQL lekérdezés eredménytáblája egy PHP mátrixba kerül. Ennek tartalma alapján pedig legeneráljuk a szükséges HTML kódot.

**3.	MySQL adatbázis létrehozása**

A feladat kérte több eredmény megjelenítését ezen adatok alapján. Célszerû volt ezért adatbázisba tenni azokat. Az adatbázisnak viszont 3. normálformában kell lennie. Ezért a redundáns értékeket tartalmazó oszlopokból külön táblák készültek. 

![adatbázis](images/database-view.png "adatbázis")


**4.	Adatbáziskapcsolat kialakítása**

A kapcsolat felállítása egy PHP osztály segítségével törtét a PDO osztály kiterjsztésével.
Neve: Database.php, tartalma megtekinthetõ a server mappában:

**5.	Feladatmegoldások**

Megoldandó feladatok:
.*	minden légitarsaság felsorolása
.*	egy kiválasztott légitársaság különféle adatainak megjelenítése
.*	top 3 reptér fogadott járatok száma alapján
-	top 3 légitársaság késés alapján

Minden feladatra és az azokon belüli részeredmények lekérdezésére külön függvény készült. Ezek egy PHP osztályban kerültek kidolgozásra. Neve: Query.php, tartalma megtekinthetõ a server mappában:

**6.	PHP**

Az idõközben elkészült html oldalak lecserélése php oldalakra, ahol a függvényhívások megtörténtek, majd a visszaadott eredmények a megtervezett arculatnak megfelelõen dinamikusan megjelentek.
A PHP fájlok megtekinthetõk a pages mappában

**7.	Kitelepítés**

Az elkészült weboldal nyilvános url címen való megjelenítéséhez ingyenes webtárhelyre volt szükség adatbázis szolgáltatással. A választás a www.000webhost.com oldalra esett.
Regisztráció után PhpMyAdmin és webes file upload szolgáltatást nyújt korlátozott méretben. Ide került fel az adatbázis és weboldalhoz tartozó állományok. 

A weboldalt így bárki megtekintheti az alábbi címen:

[http://americanflights.000webhostapp.com/]: http://americanflights.000webhostapp.com/


