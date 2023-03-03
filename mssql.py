import pymssql
from openpyxl import load_workbook

conn = pymssql.connect(server='localhost', port=1433, user='admin', password='just4Taqtile', database='your_database')

conn.execute('''
    IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Skany') AND type in (N'U'))
    CREATE TABLE Skany (
        Indeks INTEGER,
        Archiwum INTEGER,
        Data TEXT,
        Del INTEGER,
        KodKreskowy TEXT,
        Oscieznica INTEGER,
        Pozycja INTEGER,
        Skrzydlo INTEGER,
        srcdoc INTEGER,
        Stanowisko INTEGER,
        Sztuka INTEGER,
        Uzytkownik INTEGER,
        Zakonczony INTEGER,
        Czynnosc INTEGER,
        DbWHOkna INTEGER,
        Guid TEXT,
        GuidParent TEXT,
        Status INTEGER,
        Typ INTEGER,
        TypSlupka INTEGER,
        ErrIdx INTEGER
    )
''')

conn.execute('''
    IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Zlecenia') AND type in (N'U'))
    CREATE TABLE Zlecenia (
        Indeks INTEGER,
        Archiwum INTEGER,
        Data TEXT,
        DataWejscia TEXT,
        DataZakonczenia TEXT,
        Del INTEGER,
        Diler TEXT,
        FirstStanowisko INTEGER,
        Hiden INTEGER,
        ErrIdx INTEGER,
        Klient TEXT,
        LiczbaSzklen INTEGER,
        NipDilera TEXT,
        Oscieznica INTEGER,
        Pozycja INTEGER,
        Skanowanie INTEGER,
        Skrzydlo INTEGER,
        srcdoc INTEGER,
        Stanowisko INTEGER,
        StanowiskoPoprzednie INTEGER,
        Sztuka INTEGER,
        TerminRealizacji TEXT,
        Zakonczone INTEGER,
        Zlecenie TEXT,
        ZlecenieDilera INTEGER,
        DodOpis TEXT,
        optym INTEGER,
        TerminProdukcji TEXT,
        Optymalizacja TEXT,
        DbWHOkna INTEGER,
        KodBiura TEXT,
        OptSrcdoc INTEGER,
        Vip INTEGER,
        ObrazekOsc TEXT,
        ObrazekSkr TEXT,
        Referencja TEXT,
        Priorytet INTEGER,
        IloscJedn FLOAT,
        Idx_typu INTEGER,
        Typ TEXT,
        IloscJednPoz FLOAT,
        PozycjaLp INTEGER,
        Country TEXT,
        FrameWidth INTEGER,
        FrameHeight INTEGER,
        SashWidth INTEGER,
        SashHeight INTEGER,
        Glazing TEXT,
        GlazingFrame TEXT,
        GlazingFrameColor TEXT,
        Color TEXT,
        Paczka TEXT
    )
''')

conn.execute('''
    IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Skany_vs_Zlecenia') AND type in (N'U'))
    CREATE TABLE Skany_vs_Zlecenia (
    Indeks INTEGER,
    IndeksSkanu INTEGER,
    IndeksZlecenia INTEGER,
    IndeksDodatka TEXT,
    Duplicated INTEGER
    )
''')


