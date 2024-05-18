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

**108** channels, **859,815.3** hours playtime between **2023-01-17** and **2024-05-19**


### playtime per genre (top 30)

    56141.7h 6.53% Nachrichten
    40944.2h 4.76% Verkaufsshow
    35015.3h 4.07% Krimiserie
    30108.2h 3.50% Werbesendung
    27059.1h 3.15% Dokureihe
    25998.3h 3.02% Dokusoap
    25011.7h 2.91% Regionalmagazin
    22280.8h 2.59% Dokumentation
    21848.8h 2.54% *unknown*
    15804.5h 1.84% Zeichentrickserie
    15643.5h 1.82% Infomercial
    15317.3h 1.78% Animationsserie
    12964.6h 1.51% Comedyserie
    12199.1h 1.42% Magazin
    12124.1h 1.41% Morgenmagazin
    11622.0h 1.35% Religionsmagazin
    11452.5h 1.33% Talkshow
    8540.9h  0.99% E-Sport
    7951.8h  0.92% Programmende
    7940.9h  0.92% Sitcom
    7644.3h  0.89% Wetterbericht
    7550.9h  0.88% Börsenmagazin
    7440.4h  0.87% Quiz
    7368.1h  0.86% Komödie
    6347.1h  0.74% Wissensmagazin
    6331.7h  0.74% Realityshow
    6320.7h  0.74% Politikmagazin
    6123.6h  0.71% Wirtschaftsmagazin
    6109.7h  0.71% Telenovela
    5699.1h  0.66% Musikmagazin
