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

**97** channels, **423,483.4** hours playtime between **2023-01-17** and **2023-09-09**


### playtime per genre (top 30)

    27992.4h 6.61% Nachrichten
    20072.3h 4.74% Verkaufsshow
    17181.5h 4.06% Krimiserie
    14291.0h 3.37% Werbesendung
    13964.5h 3.30% Dokureihe
    12884.7h 3.04% Dokusoap
    12215.5h 2.88% Regionalmagazin
    10679.4h 2.52% Dokumentation
    10092.9h 2.38% *unknown*
    7993.1h  1.89% Zeichentrickserie
    7730.0h  1.83% Infomercial
    7504.0h  1.77% Animationsserie
    6881.3h  1.62% Comedyserie
    6000.8h  1.42% Morgenmagazin
    5653.9h  1.34% Religionsmagazin
    5583.0h  1.32% Talkshow
    5291.8h  1.25% Magazin
    4578.3h  1.08% Programmende
    4184.4h  0.99% E-Sport
    4003.6h  0.95% Wetterbericht
    3978.4h  0.94% Sitcom
    3836.4h  0.91% Börsenmagazin
    3487.6h  0.82% Quiz
    3344.9h  0.79% Musikmagazin
    3293.3h  0.78% Komödie
    3219.8h  0.76% Wirtschaftsmagazin
    3164.9h  0.75% Wissensmagazin
    2993.4h  0.71% Telenovela
    2781.3h  0.66% Reportagereihe
    2751.8h  0.65% Politikmagazin
