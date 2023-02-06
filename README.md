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

**96** channels, **39,197.0** hours playtime between **2023-01-17** and **2023-02-07**


### playtime per genre (top 30)

    2718.8h 6.94% Nachrichten
    2049.8h 5.23% Verkaufsshow
    1642.8h 4.19% Krimiserie
    1370.9h 3.50% Dokusoap
    1331.6h 3.40% Werbesendung
    1204.0h 3.07% Dokureihe
    1124.1h 2.87% Regionalmagazin
    987.4h  2.52% Dokumentation
    967.4h  2.47% *unknown*
    760.3h  1.94% Zeichentrickserie
    735.5h  1.88% Infomercial
    696.8h  1.78% Animationsserie
    660.2h  1.68% Comedyserie
    537.2h  1.37% Morgenmagazin
    521.9h  1.33% Religionsmagazin
    503.3h  1.28% Talkshow
    502.1h  1.28% Programmende
    444.1h  1.13% Magazin
    424.8h  1.08% E-Sport
    355.9h  0.91% Sitcom
    334.3h  0.85% Wetterbericht
    333.8h  0.85% Börsenmagazin
    327.2h  0.83% Wirtschaftsmagazin
    314.7h  0.80% Wissensmagazin
    311.5h  0.79% Quiz
    294.8h  0.75% Dramaserie
    289.6h  0.74% Musikmagazin
    275.2h  0.70% Gesundheitsmagazin
    267.7h  0.68% Telenovela
    261.5h  0.67% Sportmagazin
