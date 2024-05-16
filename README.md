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

**108** channels, **857,982.3** hours playtime between **2023-01-17** and **2024-05-17**


### playtime per genre (top 30)

    56065.4h 6.53% Nachrichten
    40851.6h 4.76% Verkaufsshow
    34965.3h 4.08% Krimiserie
    30037.0h 3.50% Werbesendung
    26995.4h 3.15% Dokureihe
    25911.0h 3.02% Dokusoap
    24991.0h 2.91% Regionalmagazin
    22223.6h 2.59% Dokumentation
    21802.1h 2.54% *unknown*
    15770.5h 1.84% Zeichentrickserie
    15610.0h 1.82% Infomercial
    15280.7h 1.78% Animationsserie
    12944.4h 1.51% Comedyserie
    12193.6h 1.42% Magazin
    12116.1h 1.41% Morgenmagazin
    11597.4h 1.35% Religionsmagazin
    11430.8h 1.33% Talkshow
    8527.4h  0.99% E-Sport
    7937.5h  0.93% Programmende
    7930.5h  0.92% Sitcom
    7627.2h  0.89% Wetterbericht
    7543.1h  0.88% Börsenmagazin
    7429.1h  0.87% Quiz
    7321.4h  0.85% Komödie
    6344.4h  0.74% Wissensmagazin
    6341.8h  0.74% Politikmagazin
    6339.9h  0.74% Realityshow
    6121.5h  0.71% Wirtschaftsmagazin
    6109.1h  0.71% Telenovela
    5685.6h  0.66% Musikmagazin
