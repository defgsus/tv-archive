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

**102** channels, **815,881.9** hours playtime between **2023-01-17** and **2024-04-19**


### playtime per genre (top 30)

    53156.6h 6.52% Nachrichten
    39154.3h 4.80% Verkaufsshow
    33233.7h 4.07% Krimiserie
    28486.9h 3.49% Werbesendung
    25830.8h 3.17% Dokureihe
    24607.8h 3.02% Dokusoap
    23745.7h 2.91% Regionalmagazin
    21103.9h 2.59% Dokumentation
    20900.3h 2.56% *unknown*
    14973.9h 1.84% Zeichentrickserie
    14810.8h 1.82% Infomercial
    14511.1h 1.78% Animationsserie
    12376.9h 1.52% Comedyserie
    11531.3h 1.41% Morgenmagazin
    11382.8h 1.40% Magazin
    11005.2h 1.35% Religionsmagazin
    10857.8h 1.33% Talkshow
    8058.1h  0.99% E-Sport
    7607.5h  0.93% Programmende
    7533.2h  0.92% Sitcom
    7240.8h  0.89% Wetterbericht
    7190.4h  0.88% Börsenmagazin
    7038.9h  0.86% Quiz
    6963.9h  0.85% Komödie
    6049.2h  0.74% Wissensmagazin
    5962.2h  0.73% Politikmagazin
    5888.4h  0.72% Realityshow
    5849.9h  0.72% Wirtschaftsmagazin
    5843.6h  0.72% Telenovela
    5457.8h  0.67% Musikmagazin
