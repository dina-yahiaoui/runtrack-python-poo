import tkinter as tk
from tkinter import messagebox

class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material
    
    def change_material(self, new_material):
        self.material = new_material
    
    def __str__(self):
        return f"{self.name} en {self.material}"

class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {
            "Mât": Part("Mât", "Bois"),
            "Coque": Part("Coque", "Bois"),
            "Voile": Part("Voile", "Coton")
        }
        self.history = []
    
    def display_state(self):
        return "\n".join(str(part) for part in self.__parts.values())
    
    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.history.append(f"Remplacement de {part_name} par {new_part}")
            self.__parts[part_name] = new_part
        else:
            messagebox.showerror("Erreur", "Pièce introuvable !")
    
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.history.append(f"Changement de matériau de {part_name} en {new_material}")
            self.__parts[part_name].change_material(new_material)
        else:
            messagebox.showerror("Erreur", "Pièce introuvable !")
    
    def display_history(self):
        return "\n".join(self.history) if self.history else "Aucune modification enregistrée."

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed
    
    def display_speed(self):
        return f"Vitesse maximale du navire {self.name} : {self.max_speed} nœuds"

def update_display():
    state_label.config(text=ship.display_state())

def change_material():
    part_name = part_entry.get()
    new_material = material_entry.get()
    ship.change_part(part_name, new_material)
    update_display()

def replace_part():
    part_name = part_entry.get()
    new_material = material_entry.get()
    ship.replace_part(part_name, Part(part_name, new_material))
    update_display()

def show_history():
    messagebox.showinfo("Historique", ship.display_history())

ship = Ship("Navire de Thésée")

root = tk.Tk()
root.title("Gestion du Navire de Thésée")

tk.Label(root, text="État du navire :").pack()
state_label = tk.Label(root, text=ship.display_state(), justify="left")
state_label.pack()

tk.Label(root, text="Nom de la pièce :").pack()
part_entry = tk.Entry(root)
part_entry.pack()

tk.Label(root, text="Nouveau matériau :").pack()
material_entry = tk.Entry(root)
material_entry.pack()

tk.Button(root, text="Modifier matériau", command=change_material).pack()
tk.Button(root, text="Remplacer pièce", command=replace_part).pack()
tk.Button(root, text="Afficher historique", command=show_history).pack()
tk.Button(root, text="Quitter", command=root.quit).pack()

root.mainloop()
