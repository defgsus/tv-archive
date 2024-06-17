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

**109** channels, **907,113.3** hours playtime between **2023-01-17** and **2024-06-18**


### playtime per genre (top 30)

    59269.5h 6.53% Nachrichten
    42752.6h 4.71% Verkaufsshow
    36942.6h 4.07% Krimiserie
    32036.7h 3.53% Werbesendung
    28554.9h 3.15% Dokureihe
    27419.2h 3.02% Dokusoap
    26370.3h 2.91% Regionalmagazin
    23574.0h 2.60% Dokumentation
    22815.7h 2.52% *unknown*
    16684.6h 1.84% Zeichentrickserie
    16529.8h 1.82% Infomercial
    16185.4h 1.78% Animationsserie
    13580.3h 1.50% Comedyserie
    12943.6h 1.43% Magazin
    12759.2h 1.41% Morgenmagazin
    12287.6h 1.35% Religionsmagazin
    12077.1h 1.33% Talkshow
    8969.9h  0.99% E-Sport
    8465.4h  0.93% Sitcom
    8310.1h  0.92% Programmende
    8097.6h  0.89% Wetterbericht
    7857.8h  0.87% Komödie
    7855.1h  0.87% Quiz
    7802.6h  0.86% Börsenmagazin
    6789.4h  0.75% Politikmagazin
    6728.7h  0.74% Wissensmagazin
    6712.9h  0.74% Realityshow
    6379.0h  0.70% Wirtschaftsmagazin
    6279.6h  0.69% Telenovela
    5959.7h  0.66% Musikmagazin
