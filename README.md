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

**109** channels, **899,865.2** hours playtime between **2023-01-17** and **2024-06-13**


### playtime per genre (top 30)

    58841.6h 6.54% Nachrichten
    42482.7h 4.72% Verkaufsshow
    36620.3h 4.07% Krimiserie
    31743.2h 3.53% Werbesendung
    28317.3h 3.15% Dokureihe
    27219.5h 3.02% Dokusoap
    26182.3h 2.91% Regionalmagazin
    23377.2h 2.60% Dokumentation
    22659.7h 2.52% *unknown*
    16551.7h 1.84% Zeichentrickserie
    16389.9h 1.82% Infomercial
    16044.3h 1.78% Animationsserie
    13482.0h 1.50% Comedyserie
    12844.8h 1.43% Magazin
    12676.6h 1.41% Morgenmagazin
    12178.4h 1.35% Religionsmagazin
    11988.6h 1.33% Talkshow
    8899.0h  0.99% E-Sport
    8394.9h  0.93% Sitcom
    8255.0h  0.92% Programmende
    8027.4h  0.89% Wetterbericht
    7795.9h  0.87% Quiz
    7785.2h  0.87% Börsenmagazin
    7771.4h  0.86% Komödie
    6732.2h  0.75% Politikmagazin
    6669.6h  0.74% Wissensmagazin
    6657.1h  0.74% Realityshow
    6347.4h  0.71% Wirtschaftsmagazin
    6259.3h  0.70% Telenovela
    5922.8h  0.66% Musikmagazin
