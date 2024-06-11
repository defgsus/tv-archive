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

**108** channels, **898,051.6** hours playtime between **2023-01-17** and **2024-06-12**


### playtime per genre (top 30)

    58707.1h 6.54% Nachrichten
    42419.1h 4.72% Verkaufsshow
    36558.3h 4.07% Krimiserie
    31660.3h 3.53% Werbesendung
    28258.3h 3.15% Dokureihe
    27149.5h 3.02% Dokusoap
    26109.0h 2.91% Regionalmagazin
    23341.4h 2.60% Dokumentation
    22630.4h 2.52% *unknown*
    16519.8h 1.84% Zeichentrickserie
    16355.9h 1.82% Infomercial
    16010.3h 1.78% Animationsserie
    13459.1h 1.50% Comedyserie
    12826.0h 1.43% Magazin
    12640.7h 1.41% Morgenmagazin
    12157.6h 1.35% Religionsmagazin
    11961.6h 1.33% Talkshow
    8888.6h  0.99% E-Sport
    8363.8h  0.93% Sitcom
    8240.7h  0.92% Programmende
    8007.5h  0.89% Wetterbericht
    7778.1h  0.87% Quiz
    7776.2h  0.87% Börsenmagazin
    7755.6h  0.86% Komödie
    6699.6h  0.75% Politikmagazin
    6655.0h  0.74% Wissensmagazin
    6638.4h  0.74% Realityshow
    6334.1h  0.71% Wirtschaftsmagazin
    6251.7h  0.70% Telenovela
    5915.6h  0.66% Musikmagazin
