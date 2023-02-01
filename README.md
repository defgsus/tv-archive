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

**96** channels, **30,094.1** hours playtime between **2023-01-17** and **2023-02-02**


### playtime per genre (top 30)

    2125.3h 7.06% Nachrichten
    1604.6h 5.33% Verkaufsshow
    1273.9h 4.23% Krimiserie
    1041.3h 3.46% Dokusoap
    995.2h  3.31% Werbesendung
    915.1h  3.04% Dokureihe
    883.4h  2.94% Regionalmagazin
    753.1h  2.50% Dokumentation
    729.5h  2.42% *unknown*
    587.7h  1.95% Zeichentrickserie
    574.2h  1.91% Infomercial
    527.9h  1.75% Animationsserie
    523.9h  1.74% Comedyserie
    420.0h  1.40% Morgenmagazin
    399.5h  1.33% Religionsmagazin
    388.1h  1.29% Talkshow
    369.8h  1.23% Programmende
    346.5h  1.15% Magazin
    327.4h  1.09% E-Sport
    278.7h  0.93% Sitcom
    265.3h  0.88% Börsenmagazin
    256.6h  0.85% Wirtschaftsmagazin
    254.5h  0.85% Wetterbericht
    245.3h  0.82% Wissensmagazin
    236.1h  0.78% Quiz
    232.5h  0.77% Dramaserie
    224.2h  0.74% Musikmagazin
    220.8h  0.73% Gesundheitsmagazin
    212.4h  0.71% Telenovela
    206.8h  0.69% Realityshow
