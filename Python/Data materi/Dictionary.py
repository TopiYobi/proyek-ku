# Dictionary merupakan kumpulan data yang menggunakan kunci untuk memanggil nya
# data yang di panggil bisa berupa bool,str,int,bahkan list

data_list = ["as",23,"asr",9,"ucp"]
data_d = {
    'key': 'Value' , 
    'As': 'Amerika', 
    'Ank': 12345, 
    'data_list': data_list
}
print(data_d)
# Memanggil salah satu data
print(data_d['As'])
print(data_d['data_list'])