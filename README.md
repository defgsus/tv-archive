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

**97** channels, **428,853.2** hours playtime between **2023-01-17** and **2023-09-12**


### playtime per genre (top 30)

    28292.3h 6.60% Nachrichten
    20337.0h 4.74% Verkaufsshow
    17380.0h 4.05% Krimiserie
    14474.3h 3.38% Werbesendung
    14142.0h 3.30% Dokureihe
    13037.8h 3.04% Dokusoap
    12335.6h 2.88% Regionalmagazin
    10822.7h 2.52% Dokumentation
    10212.5h 2.38% *unknown*
    8102.1h  1.89% Zeichentrickserie
    7826.0h  1.82% Infomercial
    7593.2h  1.77% Animationsserie
    6949.1h  1.62% Comedyserie
    6049.5h  1.41% Morgenmagazin
    5742.1h  1.34% Religionsmagazin
    5671.1h  1.32% Talkshow
    5361.4h  1.25% Magazin
    4620.6h  1.08% Programmende
    4245.0h  0.99% E-Sport
    4048.4h  0.94% Wetterbericht
    4025.4h  0.94% Sitcom
    3885.8h  0.91% Börsenmagazin
    3539.5h  0.83% Quiz
    3382.1h  0.79% Musikmagazin
    3328.2h  0.78% Komödie
    3248.6h  0.76% Wirtschaftsmagazin
    3203.4h  0.75% Wissensmagazin
    3014.7h  0.70% Telenovela
    2825.8h  0.66% Reportagereihe
    2785.1h  0.65% Politikmagazin
