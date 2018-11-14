from random import shuffle
import tkinter as tk

perk = ["Ace In The Hole",
"Adrenaline",
"Alert",
"Autodidact",
"Balanced Landing",
"Boil Over",
"Bond",
"Borrowed Time",
"Botany Knowledge",
"Calm Spirit",
"Dance With Me",
"Dark Sense",
"Dead Hard",
"Decisive Strike",
"Deliverance",
"Detective's Hunch",
"Diversion",
"Déjà Vu",
"Empathy",
"Hope",
"Iron Will",
"Kindred",
"Leader",
"Left Behind",
"Lightweight",
"Lithe",
"No Mither",
"No One Left Behind",
"Object Of Obsession",
"Open-Handed",
"Pharmacy",
"Plunderer's Instinct",
"Premonition",
"Prove Thyself",
"Quick & Quiet",
"Resilience",
"Saboteur",
"Self-Care",
"Slippery Meat",
"Small Game",
"Sole Survivor",
"Spine Chill",
"Sprint Burst",
"Stake Out",
"Streetwise",
"Technician",
"Tenacity",
"This Is Not Happening",
"Unbreakable",
"Up The Ante",
"Urban Evasion",
"Vigil",
"Wake Up!",
"We'll Make It",
"We're Gonna Live Forever",
"Windows Of Opportunity",
"You Choose"]

def nextfive():
    shuffle(perk)
    output = "1) " + perk[0] + "\n" + "2) " + perk[1] + "\n" + "3) " + perk[2] + "\n" + "4) " + perk[3] + "\n" + "5) " + perk[4]
    label.config(text=output)

root = tk.Tk()
root.title("Perks")
root.geometry("200x85")
label = tk.Label(root, fg="dark green", anchor="w", justify=tk.LEFT)
label.pack(side=tk.LEFT)
nextfive()
button = tk.Button(root, text='Again', height=5, command=lambda: nextfive())
button.pack(side=tk.RIGHT)
root.mainloop()
