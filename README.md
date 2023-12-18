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

**97** channels, **602,731.0** hours playtime between **2023-01-17** and **2023-12-19**


### playtime per genre (top 30)

    39566.0h 6.56% Nachrichten
    28939.5h 4.80% Verkaufsshow
    24327.3h 4.04% Krimiserie
    20493.5h 3.40% Werbesendung
    19588.7h 3.25% Dokureihe
    18100.4h 3.00% Dokusoap
    17435.0h 2.89% Regionalmagazin
    15448.5h 2.56% Dokumentation
    14772.5h 2.45% *unknown*
    11136.5h 1.85% Zeichentrickserie
    10981.4h 1.82% Infomercial
    10679.2h 1.77% Animationsserie
    9234.2h  1.53% Comedyserie
    8587.1h  1.42% Morgenmagazin
    8173.7h  1.36% Religionsmagazin
    8074.4h  1.34% Talkshow
    7778.2h  1.29% Magazin
    5949.1h  0.99% Programmende
    5933.8h  0.98% E-Sport
    5835.3h  0.97% Sitcom
    5512.0h  0.91% Wetterbericht
    5437.9h  0.90% Börsenmagazin
    4994.4h  0.83% Quiz
    4720.5h  0.78% Komödie
    4596.0h  0.76% Wissensmagazin
    4492.8h  0.75% Wirtschaftsmagazin
    4369.3h  0.72% Telenovela
    4357.9h  0.72% Musikmagazin
    4349.1h  0.72% Realityshow
    4280.2h  0.71% Politikmagazin
