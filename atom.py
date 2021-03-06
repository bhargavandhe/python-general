"""Problem Statement: To replace individual letters of words with respective Element symbols
Today: 07/08/20
Author: Andhe Bhargav"""
from random import randrange

elements = {
    'a': ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine'],
    'b': ['Barium', 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine'],
    'c': ['Cadmium', 'Caesium', 'Calcium', 'Californium', 'Carbon', 'Cerium', 'Chlorine', 'Chromium', 'Cobalt',
          'Copernicium', 'Copper', 'Curium'],
    'd': ['Darmstadtium', 'Dubnium', 'Dysprosium'],
    'e': ['Einsteinium', 'Erbium', 'Europium'],
    'f': ['Fermium', 'Flerovium', 'Fluorine', 'Francium'],
    'g': ['Gadolinium', 'Gallium', 'Germanium', 'Gold'],
    'h': ['Hafnium', 'Hassium', 'Helium', 'Holmium', 'Hydrogen'],
    'i': ['Indium', 'Iodine', 'Iridium', 'Iron'],
    'j': ['-'],
    'k': ['Krypton'],
    'l': ['Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 'Livermorium', 'Lutetium'],
    'm': ['Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury', 'Molybdenum', 'Moscovium'],
    'n': ['Neodymium', 'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium', 'Nitrogen'],
    'o': ['Oganesson', 'Osmium', 'Oxygen'],
    'p': ['Palladium', 'Phosphorous', 'Platinum', 'Plutonium', 'Polonium', 'Potassium', 'Praseodymium', 'Promethium',
          'Protactinium'],
    'r': ['Radium', 'Rhenium', 'Rhodium', 'Radon', 'Roentgenium', 'Rubidium', 'Rutherfordium'],
    's': ['Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 'Silver', 'Sodium', 'Strontium', 'Sulphur'],
    't': ['Tantalum', 'Technetium', 'Tellurium', 'Tennessine', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin',
          'Titanium', 'Tungsten'],
    'u': ['Uranium'],
    'v': ['Vanadium'],
    'w': ['-'],
    'x': ['Xenon'],
    'y': ['Ytterbium', 'Yttrium'],
    'z': ['Zinc', 'Zirconium'],
    ' ': [' '],
    '.': ['.']
}
sent = input("Enter text: ")

for char in sent:
    if char.lower() in elements and char.isalpha():
        print(f'{char} : {elements[char.lower()][randrange(0, len(elements[char.lower()]))]}')
