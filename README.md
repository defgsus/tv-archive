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

**109** channels, **1,163,354.5** hours playtime between **2023-01-17** and **2024-12-02**


### playtime per genre (top 30)

    75939.5h 6.53% Nachrichten
    53061.4h 4.56% Verkaufsshow
    48519.2h 4.17% Krimiserie
    42864.4h 3.68% Werbesendung
    36295.8h 3.12% Dokureihe
    34578.7h 2.97% Dokusoap
    34023.0h 2.92% Regionalmagazin
    30599.0h 2.63% Dokumentation
    27428.1h 2.36% *unknown*
    21803.5h 1.87% Zeichentrickserie
    21505.1h 1.85% Infomercial
    20794.6h 1.79% Animationsserie
    16586.7h 1.43% Comedyserie
    16272.1h 1.40% Morgenmagazin
    15466.8h 1.33% Religionsmagazin
    15441.9h 1.33% Talkshow
    14468.9h 1.24% Magazin
    11482.9h 0.99% E-Sport
    11218.6h 0.96% Sitcom
    10508.2h 0.90% Wetterbericht
    10274.0h 0.88% Programmende
    10271.4h 0.88% Quiz
    10221.3h 0.88% Komödie
    8948.5h  0.77% Realityshow
    8842.1h  0.76% Politikmagazin
    8737.4h  0.75% Wissensmagazin
    8613.7h  0.74% Börsenmagazin
    7772.5h  0.67% Wirtschaftsmagazin
    7690.0h  0.66% Telenovela
    7686.8h  0.66% Dramaserie
