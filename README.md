### Parcijalni Ispit - Razvoj Web Aplikacija u Programskom Jeziku Python

## Upute za Rješavanje Zadatka

### 1. **Priprema okruženja:**

- Kreirajte **"fork"** repozitorija  na GitHubu.
- Dodijelite repozitoriju naziv u formatu `pydev_parcijalni_ime_prezime` (primjer: `pydev_parcijalni_pero_peric`).
- **VAŽNO:** Nemojte kreirati **"clone"** repozitorija jer nemate pravo mijenjanja.

### 2. **Postavljanje Projekta:**

- Nakon što ste kreirali **fork**, klonirajte repozitorij s vašeg GitHub profila na lokalno računalo koristeći GitHub Desktop ili drugu omiljenu metodu.
- Uklonite postojeće virtualno okruženje ako je prisutno i kreirajte novo koristeći `venv` (Python virtualno okruženje).
- Ako je potrebno, instalirajte module iz datoteke `requirements.txt` pomoću `pip install -r requirements.txt`.

### 3. **Implementacija Funkcionalnosti:**

Repozitorij sadrži djelomično implementiranu aplikaciju kojoj nedostaju određene funkcionalnosti. Mjesta gdje treba dodati funkcionalnosti označena su komentarima `#TODO` i ključnom riječi `pass`. Vaš zadatak je dopuniti funkcije, ukloniti `pass`, te ostaviti `#TODO` komentar netaknutim.

### 4. **Zadaci za Implementaciju:**

- **Kreiranje nedostajucih putanja i `urls.py` datoteka u aplikacijama**.
- **Integrirati Bootstrap u projekt. Download i dodavanje u projekt**.


### 5. **Upute za Korištenje Django Usera:**
Za korisnike ćete koristiti Django-ov integrirani model **User**. Ovo će omogućiti autentifikaciju i pohranu korisničkih podataka.

### 6. **Struktura Projekta:**
```
offers_calculator/            # Glavni direktorij Django projekta
│
├── offers_calculator/        # Direktorij glavnih postavki projekta
│   ├── __init__.py           # Oznaka za Python paket
│   ├── asgi.py               # Konfiguracija za ASGI server
│   ├── settings.py           # Postavke projekta
│   ├── urls.py               # Globalne rute aplikacije
│   ├── wsgi.py               # Konfiguracija za WSGI server
│   └── manage.py             # Glavna skripta za upravljanje projektom
│
├── db.sqlite3                # SQLite baza podataka
│
├── accounts/                 # Aplikacija za upravljanje korisnicima (Django User model)
│   ├── __init__.py
│   ├── admin.py              # Registracija modela u admin sučelju
│   ├── apps.py               # Konfiguracija aplikacije
│   ├── models.py             # Modeli za korisnike
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za korisnike
│   ├── views.py              # Pogledi za korisnike
│   └── migrations/           # Migracije baze podataka
│       └── __init__.py
│
├── products/                 # Aplikacija za upravljanje proizvodima
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modeli za proizvode
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za proizvode
│   ├── views.py              # Pogledi za proizvode
│   └── migrations/
│       └── __init__.py
│
├── offers/                   # Aplikacija za upravljanje ponudama
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modeli za ponude
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za ponude
│   ├── views.py              # Pogledi za ponude
│   └── migrations/
│       └── __init__.py
│
├── templates/                # Globalni direktorij za HTML predloške
│   ├── base.html             # Osnovni HTML predložak za aplikaciju
│   ├── users/
│   │   └── user_list.html    # Predložak za prikaz korisnika
│   ├── products/
│   │   └── product_list.html # Predložak za prikaz proizvoda
│   └── offers/
│       └── offer_list.html   # Predložak za prikaz ponuda
│
└── static/                   # Globalni direktorij za statičke datoteke
    ├── css/                  # CSS datoteke
    ├── js/                   # JavaScript datoteke
    └── images/               # Slike
```

### 7. **Detalji Implementacije:**

1. **Učitavanje podataka o korisnicima**:
   - Ovdje se koristi Django-ov **User model** za upravljanje korisnicima.
   - Za autentifikaciju korisnika koristit ćemo Django formu za prijavu.

2. **Kreiranje novih ponuda**:
   - Kreirajte obrazac za unos novih ponuda (kao što je ime kupca, datum, proizvodi).
   - Osigurajte da ponuda bude pohranjena u **SQLite**.

3. **Upravljanje proizvodima**:
   - Omogućite dodavanje i izmjenu proizvoda.
   - Proizvodi bi trebali biti povezani s ponudama.

4. **Pohrana novih ponuda**:
   - Osigurajte da se ponude pohranjuju u **SQLite**.

5. **Ispis ponuda**:
   - Omogućite ispis svih ponuda ili filtriranje ponuda prema mjesecu.

### 8. **Kreiranje Django Modela:**
Zadatak uključuje korištenje Django-ovih modela za rad s korisnicima, proizvodima i ponudama. Svaki model treba biti u odgovarajućem direktoriju (`users`, `products`, `offers`) i biti povezan s bazom podataka (`db.sqlite3`).

#### Model korisnika (`users/models.py`):
```python
from django.contrib.auth.models import User

class CustomUser(User):
    # Ovdje možete dodati dodatna polja za korisnika ako je potrebno.
    pass
```

#### Model proizvoda (`products/models.py`):
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
```

#### Model ponude (`offers/models.py`):
```python
from django.db import models
from products.models import Product
from users.models import CustomUser

class Offer(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    products = models.ManyToManyField(Product)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Offer #{self.id} for {self.customer.username}"
```

### 9. **Dodatni Zadaci:**
- Implementirati REST API za dohvaćanje korisničkih podataka putem **Django REST Framework** (ako se zahtijeva).
- Kreirati obrasce i prikaze za unos novih ponuda i proizvoda.

### 10. **Upute za Uporabu:**
- **Pokretanje aplikacije**: Koristite **Django** komandu za migraciju i pokretanje aplikacije:
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

- **Dodavanje korisnika**:
  U Django administraciji možete dodavati korisnike ili koristiti Django-ovu formu za prijavu.

- **Testiranje funkcionalnosti**:
  Provjerite sve funkcionalnosti aplikacije putem sučelja i konzole.

### 11. **Dodatne Upute:**

- Nemojte mijenjati druge dijelove aplikacije. Ako Vaša implementacija ne radi, prilagodite svoje rješenje aplikaciji, a ne obrnuto.
- Koristite **TypeHints** za sve metode kako biste osigurali konzistentnost tipova podataka.
- Pripazite na Django konfiguraciju i postavke vezane uz bazu podataka i autentifikaciju korisnika.

### 12. **Podnošenje Rješenja:**

Nakon što završite implementaciju:

1. Napravite **commit** za sve promjene koje ste unijeli koristeći **git commit**.
2. **Pushajte** promjene na vaš GitHub repozitorij pomoću **git push**.

### 13. **Podjela Repozitorija s Predavačem:**

1. Otvorite vaš repozitorij na GitHubu.
2. Kliknite na karticu **Settings** u repozitoriju.
3. Pronađite opciju **Collaborators** i dodajte predavača kao **Contributor**.
4. Provjerite da su sve promjene commitane i pushane prije dodavanja predavača.

### **Sretno!**


admin
admin@offers-calculator.hr
!Pa$$w0rd!

Dodati CUSTOMERS u aplikaciju
