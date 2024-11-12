from .. import Provider as PersonProvider


class Provider(PersonProvider):
    # Source: https://ismlar.com/top100

    formats_female = (
        "{{first_name_female}} {{last_name_female}}",
        "{{last_name_female}} {{first_name_female}}",
    )

    formats_male = (
        "{{first_name_male}} {{last_name_male}}",
        "{{last_name_male}} {{first_name_male}}",
    )

    formats = formats_male + formats_female

    first_names_female = (
        "Sa’diya",
        "Sumayya",
        "Safiya",
        "Yasmina",
        "Hadicha",
        "Samiya",
        "Maryam",
        "Asma",
        "Mursalina",
        "Mubina",
        "Rayyona",
        "Safina",
        "Madina",
        "Oysha",
        "Yasina",
        "Aylin",
        "Musfira",
        "Sabina",
        "Muslima",
        "Osiyo",
        "Soliha",
        "Imona",
        "Farzona",
        "Humayra",
        "Samira",
        "Maftuna",
        "Ifora",
        "Farangiz",
        "Sakina",
        "Robiya",
        "Elif",
        "Bibisora",
        "Omina",
        "Asmira",
        "Marjona",
        "Sabrina",
        "Zahro",
        "Malak",
        "Sevinch",
        "Afruza",
        "Sadia",
        "Jasmina",
        "Mushtariy",
        "Nuriya",
        "Muzayyana",
        "Anisa",
        "Fotima",
        "Diyora",
        "Ruhshona",
        "Mehrimoh",
        "Shahina",
        "Muxlisa",
        "Shukrona",
        "Milana",
        "Dilnur",
        "Iymona",
        "Mohinur",
        "Sarvinoz",
        "Shahnoza",
        "Alzina",
        "Munisa",
        "Charos",
        "Aliya",
        "Odina",
        "Durdona",
        "Malika",
        "E’zoza",
        "Rayhona",
        "Roziya",
        "Samina",
        "Feruza",
        "Asila",
        "Fariza",
        "Muzdalifa",
        "Hadija",
        "Mohlaroyim",
        "Laylo",
        "Rumaysa",
        "Kumush",
        "Nilufar",
        "Saida",
        "Bonu",
        "Zarina",
        "Aziza",
        "Ansora",
        "Muizza",
        "Dilnoz",
        "Amira",
        "Dildora",
        "Ruqiya",
        "Dunyo",
        "Zinnura",
        "Nozima",
        "Zaynab",
        "Muhsina",
        "Habiba",
        "Sevara",
        "Amina",
        "Zakiyaxon",
        "Mumtoz",
    )

    first_names_male = (
        "Zubayr",
        "Mustafo",
        "Muhammad",
        "Umar",
        "Ali",
        "Imron",
        "Muhammadyusuf",
        "Ayub",
        "Abubakr",
        "Muhammadali",
        "Muhammadamin",
        "Usmon",
        "Ibrohim",
        "Bilol",
        "Zayd",
        "Muhammadyasin",
        "Yasin",
        "Aziz",
        "Samir",
        "Firdavs",
        "Abdulloh",
        "Behruz",
        "Shohrux",
        "Amir",
        "Yahyo",
        "Asad",
        "Kamron",
        "Mironshoh",
        "Islom",
        "Halid",
        "Habib",
        "Jamshid",
        "Shahzoda",
        "Akbar",
        "Abduaziz",
        "Sardor",
        "Javohir",
        "Abdurahmon",
        "Ja’far",
        "Muhammadziyo",
        "Muhammadumar",
        "Muhammadayub",
        "Akobir",
        "Jahongir",
        "Yusuf",
        "Diyor",
        "Salohiddin",
        "Farhod",
        "Humoyun",
        "Bobur",
        "Abror",
        "Samandar",
        "Asilbek",
        "Sarvar",
        "Muhammadrizo",
        "Shohjahon",
        "Ahmad",
        "Yunus",
        "Sanjar",
        "Doniyor",
        "Daler",
        "Shahzod",
        "Said",
        "Muhammadsafo",
        "Ismoil",
        "Nurmuhammad",
        "Muhammadamir",
        "Otabek",
        "Ulug‘bek",
        "Miron",
        "Xolid",
        "Dovud",
        "Damir",
        "Abbos",
        "Gabriel",
        "Zakariyo",
        "Abdulhamid",
        "Jalol",
        "Mahmud",
        "Shahriyor",
        "Saddam",
        "Fuzayl",
        "Akmal",
        "Alinur",
        "Hasan",
        "Murod",
        "Isfandiyor",
        "Miran",
        "Temir",
        "Muhammadaziz",
        "Abdumalik",
        "Muhammadsodiq",
        "Muslim",
        "Abduboriy",
        "Laziz",
        "Fariz",
        "Jasur",
        "Muhammadsolih",
        "Mahdi",
        "Anvar",
    )

    first_names = first_names_male + first_names_female

    last_names_female = (
        "Sadiyeva",
        "Sumayyeva",
        "Safiyeva",
        "Yasminova",
        "Hadichayeva",
        "Samiyeva",
        "Maryamova",
        "Asmanova",
        "Mursalinaeva",
        "Mubinova",
        "Rayyonova",
        "Safinayeva",
        "Madinaeva",
        "Oyshayeva",
        "Yasinaeva",
        "Aylinova",
        "Musfirayeva",
        "Sabinova",
        "Muslimaeva",
        "Osiyeva",
        "Solihayeva",
        "Imonova",
        "Farzonova",
        "Humayrova",
        "Samirova",
        "Maftunova",
        "Iforayeva",
        "Farangizova",
        "Sakinayeva",
        "Robiyayeva",
        "Elifova",
        "Bibisorayeva",
        "Ominova",
        "Asmiraeva",
        "Marjonova",
        "Sabrinova",
        "Zahroyeva",
        "Malakova",
        "Sevinchova",
        "Afruzova",
        "Sadiyeva",
        "Jasminova",
        "Mushtariyeva",
        "Nuriyeva",
        "Muzayyanova",
        "Anisayeva",
        "Fotimayeva",
        "Diyorayeva",
        "Ruhshonova",
        "Mehrimohova",
        "Shahinova",
        "Muxlisayeva",
        "Shukronova",
        "Milanova",
        "Dilnurova",
        "Iymonova",
        "Mohinurova",
        "Sarvinozova",
        "Shahnozova",
        "Alzinova",
        "Munisayeva",
        "Charosova",
        "Aliyeva",
        "Odinaeva",
        "Durdonova",
        "Malikova",
        "E’zozova",
        "Rayhonova",
        "Roziyayeva",
        "Saminova",
        "Feruzova",
        "Asilayeva",
        "Farizayeva",
        "Muzdalifayeva",
        "Hadijayeva",
        "Mohlaroyimova",
        "Laylova",
        "Rumaysayeva",
        "Kumushova",
        "Nilufarova",
        "Saidova",
        "Bonueva",
        "Zarinova",
        "Azizova",
        "Ansorova",
        "Muizzova",
        "Dilnozova",
        "Amirayeva",
        "Dildorova",
        "Ruqiyayeva",
        "Dunyoeva",
        "Zinnurova",
        "Nozimova",
        "Zaynabova",
        "Muhsinova",
        "Habibova",
        "Sevarova",
        "Aminova",
        "Zakiyaxonova",
        "Mumtozova",
    )

    last_names_male = (
        "Zubayrov",
        "Mustafayev",
        "Muhammadov",
        "Umarov",
        "Aliyev",
        "Imronov",
        "Muhammadyusupov",
        "Ayubov",
        "Abubakrov",
        "Muhammadaliyev",
        "Muhammadaminov",
        "Usmonov",
        "Ibrohimov",
        "Bilolov",
        "Zayidov",
        "Muhammadyasinov",
        "Yasinov",
        "Azizov",
        "Samirov",
        "Firdavsev",
        "Abdullohov",
        "Behruzov",
        "Shohruxov",
        "Amirov",
        "Yahyoev",
        "Asadov",
        "Kamronov",
        "Mironshohov",
        "Islomov",
        "Halidov",
        "Habibov",
        "Jamshidov",
        "Shahzodov",
        "Akbarov",
        "Abduazizov",
        "Sardorov",
        "Javohirov",
        "Abdurahmonov",
        "Ja’farov",
        "Muhammadziyoev",
        "Muhammadumarov",
        "Muhammadayubov",
        "Akobirov",
        "Jahongirov",
        "Yusupov",
        "Diyorov",
        "Salohiddinov",
        "Farhodov",
        "Humoyunov",
        "Boburov",
        "Abrorov",
        "Samandarov",
        "Asilbekov",
        "Sarvarov",
        "Muhammadrizoyev",
        "Shohjahonov",
        "Ahmadov",
        "Yunusov",
        "Sanjarov",
        "Doniyorov",
        "Dalerov",
        "Shahzodov",
        "Saidov",
        "Muhammadsafoev",
        "Ismoilov",
        "Nurmuhammadov",
        "Muhammadamirov",
        "Otabekov",
        "Ulug‘bekov",
        "Mironov",
        "Xolidov",
        "Dovudov",
        "Damirov",
        "Abbosov",
        "Gabriyelov",
        "Zakariyoev",
        "Abdulhamidov",
        "Jalolov",
        "Mahmudov",
        "Shahriyorov",
        "Saddamov",
        "Fuzaylov",
        "Akmalov",
        "Alinurov",
        "Hasanov",
        "Murodov",
        "Isfandiyorov",
        "Miranov",
        "Temirov",
        "Muhammadazizov",
        "Abdumalikov",
        "Muhammadsodiqov",
        "Muslimov",
        "Abduboriyov",
        "Lazizov",
        "Farizov",
        "Mehrojov",
        "Muhammadsolihov",
        "Mahdiev",
        "Anvarov",
    )

    last_names = last_names_female + last_names_male
