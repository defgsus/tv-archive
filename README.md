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

**97** channels, **403,905.1** hours playtime between **2023-01-17** and **2023-08-29**


### playtime per genre (top 30)

    26668.5h 6.60% Nachrichten
    19078.8h 4.72% Verkaufsshow
    16388.7h 4.06% Krimiserie
    13615.7h 3.37% Werbesendung
    13362.3h 3.31% Dokureihe
    12252.1h 3.03% Dokusoap
    11582.5h 2.87% Regionalmagazin
    10258.1h 2.54% Dokumentation
    9743.0h  2.41% *unknown*
    7616.9h  1.89% Zeichentrickserie
    7375.4h  1.83% Infomercial
    7137.0h  1.77% Animationsserie
    6569.3h  1.63% Comedyserie
    5682.2h  1.41% Morgenmagazin
    5395.5h  1.34% Religionsmagazin
    5315.3h  1.32% Talkshow
    5030.8h  1.25% Magazin
    4425.7h  1.10% Programmende
    4003.2h  0.99% E-Sport
    3822.8h  0.95% Wetterbericht
    3778.6h  0.94% Sitcom
    3650.9h  0.90% Börsenmagazin
    3286.8h  0.81% Quiz
    3204.0h  0.79% Musikmagazin
    3150.9h  0.78% Komödie
    3066.7h  0.76% Wirtschaftsmagazin
    3025.5h  0.75% Wissensmagazin
    2822.4h  0.70% Telenovela
    2666.6h  0.66% Reportagereihe
    2597.1h  0.64% Politikmagazin
