# Vaatimusmäärittely

## Sovelluksen perusidea
Sovellus tarjoaa katsauksen käyttäjän valitsemaan matkustuskohteeseen. 
Tämä katsaus sisältää kohteen valuuttakurssin/muuntajan, kohteen sää-ennusteen tulevilta päiviltä, viimeisemmät uutiset kohteesta,
sekä tiedot kohteen nähtävyyksistä.

## Käyttöliittymä
### Home page
Sovellus aukeaa "Home page" näkymään jossa olevaan syötekenttään käyttäjä syöttää halutun kohdekaupungin. Mikäli syöte ei vastaa oikeaa kaupunkia, pyytää sovellus uutta syötettä.
Mikäli syöte on validi, avaa "Take me there!" painike seuraavan näkymän joka näyttää tiedot kohteesta.

![](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Home_page.png)

### HUB page
Toinen näkymä, HUB page, näyttää tiedot käyttäjän syöttämästä kohteesta. HUB page sisältää linkkejä ulkoisiin lähteisiin kuten uutisiin ja nähtävyyksiin. Sivulta on myös nähtävissä kohteen seuraavien päivien sääennuste, sekä valuuttamuuntaja paikallisen valuutan ja Euron välillä.
"Return" painiketta painamalla käyttäjä pääsee takaisin aloitus-sivulle, jossa hän voi syöttää uuden kohteen.

![](https://github.com/kodtld/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/HUB_page.png)

## Sovelluksen toiminnallisuus
Sovelluksen tämänhetkinen toiminnallisuus:
- Etusivu
  - Tarjoaa syötekentän, johon käyttäjä voi syöttää toivomansa kohde-kaupungin.
  - Mikäli syöte ei ole validi (numeroita tai olematon kaupunki), pyytää ohjelma uutta syötettä.
- Sisältösivu
  - Käyttäjä voi syöttää arvoja valuuttamuuntajaan.
  - Käyttäjä näkee kohteen uutiset, suositut nähtävyydet lähellä keskustaa, valuuttamuuntajan, sekä sääennusteen. (Uutiset, sekä nähtävyydet sisältävät linkit ulkoisiin lähteisiin).
  - Sisältösivulta pääsee "return" painikkeella takaisin etusivulle.

## Jatkokehitysideoita
Sovelluksen toiminta perustuu eri API rajapintojen höydyntämiseen. Tämänhetkinen versio rakentuu näiden ilmaisversiohin,
joissa toiminnallisuus/ominaisuudet ovat rajattuja. Tulevaisuudessa ohjelman toimintaa voisi laajentaa monin tavoin.

- Historiallisen säädatan näyttäminen esim. edellisen vuoden vastaavien päivien säästä.
- Edulliset lennot kohteeseen.
- Lisätä maakohtaiset uutislähteet, sen sijaan että hakee vain suurimpien englanninkielisten uutislähteiden julkaisut.
- Lisätä kohteen suositut ja vapaat hotellit/AirBnb:t valituille päiville.
- Mahdollisuus vertailla matkakohteita keskenään.
- Näkymä joka näyttää hyödylliset "peruslauseet" kohdemaan kielellä.
- Museo, ravintola, tapahtuma, jne. suositukset kohteesta.
- Yms. Jatkokehitysmahdollisuudet ovat melkein rajattomat. Kehityksen suuntana olisi näyttää mahdollisimman tarkka ja ajankohtainen "ote" kohteen tämänhetkisestä tilasta ja elämästä.
