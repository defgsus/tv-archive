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

**97** channels, **423,485.1** hours playtime between **2023-01-17** and **2023-09-09**


### playtime per genre (top 30)

    27992.6h 6.61% Nachrichten
    20069.2h 4.74% Verkaufsshow
    17181.4h 4.06% Krimiserie
    14291.0h 3.37% Werbesendung
    13963.0h 3.30% Dokureihe
    12884.4h 3.04% Dokusoap
    12215.5h 2.88% Regionalmagazin
    10674.8h 2.52% Dokumentation
    10096.2h 2.38% *unknown*
    7993.8h  1.89% Zeichentrickserie
    7730.0h  1.83% Infomercial
    7503.5h  1.77% Animationsserie
    6881.4h  1.62% Comedyserie
    6000.8h  1.42% Morgenmagazin
    5653.9h  1.34% Religionsmagazin
    5585.7h  1.32% Talkshow
    5292.8h  1.25% Magazin
    4578.3h  1.08% Programmende
    4184.4h  0.99% E-Sport
    4003.4h  0.95% Wetterbericht
    3978.2h  0.94% Sitcom
    3836.5h  0.91% Börsenmagazin
    3487.6h  0.82% Quiz
    3347.6h  0.79% Musikmagazin
    3293.2h  0.78% Komödie
    3219.8h  0.76% Wirtschaftsmagazin
    3164.9h  0.75% Wissensmagazin
    2993.4h  0.71% Telenovela
    2781.4h  0.66% Reportagereihe
    2756.8h  0.65% Politikmagazin
