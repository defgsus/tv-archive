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

**97** channels, **625,996.6** hours playtime between **2023-01-17** and **2024-01-01**


### playtime per genre (top 30)

    40865.5h 6.53% Nachrichten
    29979.2h 4.79% Verkaufsshow
    25045.9h 4.00% Krimiserie
    21269.2h 3.40% Werbesendung
    20337.3h 3.25% Dokureihe
    18697.3h 2.99% Dokusoap
    17982.0h 2.87% Regionalmagazin
    16234.4h 2.59% Dokumentation
    15533.7h 2.48% *unknown*
    11532.5h 1.84% Zeichentrickserie
    11355.8h 1.81% Infomercial
    11028.8h 1.76% Animationsserie
    9516.1h  1.52% Comedyserie
    8850.7h  1.41% Morgenmagazin
    8486.8h  1.36% Religionsmagazin
    8295.5h  1.33% Talkshow
    8190.3h  1.31% Magazin
    6148.2h  0.98% E-Sport
    6129.4h  0.98% Programmende
    6083.6h  0.97% Sitcom
    5707.0h  0.91% Wetterbericht
    5602.5h  0.89% Börsenmagazin
    5272.6h  0.84% Komödie
    5116.5h  0.82% Quiz
    4725.7h  0.75% Wissensmagazin
    4613.8h  0.74% Wirtschaftsmagazin
    4526.3h  0.72% Realityshow
    4504.4h  0.72% Musikmagazin
    4476.2h  0.72% Telenovela
    4401.6h  0.70% Politikmagazin
