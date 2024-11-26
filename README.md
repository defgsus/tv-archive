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

**109** channels, **1,156,367.7** hours playtime between **2023-01-17** and **2024-11-27**


### playtime per genre (top 30)

    75471.4h 6.53% Nachrichten
    52810.2h 4.57% Verkaufsshow
    48251.9h 4.17% Krimiserie
    42581.7h 3.68% Werbesendung
    36071.9h 3.12% Dokureihe
    34417.3h 2.98% Dokusoap
    33845.4h 2.93% Regionalmagazin
    30419.7h 2.63% Dokumentation
    27247.2h 2.36% *unknown*
    21665.1h 1.87% Zeichentrickserie
    21359.2h 1.85% Infomercial
    20666.8h 1.79% Animationsserie
    16521.5h 1.43% Comedyserie
    16182.2h 1.40% Morgenmagazin
    15399.6h 1.33% Religionsmagazin
    15334.1h 1.33% Talkshow
    14410.0h 1.25% Magazin
    11428.9h 0.99% E-Sport
    11164.0h 0.97% Sitcom
    10442.1h 0.90% Wetterbericht
    10221.5h 0.88% Quiz
    10217.9h 0.88% Programmende
    10139.5h 0.88% Komödie
    8884.9h  0.77% Realityshow
    8789.9h  0.76% Politikmagazin
    8690.0h  0.75% Wissensmagazin
    8595.9h  0.74% Börsenmagazin
    7735.1h  0.67% Wirtschaftsmagazin
    7650.4h  0.66% Telenovela
    7616.8h  0.66% Dramaserie
