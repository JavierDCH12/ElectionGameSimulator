from src.party import Party
from src.prefecture import Prefecture
from src.actions import Action


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
    "Constitutional Democratic Party of Japan": 25,
    "Komeito": 25,
    "Japanese Communist Party": 20
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
    "Incumbent": 1,
    "New Candidate": 0.8,
    
}

#Random Events#####################################################################################################
EVENTS = [
    ("Positive Media Coverage", 10),
    ("Minor Gaffe", -5),
    ("Small Corruption Scandal", -10),
    ("Successful Small Rally", 10),
    ("Internal Party Disagreement", -5),
    ("Controversial Statement During Diet Session", -10),
    ("Positive Coverage in the Newspapers", 5),
    ("Minor Scandal Involving Staff Member", -5),
    ("Endorsement by Influential Industry Group", 20),
    ("Public Criticism from Former Party Leader", -5),
    ("Positive Reception in Social Media", 5)
]
SPECIAL_EVENTS = [
    ("Major Positive Media Coverage", 20),
    ("Major Sex Scandal", -25),
    ("Major Corruption Scandal", -20),
    ("Major Gaffe", -20),
    ("Severe Economic Crisis", -30),
    ("Massively Successful Rally", 20),
    ("Severe Internal Party Conflict", -15),
    ("Prime Minister Endorsement", 25),
    ("Sudden Health Issue", -10)
]


#Strategies#####################################################################################################

STRATEGIES= ["aggressive campaign", "neutral campaign", "defensive campaign"]

#Actions#####################################################################################################



# Acciones posibles que el jugador puede tomar
ACTION_KOENKAI = Action(
    name="Set up support groups (Koenkai)",
    cost={"financial": 20, "influence": 10},
    benefit=40,
    description="Mobilize support by establishing grassroots volunteer groups in each prefecture."
)

ACTION_TV_PRESENCE = Action(
    name="Increase your presence in traditional media",
    cost={"financial": 15, "influence": 5},
    benefit=30,
    description="Boost your presence and popularity through a series of Tv appareances."
)

ACTION_HOST_RALLY = Action(
    name="Host a Rally",
    cost={"financial": 25, "influence": 15},
    benefit=40,
    description="Host a large rally in a major city to energize your supporters and gain media attention."
)

ACTION_POLICY_ANNOUNCEMENT = Action(
    name="Announce New Policy",
    cost={"financial": 10, "influence": 20},
    benefit=35,
    description="Introduce a new policy proposal to attract undecided voters and sway public opinion."
)

ACTION_INTERNAL_MEETING = Action(
    name="Hold Internal Party Meeting",
    cost={"financial": 5, "influence": 10},
    benefit=25,
    description="Strengthen internal support by discussing strategy and uniting party members."
)

# Lista de todas las acciones disponibles
ACTIONS = [
    ACTION_KOENKAI,
    ACTION_TV_PRESENCE,
    ACTION_HOST_RALLY,
    ACTION_POLICY_ANNOUNCEMENT,
    ACTION_INTERNAL_MEETING,
]
