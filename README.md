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

**96** channels, **42,835.6** hours playtime between **2023-01-17** and **2023-02-09**


### playtime per genre (top 30)

    3000.3h 7.00% Nachrichten
    2224.6h 5.19% Verkaufsshow
    1822.7h 4.26% Krimiserie
    1487.8h 3.47% Dokusoap
    1458.1h 3.40% Werbesendung
    1307.5h 3.05% Dokureihe
    1249.0h 2.92% Regionalmagazin
    1075.4h 2.51% Dokumentation
    1059.7h 2.47% *unknown*
    826.9h  1.93% Zeichentrickserie
    798.9h  1.87% Infomercial
    768.6h  1.79% Animationsserie
    734.0h  1.71% Comedyserie
    606.7h  1.42% Morgenmagazin
    563.5h  1.32% Religionsmagazin
    556.8h  1.30% Talkshow
    550.9h  1.29% Programmende
    487.2h  1.14% Magazin
    452.9h  1.06% E-Sport
    401.1h  0.94% Sitcom
    371.2h  0.87% Börsenmagazin
    368.5h  0.86% Wetterbericht
    361.4h  0.84% Wirtschaftsmagazin
    345.0h  0.81% Wissensmagazin
    336.0h  0.78% Quiz
    319.3h  0.75% Dramaserie
    317.8h  0.74% Musikmagazin
    311.3h  0.73% Gesundheitsmagazin
    302.2h  0.71% Telenovela
    282.2h  0.66% Gerichtsshow