conn.execute('''
    IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Stanowiska') AND type in (N'U'))
    CREATE TABLE Stanowiska (
    Indeks INTEGER,
    Aktywny INTEGER,
    Data TEXT,
    Del INTEGER,
    DrukujRaport TEXT,
    LiczbaPorzadkowa INTEGER,
    LiniaProdukcyjna INTEGER,
    ObslugaStojakow INTEGER,
    Opis TEXT,
    OpisCzynnosci TEXT,
    PodstatusPrzed TEXT,
    PodstatusPo TEXT,
    Raport TEXT,
    RaportDodatki TEXT,
    RozwinTabelke INTEGER,
    Skanowanie INTEGER,
    StanowiskoKoncowe INTEGER,
    WielkoscCzcionki INTEGER,
    Zdejmowanie INTEGER,
    Zliczanie INTEGER,
    Zoom1 INTEGER,
    Zoom2 INTEGER,
    ProceduraSkladowa INTEGER,
    Viewer TEXT,
    CzynnoscOsc INTEGER,
    CzynnoscSkr INTEGER,
    CzynnoscSlr INTEGER,
    CzynnoscSls INTEGER,
    CzynnoscSzkl INTEGER,
    ObslugaTransportu INTEGER,
    BarcodeIdx INTEGER,
    BarcodePrevIdx INTEGER,
    BarcodeNextIdx INTEGER,
    CursorTimeout INTEGER,
    DefaultEvent INTEGER,
    TableFilter INTEGER,
    PanelInfoWidth INTEGER,
    Printer TEXT,
    RaportStojaki TEXT,
    ZoomStands INTEGER,
    Middle INTEGER,
    Middle_type INTEGER,
    ObslugaSektorow INTEGER,
    UserDescription TEXT,
    UserStatus TEXT,
    CanHaveDifferentIP TEXT,
    QualityControlWorkplace TEXT,
    AlTEXTrasWorkplace INTEGER,
    AllowGlassScan INTEGER,
    OnlyOneWorkerOnThisWorkplace INTEGER,
    AlTEXTrasDateColumnName TEXT,
    HideLaborButton INTEGER,
    ImportPackagesToSzybyXLS INTEGER,
    HideTableInPackagesLoading INTEGER,
    AltCuttingWorkplace INTEGER,
    Mobile INTEGER,
    markwhentransportispacked INTEGER
    )
''')



conn.execute('''
    IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'dbo.Uzytkownicy') AND type in (N'U'))
    CREATE TABLE Uzytkownicy (
    Indeks INTEGER,
    Aktywny INTEGER,
    Data TEXT,
    Dealer TEXT,
    Del INTEGER,
    Haslo TEXT,
    Imie TEXT,
    Login TEXT,
    Nazwa TEXT,
    Nazwisko TEXT,
    Nip TEXT,
    Uprawnienia INTEGER,
    Usr INTEGER,
    Uwagi TEXT,
    StawkaDzienna INTEGER,
    BarcodeIdx INTEGER,
    Language TEXT,
    GrupaPlacowa INTEGER,
    TworzenieArtykulow INTEGER,
    Email TEXT,
    ZestawienieZlecenNaProdukcjiVisible INTEGER,
    ZawartoscStojakowVisible INTEGER,
    ZawartoscSamochodowVisible INTEGER,
    ZawartoscSektorowVisible INTEGER,
    ZawartoscSektorowSzkleniaVisible INTEGER,
    ZestawienieCzynnosciVisible INTEGER,
    ZestawienieOdpowiedziNaPytaniaVisible INTEGER,
    ZestawienieRobociznyVisible INTEGER,
    ZestawienieBledowKomunikatowNotatekVisible INTEGER,
    EksportWykonanychOscieznicVisible INTEGER,
    PostepRealizacjiVisible	INTEGER,
    DodajPracownikaVisible INTEGER,
    CofnijSkanVisible INTEGER,
    ZestawienieCzynnosciNewVisible INTEGER,
    VisibilityLastDateChange TEXT,
    Image TEXT
    )
''')
wb = load_workbook(filename='file/skany.xlsx', read_only=True)
ws = wb.active

sheet_names = wb.sheetnames
worksheets = [wb[sheet_name] for sheet_name in sheet_names]

