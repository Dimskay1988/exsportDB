create table Skany_vs_Zlecenia
(
    Indeks         int not null
        primary key,
    IndeksSkanu    int,
    IndeksZlecenia int,
    IndeksDodatka  varchar(250),
    Duplicated     int
)
go

