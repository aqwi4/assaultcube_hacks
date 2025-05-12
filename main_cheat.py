import pymem

try:
	pm = pymem.Pymem("ac_client.exe")
	base_address = pymem.process.module_from_name(pm.process_handle, "ac_client.exe").lpBaseOfDll
	print(f"Base address is: {hex(base_address)}")
	base_offsets = [0x17E254, 0x17E360,0x18AC00]
	final_offset = 0xEC
	for offset in base_offsets:
		pointer = pm.read_int(base_address + offset)
		if pointer:
			hp_adress = pointer + final_offset
			value = pm.read_int(hp_adress)
			if value > 0:
				print(f"We found hp by address {hex(hp_adress)}")
except Exception as e:
	print(f"Error {e}")
