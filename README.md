# MSc Business Analytics at Cass Business School 2020/21

This repository contains files for Network Analytics Midterm Project

## Result: Gumbel Softmax model 

- Number of communities: 6
```
Commu 0: [8, 28, 29, 30, 31, 32, 33, 38, 39, 53, 56, 58, 59, 60]

Commu 1: [0, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 35, 36, 37, 40, 41, 42]

Commu 2: [45, 57, 63, 67, 68, 69, 70, 76, 77, 80, 81, 84, 85, 86, 88, 89, 103, 104]

Commu 3: [21, 47, 48, 49, 62, 64, 65, 66, 71, 72, 73, 74, 75, 78, 79, 82, 83, 87]

Commu 4: [1, 2, 3, 4, 5, 6, 7, 22, 34, 43, 44, 46, 50, 51, 52, 54, 55, 61]

Commu 5: [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 105, 106, 107, 108, 109]
```

## Result: Infomap model 

- Number of communities: 12 (One isolated node)
```
Commu 1: [0, 4, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 37, 38, 39, 44, 50, 53, 54, 55, 59, 60, 61, 62]

Commu 2: [21, 26, 64, 67, 70, 77, 78, 79, 82, 85, 87, 88, 89, 93, 94, 95, 96, 99, 101, 102, 104]

Commu 3: [1, 2, 3, 5, 6, 7, 22, 34, 51, 52]

Commu 4: [63, 68, 69, 80, 81, 84, 86]

Commu 5: [90, 91, 103, 105, 107, 108, 109]

Commu 6: [65, 66, 71, 72, 73, 74, 75, 83]

Commu 7: [47, 48, 49]

Commu 8: [92, 97, 98, 100, 106]

Commu 9: [15, 35, 36]

Commu 10: [43, 45, 46]

Commu 11: [56, 57, 58]

Commu 12: [40, 41, 42]

Commu x: [76]
```

## Result: Infomap model 

- Number of communities: 12 (One isolated node)
```
Commu 1: 
['QUI-GON', 'OBI-WAN', 'EMPEROR', 'CAPTAIN PANAKA', 'SIO BIBBLE', 'JAR JAR', 'TARPALS', 'BOSS NASS', 'PADME', 'WATTO', 'ANAKIN', 'SEBULBA', 'JIRA', 'SHMI', 'KITSTER', 'WALD', 'FODE/BEED', 'GREEDO', 'VALORUM', 'MACE WINDU', 'KI-ADI-MUNDI', 'YODA', 'RABE', 'BAIL ORGANA', 'CAPTAIN TYPHO', 'SENATOR ASK AAK', 'ORN FREE TAA', 'LAMA SU', 'COUNT DOOKU', 'PLO KOON', 'ODD BALL', 'GENERAL GRIEVOUS', 'CLONE COMMANDER GREE', 'CLONE COMMANDER CODY', 'TION MEDON', 'CAPTAIN ANTILLES']
Commu 2: 
['C-3PO', 'JABBA', 'LUKE', 'LEIA', 'HAN', 'RIEEKAN', 'DERLIN', 'ZEV', 'DACK', 'LANDO', 'BIB FORTUNA', 'BOUSHH', 'ADMIRAL ACKBAR', 'CAPTAIN PHASMA', 'FINN', 'UNKAR PLUTT', 'REY', 'BALA-TIK', 'MAZ', 'BB-8', 'ADMIRAL STATURA']
Commu 3: 
['NUTE GUNRAY', 'PK-4', 'TC-14', 'DOFINE', 'RUNE', 'TEY HOW', 'DARTH MAUL', 'GENERAL CEEL', 'SUN RIT', 'POGGLE']
Commu 4: 
['DARTH VADER', 'MOTTI', 'TARKIN', 'PIETT', 'OZZEL', 'NEEDA', 'JERJERROD']
Commu 5: 
['LOR SAN TEKKA', 'POE', 'SNAP', 'YOLO ZIFF', 'ELLO ASTY', 'JESS', 'NIV LEK']
Commu 6: 
['CAMIE', 'BIGGS', 'DODONNA', 'GOLD LEADER', 'WEDGE', 'RED LEADER', 'RED TEN', 'JANSON']
Commu 7: 
['OWEN', 'BERU', 'CLIEGG']
Commu 8: 
['KYLO REN', 'GENERAL HUX', 'LIEUTENANT MITAKA', 'SNOKE', 'COLONEL DATOO']
Commu 9: 
['RIC OLIE', 'BRAVO TWO', 'BRAVO THREE']
Commu 10: 
['TAUN WE', 'BOBA FETT', 'JANGO FETT']
Commu 11: 
['FANG ZAR', 'MON MOTHMA', 'GIDDEAN DANU']
Commu 12: 
['SOLA', 'JOBAL', 'RUWEE']
Commu x: 
['GOLD FIVE']
```
# Reference

