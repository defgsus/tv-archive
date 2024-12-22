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

**109** channels, **1,194,444.4** hours playtime between **2023-01-17** and **2024-12-23**


### playtime per genre (top 30)

    78155.2h 6.54% Nachrichten
    54262.2h 4.54% Verkaufsshow
    49767.5h 4.17% Krimiserie
    44145.1h 3.70% Werbesendung
    37173.3h 3.11% Dokureihe
    35268.6h 2.95% Dokusoap
    34939.5h 2.93% Regionalmagazin
    31597.9h 2.65% Dokumentation
    28229.5h 2.36% *unknown*
    22403.2h 1.88% Zeichentrickserie
    22130.5h 1.85% Infomercial
    21364.6h 1.79% Animationsserie
    16907.1h 1.42% Comedyserie
    16731.9h 1.40% Morgenmagazin
    15861.2h 1.33% Talkshow
    15745.2h 1.32% Religionsmagazin
    14693.0h 1.23% Magazin
    11813.2h 0.99% E-Sport
    11476.2h 0.96% Sitcom
    10805.1h 0.90% Wetterbericht
    10592.6h 0.89% Komödie
    10569.8h 0.88% Quiz
    10523.5h 0.88% Programmende
    9218.5h  0.77% Realityshow
    9109.1h  0.76% Politikmagazin
    8930.0h  0.75% Wissensmagazin
    8713.0h  0.73% Börsenmagazin
    7960.8h  0.67% Wirtschaftsmagazin
    7933.5h  0.66% Arztserie
    7914.9h  0.66% Dramaserie
