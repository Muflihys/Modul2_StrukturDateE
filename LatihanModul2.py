# membuat objek list Hewan
Hewan = ["Sapi", "Kelinci", "Kambing", "Unta", "Domba"]

# membuat objek list DeleteHewan
DeleteHewan = ["Kelinci", "Kambing", "Unta"]

# menampilkan data awal pada kedua objek list
print("Data pada objek list Hewan:", Hewan)
print("Data pada objek list DeleteHewan:", DeleteHewan)

# menghapus data yang sama dari kedua objek list
for hewan in DeleteHewan:
  if hewan in Hewan:
    Hewan.remove(hewan)

# menampilkan data setelah data yang sama dihapus
print("Data pada objek list Hewan setelah data yang sama dihapus:", Hewan)