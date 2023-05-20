create table Uzytkownicy
(
    Indeks                                     int not null
        primary key,
    Aktywny                                    int,
    Data                                       datetime,
    Dealer                                     varchar(250),
    Del                                        int,
    Haslo                                      varchar(250),
    Imie                                       varchar(250),
    Login                                      varchar(250),
    Nazwa                                      varchar(250),
    Nazwisko                                   varchar(250),
    Nip                                        varchar(250),
    Uprawnienia                                int,
    Usr                                        int,
    Uwagi                                      varchar(250),
    StawkaDzienna                              int,
    BarcodeIdx                                 int,
    Language                                   varchar(250),
    GrupaPlacowa                               int,
    TworzenieArtykulow                         int,
    Email                                      varchar(250),
    ZestawienieZlecenNaProdukcjiVisible        int,
    ZawartoscStojakowVisible                   int,
    ZawartoscSamochodowVisible                 int,
    ZawartoscSektorowVisible                   int,
    ZawartoscSektorowSzkleniaVisible           int,
    ZestawienieCzynnosciVisible                int,
    ZestawienieOdpowiedziNaPytaniaVisible      int,
    ZestawienieRobociznyVisible                int,
    ZestawienieBledowKomunikatowNotatekVisible int,
    EksportWykonanychOscieznicVisible          int,
    PostepRealizacjiVisible                    int,
    DodajPracownikaVisible                     int,
    CofnijSkanVisible                          int,
    ZestawienieCzynnosciNewVisible             int,
    VisibilityLastDateChange                   datetime,
    Image                                      varchar(250)
)
go