This table shows which episode(s) each character was in the movie. 
```
|     | name                 |   ep_1 |   ep_2 |   ep_3 |   ep_4 |   ep_5 |   ep_6 |   ep_7 |
|----:|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|   0 | QUI-GON              |      1 |      0 |      1 |      0 |      0 |      0 |      0 |
|   1 | NUTE GUNRAY          |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|   2 | PK-4                 |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|   3 | TC-14                |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|   4 | OBI-WAN              |      1 |      1 |      1 |      1 |      1 |      1 |      0 |
|   5 | DOFINE               |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|   6 | RUNE                 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|   7 | TEY HOW              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|   8 | EMPEROR              |      1 |      1 |      1 |      0 |      1 |      1 |      0 |
|   9 | CAPTAIN PANAKA       |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  10 | SIO BIBBLE           |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|  11 | JAR JAR              |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|  12 | TARPALS              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  13 | BOSS NASS            |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  14 | PADME                |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|  15 | RIC OLIE             |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  16 | WATTO                |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|  17 | ANAKIN               |      1 |      1 |      1 |      0 |      0 |      1 |      0 |
|  18 | SEBULBA              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  19 | JIRA                 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  20 | SHMI                 |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|  21 | C-3PO                |      1 |      1 |      1 |      1 |      1 |      1 |      1 |
|  22 | DARTH MAUL           |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  23 | KITSTER              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  24 | WALD                 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  25 | FODE/BEED            |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  26 | JABBA                |      1 |      0 |      0 |      1 |      0 |      1 |      0 |
|  27 | GREEDO               |      1 |      0 |      0 |      1 |      0 |      0 |      0 |
|  28 | VALORUM              |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  29 | MACE WINDU           |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|  30 | KI-ADI-MUNDI         |      1 |      1 |      0 |      0 |      0 |      0 |      0 |
|  31 | YODA                 |      1 |      1 |      1 |      0 |      1 |      1 |      0 |
|  32 | RABE                 |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  33 | BAIL ORGANA          |      1 |      1 |      1 |      0 |      0 |      0 |      0 |
|  34 | GENERAL CEEL         |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  35 | BRAVO TWO            |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  36 | BRAVO THREE          |      1 |      0 |      0 |      0 |      0 |      0 |      0 |
|  37 | CAPTAIN TYPHO        |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
|  38 | SENATOR ASK AAK      |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  39 | ORN FREE TAA         |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  40 | SOLA                 |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  41 | JOBAL                |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  42 | RUWEE                |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  43 | TAUN WE              |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  44 | LAMA SU              |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  45 | BOBA FETT            |      0 |      1 |      0 |      0 |      1 |      0 |      0 |
|  46 | JANGO FETT           |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  47 | OWEN                 |      0 |      1 |      0 |      1 |      0 |      0 |      0 |
|  48 | BERU                 |      0 |      1 |      0 |      1 |      0 |      0 |      0 |
|  49 | CLIEGG               |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  50 | COUNT DOOKU          |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
|  51 | SUN RIT              |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  52 | POGGLE               |      0 |      1 |      0 |      0 |      0 |      0 |      0 |
|  53 | PLO KOON             |      0 |      1 |      1 |      0 |      0 |      0 |      0 |
|  54 | ODD BALL             |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  55 | GENERAL GRIEVOUS     |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  56 | FANG ZAR             |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  57 | MON MOTHMA           |      0 |      0 |      1 |      0 |      0 |      1 |      0 |
|  58 | GIDDEAN DANU         |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  59 | CLONE COMMANDER GREE |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  60 | CLONE COMMANDER CODY |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  61 | TION MEDON           |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  62 | CAPTAIN ANTILLES     |      0 |      0 |      1 |      0 |      0 |      0 |      0 |
|  63 | DARTH VADER          |      0 |      0 |      1 |      1 |      1 |      1 |      0 |
|  64 | LUKE                 |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
|  65 | CAMIE                |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  66 | BIGGS                |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  67 | LEIA                 |      0 |      0 |      0 |      1 |      1 |      1 |      1 |
|  68 | MOTTI                |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  69 | TARKIN               |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  70 | HAN                  |      0 |      0 |      0 |      1 |      1 |      1 |      1 |
|  71 | DODONNA              |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  72 | GOLD LEADER          |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  73 | WEDGE                |      0 |      0 |      0 |      1 |      1 |      1 |      0 |
|  74 | RED LEADER           |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  75 | RED TEN              |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  76 | GOLD FIVE            |      0 |      0 |      0 |      1 |      0 |      0 |      0 |
|  77 | RIEEKAN              |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  78 | DERLIN               |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  79 | ZEV                  |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  80 | PIETT                |      0 |      0 |      0 |      0 |      1 |      1 |      0 |
|  81 | OZZEL                |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  82 | DACK                 |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  83 | JANSON               |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  84 | NEEDA                |      0 |      0 |      0 |      0 |      1 |      0 |      0 |
|  85 | LANDO                |      0 |      0 |      0 |      0 |      1 |      1 |      0 |
|  86 | JERJERROD            |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
|  87 | BIB FORTUNA          |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
|  88 | BOUSHH               |      0 |      0 |      0 |      0 |      0 |      1 |      0 |
|  89 | ADMIRAL ACKBAR       |      0 |      0 |      0 |      0 |      0 |      1 |      1 |
|  90 | LOR SAN TEKKA        |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  91 | POE                  |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  92 | KYLO REN             |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  93 | CAPTAIN PHASMA       |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  94 | FINN                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  95 | UNKAR PLUTT          |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  96 | REY                  |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  97 | GENERAL HUX          |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  98 | LIEUTENANT MITAKA    |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|  99 | BALA-TIK             |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 100 | SNOKE                |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 101 | MAZ                  |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 102 | BB-8                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 103 | SNAP                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 104 | ADMIRAL STATURA      |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 105 | YOLO ZIFF            |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 106 | COLONEL DATOO        |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 107 | ELLO ASTY            |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 108 | JESS                 |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
| 109 | NIV LEK              |      0 |      0 |      0 |      0 |      0 |      0 |      1 |
|----:|:---------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
```
