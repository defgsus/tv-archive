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

**101** channels, **751,858.8** hours playtime between **2023-01-17** and **2024-03-12**


### playtime per genre (top 30)

    48911.3h 6.51% Nachrichten
    36107.9h 4.80% Verkaufsshow
    30602.9h 4.07% Krimiserie
    26060.8h 3.47% Werbesendung
    23994.2h 3.19% Dokureihe
    22734.5h 3.02% Dokusoap
    21816.8h 2.90% Regionalmagazin
    19406.1h 2.58% Dokumentation
    19284.0h 2.56% *unknown*
    13901.4h 1.85% Zeichentrickserie
    13673.1h 1.82% Infomercial
    13269.1h 1.76% Animationsserie
    11412.5h 1.52% Comedyserie
    10658.3h 1.42% Morgenmagazin
    10193.5h 1.36% Magazin
    10159.6h 1.35% Religionsmagazin
    10008.7h 1.33% Talkshow
    7420.8h  0.99% E-Sport
    7110.5h  0.95% Programmende
    7066.3h  0.94% Sitcom
    6681.1h  0.89% Börsenmagazin
    6677.8h  0.89% Wetterbericht
    6374.4h  0.85% Quiz
    6361.6h  0.85% Komödie
    5618.4h  0.75% Wissensmagazin
    5461.3h  0.73% Realityshow
    5434.6h  0.72% Wirtschaftsmagazin
    5419.5h  0.72% Politikmagazin
    5363.3h  0.71% Telenovela
    5135.0h  0.68% Musikmagazin
