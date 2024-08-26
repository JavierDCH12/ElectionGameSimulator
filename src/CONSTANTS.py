from src.party import Party
from src.prefecture import Prefecture


#Rounds#####################################################################################################

ROUND_WEEKS=5

#Parties#####################################################################################################
PARTY_LDP = Party("Liberal Democratic Party", 1955, "Conservative")
PARTY_CDPJ = Party("Constitutional Democratic Party of Japan", 2017, "Liberal")
PARTY_KOMEITO = Party("Komeito", 1964, "Centrist")
PARTY_JCP = Party("Japanese Communist Party", 1922, "Left-wing")

PARTIES = [PARTY_LDP, PARTY_CDPJ, PARTY_KOMEITO, PARTY_JCP]

#Prefectures#####################################################################################################
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

#Male Names#####################################################################################################
MALE_NAMES = [
    "Hiroshi Suzuki",
    "Takeshi Takahashi",
    "Yoshio Tanaka",
    "Kenji Watanabe",
    "Kazuo Yamamoto",
    "Shinji Nakamura",
    "Makoto Kobayashi",
    "Akira Saito",
    "Katsuo Kato",
    "Hidetoshi Yoshida"
]

#Female Names#####################################################################################################

FEMALE_NAMES = [
    "Yuki Tanaka",
    "Aiko Suzuki",
    "Hana Sato",
    "Miyuki Nakamura",
    "Emi Watanabe",
    "Rina Yamamoto",
    "Sakura Kobayashi",
    "Yumi Saito",
    "Mika Kato",
    "Akiko Yoshida"
]


#initial Points#####################################################################################################
PARTY_POPULARITY_BONUS = {
    "Liberal Democratic Party": 30,
    "Constitutional Democratic Party of Japan": 20,
    "Komeito": 15,
    "Japanese Communist Party": 10
}

PREFECTURE_BONUS = {
    "Tokyo": 20,
    "Kanagawa": 15,
    "Aichi": 10,
    "Osaka": 15
}

AGE_BONUS = {
    "25-40": 5,
    "40-60": 15,
    "60-80": 10,
    "80+": 5
}

#INITIAL MODIFIER
EXPERIENCE_LEVEL_MODIFIER={
    "Incumbent": 0.5,
    "New Candidate": 0.2,
    
}

#Random Events#####################################################################################################
EVENTS = [
    ("Positive Media Coverage", 10),
    ("Minor Gaffe", -5),
    ("Small Corruption Scandal", -10),
    ("Economic Slowdown", -10),
    ("Successful Small Rally", 10),
    ("Internal Party Disagreement", -5)
]

SPECIAL_EVENTS = [
    ("Major Positive Media Coverage", 20),
    ("Major Sex Scandal", -30),
    ("Major Corruption Scandal", -20),
    ("Major Gaffe", -20),
    ("Severe Economic Crisis", -30),
    ("Massively Successful Rally", 20),
    ("Severe Internal Party Conflict", -15)
]

#Strategies#####################################################################################################

STRATEGIES= ["aggressive campaign", "neutral campaign", "defensive campaign"]

#Actions#####################################################################################################


ACTIONS={
    "Set up Local Support Groups (Koenkai),"
    
}