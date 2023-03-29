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

**96** channels, **130,036.2** hours playtime between **2023-01-17** and **2023-03-30**


### playtime per genre (top 30)

    9121.8h 7.01% Nachrichten
    6496.9h 5.00% Verkaufsshow
    5438.3h 4.18% Krimiserie
    4392.2h 3.38% Werbesendung
    4055.7h 3.12% Dokureihe
    4040.6h 3.11% Dokusoap
    3834.9h 2.95% Regionalmagazin
    3220.6h 2.48% Dokumentation
    2984.0h 2.29% *unknown*
    2468.8h 1.90% Animationsserie
    2394.1h 1.84% Infomercial
    2378.2h 1.83% Zeichentrickserie
    2145.0h 1.65% Comedyserie
    1860.0h 1.43% Morgenmagazin
    1801.6h 1.39% Programmende
    1732.5h 1.33% Talkshow
    1685.2h 1.30% Religionsmagazin
    1365.8h 1.05% Magazin
    1348.2h 1.04% E-Sport
    1248.0h 0.96% Sitcom
    1222.3h 0.94% Börsenmagazin
    1167.7h 0.90% Wetterbericht
    1065.9h 0.82% Wirtschaftsmagazin
    1020.5h 0.78% Wissensmagazin
    995.3h  0.77% Quiz
    980.7h  0.75% Musikmagazin
    936.9h  0.72% Dramaserie
    917.7h  0.71% Telenovela
    900.7h  0.69% Gesundheitsmagazin
    892.4h  0.69% Sportmagazin
