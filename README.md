# Archive of TV-shows

Scraped directly from a german webpage, started at about mid-January 2023.

TV is not as important anymore but still, archiving the decisions of which programs to run at what time
becomes another puzzle piece in the revelation of mind-control.. 

Data is stored in [docs/data/YEAR/MONTH/YEAR-MONTH-DAY.ndjson](docs/data/) files. 
Each entry looks like this:

```python
{
  "id": "181043890", 
  "url": "https://www.hoerzu.de/tv-programm/south-park-kohle-an-den-chefkoch/bid_181043890/", 
  "channel": "Comedy Central", 
  "title": "South Park", 
  "date": "2023-01-17T05:15:00",    # probably Europe/Berlin timezone 
  "length": 25,                     # minutes 
  "sub_title": "Serie", 
  "genre": "Erwachsenen-Animationsserie", 
  "season": 2, 
  "episode": 14, 
  "year": 1998, 
  "countries": ["USA"],
}
```

## Statistics

**96** channels, **373,390.1** hours playtime between **2023-01-17** and **2023-08-12**


### playtime per genre (top 30)

    24756.3h 6.63% Nachrichten
    17698.7h 4.74% Verkaufsshow
    15096.2h 4.04% Krimiserie
    12570.4h 3.37% Werbesendung
    12286.1h 3.29% Dokureihe
    11306.9h 3.03% Dokusoap
    10739.4h 2.88% Regionalmagazin
    9378.3h  2.51% Dokumentation
    9070.2h  2.43% *unknown*
    7059.8h  1.89% Zeichentrickserie
    6823.5h  1.83% Infomercial
    6603.0h  1.77% Animationsserie
    6131.3h  1.64% Comedyserie
    5263.7h  1.41% Morgenmagazin
    4955.4h  1.33% Religionsmagazin
    4919.9h  1.32% Talkshow
    4536.0h  1.21% Magazin
    4187.8h  1.12% Programmende
    3693.4h  0.99% E-Sport
    3516.6h  0.94% Wetterbericht
    3511.2h  0.94% Sitcom
    3388.7h  0.91% Börsenmagazin
    3002.2h  0.80% Quiz
    2938.9h  0.79% Musikmagazin
    2870.6h  0.77% Wirtschaftsmagazin
    2858.7h  0.77% Komödie
    2808.7h  0.75% Wissensmagazin
    2602.2h  0.70% Telenovela
    2422.3h  0.65% Sportmagazin
    2416.3h  0.65% Reportagereihe
