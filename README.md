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

**96** channels, **99,297.5** hours playtime between **2023-01-17** and **2023-03-12**


### playtime per genre (top 30)

    6990.6h 7.04% Nachrichten
    5000.8h 5.04% Verkaufsshow
    4168.9h 4.20% Krimiserie
    3365.8h 3.39% Werbesendung
    3211.4h 3.23% Dokusoap
    2993.8h 3.01% Dokureihe
    2921.7h 2.94% Regionalmagazin
    2450.3h 2.47% Dokumentation
    2381.6h 2.40% *unknown*
    1905.1h 1.92% Animationsserie
    1819.9h 1.83% Infomercial
    1787.5h 1.80% Zeichentrickserie
    1608.2h 1.62% Comedyserie
    1411.0h 1.42% Morgenmagazin
    1355.8h 1.37% Programmende
    1303.9h 1.31% Talkshow
    1293.6h 1.30% Religionsmagazin
    1028.8h 1.04% E-Sport
    1025.8h 1.03% Magazin
    950.5h  0.96% Sitcom
    908.2h  0.91% Börsenmagazin
    880.4h  0.89% Wetterbericht
    807.0h  0.81% Wirtschaftsmagazin
    775.0h  0.78% Wissensmagazin
    741.5h  0.75% Quiz
    730.9h  0.74% Musikmagazin
    712.8h  0.72% Dramaserie
    696.4h  0.70% Gesundheitsmagazin
    695.3h  0.70% Telenovela
    641.2h  0.65% Gerichtsshow
