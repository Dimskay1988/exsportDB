create table Stanowiska
(
    Indeks                       int not null
        primary key,
    Aktywny                      int,
    Data                         datetime,
    Del                          int,
    DrukujRaport                 varchar(250),
    LiczbaPorzadkowa             int,
    LiniaProdukcyjna             int,
    ObslugaStojakow              int,
    Opis                         varchar(250),
    OpisCzynnosci                varchar(250),
    PodstatusPrzed               varchar(250),
    PodstatusPo                  varchar(250),
    Raport                       varchar(250),
    RaportDodatki                varchar(250),
    RozwinTabelke                int,
    Skanowanie                   int,
    StanowiskoKoncowe            int,
    WielkoscCzcionki             int,
    Zdejmowanie                  int,
    Zliczanie                    int,
    Zoom1                        int,
    Zoom2                        int,
    ProceduraSkladowa            int,
    Viewer                       varchar(250),
    CzynnoscOsc                  int,
    CzynnoscSkr                  int,
    CzynnoscSlr                  int,
    CzynnoscSls                  int,
    CzynnoscSzkl                 int,
    ObslugaTransportu            int,
    BarcodeIdx                   int,
    BarcodePrevIdx               int,
    BarcodeNextIdx               int,
    CursorTimeout                int,
    DefaultEvent                 int,
    TableFilter                  int,
    PanelInfoWidth               int,
    Printer                      varchar(250),
    RaportStojaki                varchar(250),
    ZoomStands                   int,
    Middle                       int,
    Middle_type                  int,
    ObslugaSektorow              int,
    UserDescription              varchar(250),
    UserStatus                   varchar(250),
    CanHaveDifferentIP           varchar(250),
    QualityControlWorkplace      varchar(250),
    AlVARCHAR                    varchar(250),
    AlTEXTrasWorkplace           int,
    AllowGlassScan               int,
    OnlyOneWorkerOnThisWorkplace int,
    AlTEXTrasDateColumnName      varchar(250),
    HideLaborButton              int,
    ImportPackagesToSzybyXLS     int,
    HideTableInPackagesLoading   int,
    AltCuttingWorkplace          int,
    Mobile                       int,
    markwhentransportispacked    int
)
go

