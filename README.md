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

**109** channels, **901,684.4** hours playtime between **2023-01-17** and **2024-06-15**


### playtime per genre (top 30)

    58962.8h 6.54% Nachrichten
    42551.3h 4.72% Verkaufsshow
    36714.3h 4.07% Krimiserie
    31814.9h 3.53% Werbesendung
    28350.4h 3.14% Dokureihe
    27270.9h 3.02% Dokusoap
    26242.3h 2.91% Regionalmagazin
    23414.0h 2.60% Dokumentation
    22696.2h 2.52% *unknown*
    16583.0h 1.84% Zeichentrickserie
    16425.5h 1.82% Infomercial
    16081.2h 1.78% Animationsserie
    13518.6h 1.50% Comedyserie
    12871.7h 1.43% Magazin
    12712.0h 1.41% Morgenmagazin
    12202.2h 1.35% Religionsmagazin
    12013.5h 1.33% Talkshow
    8916.4h  0.99% E-Sport
    8413.9h  0.93% Sitcom
    8268.6h  0.92% Programmende
    8045.5h  0.89% Wetterbericht
    7816.2h  0.87% Quiz
    7794.1h  0.86% Börsenmagazin
    7776.8h  0.86% Komödie
    6748.8h  0.75% Politikmagazin
    6682.9h  0.74% Wissensmagazin
    6674.8h  0.74% Realityshow
    6359.9h  0.71% Wirtschaftsmagazin
    6272.0h  0.70% Telenovela
    5933.3h  0.66% Musikmagazin
