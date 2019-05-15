import requests
import re
import os
import csv

###############################################################################
# Najprej definirajmo nekaj pomožnih orodij za pridobivanje podatkov s spleta.
###############################################################################

# definiratje URL glavne strani bolhe za oglase z mačkami
<<<<<<< HEAD
cats_frontpage_url = 'http://www.bolha.com/zivali/male-zivali/macke/?page=2'
=======
cats_frontpage_url = 'http://www.bolha.com/zivali/male-zivali/macke/'
>>>>>>> 5d55d54c1b7447892f96579b455aebf0fac58574
# mapa, v katero bomo shranili podatke
cat_directory = 'moje_macke'
# ime datoteke v katero bomo shranili glavno stran
frontpage_filename = 'macke.html'
# ime CSV datoteke v katero bomo shranili podatke
csv_filename = 'macke.csv'
  
def download_url_to_string(url, ime_datoteke, directory, vsili_prenos = False):
    '''This function takes a URL as argument and tries to download it
    using requests. Upon success, it returns the page contents as string.'''
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Stran ne obstaja.')
        # koda, ki se izvede pri napaki
        # dovolj je če izpišemo opozorilo in prekinemo izvajanje funkcije
        return None
        # nadaljujemo s kodo če ni prišlo do napake
    return r.text


def save_string_to_file(text, directory, filename):
    '''Write "text" to the file "filename" located in directory "directory",
    creating "directory" if necessary. If "directory" is the empty string, use
    the current directory.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

# Definirajte funkcijo, ki prenese glavno stran in jo shrani v datoteko.


def save_frontpage(url, directory, filename):
    '''Save "cats_frontpage_url" to the file
    "cat_directory"/"frontpage_filename"'''
    save_string_to_file(download_url_to_string(http://www.bolha.com/zivali/male-zivali/macke/, macke.html, moje_macke))
    return  

###############################################################################
# Po pridobitvi podatkov jih želimo obdelati.
###############################################################################


def read_file_to_string(directory, filename):
    '''Return the contents of the file "directory"/"filename" as a string.'''
    with open(directory/filename) as datoteka:
        return datoteka.read()

# Definirajte funkcijo, ki sprejme niz, ki predstavlja vsebino spletne strani,
# in ga razdeli na dele, kjer vsak del predstavlja en oglas. To storite s
# pomočjo regularnih izrazov, ki označujejo začetek in konec posameznega
# oglasa. Funkcija naj vrne seznam nizov.


def page_to_ads(niz):
    '''Split "page" to a list of advertisement blocks.'''
    vzorec = ''
    return TODO

# Definirajte funkcijo, ki sprejme niz, ki predstavlja oglas, in izlušči
# podatke o imenu, ceni in opisu v oglasu.


def get_dict_from_ad_block(TODO):
    '''Build a dictionary containing the name, description and price
    of an ad block.'''
    return TODO

# Definirajte funkcijo, ki sprejme ime in lokacijo datoteke, ki vsebuje
# besedilo spletne strani, in vrne seznam slovarjev, ki vsebujejo podatke o
# vseh oglasih strani.


def ads_from_file(TODO):
    '''Parse the ads in filename/directory into a dictionary list.'''
    return TODO

###############################################################################
# Obdelane podatke želimo sedaj shraniti.
###############################################################################


def write_csv(fieldnames, rows, directory, filename):
    '''Write a CSV file to directory/filename. The fieldnames must be a list of
    strings, the rows a list of dictionaries each mapping a fieldname to a
    cell-value.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None

# Definirajte funkcijo, ki sprejme neprazen seznam slovarjev, ki predstavljajo
# podatke iz oglasa mačke, in zapiše vse podatke v csv datoteko. Imena za
# stolpce [fieldnames] pridobite iz slovarjev.


def write_cat_ads_to_csv(seznam):

    return write_csv
