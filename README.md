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

**109** channels, **1,043,360.1** hours playtime between **2023-01-17** and **2024-09-14**


### playtime per genre (top 30)

    67898.5h 6.51% Nachrichten
    48457.9h 4.64% Verkaufsshow
    43042.1h 4.13% Krimiserie
    37802.7h 3.62% Werbesendung
    32751.3h 3.14% Dokureihe
    31445.5h 3.01% Dokusoap
    30482.5h 2.92% Regionalmagazin
    27271.1h 2.61% Dokumentation
    25120.3h 2.41% *unknown*
    19363.5h 1.86% Zeichentrickserie
    19134.3h 1.83% Infomercial
    18696.2h 1.79% Animationsserie
    15267.3h 1.46% Comedyserie
    14624.2h 1.40% Morgenmagazin
    14184.4h 1.36% Religionsmagazin
    13718.3h 1.31% Talkshow
    13640.9h 1.31% Magazin
    10308.1h 0.99% E-Sport
    9993.0h  0.96% Sitcom
    9443.1h  0.91% Wetterbericht
    9346.4h  0.90% Programmende
    9163.8h  0.88% Komödie
    9041.5h  0.87% Quiz
    8247.7h  0.79% Börsenmagazin
    7823.6h  0.75% Politikmagazin
    7812.9h  0.75% Wissensmagazin
    7781.2h  0.75% Realityshow
    7099.2h  0.68% Wirtschaftsmagazin
    6878.8h  0.66% Telenovela
    6799.8h  0.65% Dramaserie
