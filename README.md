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

**102** channels, **810,119.0** hours playtime between **2023-01-17** and **2024-04-16**


### playtime per genre (top 30)

    52719.8h 6.51% Nachrichten
    38903.8h 4.80% Verkaufsshow
    32950.7h 4.07% Krimiserie
    28276.6h 3.49% Werbesendung
    25694.2h 3.17% Dokureihe
    24408.5h 3.01% Dokusoap
    23537.9h 2.91% Regionalmagazin
    20990.3h 2.59% Dokumentation
    20801.6h 2.57% *unknown*
    14874.9h 1.84% Zeichentrickserie
    14704.0h 1.82% Infomercial
    14400.3h 1.78% Animationsserie
    12283.5h 1.52% Comedyserie
    11423.0h 1.41% Morgenmagazin
    11252.6h 1.39% Magazin
    10940.0h 1.35% Religionsmagazin
    10783.9h 1.33% Talkshow
    7981.3h  0.99% E-Sport
    7565.7h  0.93% Programmende
    7487.9h  0.92% Sitcom
    7189.6h  0.89% Wetterbericht
    7134.5h  0.88% Börsenmagazin
    6973.9h  0.86% Quiz
    6934.9h  0.86% Komödie
    6009.6h  0.74% Wissensmagazin
    5905.0h  0.73% Politikmagazin
    5828.6h  0.72% Realityshow
    5803.6h  0.72% Wirtschaftsmagazin
    5781.0h  0.71% Telenovela
    5428.4h  0.67% Musikmagazin
