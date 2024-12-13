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

**109** channels, **1,180,592.8** hours playtime between **2023-01-17** and **2024-12-14**


### playtime per genre (top 30)

    77231.3h 6.54% Nachrichten
    53704.2h 4.55% Verkaufsshow
    49261.9h 4.17% Krimiserie
    43561.8h 3.69% Werbesendung
    36759.6h 3.11% Dokureihe
    34982.8h 2.96% Dokusoap
    34578.4h 2.93% Regionalmagazin
    31125.7h 2.64% Dokumentation
    27854.3h 2.36% *unknown*
    22130.4h 1.87% Zeichentrickserie
    21851.9h 1.85% Infomercial
    21109.0h 1.79% Animationsserie
    16782.4h 1.42% Comedyserie
    16563.1h 1.40% Morgenmagazin
    15664.6h 1.33% Talkshow
    15612.6h 1.32% Religionsmagazin
    14582.1h 1.24% Magazin
    11673.5h 0.99% E-Sport
    11374.4h 0.96% Sitcom
    10676.0h 0.90% Wetterbericht
    10461.6h 0.89% Quiz
    10413.4h 0.88% Programmende
    10393.3h 0.88% Komödie
    9109.6h  0.77% Realityshow
    9013.1h  0.76% Politikmagazin
    8842.4h  0.75% Wissensmagazin
    8679.7h  0.74% Börsenmagazin
    7892.2h  0.67% Wirtschaftsmagazin
    7842.6h  0.66% Telenovela
    7825.7h  0.66% Dramaserie
