print(r"""
------------------
rano    | koko   |
rani    | jojo   |
ranto   | nima   |
joko    | teko   |
heno    | meme   |
moro    | roro   |
------------------
""")

data1="rano"
data2="koko"
data3="rani"
data4="jojo"
data5="ranto"
data6="nima"
data7="joko"
data8="teko"
data9="heno"
data0="meme"
data11="moro"
data87="roro" 

alldata = data1 + data2 + data3 + data4 + data5 + data6 + data7 + data8 + data9 + data0 + data11 + data87

user = str(input("masukan nama "))

kondisi = user in alldata
print(kondisi)
