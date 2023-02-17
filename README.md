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

**96** channels, **59,232.6** hours playtime between **2023-01-17** and **2023-02-18**


### playtime per genre (top 30)

    4167.1h 7.04% Nachrichten
    3040.2h 5.13% Verkaufsshow
    2532.3h 4.28% Krimiserie
    2033.9h 3.43% Dokusoap
    2001.9h 3.38% Werbesendung
    1738.0h 2.93% Regionalmagazin
    1717.2h 2.90% Dokureihe
    1474.0h 2.49% *unknown*
    1468.7h 2.48% Dokumentation
    1120.4h 1.89% Zeichentrickserie
    1090.7h 1.84% Animationsserie
    1089.3h 1.84% Infomercial
    988.4h  1.67% Comedyserie
    859.2h  1.45% Morgenmagazin
    781.8h  1.32% Programmende
    780.9h  1.32% Talkshow
    763.2h  1.29% Religionsmagazin
    656.6h  1.11% Magazin
    622.8h  1.05% E-Sport
    559.2h  0.94% Sitcom
    530.0h  0.89% Börsenmagazin
    519.0h  0.88% Wetterbericht
    497.7h  0.84% Wirtschaftsmagazin
    462.8h  0.78% Wissensmagazin
    456.1h  0.77% Quiz
    443.5h  0.75% Dramaserie
    435.2h  0.73% Musikmagazin
    420.9h  0.71% Gesundheitsmagazin
    420.7h  0.71% Telenovela
    387.9h  0.65% Gerichtsshow
