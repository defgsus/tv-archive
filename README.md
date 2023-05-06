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

**96** channels, **199,405.3** hours playtime between **2023-01-17** and **2023-05-07**


### playtime per genre (top 30)

    13481.8h 6.76% Nachrichten
    9755.6h  4.89% Verkaufsshow
    8140.1h  4.08% Krimiserie
    6640.0h  3.33% Werbesendung
    6431.5h  3.23% Dokureihe
    5920.9h  2.97% Dokusoap
    5738.5h  2.88% Regionalmagazin
    5068.8h  2.54% Dokumentation
    4860.4h  2.44% *unknown*
    3699.7h  1.86% Zeichentrickserie
    3652.6h  1.83% Infomercial
    3624.1h  1.82% Animationsserie
    3313.4h  1.66% Comedyserie
    2756.4h  1.38% Programmende
    2755.4h  1.38% Morgenmagazin
    2615.2h  1.31% Talkshow
    2600.4h  1.30% Religionsmagazin
    2226.9h  1.12% Magazin
    2006.1h  1.01% E-Sport
    1888.5h  0.95% Sitcom
    1802.4h  0.90% Wetterbericht
    1800.4h  0.90% Börsenmagazin
    1577.5h  0.79% Wirtschaftsmagazin
    1557.7h  0.78% Wissensmagazin
    1535.0h  0.77% Musikmagazin
    1525.5h  0.77% Quiz
    1406.8h  0.71% Telenovela
    1387.6h  0.70% Sportmagazin
    1377.4h  0.69% Gesundheitsmagazin
    1368.8h  0.69% Komödie
