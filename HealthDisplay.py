import pymem
import pymem.process
import tkinter as tk

font_size = 16
process_name = 'javaw.exe'
health_address = 0x20BB5899C  # Replace with the actual memory address for health
health_absorption_address = 0x21025D014  # Replace with the actual memory address for combined health

def get_health_values():
    pm = pymem.Pymem(process_name)
    health_value = pm.read_int(health_address)
    health_absorption_value = pm.read_int(health_absorption_address)
    absorption_hearts = health_absorption_value - health_value
    return health_value, absorption_hearts

def update_health_label():
    health_value, absorption_hearts = get_health_values()
    health_label.config(text=f'Health: {health_value}', font=('Helvetica', font_size))
    absorption_label.config(text=f'Absorption Hearts: {absorption_hearts}', font=('Helvetica', font_size))
    root.after(250, update_health_label)

# Create a simple GUI window
root = tk.Tk()
root.title('Minecraft Health Monitor')

health_label = tk.Label(root, text='Health: ', font=('Helvetica', font_size))
health_label.pack()

absorption_label = tk.Label(root, text='Absorption Hearts: ', font=('Helvetica', font_size))
absorption_label.pack()

update_health_label()

root.mainloop()