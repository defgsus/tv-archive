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

**109** channels, **1,185,793.4** hours playtime between **2023-01-17** and **2024-12-17**


### playtime per genre (top 30)

    77550.9h 6.54% Nachrichten
    53927.1h 4.55% Verkaufsshow
    49431.4h 4.17% Krimiserie
    43772.8h 3.69% Werbesendung
    36921.2h 3.11% Dokureihe
    35095.5h 2.96% Dokusoap
    34709.8h 2.93% Regionalmagazin
    31316.7h 2.64% Dokumentation
    28006.5h 2.36% *unknown*
    22232.1h 1.87% Zeichentrickserie
    21961.2h 1.85% Infomercial
    21207.0h 1.79% Animationsserie
    16821.3h 1.42% Comedyserie
    16614.8h 1.40% Morgenmagazin
    15740.6h 1.33% Talkshow
    15666.7h 1.32% Religionsmagazin
    14628.3h 1.23% Magazin
    11736.9h 0.99% E-Sport
    11407.6h 0.96% Sitcom
    10722.4h 0.90% Wetterbericht
    10497.0h 0.89% Quiz
    10469.4h 0.88% Komödie
    10455.4h 0.88% Programmende
    9146.6h  0.77% Realityshow
    9043.2h  0.76% Politikmagazin
    8877.9h  0.75% Wissensmagazin
    8687.5h  0.73% Börsenmagazin
    7913.7h  0.67% Wirtschaftsmagazin
    7858.9h  0.66% Telenovela
    7858.2h  0.66% Dramaserie
