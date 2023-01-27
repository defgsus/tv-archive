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

**96** channels, **20,976.8** hours playtime between **2023-01-17** and **2023-01-28**


### playtime per genre (top 30)

    1529.7h 7.29% Nachrichten
    1136.9h 5.42% Verkaufsshow
    899.6h  4.29% Krimiserie
    739.6h  3.53% Dokusoap
    668.9h  3.19% Werbesendung
    633.2h  3.02% Regionalmagazin
    629.3h  3.00% Dokureihe
    547.2h  2.61% *unknown*
    519.2h  2.48% Dokumentation
    412.1h  1.96% Infomercial
    396.2h  1.89% Zeichentrickserie
    368.3h  1.76% Animationsserie
    366.8h  1.75% Comedyserie
    302.6h  1.44% Morgenmagazin
    289.7h  1.38% Talkshow
    272.0h  1.30% Magazin
    263.1h  1.25% Religionsmagazin
    231.4h  1.10% Programmende
    230.8h  1.10% E-Sport
    194.2h  0.93% Sitcom
    186.5h  0.89% Wirtschaftsmagazin
    176.4h  0.84% Börsenmagazin
    173.5h  0.83% Wetterbericht
    169.4h  0.81% Dramaserie
    167.7h  0.80% Wissensmagazin
    166.8h  0.80% Tennis
    165.9h  0.79% Quiz
    160.8h  0.77% Realityshow
    155.2h  0.74% Musikmagazin
    152.1h  0.73% Telenovela
