class Staff:
    def __init__(self, name, surname, lastname, position, number, email, reception):
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.position = position
        self.number = number
        self.email = email
        self.reception = reception

    def get_fullname(self):
        return f"{self.name} {self.surname} {self.lastname}"

    def get_position(self):
        return f"{self.position}"

    def get_number(self):
        return f"{self.number}"

    def get_email(self):
        return f"{self.email}"

    def get_reception(self):
        return f"{self.reception}"


Rector_uz = Staff("USMONOV", "BOTIR", "SHUKURILLAYEVICH", "Rektor", "(71) 244-79-20", "txti_rektor@edu.uz", "Har kuni: 16:00-18:00")
Prorector_uquv_uz = Staff("SAFAROV", "TOYIR", "TURSUNOVICH", "Prorektor", "(71) 244-79-18", "uquv_prorektor@tcti.uz", "Har kuni: 15:00-18:00")
Prorector_ilmiy_uz = Staff("PULATOV", "XAYRULLA", "LUTPULLAYEVICH", "Prorektor", "(71) 244-79-21", "ilmiy_prorektor@tcti.uz", "Har kuni: 16:00-18:00")
Prorector_yoshlar_uz = Staff("SHERMUHAMMADOV", "BAHODIR", "SHERMUHAMMADOVICH", "Prorektor", "(71) 244-79-24", "yoshlar_prorektor@tcti.uz", "Seshanba va juma: 15:00-18:00")
Ishlar_uz = Staff("SAMANDAROV", "XAMIDULLA", "SAYDULLAYEVICH", "Ishlar boshqarmasi boshlig‘i", "(71) 244-79-15", "ishlar_bosh@tcti.uz", "Dushanba, chorshanba va juma: 09:00-18:00")
oomtf_dekani_uz = Staff("BALTABAYEV", "ULUG‘BEK", "NARBAYEVICH", "Dekan", "(71) 244-92-35", "oomtf@tcti.uz  ulug85bek77@gmail.com", "Seshanba va payshanba: 16:00-17:00")
yobktf_dekani_uz = Staff("ABDULLAYEV", "ALISHER", "SHONAZAROVICH", "Dekan", "(71) 244-19-72", "yoobktf@tcti.uz  alishon73@uks.uz", "Har kuni: 14:00-16:00")
nmktf_dekani_uz = Staff("SAFAROV", "YODGORJON", "TOYIROVICH", "Dekan", "(97) 344-72-30", "nmktf@tcti.uz  yodi.18@mail.ru", "Payshanba va shanba: 14:00-16:00")
mktf_dekani_uz = Staff("VAPAYEV", "MURODJON", "DUSUMMATOVICH", "Dekan", "(99) 841-20-17", "mktf@tcti.uz", "hozircha mavjud emas")
vtsuf_dekani_uz = Staff("XO‘JAMSHUKUROV", "NORTOJI", "ABDIXOLIQOVICH", "Dekan", "(93) 578-15-03", "vtsuf@tcti.uz", "hozirda mavjud emas")
Devonxona_uz = Staff("AXMEDOVA", "FOTIMA", "BAXTIYAROVNA", "Bo‘lim mudiri", "(71) 244-79-04", "devonxona@tcti.uz", "hozirda mavjud emas")
Monitoring_uz = Staff("KADIROV", "ULUG‘BEK", "RAVSHANOVICH", "Bo‘lim boshlig‘i", "(71) 244-79-23", "nazorat@tcti.uz  tkti.nazorat@mail.ru", "hozirda mavjud emas")
Marketing_uz = Staff("XUSAYNOV", "SHUXRAT", "ABDIMITALOVICH", "Bo‘lim boshlig‘i", "(71) 244-79-27", "market@tcti.uz  marketingtkti@gmail.com", "hozirda mavjud emas")
Buxgalteriya_uz = Staff("MIRSAIDOVA", "GULCHEXRA", "SABIROVNA", "Bosh hisobchi", "(71) 244-78-53", "hozirda mavjud emas", "hozirda mavjud emas")
Xalqaro_uz = Staff("BABAXANOVA", "ZEBO", "ABDULLAYEVNA", "Bo‘lim boshlig‘i", "(93) 527-95-00", "xab@tcti.uz  tkti_xab@mail.ru", "hozirda mavjud emas")
Talimsifat_uz = Staff("TO‘RAYEV", "TOLIB", "BOZOROVICH", "Bo‘lim boshlig‘i", "(71) 244-35-72", "talim_sifat@tcti.uz  t_tolibbek@mail.ru", "hozirda mavjud emas")
Oquv_uz = Staff("XABIBULLAYEV", "RASHID", "AZAMATOVICH", "Bo‘lim boshlig‘i", "(71) 244-79-34", "uub@tcti.uz", "hozirda mavjud emas")
Kadrlar_uz = Staff("LUTFULLAYEV", "SHERZOD", "SHUXRATILLAYEVICH", "Bo‘lim boshlig‘i", "(71) 244-79-31", "kadrlar@tcti.uz", "hozirda mavjud emas")
Manaviyat_uz = Staff("OPAYEV", "ASAN", "AYMANOVICH", "Bo‘lim boshlig‘i", "(71) 244-79-24", "hozirda mavjud emas", "hozirda mavjud emas")
Magistratura_uz = Staff("XAMRAQULOV", "G‘OFURJON", "XOLYIGITOVICH", "Bo‘lim boshlig‘i", "hozirda mavjud emas", "magistratura@tcti.uz", "hozirda mavjud emas")
Sirtqi_uz = Staff("BUXOROV", "SHUXRAT", "BURIYEVICH", "Bo‘lim boshlig‘i", "(71) 244-79-34", "sirtqi@tcti.uz", "hozirda mavjud emas")
ATM_uz = Staff("KASIMOV", "BEXZOD", "ALISHEROVICH", "Markaz boshlig‘i", "(71) 244-79-32", "atm@tcti.uz", "hozirda mavjud emas")
ARM_uz = Staff("ONAROVA", "RAYXONA", "AZZAMJON QIZI", "Markaz boshlig‘i", "hozirda mavjud emas", "arm@tcti.uz", "hozirda mavjud emas")
PKQT_uz = Staff("MIRZAQULOV", "XOLTURA", "CHORIYEVICH", "Markaz boshlig‘i", "(71) 244-79-28", "tkti.tm@mail.ru", "hozirda mavjud emas")
Filial_sh_uz = Staff("MUTALOV", "SHUXRAT", "AXMADJONOVICH", "Filial direktori", "(75) 522-50-68", "tkti_shf@edu.uz", "Har kuni: 08:00-10:00")
Filial_y_uz = Staff("XAKIMOV", "ZAFAR", "TULYAGANOVICH", "Filial direktori", "(95) 510-58-56", "tktiyaf@tcti.uz", "hozirda mavjud emas")
Union_uz = Staff("ERNAZAROV", "DAVRONBEK", "JAVLON O‘G‘LI", "Institut Boshlang‘ich Tashkiloti yetakchisi", "(93) 528-76-93", "@Ernazarov18", "hozirda mavjud emas")
Moliya_uz = Staff("UMAROV", "KAMOL", "DAVRONBEKOVICH", "Bo‘lim boshlig‘i", "hozirda mavjud emas", "reja_moliya@tcti.uz", "hozirda mavjud emas")


