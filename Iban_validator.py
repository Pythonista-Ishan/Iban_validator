import tkinter as tk
from tkinter import messagebox

def validate_iban(iban):
    # Remove spaces and convert to uppercase
    iban = iban.replace(" ", "").upper()

    # Check length based on country code
    country_lengths = {
        'AL': 28, 'AD': 24, 'AT': 20, 'AZ': 28, 'BH': 22, 'BE': 16,
        'BA': 20, 'BR': 29, 'BG': 22, 'CR': 21, 'HR': 21, 'CY': 28,
        'CZ': 24, 'DK': 18, 'DO': 28, 'EE': 20, 'FI': 18, 'FR': 27,
        'GE': 22, 'DE': 22, 'GH': 27, 'GR': 27, 'GT': 28, 'HU': 28,
        'IS': 26, 'IE': 22, 'IL': 23, 'IT': 27, 'KZ': 20, 'KW': 30,
        'LV': 21, 'LB': 28, 'LI': 21, 'LT': 20, 'LU': 20, 'MT': 31,
        'MR': 27, 'MU': 30, 'MX': 27, 'MD': 24, 'MC': 27, 'ME': 22,
        'NL': 18, 'NZ': 27, 'NO': 15, 'PK': 24, 'PT': 25, 'QA': 29,
        'RO': 24, 'RU': 33, 'SM': 27, 'SA': 24, 'RS': 22, 'SK': 24,
        'SI': 19, 'ES': 24, 'SD': 18, 'SE': 24, 'CH': 21, 'TN': 24,
        'TR': 26, 'UA': 29, 'GB': 22, 'VG': 24
    }

    country_code = iban[:2]
    if country_code not in country_lengths:
        return False
    if len(iban) != country_lengths[country_code]:
        return False

    # Rearranging the IBAN and replacing letters with numbers
    iban_rearranged = iban[4:] + iban[:4]
    iban_numeric = ''.join(str(int(char, 36)) for char in iban_rearranged)

    # Performing mod-97 check
    return int(iban_numeric) % 97 == 1

def check_iban():
    iban = iban_entry.get()
    if validate_iban(iban):
        messagebox.showinfo("Validation Result", "IBAN is valid.")
    else:
        messagebox.showerror("Validation Result", "IBAN is invalid.")

# Setting up the GUI
root = tk.Tk()
root.title("IBAN Validator")

label = tk.Label(root, text="Enter IBAN:")
label.pack(pady=10)

iban_entry = tk.Entry(root, width=30)
iban_entry.pack(pady=10)

validate_button = tk.Button(root, text="Validate IBAN", command=check_iban)
validate_button.pack(pady=20)

root.mainloop()
