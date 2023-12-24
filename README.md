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

**97** channels, **613,519.4** hours playtime between **2023-01-17** and **2023-12-25**


### playtime per genre (top 30)

    40232.2h 6.56% Nachrichten
    29425.0h 4.80% Verkaufsshow
    24722.8h 4.03% Krimiserie
    20861.1h 3.40% Werbesendung
    19919.0h 3.25% Dokureihe
    18371.3h 2.99% Dokusoap
    17735.2h 2.89% Regionalmagazin
    15762.9h 2.57% Dokumentation
    15104.3h 2.46% *unknown*
    11325.0h 1.85% Zeichentrickserie
    11162.9h 1.82% Infomercial
    10828.1h 1.76% Animationsserie
    9378.3h  1.53% Comedyserie
    8733.0h  1.42% Morgenmagazin
    8322.8h  1.36% Religionsmagazin
    8189.4h  1.33% Talkshow
    7976.2h  1.30% Magazin
    6038.5h  0.98% E-Sport
    6033.0h  0.98% Programmende
    5947.6h  0.97% Sitcom
    5605.8h  0.91% Wetterbericht
    5524.8h  0.90% Börsenmagazin
    5059.6h  0.82% Quiz
    4950.9h  0.81% Komödie
    4661.8h  0.76% Wissensmagazin
    4563.5h  0.74% Wirtschaftsmagazin
    4449.2h  0.73% Telenovela
    4431.7h  0.72% Realityshow
    4416.2h  0.72% Musikmagazin
    4337.9h  0.71% Politikmagazin
