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

**96** channels, **81,095.0** hours playtime between **2023-01-17** and **2023-03-02**


### playtime per genre (top 30)

    5761.0h 7.10% Nachrichten
    4088.8h 5.04% Verkaufsshow
    3440.2h 4.24% Krimiserie
    2753.1h 3.39% Werbesendung
    2670.6h 3.29% Dokusoap
    2414.4h 2.98% Dokureihe
    2399.8h 2.96% Regionalmagazin
    1975.1h 2.44% Dokumentation
    1918.2h 2.37% *unknown*
    1537.3h 1.90% Animationsserie
    1491.0h 1.84% Zeichentrickserie
    1482.6h 1.83% Infomercial
    1326.1h 1.64% Comedyserie
    1163.3h 1.43% Morgenmagazin
    1094.3h 1.35% Programmende
    1063.4h 1.31% Talkshow
    1063.0h 1.31% Religionsmagazin
    865.2h  1.07% Magazin
    845.4h  1.04% E-Sport
    769.2h  0.95% Sitcom
    731.4h  0.90% Börsenmagazin
    715.2h  0.88% Wetterbericht
    659.8h  0.81% Wirtschaftsmagazin
    638.8h  0.79% Wissensmagazin
    610.4h  0.75% Quiz
    592.8h  0.73% Musikmagazin
    589.2h  0.73% Dramaserie
    584.1h  0.72% Gesundheitsmagazin
    561.8h  0.69% Telenovela
    529.0h  0.65% Gerichtsshow
