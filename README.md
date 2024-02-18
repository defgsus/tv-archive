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

**99** channels, **712,834.7** hours playtime between **2023-01-17** and **2024-02-19**


### playtime per genre (top 30)

    46392.9h 6.51% Nachrichten
    34215.9h 4.80% Verkaufsshow
    28861.2h 4.05% Krimiserie
    24540.3h 3.44% Werbesendung
    22899.3h 3.21% Dokureihe
    21486.3h 3.01% Dokusoap
    20613.3h 2.89% Regionalmagazin
    18393.1h 2.58% Dokumentation
    18070.5h 2.54% *unknown*
    13222.7h 1.85% Zeichentrickserie
    12958.7h 1.82% Infomercial
    12531.7h 1.76% Animationsserie
    10786.4h 1.51% Comedyserie
    10081.2h 1.41% Morgenmagazin
    9646.3h  1.35% Religionsmagazin
    9531.3h  1.34% Magazin
    9450.5h  1.33% Talkshow
    7034.4h  0.99% E-Sport
    6806.7h  0.95% Programmende
    6766.5h  0.95% Sitcom
    6354.8h  0.89% Börsenmagazin
    6339.5h  0.89% Wetterbericht
    6082.3h  0.85% Komödie
    5940.7h  0.83% Quiz
    5350.5h  0.75% Wissensmagazin
    5222.6h  0.73% Realityshow
    5173.9h  0.73% Wirtschaftsmagazin
    5099.2h  0.72% Politikmagazin
    5068.2h  0.71% Telenovela
    4939.4h  0.69% Musikmagazin