Rector_ru = Staff("УСМОНОВ", "БОТИР", "ШУКУРИЛЛАЕВИЧ", "Ректор", "(71) 244-79-20", "txti_rektor@edu.uz", "Каждый день: 16:00-18:00")
Prorector_uquv_ru = Staff("САФАРОВ", "ТОЙИР", "ТУРСУНОВИЧ", "Проректор", "(71) 244-79-18", "uquv_prorektor@tcti.uz", "Каждый день: 15:00-18:00")
Prorector_ilmiy_ru = Staff("ПУЛАТОВ", "ХАЙРУЛЛА", "ЛУТПУЛЛАЕВИЧ", "Проректор", "(71) 244-79-21", "ilmiy_prorektor@tcti.uz", "Каждый день: 16:00-18:00")
Prorector_yoshlar_ru = Staff("ШЕРМУХАММАДОВ", "БАХОДИР", "ШЕРМУХАММАДОВИЧ", "Проректор", "(71) 244-79-24", "yoshlar_prorektor@tcti.uz", "Вторник и пятница: 15:00-18:00")
Ishlar_ru = Staff("САМАНДАРОВ", "ХАМИДУЛЛА", "САЙДУЛЛАЕВИЧ", "Начальник штаба", "(71) 244-79-15", "ishlar_bosh@tcti.uz", "Понедельник, среда и пятница: 09:00-18:00")
oomtf_dekani_ru = Staff("БАЛТАБАЕВ", "УЛУГБЕК", "НАРБАЕВИЧ", "Декан", "(71) 244-92-35", "oomtf@tcti.uz ulug85bek77@gmail.com", "Вторник и четверг: 16:00-17:00")
yobktf_dekani_ru = Staff("АБДУЛЛАЕВ", "АЛИШЕР", "ШОНАЗАРОВИЧ", "Декан", "(71) 244-19-72", "yoobktf@tcti.uz alishon73@uks.uz", "Каждый день: 14:00-16:00")
nmktf_dekani_ru = Staff("САФАРОВ", "ЁДГОРЖОН", "ТОЙИРОВИЧ", "Декан", "(97) 344-72-30", "nmktf@tcti.uz yodi.18@mail.ru", "Четверг и суббота: 14:00-16:00")
mktf_dekani_ru = Staff("ВАПАЕВ", "МУРОДЖОН", "ДУСУММАТОВИЧ", "Декан", "(99) 841-20-17", "mktf@tcti.uz", "в настоящее время недоступен")
vtsuf_dekani_ru = Staff("ХУЖАМШУКУРОВ", "НОРТОЖИ", "АБДИХОЛИКОВИЧ", "Декан", "(93) 578-15-03", "vtsuf@tcti.uz", "в настоящее время недоступен")
Devonxona_ru = Staff("АХМЕДОВА", "ФОТИМА", "БАХТИЯРОВНА", "Начальник отдела", "(71) 244-79-04", "devonxona@tcti.uz", "в настоящее время недоступен")
Monitoring_ru = Staff("КАДИРОВ", "УЛУГБЕК", "РАВШАНОВИЧ", "Начальник отдела", "(71) 244-79-23", "nazorat@tcti.uz , tkti.nazorat@mail.ru", "в настоящее время недоступен")
Marketing_ru = Staff("ХУСАЙНОВ", "ШУХРАТ", "АБДИМИТАЛОВИЧ", "Начальник отдела", "(71) 244-79-27", "market@tcti.uz marketingtkti@gmail.com", "в настоящее время недоступен")
Buxgalteriya_ru = Staff("МИРСАИДОВА", "ГУЛЧЕХРА", "САБИРОВНА", "Главный бухгалтер", "(71) 244-78-53", "в настоящее время недоступен", "в настоящее время недоступен")
Xalqaro_ru = Staff("БАБАХАНОВА", "ЗЕБО", "АБДУЛЛАЕВНА", "Начальник отдела", "(93) 527-95-00", "xab@tcti.uz tkti_xab@mail.ru", "в настоящее время недоступен")
Talimsifat_ru = Staff("ТУРАЕВ", "ТОЛИБ", "БОЗОРОВИЧ", "Начальник отдела", "(71) 244-35-72", "talim_sifat@tcti.uz t_tolibbek@mail.ru", "в настоящее время недоступен")
Oquv_ru = Staff("ХАБИБУЛЛАЕВ", "РАШИД", "АЗАМАТОВИЧ", "Начальник отдела", "(71) 244-79-34", "uub@tcti.uz", "в настоящее время недоступен")
Kadrlar_ru = Staff("ЛУТФУЛЛАЕВ", "ШЕРЗОД", "ШУХРАТИЛЛАЕВИЧ", "Начальник отдела", "(71) 244-79-31", "kadrlar@tcti.uz", "в настоящее время недоступен")
Manaviyat_ru = Staff("ОПАЕВ", "АСАН", "АЙМАНОВИЧ", "Начальник отдела", "(71) 244-79-24", "в настоящее время недоступен", "в настоящее время недоступен")
Magistratura_ru = Staff("ХАМРАКУЛОВ", "ГОФУРЖОН", "ХОЛЙИГИТОВИЧ", "Начальник отдела", "в настоящее время недоступен", "magistratura@tcti.uz", "в настоящее время недоступен")
Sirtqi_ru = Staff("БУХОРОВ", "ШУХРАТ", "БУРИЕВИЧ", "Начальник отдела", "(71) 244-79-34", "sirtqi@tcti.uz", "в настоящее время недоступен")
ATM_ru = Staff("КАСИМОВ", "БЕХЗОД", "АЛИШЕРОВИЧ", "Руководитель центра", "(71) 244-79-32", "atm@tcti.uz", "в настоящее время недоступен")
ARM_ru = Staff("ОНАРОВА", "РАЙХОНА", "АЗЗАМЖОНОВНА", "Руководитель центра", "в настоящее время недоступен", "arm@tcti.uz", "в настоящее время недоступен")
PKQT_ru = Staff("МИРЗАКУЛОВ", "ХОЛТУРА", "ЧОРИЕВИЧ", "Руководитель центра", "(71) 244-79-28", "tkti.tm@mail.ru", "в настоящее время недоступен")
Filial_sh_ru = Staff("МУТАЛОВ", "ШУХРАТ", "АХМАДЖОНОВИЧ", "Директор филиала", "(75) 522-50-68", "tkti_shf@edu.uz", "Каждый день: 08:00-10:00")
Filial_y_ru = Staff("ХАКИМОВ", "ЗАФАР", "ТУЛЯГАНОВИЧ", "Директор филиала", "(95) 510-58-56", "tktiyaf@tcti.uz", "в настоящее время недоступен")
Union_ru = Staff("ЭРНАЗАРОВ", "ДАВРОНБЕК", "ДЖАВЛОНОВИЧ", "Руководитель первичной организации института", "(93) 528-76-93", "@Ernazarov18", "в настоящее время недоступен")
Moliya_ru = Staff("УМАРОВ", "КАМОЛ", "ДАВРОНБЕКОВИЧ", "Начальник отдела", "в настоящее время недоступен", "reja_moliya@tcti.uz", "в настоящее время недоступен")


