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

**109** channels, **1,166,737.5** hours playtime between **2023-01-17** and **2024-12-04**


### playtime per genre (top 30)

    76212.6h 6.53% Nachrichten
    53173.4h 4.56% Verkaufsshow
    48691.6h 4.17% Krimiserie
    42998.9h 3.69% Werbesendung
    36364.9h 3.12% Dokureihe
    34660.5h 2.97% Dokusoap
    34149.3h 2.93% Regionalmagazin
    30709.6h 2.63% Dokumentation
    27493.8h 2.36% *unknown*
    21866.1h 1.87% Zeichentrickserie
    21571.5h 1.85% Infomercial
    20857.1h 1.79% Animationsserie
    16625.5h 1.42% Comedyserie
    16342.0h 1.40% Morgenmagazin
    15493.9h 1.33% Religionsmagazin
    15478.6h 1.33% Talkshow
    14488.0h 1.24% Magazin
    11524.4h 0.99% E-Sport
    11253.3h 0.96% Sitcom
    10539.7h 0.90% Wetterbericht
    10317.7h 0.88% Quiz
    10301.2h 0.88% Programmende
    10242.7h 0.88% Komödie
    8982.4h  0.77% Realityshow
    8882.8h  0.76% Politikmagazin
    8754.7h  0.75% Wissensmagazin
    8629.4h  0.74% Börsenmagazin
    7797.7h  0.67% Wirtschaftsmagazin
    7728.1h  0.66% Telenovela
    7719.4h  0.66% Dramaserie
