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

**97** channels, **487,864.9** hours playtime between **2023-01-17** and **2023-10-15**


### playtime per genre (top 30)

    32138.8h 6.59% Nachrichten
    23279.4h 4.77% Verkaufsshow
    19640.1h 4.03% Krimiserie
    16489.9h 3.38% Werbesendung
    16053.7h 3.29% Dokureihe
    14907.5h 3.06% Dokusoap
    14054.3h 2.88% Regionalmagazin
    12334.0h 2.53% Dokumentation
    11685.8h 2.40% *unknown*
    9148.5h  1.88% Zeichentrickserie
    8886.6h  1.82% Infomercial
    8691.5h  1.78% Animationsserie
    7798.8h  1.60% Comedyserie
    6896.2h  1.41% Morgenmagazin
    6546.1h  1.34% Religionsmagazin
    6486.9h  1.33% Talkshow
    6090.6h  1.25% Magazin
    5069.8h  1.04% Programmende
    4802.5h  0.98% E-Sport
    4639.9h  0.95% Sitcom
    4548.9h  0.93% Wetterbericht
    4391.2h  0.90% Börsenmagazin
    4097.7h  0.84% Quiz
    3788.6h  0.78% Komödie
    3709.5h  0.76% Musikmagazin
    3679.6h  0.75% Wirtschaftsmagazin
    3672.3h  0.75% Wissensmagazin
    3481.7h  0.71% Telenovela
    3313.8h  0.68% Politikmagazin
    3169.1h  0.65% Reportagereihe
