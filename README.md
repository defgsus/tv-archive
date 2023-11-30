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

**97** channels, **572,228.3** hours playtime between **2023-01-17** and **2023-12-01**


### playtime per genre (top 30)

    37662.9h 6.58% Nachrichten
    27415.5h 4.79% Verkaufsshow
    23118.3h 4.04% Krimiserie
    19432.4h 3.40% Werbesendung
    18623.7h 3.25% Dokureihe
    17277.7h 3.02% Dokusoap
    16579.5h 2.90% Regionalmagazin
    14587.8h 2.55% Dokumentation
    13955.9h 2.44% *unknown*
    10580.4h 1.85% Zeichentrickserie
    10426.1h 1.82% Infomercial
    10179.3h 1.78% Animationsserie
    8899.7h  1.56% Comedyserie
    8164.9h  1.43% Morgenmagazin
    7722.9h  1.35% Religionsmagazin
    7654.8h  1.34% Talkshow
    7323.7h  1.28% Magazin
    5719.9h  1.00% Programmende
    5600.6h  0.98% E-Sport
    5516.1h  0.96% Sitcom
    5245.3h  0.92% Wetterbericht
    5191.4h  0.91% Börsenmagazin
    4770.3h  0.83% Quiz
    4413.8h  0.77% Komödie
    4356.9h  0.76% Wissensmagazin
    4296.4h  0.75% Wirtschaftsmagazin
    4183.6h  0.73% Musikmagazin
    4160.8h  0.73% Telenovela
    4058.0h  0.71% Politikmagazin
    4055.0h  0.71% Realityshow
