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

**109** channels, **1,150,135.3** hours playtime between **2023-01-17** and **2024-11-23**


### playtime per genre (top 30)

    75030.3h 6.52% Nachrichten
    52549.1h 4.57% Verkaufsshow
    48004.6h 4.17% Krimiserie
    42343.3h 3.68% Werbesendung
    35865.2h 3.12% Dokureihe
    34287.2h 2.98% Dokusoap
    33671.2h 2.93% Regionalmagazin
    30218.1h 2.63% Dokumentation
    27144.5h 2.36% *unknown*
    21528.5h 1.87% Zeichentrickserie
    21221.9h 1.85% Infomercial
    20549.2h 1.79% Animationsserie
    16475.6h 1.43% Comedyserie
    16103.1h 1.40% Morgenmagazin
    15325.4h 1.33% Religionsmagazin
    15238.4h 1.32% Talkshow
    14361.8h 1.25% Magazin
    11367.7h 0.99% E-Sport
    11133.2h 0.97% Sitcom
    10404.7h 0.90% Wetterbericht
    10169.3h 0.88% Quiz
    10163.2h 0.88% Programmende
    10094.5h 0.88% Komödie
    8825.5h  0.77% Realityshow
    8732.8h  0.76% Politikmagazin
    8642.4h  0.75% Wissensmagazin
    8578.8h  0.75% Börsenmagazin
    7703.4h  0.67% Wirtschaftsmagazin
    7614.5h  0.66% Telenovela
    7573.2h  0.66% Dramaserie
