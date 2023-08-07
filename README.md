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

**96** channels, **366,158.6** hours playtime between **2023-01-17** and **2023-08-08**


### playtime per genre (top 30)

    24231.1h 6.62% Nachrichten
    17421.5h 4.76% Verkaufsshow
    14776.6h 4.04% Krimiserie
    12338.4h 3.37% Werbesendung
    12030.5h 3.29% Dokureihe
    11060.8h 3.02% Dokusoap
    10493.5h 2.87% Regionalmagazin
    9223.3h  2.52% Dokumentation
    8914.2h  2.43% *unknown*
    6926.6h  1.89% Zeichentrickserie
    6693.5h  1.83% Infomercial
    6470.7h  1.77% Animationsserie
    6004.9h  1.64% Comedyserie
    5125.9h  1.40% Morgenmagazin
    4868.7h  1.33% Religionsmagazin
    4829.9h  1.32% Talkshow
    4381.3h  1.20% Magazin
    4130.2h  1.13% Programmende
    3617.8h  0.99% E-Sport
    3443.4h  0.94% Wetterbericht
    3441.9h  0.94% Sitcom
    3310.5h  0.90% Börsenmagazin
    2926.6h  0.80% Quiz
    2879.2h  0.79% Musikmagazin
    2807.5h  0.77% Wirtschaftsmagazin
    2806.0h  0.77% Komödie
    2760.6h  0.75% Wissensmagazin
    2527.0h  0.69% Telenovela
    2380.2h  0.65% Sportmagazin
    2375.7h  0.65% Reportagereihe
