import pymem

try:
	pm = pymem.Pymem("ac_client.exe")
	base_address = pymem.process.module_from_name(pm.process_handle, "ac_client.exe").lpBaseOfDll
	print(f"Base address is: {hex(base_address)}")
	base_offsets_hp = [0x17E254, 0x17E360,0x18AC00]
	final_offset_hp = 0xEC
	base_offsets_ammo = [0x17E0A8, 0x18AC00, 0x195404]
	final_offset_ammo = 0x140
	for offset in base_offsets_hp:
		pointer = pm.read_int(base_address + offset)
		if pointer:
			hp_adress = pointer + final_offset_hp
			value = pm.read_int(hp_adress)
			inputed_hp = int(input("How many hp do you want?: "))
			if value > 0:
				print(f"We found hp by address {hex(hp_adress)}")
				pm.write_int(hp_adress, inputed_hp)
	for offset in base_offsets_ammo:
		pointer = pm.read_int(base_address + offset)
		if pointer:
			ammo_address = pointer + final_offset_ammo
			value = pm.read_int(ammo_address)
			inputed_ammo = int(input("How many ammo do you want?: "))
			if value > 0:
				print(f"We found ammo by address {hex(ammo_address)}")
				pm.write_int(ammo_address, inputed_ammo)
except Exception as e:
	print(f"Error {e}")
