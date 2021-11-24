def fart_etter(h): # Høyde på pendel(?) svinging
    return (2*9.81*h)**0.5    
def fart_før(h, a, b): # Høyde på pendel(?) svingning, vekt på prosjektil, vekt på pendel(?)
    return ((2*9.81*h)**0.5)*(a+b)/a

INPUT = str(input("Høyde på pendel(?) svingning, vekt på prosjektil, vekt på pendel(?)"))
args = INPUT.split(", ")
h = float(args[0])
a = float(args[1])
b = float(args[2])
før = fart_før(h, a, b)
etter = fart_etter(h)
print(f"Før (prosjektil): {før}\nEtter (greie): {etter}")