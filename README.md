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

**109** channels, **901,680.5** hours playtime between **2023-01-17** and **2024-06-14**


### playtime per genre (top 30)

    58965.1h 6.54% Nachrichten
    42558.1h 4.72% Verkaufsshow
    36712.4h 4.07% Krimiserie
    31815.2h 3.53% Werbesendung
    28381.2h 3.15% Dokureihe
    27274.3h 3.02% Dokusoap
    26254.0h 2.91% Regionalmagazin
    23411.0h 2.60% Dokumentation
    22682.6h 2.52% *unknown*
    16583.2h 1.84% Zeichentrickserie
    16425.4h 1.82% Infomercial
    16079.5h 1.78% Animationsserie
    13514.2h 1.50% Comedyserie
    12875.0h 1.43% Magazin
    12712.0h 1.41% Morgenmagazin
    12195.1h 1.35% Religionsmagazin
    12014.4h 1.33% Talkshow
    8914.9h  0.99% E-Sport
    8414.9h  0.93% Sitcom
    8268.6h  0.92% Programmende
    8046.3h  0.89% Wetterbericht
    7816.3h  0.87% Quiz
    7794.6h  0.86% Börsenmagazin
    7771.4h  0.86% Komödie
    6768.6h  0.75% Politikmagazin
    6687.5h  0.74% Wissensmagazin
    6677.9h  0.74% Realityshow
    6360.4h  0.71% Wirtschaftsmagazin
    6268.6h  0.70% Telenovela
    5932.7h  0.66% Musikmagazin
