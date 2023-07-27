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

**96** channels, **346,459.4** hours playtime between **2023-01-17** and **2023-07-28**


### playtime per genre (top 30)

    23034.6h 6.65% Nachrichten
    16531.4h 4.77% Verkaufsshow
    13958.4h 4.03% Krimiserie
    11637.8h 3.36% Werbesendung
    11301.5h 3.26% Dokureihe
    10486.5h 3.03% Dokusoap
    9953.0h  2.87% Regionalmagazin
    8723.4h  2.52% Dokumentation
    8433.4h  2.43% *unknown*
    6569.5h  1.90% Zeichentrickserie
    6337.6h  1.83% Infomercial
    6113.2h  1.76% Animationsserie
    5724.9h  1.65% Comedyserie
    4865.9h  1.40% Morgenmagazin
    4590.6h  1.33% Religionsmagazin
    4574.2h  1.32% Talkshow
    4146.0h  1.20% Magazin
    3983.0h  1.15% Programmende
    3431.0h  0.99% E-Sport
    3278.6h  0.95% Sitcom
    3247.3h  0.94% Wetterbericht
    3130.6h  0.90% Börsenmagazin
    2770.4h  0.80% Quiz
    2709.8h  0.78% Musikmagazin
    2677.4h  0.77% Wirtschaftsmagazin
    2635.3h  0.76% Komödie
    2631.8h  0.76% Wissensmagazin
    2393.3h  0.69% Telenovela
    2277.6h  0.66% Sportmagazin
    2219.1h  0.64% Reportagereihe