Rector_en = Staff("USMONOV", "BOTIR", "SHUKURILLAYEVICH", "Rector", "(71) 244-79-20", "txti_rektor@edu.uz", "Every day: 4:00pm-6:00pm")
Prorector_uquv_en = Staff("SAFAROV", "TOYIR", "TURSUNOVICH", "Vice Rector", "(71) 244-79-18", "uquv_prorektor@tcti.uz", "Every day: 3:00pm-6:00pm")
Prorector_ilmiy_en = Staff("PULATOV", "KHAYRULLA", "LUTPULLAYEVICH", "Vice Rector", "(71) 244-79-21", "ilmiy_prorektor@tcti.uz", "Every day: 4:00pm-6:00pm")
Prorector_yoshlar_en = Staff("SHERMUKHAMMADOV", "BAKHODIR", "SHERMUKHAMMADOVICH", "Vice Rector", "(71) 244-79-24", "yoshlar_prorektor@tcti.uz", "Tuesday and Friday: 3:00pm-6:00pm")
Ishlar_en = Staff("SAMANDAROV", "KHAMIDULLA", "SAYDULLAYEVICH", "Chief of Staff", "(71) 244-79-15", "ishlar_bosh@tcti.uz", "Monday, Wednesday and Friday: 9:00am-6:00pm")
oomtf_dekani_en = Staff("BALTABAEV", "ULUGBEK", "NARBAYEVICH", "Dean", "(71) 244-92-35", "oomtf@tcti.uz ulug85bek77@gmail.com", "Tuesday and Thursday: 4:00pm-5:00pm")
yobktf_dekani_en = Staff("ABDULLAEV", "ALISHER", "SHONAZAROVICH", "Dean", "(71) 244-19-72", "yoobktf@tcti.uz alishon73@uks.uz", "Every day: 14:00-16:00")
nmktf_dekani_en = Staff("SAFAROV", "YODGORJON", "TOYIROVICH", "Dean", "(97) 344-72-30", "nmktf@tcti.uz yodi.18@mail.ru", "Thursday and Saturday: 2pm-4pm")
mktf_dekani_en = Staff("VAPAEV", "MURODJON", "DUSUMMATOVICH", "Dean", "(99) 841-20-17", "mktf@tcti.uz", "not currently available")
vtsuf_dekani_en = Staff("XUJAMSHUKUROV", "NORTOJI", "ABDIKHOLIKOVICH", "Dean", "(93) 578-15-03", "vtsuf@tcti.uz", "not currently available")
Devonxona_en = Staff("AKHMEDOVA", "FOTIMA", "BAKHTIYAROVNA", "Head of Department", "(71) 244-79-04", "devonxona@tcti.uz", "not currently available")
Monitoring_en = Staff("KADIROV", "ULUGBEK", "RAVSHANOVICH", "Head of Department", "(71) 244-79-23", "nazorat@tcti.uz , tkti.nazorat@mail.ru", "not currently available")
Marketing_en = Staff("KHUSAYNOV", "SHUKHRAT", "ABDIMITALOVICH", "Head of Department", "(71) 244-79-27", "market@tcti.uz marketingtkti@gmail.com", "not currently available")
Buxgalteriya_en = Staff("MIRSAIDOVA", "GULCHEKHRA", "SABIROVNA", "Chief Accountant", "(71) 244-78-53", "not currently available", "not currently available")
Xalqaro_en = Staff("BABAKHANOVA", "ZEBO", "ABDULLAYEVNA", "Head of Department", "(93) 527-95-00", "xab@tcti.uz tkti_xab@mail.ru", "not currently available")
Talimsifat_en = Staff("TURAEV", "TOLIB", "BOZOROVICH", "Head of Department", "(71) 244-35-72", "talim_sifat@tcti.uz t_tolibbek@mail.ru", "not currently available")
Oquv_en = Staff("KHABIBULLAEV", "RASHID", "AZAMATOVICH", "Head of Department", "(71) 244-79-34", "uub@tcti.uz", "not currently available")
Kadrlar_en = Staff("LUTFULLAEV", "SHERZOD", "SHUKHRATILLAYEVICH", "Head of Department", "(71) 244-79-31", "kadrlar@tcti.uz", "not currently available")
Manaviyat_en = Staff("OPAEV", "ASAN", "AYMANOVICH", "Head of Department", "(71) 244-79-24", "not currently available", "not currently available")
Magistratura_en = Staff("KHAMRAQULOV", "GOFURJON", "KHOLYIGITOVICH", "Head of Department", "not currently available", "magistratura@tcti.uz", "not currently available")
Sirtqi_en = Staff("BUKHOROV", "SHUKHRAT", "BURIYEVICH", "Head of Department", "(71) 244-79-34", "sirtqi@tcti.uz", "not currently available")
ATM_en = Staff("KASIMOV", "BEKHZOD", "ALISHEROVICH", "Head of Center", "(71) 244-79-32", "atm@tcti.uz", "not currently available")
ARM_en = Staff("ONAROVA", "RAYKHONA", "AZZAMJONOVNA", "Head of Center", "not currently available", "arm@tcti.uz", "not currently available")
PKQT_en = Staff("MIRZAKHULOV", "KHOLTURA", "CHORIYEVICH", "Head of Center", "(71) 244-79-28", "tkti.tm@mail.ru", "not currently available")
Filial_sh_en = Staff("MUTALOV", "SHUKHRAT", "AKHMADJONOVICH", "Branch director", "(75) 522-50-68", "tkti_shf@edu.uz", "Every day: 8am-10am")
Filial_y_en = Staff("KHAKIMOV", "ZAFAR", "TULYAGANOVICH", "Branch director", "(95) 510-58-56", "tktiyaf@tcti.uz", "not currently available")
Union_en = Staff("ERNAZAROV", "DAVRONBEK", "JAVLONOVICH", "Head of the primary organization of the institute", "(93) 528-76-93", "@Ernazarov18", "not currently available")
Moliya_en = Staff("UMAROV", "KAMOL", "DAVRONBEKOVICH", "Head of Department", "not currently available", "reja_moliya@tcti.uz", "not currently available")
