create table Skany
(
    Indeks      int not null
        primary key,
    Archiwum    int,
    Data        datetime,
    Del         int,
    KodKreskowy varchar(250),
    Oscieznica  int,
    Pozycja     int,
    Skrzydlo    int,
    srcdoc      int,
    Stanowisko  int,
    Sztuka      int,
    Uzytkownik  int,
    Zakonczony  int,
    Czynnosc    int,
    DbWHOkna    int,
    Guid        varchar(250),
    GuidParent  varchar(250),
    Status      int,
    Typ         int,
    TypSlupka   int,
    ErrIdx      int
)
go

