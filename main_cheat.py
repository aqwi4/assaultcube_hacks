import pymem
try:
	pm = pymem.Pymem("ac_client.exe")
	healthpoints_address = 0x007E4A5C
	ammo_address = 0x007E4AB0
	i_health = int(input())
	i_ammo = int(input())
	pm.write_int(healthpoints_address, i_health)
	pm.write_int(ammo_address, i_ammo)
	print("Values changed!")
except Exception as e:
	print(f"Ошибка {e}")
