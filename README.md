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

**109** channels, **1,189,208.6** hours playtime between **2023-01-17** and **2024-12-19**


### playtime per genre (top 30)

    77825.1h 6.54% Nachrichten
    54036.5h 4.54% Verkaufsshow
    49581.2h 4.17% Krimiserie
    43916.4h 3.69% Werbesendung
    36990.6h 3.11% Dokureihe
    35176.9h 2.96% Dokusoap
    34827.1h 2.93% Regionalmagazin
    31413.3h 2.64% Dokumentation
    28082.8h 2.36% *unknown*
    22298.8h 1.88% Zeichentrickserie
    22026.6h 1.85% Infomercial
    21271.8h 1.79% Animationsserie
    16870.0h 1.42% Comedyserie
    16676.2h 1.40% Morgenmagazin
    15779.6h 1.33% Talkshow
    15689.7h 1.32% Religionsmagazin
    14657.6h 1.23% Magazin
    11764.3h 0.99% E-Sport
    11444.1h 0.96% Sitcom
    10758.1h 0.90% Wetterbericht
    10538.7h 0.89% Quiz
    10510.3h 0.88% Komödie
    10482.5h 0.88% Programmende
    9181.6h  0.77% Realityshow
    9086.6h  0.76% Politikmagazin
    8900.8h  0.75% Wissensmagazin
    8704.2h  0.73% Börsenmagazin
    7940.4h  0.67% Wirtschaftsmagazin
    7894.2h  0.66% Dramaserie
    7893.5h  0.66% Telenovela
