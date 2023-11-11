# Blok finally dieksekusi tidak peduli apakah blok try menimbulkan kesalahan atau tidak

try:
  print(x)
except:
  print("Terjadi Kesalahan")
  
finally:
  print("'try except' diselesaikan")
