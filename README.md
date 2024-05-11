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

**108** channels, **848,797.4** hours playtime between **2023-01-17** and **2024-05-12**


### playtime per genre (top 30)

    55395.3h 6.53% Nachrichten
    40500.9h 4.77% Verkaufsshow
    34558.2h 4.07% Krimiserie
    29689.7h 3.50% Werbesendung
    26763.6h 3.15% Dokureihe
    25664.2h 3.02% Dokusoap
    24690.2h 2.91% Regionalmagazin
    22001.5h 2.59% Dokumentation
    21631.8h 2.55% *unknown*
    15610.0h 1.84% Zeichentrickserie
    15438.5h 1.82% Infomercial
    15115.9h 1.78% Animationsserie
    12824.9h 1.51% Comedyserie
    12016.5h 1.42% Magazin
    11966.1h 1.41% Morgenmagazin
    11466.1h 1.35% Religionsmagazin
    11305.7h 1.33% Talkshow
    8423.1h  0.99% E-Sport
    7869.1h  0.93% Programmende
    7824.4h  0.92% Sitcom
    7540.7h  0.89% Wetterbericht
    7471.8h  0.88% Börsenmagazin
    7337.2h  0.86% Quiz
    7269.0h  0.86% Komödie
    6266.2h  0.74% Wissensmagazin
    6229.7h  0.73% Realityshow
    6226.6h  0.73% Politikmagazin
    6058.6h  0.71% Wirtschaftsmagazin
    6045.1h  0.71% Telenovela
    5635.5h  0.66% Musikmagazin
