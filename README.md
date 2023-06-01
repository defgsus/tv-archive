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

**96** channels, **246,116.4** hours playtime between **2023-01-17** and **2023-06-02**


### playtime per genre (top 30)

    16467.7h 6.69% Nachrichten
    11889.2h 4.83% Verkaufsshow
    9893.5h  4.02% Krimiserie
    8172.8h  3.32% Werbesendung
    8023.1h  3.26% Dokureihe
    7349.9h  2.99% Dokusoap
    7055.5h  2.87% Regionalmagazin
    6307.1h  2.56% Dokumentation
    6102.1h  2.48% *unknown*
    4621.4h  1.88% Zeichentrickserie
    4506.9h  1.83% Infomercial
    4401.9h  1.79% Animationsserie
    4110.0h  1.67% Comedyserie
    3409.5h  1.39% Morgenmagazin
    3235.1h  1.31% Talkshow
    3220.8h  1.31% Religionsmagazin
    3209.9h  1.30% Programmende
    2841.8h  1.15% Magazin
    2458.2h  1.00% E-Sport
    2307.6h  0.94% Sitcom
    2244.9h  0.91% Börsenmagazin
    2242.9h  0.91% Wetterbericht
    1936.9h  0.79% Wirtschaftsmagazin
    1909.0h  0.78% Wissensmagazin
    1906.4h  0.77% Quiz
    1906.3h  0.77% Musikmagazin
    1779.3h  0.72% Komödie
    1741.8h  0.71% Telenovela
    1700.6h  0.69% Sportmagazin
    1629.2h  0.66% Gesundheitsmagazin
