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

**99** channels, **663,087.3** hours playtime between **2023-01-17** and **2024-01-22**


### playtime per genre (top 30)

    43229.6h 6.52% Nachrichten
    31703.4h 4.78% Verkaufsshow
    26640.6h 4.02% Krimiserie
    22630.7h 3.41% Werbesendung
    21570.6h 3.25% Dokureihe
    19828.1h 2.99% Dokusoap
    19090.8h 2.88% Regionalmagazin
    17186.2h 2.59% Dokumentation
    16576.9h 2.50% *unknown*
    12259.1h 1.85% Zeichentrickserie
    12040.6h 1.82% Infomercial
    11659.3h 1.76% Animationsserie
    10030.5h 1.51% Comedyserie
    9362.4h  1.41% Morgenmagazin
    8969.8h  1.35% Religionsmagazin
    8795.8h  1.33% Magazin
    8772.1h  1.32% Talkshow
    6514.2h  0.98% E-Sport
    6412.0h  0.97% Programmende
    6376.6h  0.96% Sitcom
    5975.4h  0.90% Wetterbericht
    5894.8h  0.89% Börsenmagazin
    5650.7h  0.85% Komödie
    5478.1h  0.83% Quiz
    4996.1h  0.75% Wissensmagazin
    4842.1h  0.73% Wirtschaftsmagazin
    4825.5h  0.73% Realityshow
    4704.3h  0.71% Telenovela
    4688.2h  0.71% Musikmagazin
    4671.5h  0.70% Politikmagazin
