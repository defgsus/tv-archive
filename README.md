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

**96** channels, **62,917.0** hours playtime between **2023-01-17** and **2023-02-20**


### playtime per genre (top 30)

    4388.8h 6.98% Nachrichten
    3209.8h 5.10% Verkaufsshow
    2651.5h 4.21% Krimiserie
    2146.1h 3.41% Werbesendung
    2138.3h 3.40% Dokusoap
    1858.2h 2.95% Dokureihe
    1801.2h 2.86% Regionalmagazin
    1565.5h 2.49% *unknown*
    1554.2h 2.47% Dokumentation
    1187.7h 1.89% Zeichentrickserie
    1157.2h 1.84% Infomercial
    1153.2h 1.83% Animationsserie
    1024.7h 1.63% Comedyserie
    872.2h  1.39% Morgenmagazin
    851.2h  1.35% Programmende
    830.6h  1.32% Religionsmagazin
    816.8h  1.30% Talkshow
    685.2h  1.09% Magazin
    650.2h  1.03% E-Sport
    585.6h  0.93% Sitcom
    550.7h  0.88% Wetterbericht
    535.0h  0.85% Börsenmagazin
    516.1h  0.82% Wirtschaftsmagazin
    487.6h  0.77% Wissensmagazin
    469.6h  0.75% Musikmagazin
    467.8h  0.74% Quiz
    445.0h  0.71% Dramaserie
    442.5h  0.70% Gesundheitsmagazin
    424.6h  0.67% Telenovela
    416.1h  0.66% Sportmagazin
