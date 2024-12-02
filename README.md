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

**109** channels, **1,165,051.3** hours playtime between **2023-01-17** and **2024-12-03**


### playtime per genre (top 30)

    76078.9h 6.53% Nachrichten
    53111.1h 4.56% Verkaufsshow
    48600.8h 4.17% Krimiserie
    42932.5h 3.69% Werbesendung
    36332.1h 3.12% Dokureihe
    34621.2h 2.97% Dokusoap
    34081.4h 2.93% Regionalmagazin
    30640.8h 2.63% Dokumentation
    27458.7h 2.36% *unknown*
    21833.7h 1.87% Zeichentrickserie
    21537.0h 1.85% Infomercial
    20825.7h 1.79% Animationsserie
    16606.7h 1.43% Comedyserie
    16308.0h 1.40% Morgenmagazin
    15478.2h 1.33% Religionsmagazin
    15457.4h 1.33% Talkshow
    14480.0h 1.24% Magazin
    11507.2h 0.99% E-Sport
    11236.2h 0.96% Sitcom
    10527.4h 0.90% Wetterbericht
    10306.5h 0.88% Quiz
    10287.5h 0.88% Programmende
    10230.5h 0.88% Komödie
    8957.0h  0.77% Realityshow
    8862.9h  0.76% Politikmagazin
    8745.5h  0.75% Wissensmagazin
    8621.0h  0.74% Börsenmagazin
    7786.1h  0.67% Wirtschaftsmagazin
    7708.2h  0.66% Telenovela
    7706.0h  0.66% Dramaserie
