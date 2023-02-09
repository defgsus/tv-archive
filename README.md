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

**96** channels, **44,664.5** hours playtime between **2023-01-17** and **2023-02-10**


### playtime per genre (top 30)

    3145.1h 7.04% Nachrichten
    2314.1h 5.18% Verkaufsshow
    1904.0h 4.26% Krimiserie
    1577.1h 3.53% Dokusoap
    1512.8h 3.39% Werbesendung
    1341.0h 3.00% Dokureihe
    1310.7h 2.93% Regionalmagazin
    1128.3h 2.53% Dokumentation
    1118.0h 2.50% *unknown*
    858.5h  1.92% Zeichentrickserie
    833.2h  1.87% Infomercial
    806.6h  1.81% Animationsserie
    762.3h  1.71% Comedyserie
    640.9h  1.43% Morgenmagazin
    586.2h  1.31% Programmende
    582.5h  1.30% Religionsmagazin
    578.5h  1.30% Talkshow
    517.8h  1.16% Magazin
    468.6h  1.05% E-Sport
    419.3h  0.94% Sitcom
    386.2h  0.86% Wetterbericht
    382.9h  0.86% Börsenmagazin
    380.2h  0.85% Wirtschaftsmagazin
    358.4h  0.80% Wissensmagazin
    351.3h  0.79% Quiz
    336.4h  0.75% Dramaserie
    334.8h  0.75% Musikmagazin
    321.7h  0.72% Gesundheitsmagazin
    321.0h  0.72% Telenovela
    299.0h  0.67% Wirtschaftstalk
