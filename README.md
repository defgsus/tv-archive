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

**97** channels, **477,119.7** hours playtime between **2023-01-17** and **2023-10-09**


### playtime per genre (top 30)

    31405.3h 6.58% Nachrichten
    22730.9h 4.76% Verkaufsshow
    19205.9h 4.03% Krimiserie
    16114.1h 3.38% Werbesendung
    15746.3h 3.30% Dokureihe
    14587.2h 3.06% Dokusoap
    13704.6h 2.87% Regionalmagazin
    12041.7h 2.52% Dokumentation
    11401.2h 2.39% *unknown*
    8958.3h  1.88% Zeichentrickserie
    8692.4h  1.82% Infomercial
    8482.5h  1.78% Animationsserie
    7638.6h  1.60% Comedyserie
    6718.5h  1.41% Morgenmagazin
    6408.4h  1.34% Religionsmagazin
    6343.6h  1.33% Talkshow
    5941.8h  1.25% Magazin
    4987.7h  1.05% Programmende
    4713.5h  0.99% E-Sport
    4518.0h  0.95% Sitcom
    4456.1h  0.93% Wetterbericht
    4299.9h  0.90% Börsenmagazin
    3983.0h  0.83% Quiz
    3730.3h  0.78% Komödie
    3652.5h  0.77% Musikmagazin
    3590.2h  0.75% Wirtschaftsmagazin
    3587.7h  0.75% Wissensmagazin
    3379.5h  0.71% Telenovela
    3208.9h  0.67% Politikmagazin
    3104.8h  0.65% Reportagereihe