for worksheet in worksheets:
    for row in worksheet.rows:
        Indeks = row[0].value
        Archiwum = row[1].value
        Data = row[2].value
        Del = row[3].value
        KodKreskowy = row[4].value
        Oscieznica = row[5].value
        Pozycja = row[6].value
        Skrzydlo = row[7].value
        srcdoc = row[8].value
        Stanowisko = row[9].value
        Sztuka = row[10].value
        Uzytkownik = row[11].value
        Zakonczony = row[12].value
        Czynnosc = row[13].value
        DbWHOkna = row[14].value
        Guid = row[15].value
        GuidParent = row[16].value
        Status = row[17].value
        Typ = row[18].value
        TypSlupka = row[19].value
        ErrIdx = row[20].value

        # print(Indeks, Archiwum, Data, Del, KodKreskowy, Oscieznica, Pozycja, Skrzydlo, srcdoc, Stanowisko, Sztuka, Uzytkownik, Zakonczony, Czynnosc, DbWHOkna, Guid, GuidParent, Status, Typ, TypSlupka, ErrIdx)
        conn.execute("INSERT INTO Skany(Indeks, Archiwum, Data, Del, KodKreskowy, Oscieznica, Pozycja, Skrzydlo, srcdoc, Stanowisko, Sztuka, Uzytkownik, Zakonczony, Czynnosc, DbWHOkna, Guid, GuidParent, Status, Typ, TypSlupka, ErrIdx) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Indeks, Archiwum, Data, Del, KodKreskowy, Oscieznica, Pozycja, Skrzydlo, srcdoc, Stanowisko, Sztuka, Uzytkownik, Zakonczony, Czynnosc, DbWHOkna, Guid, GuidParent, Status, Typ, TypSlupka, ErrIdx))

wbz = load_workbook(filename='file/Zlecenia.xlsx', read_only=True)
wsz = wbz.active
for row in wsz.rows:
    Indeks = row[0].value
    Archiwum = row[1].value
    Data = row[2].value
    DataWejscia = row[3].value
    DataZakonczenia = row[4].value
    Del = row[5].value
    Diler = row[6].value
    FirstStanowisko = row[7].value
    Hiden = row[8].value
    ErrIdx = row[9].value
    Klient = row[10].value
    LiczbaSzklen = row[11].value
    NipDilera = row[12].value
    Oscieznica = row[13].value
    Pozycja = row[14].value
    Skanowanie = row[15].value
    Skrzydlo = row[16].value
    srcdoc = row[17].value
    Stanowisko = row[18].value
    StanowiskoPoprzednie = row[19].value
    Sztuka = row[20].value
    TerminRealizacji = row[21].value
    Zakonczone = row[22].value
    Zlecenie = row[23].value
    ZlecenieDilera = row[24].value
    DodOpis = row[25].value
    optym = row[26].value
    TerminProdukcji = row[27].value
    Optymalizacja = row[28].value
    DbWHOkna = row[29].value
    KodBiura = row[30].value
    OptSrcdoc = row[31].value
    Vip = row[32].value
    ObrazekOsc = row[33].value
    ObrazekSkr = row[34].value
    Referencja = row[35].value
    Priorytet = row[36].value
    IloscJedn = row[37].value
    Idx_typu = row[38].value
    Typ = row[39].value
    IloscJednPoz = row[40].value
    PozycjaLp = row[41].value
    Country = row[42].value
    FrameWidth = row[43].value
    FrameHeight = row[44].value
    SashWidth = row[45].value
    SashHeight = row[46].value
    Glazing = row[47].value
    GlazingFrame = row[48].value
    GlazingFrameColor = row[49].value
    Color = row[50].value
    Paczka = row[51].value

    conn.execute(
        "INSERT INTO Zlecenia (Indeks, Archiwum, Data, DataWejscia, DataZakonczenia, Del, Diler, FirstStanowisko, Hiden, ErrIdx, Klient, LiczbaSzklen, NipDilera, Oscieznica, Pozycja, Skanowanie, Skrzydlo, srcdoc, Stanowisko, StanowiskoPoprzednie, Sztuka, TerminRealizacji, Zakonczone, Zlecenie, ZlecenieDilera, DodOpis, optym, TerminProdukcji, Optymalizacja, DbWHOkna, KodBiura, OptSrcdoc, Vip, ObrazekOsc, ObrazekSkr, Referencja, Priorytet, IloscJedn, Idx_typu, Typ, IloscJednPoz, PozycjaLp, Country, FrameWidth, FrameHeight, SashWidth, SashHeight, Glazing, GlazingFrame, GlazingFrameColor, Color, Paczka) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
        (Indeks, Archiwum, Data, DataWejscia, DataZakonczenia, Del, Diler, FirstStanowisko, Hiden, ErrIdx, Klient,
         LiczbaSzklen, NipDilera, Oscieznica, Pozycja, Skanowanie, Skrzydlo, srcdoc, Stanowisko,
         StanowiskoPoprzednie, Sztuka, TerminRealizacji, Zakonczone, Zlecenie, ZlecenieDilera, DodOpis, optym,
         TerminProdukcji, Optymalizacja, DbWHOkna, KodBiura, OptSrcdoc, Vip, ObrazekOsc, ObrazekSkr, Referencja,
         Priorytet, IloscJedn, Idx_typu, Typ, IloscJednPoz, PozycjaLp, Country, FrameWidth, FrameHeight, SashWidth,
         SashHeight, Glazing, GlazingFrame, GlazingFrameColor, Color, Paczka))


wbzvz = load_workbook(filename='file/Skany_vs_Zlecenia.xlsx', read_only=True)
wszvz = wbzvz.active
for row in wszvz.rows:
    Indeks = row[0].value
    IndeksSkanu = row[1].value
    IndeksZlecenia = row[2].value
    IndeksDodatka = row[3].value
    Duplicated = row[4].value
    # print(Indeks, IndeksSkanu, IndeksZlecenia, IndeksDodatka, Duplicated)
    conn.execute(
        "INSERT INTO Skany_vs_Zlecenia(Indeks, IndeksSkanu, IndeksZlecenia, IndeksDodatka, Duplicated) VALUES (?, ?, ?, ?, ?)",
        (Indeks, IndeksSkanu, IndeksZlecenia, IndeksDodatka, Duplicated))

wbzvzs = load_workbook(filename='file/Stanowiska.xlsx', read_only=True)
wszvzs = wbzvzs.active
for row in wszvzs.rows:
    Indeks = row[0].value
    Aktywny = row[1].value
    Data = row[2].value
    Del = row[3].value
    DrukujRaport = row[4].value
    LiczbaPorzadkowa = row[5].value
    LiniaProdukcyjna = row[6].value
    ObslugaStojakow = row[7].value
    Opis = row[8].value
    OpisCzynnosci = row[9].value
    PodstatusPrzed = row[10].value
    PodstatusPo = row[11].value
    Raport = row[12].value
    RaportDodatki = row[13].value
    RozwinTabelke = row[14].value
    Skanowanie = row[15].value
    StanowiskoKoncowe = row[16].value
    WielkoscCzcionki = row[17].value
    Zdejmowanie = row[18].value
    Zliczanie = row[19].value
    Zoom1 = row[20].value
    Zoom2 = row[21].value
    ProceduraSkladowa = row[22].value
    Viewer = row[23].value
    CzynnoscOsc = row[24].value
    CzynnoscSkr = row[25].value
    CzynnoscSlr = row[26].value
    CzynnoscSls = row[27].value
    CzynnoscSzkl = row[28].value
    ObslugaTransportu = row[29].value
    BarcodeIdx = row[30].value
    BarcodePrevIdx = row[31].value
    BarcodeNextIdx = row[32].value
    CursorTimeout = row[33].value
    DefaultEvent = row[34].value
    TableFilter = row[35].value
    PanelInfoWidth = row[36].value
    Printer = row[37].value
    RaportStojaki = row[38].value
    ZoomStands = row[39].value
    Middle = row[40].value
    Middle_type = row[41].value
    ObslugaSektorow = row[42].value
    UserDescription = row[43].value
    UserStatus = row[44].value
    CanHaveDifferentIP = row[45].value
    QualityControlWorkplace = row[46].value
    AlTEXTrasWorkplace = row[47].value
    AllowGlassScan = row[48].value
    OnlyOneWorkerOnThisWorkplace = row[49].value
    AlTEXTrasDateColumnName = row[50].value
    HideLaborButton = row[51].value
    ImportPackagesToSzybyXLS = row[52].value
    HideTableInPackagesLoading = row[53].value
    Mobile = row[54].value
    AltCuttingWorkplace = row[55].value
    markwhentransportispacked = row[56].value
    # print(Indeks, Aktywny, Data, Del, DrukujRaport, LiczbaPorzadkowa, LiniaProdukcyjna, ObslugaStojakow, Opis, OpisCzynnosci, PodstatusPrzed, PodstatusPo, Raport, RaportDodatki, RozwinTabelke, Skanowanie, StanowiskoKoncowe, WielkoscCzcionki, Zdejmowanie, Zliczanie, Zoom1, Zoom2, ProceduraSkladowa, Viewer, CzynnoscOsc, CzynnoscSkr, CzynnoscSlr, CzynnoscSls, CzynnoscSzkl, ObslugaTransportu, BarcodeIdx, BarcodePrevIdx, BarcodeNextIdx, CursorTimeout, DefaultEvent, TableFilter, PanelInfoWidth, Printer, RaportStojaki, ZoomStands, Middle, Middle_type, ObslugaSektorow, UserDescription, UserStatus, CanHaveDifferentIP, QualityControlWorkplace, AlTEXTrasWorkplace, AllowGlassScan, OnlyOneWorkerOnThisWorkplace, AlTEXTrasDateColumnName, HideLaborButton, ImportPackagesToSzybyXLS, HideTableInPackagesLoading, Mobile, AltCuttingWorkplace, markwhentransportispacked)
    conn.execute(
        "INSERT INTO Stanowiska(Indeks, Aktywny, Data, Del, DrukujRaport, LiczbaPorzadkowa, LiniaProdukcyjna, ObslugaStojakow, Opis, OpisCzynnosci, PodstatusPrzed, PodstatusPo, Raport, RaportDodatki, RozwinTabelke, Skanowanie, StanowiskoKoncowe, WielkoscCzcionki, Zdejmowanie, Zliczanie, Zoom1, Zoom2, ProceduraSkladowa, Viewer, CzynnoscOsc, CzynnoscSkr, CzynnoscSlr, CzynnoscSls, CzynnoscSzkl, ObslugaTransportu, BarcodeIdx, BarcodePrevIdx, BarcodeNextIdx, CursorTimeout, DefaultEvent, TableFilter, PanelInfoWidth, Printer, RaportStojaki, ZoomStands, Middle, Middle_type, ObslugaSektorow, UserDescription, UserStatus, CanHaveDifferentIP, QualityControlWorkplace, AlTEXTrasWorkplace, AllowGlassScan, OnlyOneWorkerOnThisWorkplace, AlTEXTrasDateColumnName, HideLaborButton, ImportPackagesToSzybyXLS, HideTableInPackagesLoading, Mobile, AltCuttingWorkplace, markwhentransportispacked) VALUES (?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?)",
        (Indeks, Aktywny, Data, Del, DrukujRaport, LiczbaPorzadkowa, LiniaProdukcyjna, ObslugaStojakow, Opis, OpisCzynnosci, PodstatusPrzed, PodstatusPo, Raport, RaportDodatki, RozwinTabelke, Skanowanie, StanowiskoKoncowe, WielkoscCzcionki, Zdejmowanie, Zliczanie, Zoom1, Zoom2, ProceduraSkladowa, Viewer, CzynnoscOsc, CzynnoscSkr, CzynnoscSlr, CzynnoscSls, CzynnoscSzkl, ObslugaTransportu, BarcodeIdx, BarcodePrevIdx, BarcodeNextIdx, CursorTimeout, DefaultEvent, TableFilter, PanelInfoWidth, Printer, RaportStojaki, ZoomStands, Middle, Middle_type, ObslugaSektorow, UserDescription, UserStatus, CanHaveDifferentIP, QualityControlWorkplace, AlTEXTrasWorkplace, AllowGlassScan, OnlyOneWorkerOnThisWorkplace, AlTEXTrasDateColumnName, HideLaborButton, ImportPackagesToSzybyXLS, HideTableInPackagesLoading, Mobile, AltCuttingWorkplace, markwhentransportispacked))

#
wbzvzuz = load_workbook(filename='file/Uzytkownicy.xlsx', read_only=True)
wszvzu = wbzvzuz.worksheets[0]
for row in wszvzu.rows:
    if len(row) == 36:
        Indeks = row[0].value
        Aktywny = row[1].value
        Data = row[2].value
        Dealer = row[3].value
        Del = row[4].value
        Haslo = row[5].value
        Imie = row[6].value
        Login = row[7].value
        Nazwa = row[8].value
        Nazwisko = row[9].value
        Nip = row[10].value
        Uprawnienia = row[11].value
        Usr = row[12].value
        Uwagi = row[13].value
        StawkaDzienna = row[14].value
        BarcodeIdx = row[15].value
        Language = row[16].value
        GrupaPlacowa = row[17].value
        TworzenieArtykulow = row[18].value
        Email = row[19].value
        ZestawienieZlecenNaProdukcjiVisible = row[20].value
        ZawartoscStojakowVisible = row[21].value
        ZawartoscSamochodowVisible = row[22].value
        ZawartoscSektorowVisible = row[23].value
        ZawartoscSektorowSzkleniaVisible = row[24].value
        ZestawienieCzynnosciVisible = row[25].value
        ZestawienieOdpowiedziNaPytaniaVisible = row[26].value
        ZestawienieRobociznyVisible = row[27].value
        ZestawienieBledowKomunikatowNotatekVisible = row[28].value
        EksportWykonanychOscieznicVisible = row[29].value
        PostepRealizacjiVisible = row[30].value
        DodajPracownikaVisible = row[31].value
        CofnijSkanVisible = row[32].value
        ZestawienieCzynnosciNewVisible = row[33].value
        VisibilityLastDateChange = row[34].value
        Image = row[35].value
        # print(Indeks, Aktywny, Data, Dealer, Del, Haslo, Imie, Login, Nazwa, Nazwisko, Nip, Uprawnienia, Usr, Uwagi, StawkaDzienna, BarcodeIdx, Language, GrupaPlacowa, TworzenieArtykulow, Email, ZestawienieZlecenNaProdukcjiVisible, ZawartoscStojakowVisible, ZawartoscSamochodowVisible, ZawartoscSektorowVisible, ZawartoscSektorowSzkleniaVisible, ZestawienieCzynnosciVisible, ZestawienieOdpowiedziNaPytaniaVisible, ZestawienieRobociznyVisible, ZestawienieBledowKomunikatowNotatekVisible, EksportWykonanychOscieznicVisible, PostepRealizacjiVisible, DodajPracownikaVisible, CofnijSkanVisible, ZestawienieCzynnosciNewVisible, VisibilityLastDateChange, Image)
        conn.execute(
                "INSERT INTO Uzytkownicy(Indeks, Aktywny, Data, Dealer, Del, Haslo, Imie, Login, Nazwa, Nazwisko, Nip, Uprawnienia, Usr, Uwagi, StawkaDzienna, BarcodeIdx, Language, GrupaPlacowa, TworzenieArtykulow, Email, ZestawienieZlecenNaProdukcjiVisible, ZawartoscStojakowVisible, ZawartoscSamochodowVisible, ZawartoscSektorowVisible, ZawartoscSektorowSzkleniaVisible, ZestawienieCzynnosciVisible, ZestawienieOdpowiedziNaPytaniaVisible, ZestawienieRobociznyVisible, ZestawienieBledowKomunikatowNotatekVisible, EksportWykonanychOscieznicVisible, PostepRealizacjiVisible, DodajPracownikaVisible, CofnijSkanVisible, ZestawienieCzynnosciNewVisible, VisibilityLastDateChange, Image) VALUES (?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?)",
                (Indeks, Aktywny, Data, Dealer, Del, Haslo, Imie, Login, Nazwa, Nazwisko, Nip, Uprawnienia, Usr, Uwagi, StawkaDzienna, BarcodeIdx, Language, GrupaPlacowa, TworzenieArtykulow, Email, ZestawienieZlecenNaProdukcjiVisible, ZawartoscStojakowVisible, ZawartoscSamochodowVisible, ZawartoscSektorowVisible, ZawartoscSektorowSzkleniaVisible, ZestawienieCzynnosciVisible, ZestawienieOdpowiedziNaPytaniaVisible, ZestawienieRobociznyVisible, ZestawienieBledowKomunikatowNotatekVisible, EksportWykonanychOscieznicVisible, PostepRealizacjiVisible, DodajPracownikaVisible, CofnijSkanVisible, ZestawienieCzynnosciNewVisible, VisibilityLastDateChange, Image))


conn.commit()
