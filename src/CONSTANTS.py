from src import Party, Prefecture


#Parties
PARTY_LDP = Party("Liberal Democratic Party", 1955, "Conservative")
PARTY_CDPJ = Party("Constitutional Democratic Party of Japan", 2017, "Liberal")
PARTY_KOMEITO = Party("Komeito", 1964, "Centrist")
PARTY_CP = Party("Communist Party", 1922, "Left-wing")

PARTIES = [PARTY_LDP, PARTY_CDPJ, PARTY_KOMEITO, PARTY_CP]

#Prefectures
HOKKAIDO = Prefecture("Hokkaido")
AOMORI = Prefecture("Aomori")
IWATE = Prefecture("Iwate")
MIYAGI = Prefecture("Miyagi")
AKITA = Prefecture("Akita")
YAMAGATA = Prefecture("Yamagata")
FUKUSHIMA = Prefecture("Fukushima")
IBARAKI = Prefecture("Ibaraki")
TOCHIGI = Prefecture("Tochigi")
GUNMA = Prefecture("Gunma")
SAITAMA = Prefecture("Saitama")
CHIBA = Prefecture("Chiba")
TOKYO = Prefecture("Tokyo")
KANAGAWA = Prefecture("Kanagawa")
NIIGATA = Prefecture("Niigata")
TOYAMA = Prefecture("Toyama")
ISHIKAWA = Prefecture("Ishikawa")
FUKUI = Prefecture("Fukui")
YAMANASHI = Prefecture("Yamanashi")
NAGANO = Prefecture("Nagano")
GIFU = Prefecture("Gifu")
SHIZUOKA = Prefecture("Shizuoka")
AICHI = Prefecture("Aichi")
MIE = Prefecture("Mie")
SHIGA = Prefecture("Shiga")
KYOTO = Prefecture("Kyoto")
OSAKA = Prefecture("Osaka")
HYOGO = Prefecture("Hyogo")
NARA = Prefecture("Nara")
WAKAYAMA = Prefecture("Wakayama")
TOTTORI = Prefecture("Tottori")
SHIMANE = Prefecture("Shimane")
OKAYAMA = Prefecture("Okayama")
HIROSHIMA = Prefecture("Hiroshima")
YAMAGUCHI = Prefecture("Yamaguchi")
TOKUSHIMA = Prefecture("Tokushima")
KAGAWA = Prefecture("Kagawa")
EHIME = Prefecture("Ehime")
KOCHI = Prefecture("Kochi")
FUKUOKA = Prefecture("Fukuoka")
SAGA = Prefecture("Saga")
NAGASAKI = Prefecture("Nagasaki")
KUMAMOTO = Prefecture("Kumamoto")
OITA = Prefecture("Oita")
MIYAZAKI = Prefecture("Miyazaki")
KAGOSHIMA = Prefecture("Kagoshima")
OKINAWA = Prefecture("Okinawa")

PREFECTURES = [
    HOKKAIDO, AOMORI, IWATE, MIYAGI, AKITA, YAMAGATA, FUKUSHIMA, 
    IBARAKI, TOCHIGI, GUNMA, SAITAMA, CHIBA, TOKYO, KANAGAWA, 
    NIIGATA, TOYAMA, ISHIKAWA, FUKUI, YAMANASHI, NAGANO, GIFU, 
    SHIZUOKA, AICHI, MIE, SHIGA, KYOTO, OSAKA, HYOGO, NARA, 
    WAKAYAMA, TOTTORI, SHIMANE, OKAYAMA, HIROSHIMA, YAMAGUCHI, 
    TOKUSHIMA, KAGAWA, EHIME, KOCHI, FUKUOKA, SAGA, NAGASAKI, 
    KUMAMOTO, OITA, MIYAZAKI, KAGOSHIMA, OKINAWA
]

print(len(PREFECTURES))
