import tkinter
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as tb
import csv
import os
from PIL import Image, ImageTk

class myChem:
    def __init__(self, root):
        self.root = root
        self.root.title("Information of Chemical Elements in Periodic Table App")
        self.root.geometry("1000x700")
       
        frame = tkinter.Frame(self.root)
        frame.pack(pady=20)

        left_frame = tkinter.Frame(frame)
        left_frame.grid(row=0, column=0, padx=20)

        atom1_frame = tkinter.LabelFrame(left_frame, text="Chemical Elements Form")
        atom1_frame.pack(pady=10, padx=10, fill="x")

        tkinter.Label(atom1_frame, text="Nama Atom").pack()
        self.atom_combobox = ttk.Combobox(atom1_frame, values=[
            "Hidrogen (H)", "Helium (He)", "Litium (Li)", "Berilium (Be)", "Boron (B)",  
            "Karbon (C)", "Nitrogen (N)", "Oksigen (O)", "Fluor (F)", "Neon (Ne)",  
            "Natrium (Na)", "Magnesium (Mg)", "Aluminium (Al)", "Silikon (Si)", "Fosfor (P)",  
            "Belerang (S)", "Klor (Cl)", "Argon (Ar)", "Kalium (K)", "Kalsium (Ca)",  
            "Skandium (Sc)", "Titanium (Ti)", "Vanadium (V)", "Kromium (Cr)", "Mangan (Mn)",  
            "Besi (Fe)", "Kobalt (Co)", "Nikel (Ni)", "Tembaga (Cu)", "Seng (Zn)",  
            "Galium (Ga)", "Germanium (Ge)", "Arsen (As)", "Selenium (Se)", "Brom (Br)",  
            "Kripton (Kr)", "Rubidium (Rb)", "Stronsium (Sr)", "Itrium (Y)", "Zirkonium (Zr)",  
            "Niobium (Nb)", "Molibdenum (Mo)", "Teknesium (Tc)", "Rutenium (Ru)", "Rodium (Rh)",  
            "Paladium (Pd)", "Perak (Ag)", "Kadmium (Cd)", "Indium (In)", "Timah (Sn)",  
            "Antimon (Sb)", "Telurium (Te)", "Iodium (I)", "Xenon (Xe)", "Sesium (Cs)",  
            "Barium (Ba)", "Lantanum (La)", "Serium (Ce)", "Praseodimium (Pr)", "Neodimium (Nd)",  
            "Prometium (Pm)", "Samarium (Sm)", "Europium (Eu)", "Gadolinium (Gd)", "Terbium (Tb)",  
            "Disprosium (Dy)", "Holmium (Ho)", "Erbium (Er)", "Tulium (Tm)", "Iterbium (Yb)",  
            "Lutesium (Lu)", "Hafnium (Hf)", "Tantalum (Ta)", "Wolfram (W)", "Renium (Re)",  
            "Osmium (Os)", "Iridium (Ir)", "Platina (Pt)", "Emas (Au)", "Raksa (Hg)",  
            "Talium (Tl)", "Timbal (Pb)", "Bismut (Bi)", "Polonium (Po)", "Astatin (At)",  
            "Radon (Rn)", "Fransium (Fr)", "Radium (Ra)", "Aktinium (Ac)", "Torium (Th)",  
            "Protaktinium (Pa)", "Uranium (U)", "Neptunium (Np)", "Plutonium (Pu)", "Amerisium (Am)",  
            "Kurium (Cm)", "Berkelium (Bk)", "Kalifornium (Cf)", "Einsteinium (Es)", "Fermium (Fm)",  
            "Mendelevium (Md)", "Nobelium (No)", "Lawrensium (Lr)", "Rutherfordium (Rf)", "Dubnium (Db)",  
            "Seaborgium (Sg)", "Bohrium (Bh)", "Hasium (Hs)", "Meitnerium (Mt)", "Darmstadtium (Ds)",  
            "Roentgenium (Rg)", "Kopernisium (Cn)", "Nihonium (Nh)", "Flerovium (Fl)", "Moskovium (Mc)",  
            "Livermorium (Lv)", "Tennessine (Ts)", "Oganesson (Og)"], width=30)
        self.atom_combobox.pack(pady=5)

        button = tkinter.Button(left_frame, text="Find", command=self.save_to_csv, width=15)
        button.pack(pady=10)

        tree_frame = tkinter.LabelFrame(left_frame, text="Data Unsur Kimia")
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.tree = ttk.Treeview(tree_frame, columns=("simbol", "nomor_atom", "massa_atom", "titik_didih", "titik_leleh"), show="headings", height=5)
        
        self.tree.heading("simbol", text="Simbol")
        self.tree.column("simbol", width=80, anchor="center")
        
        self.tree.heading("nomor_atom", text="Nomor Atom")
        self.tree.column("nomor_atom", width=80, anchor="center")
        
        self.tree.heading("massa_atom", text="Massa Atom")
        self.tree.column("massa_atom", width=100, anchor="center")
        
        self.tree.heading("titik_didih", text="Titik Didih (°C)")
        self.tree.column("titik_didih", width=120, anchor="center")
        
        self.tree.heading("titik_leleh", text="Titik Leleh (°C)")
        self.tree.column("titik_leleh", width=120, anchor="center")
        
        self.tree.pack(fill="both", expand=True)

        self.image_frame = tb.Frame(frame)
        self.image_frame.grid(row=0, column=1)
        
        self.image_label = tkinter.Label(self.image_frame)
        self.image_label.pack()

        self.load_csv()

    def load_csv(self):
        try:
            for item in self.tree.get_children():
                self.tree.delete(item)

            if os.path.exists('data3.csv'):
                with open('data3.csv', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        self.tree.insert("", tkinter.END, values=(
                            row["simbol"],
                            row["nomor_atom"],
                            row["massa_atom"],
                            row["titik_didih"],
                            row["titik_leleh"]
                        ))
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membaca CSV: {e}")

    def tampil_gambar(self, golongan):
        path = f"img/{golongan}.png"
        for widget in self.image_frame.winfo_children():
            widget.destroy()
        if os.path.exists(path):
            try:
                img = Image.open(path)
                img = img
                photo = ImageTk.PhotoImage(img)
                label_img = tkinter.Label(self.image_frame, image=photo)
                label_img.image = photo  # Keep a reference
                label_img.pack()
            except Exception as e:
                tkinter.Label(self.image_frame, text=f"Error loading image: {e}").pack()
        else:
            tkinter.Label(self.image_frame, text="Gambar tidak ditemukan").pack()

    def save_to_csv(self):
        atom_with_symbol = self.atom_combobox.get()
        atom = atom_with_symbol.split(" (")[0] if atom_with_symbol else ""

        unsur_kimia = {
            "Hidrogen": {"simbol": "H", "nomor_atom": 1, "massa_atom": 1.008, "titik_didih": -252.87, "titik_leleh": -259.16},
            "Helium": {"simbol": "He", "nomor_atom": 2, "massa_atom": 4.0026, "titik_didih": -268.93, "titik_leleh": -272.2},
            "Litium": {"simbol": "Li", "nomor_atom": 3, "massa_atom": 6.94, "titik_didih": 1342, "titik_leleh": 180.54},
            "Berilium": {"simbol": "Be", "nomor_atom": 4, "massa_atom": 9.0122, "titik_didih": 2469, "titik_leleh": 1287},
            "Boron": {"simbol": "B", "nomor_atom": 5, "massa_atom": 10.81, "titik_didih": 4000, "titik_leleh": 2075},
            "Karbon": {"simbol": "C", "nomor_atom": 6, "massa_atom": 12.011, "titik_didih": 4827, "titik_leleh": 3500},
            "Nitrogen": {"simbol": "N", "nomor_atom": 7, "massa_atom": 14.007, "titik_didih": -195.79, "titik_leleh": -210.0},
            "Oksigen": {"simbol": "O", "nomor_atom": 8, "massa_atom": 15.999, "titik_didih": -182.96, "titik_leleh": -218.79},
            "Fluor": {"simbol": "F", "nomor_atom": 9, "massa_atom": 18.998, "titik_didih": -188.12, "titik_leleh": -219.67},
            "Neon": {"simbol": "Ne", "nomor_atom": 10, "massa_atom": 20.18, "titik_didih": -246.08, "titik_leleh": -248.59},
            "Natrium": {"simbol": "Na", "nomor_atom": 11, "massa_atom": 22.99, "titik_didih": 883, "titik_leleh": 97.72},
            "Magnesium": {"simbol": "Mg", "nomor_atom": 12, "massa_atom": 24.305, "titik_didih": 1090, "titik_leleh": 650},
            "Aluminium": {"simbol": "Al", "nomor_atom": 13, "massa_atom": 26.982, "titik_didih": 2519, "titik_leleh": 660.32},
            "Silikon": {"simbol": "Si", "nomor_atom": 14, "massa_atom": 28.085, "titik_didih": 3265, "titik_leleh": 1414},
            "Fosfor": {"simbol": "P", "nomor_atom": 15, "massa_atom": 30.974, "titik_didih": 280.5, "titik_leleh": 44.15},
            "Belerang": {"simbol": "S", "nomor_atom": 16, "massa_atom": 32.06, "titik_didih": 444.72, "titik_leleh": 115.21},
            "Klor": {"simbol": "Cl", "nomor_atom": 17, "massa_atom": 35.45, "titik_didih": -34.04, "titik_leleh": -101.5},
            "Argon": {"simbol": "Ar", "nomor_atom": 18, "massa_atom": 39.948, "titik_didih": -185.85, "titik_leleh": -189.34},
            "Kalium": {"simbol": "K", "nomor_atom": 19, "massa_atom": 39.098, "titik_didih": 774, "titik_leleh": 63.38},
            "Kalsium": {"simbol": "Ca", "nomor_atom": 20, "massa_atom": 40.078, "titik_didih": 1484, "titik_leleh": 842},
            "Skandium": {"simbol": "Sc", "nomor_atom": 21, "massa_atom": 44.956, "titik_didih": 2836, "titik_leleh": 1541},
            "Titanium": {"simbol": "Ti", "nomor_atom": 22, "massa_atom": 47.867, "titik_didih": 3287, "titik_leleh": 1668},
            "Vanadium": {"simbol": "V", "nomor_atom": 23, "massa_atom": 50.942, "titik_didih": 3407, "titik_leleh": 1910},
            "Kromium": {"simbol": "Cr", "nomor_atom": 24, "massa_atom": 51.996, "titik_didih": 2671, "titik_leleh": 1907},
            "Mangan": {"simbol": "Mn", "nomor_atom": 25, "massa_atom": 54.938, "titik_didih": 2061, "titik_leleh": 1246},
            "Besi": {"simbol": "Fe", "nomor_atom": 26, "massa_atom": 55.845, "titik_didih": 2861, "titik_leleh": 1538},
            "Kobalt": {"simbol": "Co", "nomor_atom": 27, "massa_atom": 58.933, "titik_didih": 2927, "titik_leleh": 1495},
            "Nikel": {"simbol": "Ni", "nomor_atom": 28, "massa_atom": 58.693, "titik_didih": 2913, "titik_leleh": 1455},
            "Tembaga": {"simbol": "Cu", "nomor_atom": 29, "massa_atom": 63.546, "titik_didih": 2562, "titik_leleh": 1084.62},
            "Seng": {"simbol": "Zn", "nomor_atom": 30, "massa_atom": 65.38, "titik_didih": 907, "titik_leleh": 419.53},
            "Galium": {"simbol": "Ga", "nomor_atom": 31, "massa_atom": 69.723, "titik_didih": 2204, "titik_leleh": 29.76},
            "Germanium": {"simbol": "Ge", "nomor_atom": 32, "massa_atom": 72.63, "titik_didih": 2833, "titik_leleh": 938.25},
            "Arsen": {"simbol": "As", "nomor_atom": 33, "massa_atom": 74.922, "titik_didih": 614, "titik_leleh": 817},
            "Selenium": {"simbol": "Se", "nomor_atom": 34, "massa_atom": 78.971, "titik_didih": 685, "titik_leleh": 221},
            "Brom": {"simbol": "Br", "nomor_atom": 35, "massa_atom": 79.904, "titik_didih": 58.8, "titik_leleh": -7.2},
            "Kripton": {"simbol": "Kr", "nomor_atom": 36, "massa_atom": 83.798, "titik_didih": -153.22, "titik_leleh": -157.36},
            "Rubidium": {"simbol": "Rb", "nomor_atom": 37, "massa_atom": 85.468, "titik_didih": 688, "titik_leleh": 39.31},
            "Stronsium": {"simbol": "Sr", "nomor_atom": 38, "massa_atom": 87.62, "titik_didih": 1382, "titik_leleh": 777},
            "Itrium": {"simbol": "Y", "nomor_atom": 39, "massa_atom": 88.906, "titik_didih": 3336, "titik_leleh": 1526},
            "Zirkonium": {"simbol": "Zr", "nomor_atom": 40, "massa_atom": 91.224, "titik_didih": 4409, "titik_leleh": 1855},
            "Niobium": {"simbol": "Nb", "nomor_atom": 41, "massa_atom": 92.906, "titik_didih": 4744, "titik_leleh": 2477},
            "Molibdenum": {"simbol": "Mo", "nomor_atom": 42, "massa_atom": 95.95, "titik_didih": 4639, "titik_leleh": 2623},
            "Teknesium": {"simbol": "Tc", "nomor_atom": 43, "massa_atom": 98, "titik_didih": 4265, "titik_leleh": 2157},
            "Rutenium": {"simbol": "Ru", "nomor_atom": 44, "massa_atom": 101.07, "titik_didih": 4150, "titik_leleh": 2334},
            "Rodium": {"simbol": "Rh", "nomor_atom": 45, "massa_atom": 102.91, "titik_didih": 3695, "titik_leleh": 1964},
            "Paladium": {"simbol": "Pd", "nomor_atom": 46, "massa_atom": 106.42, "titik_didih": 2963, "titik_leleh": 1554.9},
            "Perak": {"simbol": "Ag", "nomor_atom": 47, "massa_atom": 107.87, "titik_didih": 2162, "titik_leleh": 961.78},
            "Kadmium": {"simbol": "Cd", "nomor_atom": 48, "massa_atom": 112.41, "titik_didih": 767, "titik_leleh": 321.07},
            "Indium": {"simbol": "In", "nomor_atom": 49, "massa_atom": 114.82, "titik_didih": 2072, "titik_leleh": 156.6},
            "Timah": {"simbol": "Sn", "nomor_atom": 50, "massa_atom": 118.71, "titik_didih": 2602, "titik_leleh": 231.93},
            "Antimon": {"simbol": "Sb", "nomor_atom": 51, "massa_atom": 121.76, "titik_didih": 1587, "titik_leleh": 630.63},
            "Telurium": {"simbol": "Te", "nomor_atom": 52, "massa_atom": 127.6, "titik_didih": 988, "titik_leleh": 449.51},
            "Iodium": {"simbol": "I", "nomor_atom": 53, "massa_atom": 126.9, "titik_didih": 184.3, "titik_leleh": 113.7},
            "Xenon": {"simbol": "Xe", "nomor_atom": 54, "massa_atom": 131.29, "titik_didih": -108.12, "titik_leleh": -111.75},
            "Sesium": {"simbol": "Cs", "nomor_atom": 55, "massa_atom": 132.91, "titik_didih": 671, "titik_leleh": 28.44},
            "Barium": {"simbol": "Ba", "nomor_atom": 56, "massa_atom": 137.33, "titik_didih": 1870, "titik_leleh": 727},
            "Lantanum": {"simbol": "La", "nomor_atom": 57, "massa_atom": 138.91, "titik_didih": 3464, "titik_leleh": 920},
            "Serium": {"simbol": "Ce", "nomor_atom": 58, "massa_atom": 140.12, "titik_didih": 3443, "titik_leleh": 795},
            "Praseodimium": {"simbol": "Pr", "nomor_atom": 59, "massa_atom": 140.91, "titik_didih": 3520, "titik_leleh": 935},
            "Neodimium": {"simbol": "Nd", "nomor_atom": 60, "massa_atom": 144.24, "titik_didih": 3074, "titik_leleh": 1024},
            "Prometium": {"simbol": "Pm", "nomor_atom": 61, "massa_atom": 145, "titik_didih": 3000, "titik_leleh": 1042},
            "Samarium": {"simbol": "Sm", "nomor_atom": 62, "massa_atom": 150.36, "titik_didih": 1794, "titik_leleh": 1072},
            "Europium": {"simbol": "Eu", "nomor_atom": 63, "massa_atom": 151.96, "titik_didih": 1529, "titik_leleh": 822},
            "Gadolinium": {"simbol": "Gd", "nomor_atom": 64, "massa_atom": 157.25, "titik_didih": 3250, "titik_leleh": 1312},
            "Terbium": {"simbol": "Tb", "nomor_atom": 65, "massa_atom": 158.93, "titik_didih": 3230, "titik_leleh": 1356},
            "Disprosium": {"simbol": "Dy", "nomor_atom": 66, "massa_atom": 162.5, "titik_didih": 2567, "titik_leleh": 1407},
            "Holmium": {"simbol": "Ho", "nomor_atom": 67, "massa_atom": 164.93, "titik_didih": 2700, "titik_leleh": 1461},
            "Erbium": {"simbol": "Er", "nomor_atom": 68, "massa_atom": 167.26, "titik_didih": 2868, "titik_leleh": 1529},
            "Tulium": {"simbol": "Tm", "nomor_atom": 69, "massa_atom": 168.93, "titik_didih": 1950, "titik_leleh": 1545},
            "Iterbium": {"simbol": "Yb", "nomor_atom": 70, "massa_atom": 173.05, "titik_didih": 1196, "titik_leleh": 824},
            "Lutesium": {"simbol": "Lu", "nomor_atom": 71, "massa_atom": 174.97, "titik_didih": 3402, "titik_leleh": 1652},
            "Hafnium": {"simbol": "Hf", "nomor_atom": 72, "massa_atom": 178.49, "titik_didih": 4603, "titik_leleh": 2233},
            "Tantalum": {"simbol": "Ta", "nomor_atom": 73, "massa_atom": 180.95, "titik_didih": 5425, "titik_leleh": 3017},
            "Wolfram": {"simbol": "W", "nomor_atom": 74, "massa_atom": 183.84, "titik_didih": 5555, "titik_leleh": 3422},
            "Renium": {"simbol": "Re", "nomor_atom": 75, "massa_atom": 186.21, "titik_didih": 5596, "titik_leleh": 3186},
            "Osmium": {"simbol": "Os", "nomor_atom": 76, "massa_atom": 190.23, "titik_didih": 5012, "titik_leleh": 3033},
            "Iridium": {"simbol": "Ir", "nomor_atom": 77, "massa_atom": 192.22, "titik_didih": 4428, "titik_leleh": 2446},
            "Platina": {"simbol": "Pt", "nomor_atom": 78, "massa_atom": 195.08, "titik_didih": 3825, "titik_leleh": 1768.3},
            "Emas": {"simbol": "Au", "nomor_atom": 79, "massa_atom": 196.97, "titik_didih": 2856, "titik_leleh": 1064.18},
            "Raksa": {"simbol": "Hg", "nomor_atom": 80, "massa_atom": 200.59, "titik_didih": 356.73, "titik_leleh": -38.83},
            "Talium": {"simbol": "Tl", "nomor_atom": 81, "massa_atom": 204.38, "titik_didih": 1473, "titik_leleh": 304},
            "Timbal": {"simbol": "Pb", "nomor_atom": 82, "massa_atom": 207.2, "titik_didih": 1749, "titik_leleh": 327.46},
            "Bismut": {"simbol": "Bi", "nomor_atom": 83, "massa_atom": 208.98, "titik_didih": 1564, "titik_leleh": 271.3},
            "Polonium": {"simbol": "Po", "nomor_atom": 84, "massa_atom": 209, "titik_didih": 962, "titik_leleh": 254},
            "Astatin": {"simbol": "At", "nomor_atom": 85, "massa_atom": 210, "titik_didih": None, "titik_leleh": 302},
            "Radon": {"simbol": "Rn", "nomor_atom": 86, "massa_atom": 222, "titik_didih": -61.7, "titik_leleh": -71},
            "Fransium": {"simbol": "Fr", "nomor_atom": 87, "massa_atom": 223, "titik_didih": None, "titik_leleh": 27},
            "Radium": {"simbol": "Ra", "nomor_atom": 88, "massa_atom": 226, "titik_didih": 1737, "titik_leleh": 700},
            "Aktinium": {"simbol": "Ac", "nomor_atom": 89, "massa_atom": 227, "titik_didih": 3198, "titik_leleh": 1050},
            "Torium": {"simbol": "Th", "nomor_atom": 90, "massa_atom": 232.04, "titik_didih": 4788, "titik_leleh": 1750},
            "Protaktinium": {"simbol": "Pa", "nomor_atom": 91, "massa_atom": 231.04, "titik_didih": 4027, "titik_leleh": 1572},
            "Uranium": {"simbol": "U", "nomor_atom": 92, "massa_atom": 238.03, "titik_didih": 4131, "titik_leleh": 1135},
            "Neptunium": {"simbol": "Np", "nomor_atom": 93, "massa_atom": 237, "titik_didih": 4175, "titik_leleh": 644},
            "Plutonium": {"simbol": "Pu", "nomor_atom": 94, "massa_atom": 244, "titik_didih": 3232, "titik_leleh": 639.4},
            "Amerisium": {"simbol": "Am", "nomor_atom": 95, "massa_atom": 243, "titik_didih": 2607, "titik_leleh": 1176},
            "Kurium": {"simbol": "Cm", "nomor_atom": 96, "massa_atom": 247, "titik_didih": 3110, "titik_leleh": 1340},
            "Berkelium": {"simbol": "Bk", "nomor_atom": 97, "massa_atom": 247, "titik_didih": None, "titik_leleh": 986},
            "Kalifornium": {"simbol": "Cf", "nomor_atom": 98, "massa_atom": 251, "titik_didih": None, "titik_leleh": 900},
            "Einsteinium": {"simbol": "Es", "nomor_atom": 99, "massa_atom": 252, "titik_didih": None, "titik_leleh": 860},
            "Fermium": {"simbol": "Fm", "nomor_atom": 100, "massa_atom": 257, "titik_didih": None, "titik_leleh": 1527},
            "Mendelevium": {"simbol": "Md", "nomor_atom": 101, "massa_atom": 258, "titik_didih": None, "titik_leleh": 827},
            "Nobelium": {"simbol": "No", "nomor_atom": 102, "massa_atom": 259, "titik_didih": None, "titik_leleh": 827},
            "Lawrensium": {"simbol": "Lr", "nomor_atom": 103, "massa_atom": 262, "titik_didih": None, "titik_leleh": 1627},
            "Rutherfordium": {"simbol": "Rf", "nomor_atom": 104, "massa_atom": 267, "titik_didih": None, "titik_leleh": None},
            "Dubnium": {"simbol": "Db", "nomor_atom": 105, "massa_atom": 268, "titik_didih": None, "titik_leleh": None},
            "Seaborgium": {"simbol": "Sg", "nomor_atom": 106, "massa_atom": 269, "titik_didih": None, "titik_leleh": None},
            "Bohrium": {"simbol": "Bh", "nomor_atom": 107, "massa_atom": 270, "titik_didih": None, "titik_leleh": None},
            "Hasium": {"simbol": "Hs", "nomor_atom": 108, "massa_atom": 269, "titik_didih": None, "titik_leleh": None},
            "Meitnerium": {"simbol": "Mt", "nomor_atom": 109, "massa_atom": 278, "titik_didih": None, "titik_leleh": None},
            "Darmstadtium": {"simbol": "Ds", "nomor_atom": 110, "massa_atom": 281, "titik_didih": None, "titik_leleh": None},
            "Roentgenium": {"simbol": "Rg", "nomor_atom": 111, "massa_atom": 282, "titik_didih": None, "titik_leleh": None},
            "Kopernisium": {"simbol": "Cn", "nomor_atom": 112, "massa_atom": 285, "titik_didih": None, "titik_leleh": None},
            "Nihonium": {"simbol": "Nh", "nomor_atom": 113, "massa_atom": 286, "titik_didih": None, "titik_leleh": None},
            "Flerovium": {"simbol": "Fl", "nomor_atom": 114, "massa_atom": 289, "titik_didih": None, "titik_leleh": None},
            "Moskovium": {"simbol": "Mc", "nomor_atom": 115, "massa_atom": 290, "titik_didih": None, "titik_leleh": None},
            "Livermorium": {"simbol": "Lv", "nomor_atom": 116, "massa_atom": 293, "titik_didih": None, "titik_leleh": None},
            "Tennessine": {"simbol": "Ts", "nomor_atom": 117, "massa_atom": 294, "titik_didih": None, "titik_leleh": None},
            "Oganesson": {"simbol": "Og", "nomor_atom": 118, "massa_atom": 294, "titik_didih": None, "titik_leleh": None}
        }

        nomor_atom = unsur_kimia[atom]["nomor_atom"]
        golongan = "golongan"

        if nomor_atom in [1, 3, 11, 19, 37, 55, 87]:
            golongan = "golongan1a"
        elif nomor_atom in [4, 12, 20, 38, 56, 88]:
            golongan = "golongan2a"
        elif nomor_atom in [5, 13, 31, 49, 81, 113]:
            golongan = "golongan3a"
        elif nomor_atom in [6, 14, 32, 50, 82, 114]:
            golongan = "golongan4a"
        elif nomor_atom in [7, 15, 33, 51, 83, 115]:
            golongan = "golongan5a"
        elif nomor_atom in [8, 16, 34, 52, 84, 116]:
            golongan = "golongan6a"
        elif nomor_atom in [9, 17, 35, 53, 85, 117]:
            golongan = "golongan7a"
        elif nomor_atom in [2, 10, 18, 36, 54, 86, 118]:
            golongan = "golongan8a"
        elif nomor_atom in [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]:
            golongan = "lantanida"
        elif nomor_atom in [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]:
            golongan = "aktinida"
        else: golongan = "logamtransisi"

        if atom:
            try:
                if atom not in unsur_kimia:
                    raise KeyError(f"Element {atom} not found in database")
                
                data = {
                    "simbol": unsur_kimia[atom]["simbol"],
                    "nomor_atom": unsur_kimia[atom]["nomor_atom"],
                    "massa_atom": unsur_kimia[atom]["massa_atom"],
                    "titik_didih": unsur_kimia[atom]["titik_didih"],
                    "titik_leleh": unsur_kimia[atom]["titik_leleh"]
                }

                file_exists = os.path.exists("data3.csv") and os.path.getsize("data3.csv") > 0

                with open('data3.csv', mode='a', newline='') as file:
                    fieldnames = ["simbol", "nomor_atom", "massa_atom", "titik_didih", "titik_leleh"]
                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(data)

                self.load_csv()
                messagebox.showinfo("Info", "Data berhasil disimpan ke CSV!")
            except KeyError as e:
                messagebox.showerror("Error", f"Data untuk unsur {atom} tidak ditemukan")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyimpan CSV: {e}")
        else:
            messagebox.showwarning("Error", "Unsur harus diisi!")\
            
        self.tampil_gambar(golongan)

root = tb.Window(themename="superhero")
myChem(root)
root.mainloop()