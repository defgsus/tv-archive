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

**97** channels, **620,592.8** hours playtime between **2023-01-17** and **2023-12-29**


### playtime per genre (top 30)

    40602.3h 6.54% Nachrichten
    29754.0h 4.79% Verkaufsshow
    24900.8h 4.01% Krimiserie
    21084.4h 3.40% Werbesendung
    20177.0h 3.25% Dokureihe
    18539.8h 2.99% Dokusoap
    17884.2h 2.88% Regionalmagazin
    16026.2h 2.58% Dokumentation
    15303.9h 2.47% *unknown*
    11436.0h 1.84% Zeichentrickserie
    11271.8h 1.82% Infomercial
    10931.0h 1.76% Animationsserie
    9447.6h  1.52% Comedyserie
    8801.6h  1.42% Morgenmagazin
    8411.8h  1.36% Religionsmagazin
    8236.1h  1.33% Talkshow
    8079.6h  1.30% Magazin
    6099.2h  0.98% E-Sport
    6087.5h  0.98% Programmende
    6025.6h  0.97% Sitcom
    5665.4h  0.91% Wetterbericht
    5572.0h  0.90% Börsenmagazin
    5124.6h  0.83% Komödie
    5104.0h  0.82% Quiz
    4700.5h  0.76% Wissensmagazin
    4597.1h  0.74% Wirtschaftsmagazin
    4481.9h  0.72% Realityshow
    4470.7h  0.72% Musikmagazin
    4467.1h  0.72% Telenovela
    4393.1h  0.71% Politikmagazin
