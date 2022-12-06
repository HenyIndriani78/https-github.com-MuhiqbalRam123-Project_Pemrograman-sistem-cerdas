graf = {'Brebes' : ['Tegal','Slawi'],
        'Tegal' : ['Pemalang','Slawi'],
        'Slawi' : ['Tegal','Purwokerto'],
        'Purwokerto' : ['Purbalingga','Cilacap','Kroya','Kebumen'],
        'Cilacap' : ['Purwokerto','Kroya'],
        'Kroya' : ['Cilacap','Purwokerto','Kebumen'],
        'Kebumen' : ['Kroya','Purwokerto'],
        'Purworejo' : ['Kebumen','Magelang'],
        'Magelang' : ['Purworejo','Wonosobo','Temanggung','Boyolali'],
        'Purbalingga' : ['Banjarnegara','Purwokerto','Pemalang'],
        'Banjarnegara' : ['Purbalingga','Wonosobo'],
        'Pemalang' : ['Tegal','Pekalongan'],
        'Wonosobo' : ['Banjarnegara','Temanggung','Magelang'],
        'Temanggung' : ['Salatiga','Wonosobo','Magelang'],
        'Pekalongan' : ['Pemalang','Kendal'],
        'Kendal' : ['Pekalongan','Semarang','Temanggung'],
        'Boyolali' : ['Klaten','Salatiga','Solo'],
        'Salatiga' : ['Temanggung','Semarang','Boyolali'],
        'Semarang' : ['Kendal','Demak','Salatiga'],
        'Klaten' : ['Boyolali'],
        'Solo' : ['Boyolali','Purwodadi','Sragen','Sukoharjo'],
        'Purwodadi' : ['Demak','Kudus','Blora','Solo'],
        'Demak' : ['Semarang','Purwodadi','Kudus','Solo'],
        'Kudus' : ['Demak','Rembang','Purwodadi'],
        'Rembang' : ['Kudus','Blora'],
        'Blora' : ['Rembang','Purwodadi','Sragen'],
        'Sragen' : ['Blora', 'Solo'],
        'Sukoharjo' : ['Wonogiri', 'Solo'],
        'Wonogiri' : ['Sukoharjo']}

def cari_jalan(graf,awal,akhir,jalur=[]):
    jalur = jalur + [awal]
    if awal == akhir :
       return [jalur]
    if not awal in graf:
       return []
    semua_jalur = []
    for titik in graf[awal]:
        if titik not in jalur:
            jalur_jalur = cari_jalan(graf,titik,akhir,jalur)
            for jalur_baru in jalur_jalur:
                semua_jalur.append(jalur_baru)
    return semua_jalur


start = input("Masukkan Kota Awal : ")
Finish = input("Masukkan Kota Tujuan : ")

data_x = cari_jalan(graf,start,Finish)
print(f"Jumlah Rute : {len(data_x)}")
min = data_x[0]
max = []
for x in data_x :
    if len(x) < len(min):
        min = x
    if len(x) > len(max):
        max = x

print(f"Daftar Rute yang dapat dilewati : ")

for x in range(0, len(data_x)):
    print(f"RUTE {x+1} : ")
    print((data_x[x]))


