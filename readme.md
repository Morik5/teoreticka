# Řešitel problému batohu 0/1 - Běh programu

## 📋 Přehled
Program řeší **problém batohu 0/1** pomocí **rekurzivního algoritmu s návratem (backtracking)**. Najde nejlepší kombinaci balíků, která maximalizuje hodnotu a nepřekročí váhový limit.

---

## 📊 Schéma běhu algoritmu

```mermaid
graph TD
    A["🔴 START<br/>Inicializace proměnných"] --> B["Volání najdi_nejlepsi<br/>index=0, váha=0, hodnota=0"]
    B --> C{"Překročila aktuální<br/>váha limit?"}
    C -->|Ano| D["❌ PROŘEZÁNÍ<br/>Okamžitý návrat<br/>Přeskočit tuto cestu"]
    C -->|Ne| E{"Dosáhli jsme<br/>konce balíků?<br/>index == délka?"}
    E -->|Ano| F{"Je aktuální hodnota<br/>lepší než dosavadní?"}
    F -->|Ano| G["✅ AKTUALIZACE<br/>Uložit jako nejlepší řešení"]
    F -->|Ne| H["Zachovat dosavadní nejlepší"]
    G --> I["🔙 NÁVRAT<br/>Jít zpět"]
    H --> I
    E -->|Ne| J["Vezmi balík<br/>na aktuální pozici"]
    J --> K["Možnost 1: VYNECHAT<br/>Rekurzivní volání:<br/>index+1"]
    K --> L["Možnost 2: VZÍT<br/>Přidej balík"]
    L --> M["Rekurzivní volání:<br/>index+1, váha+w, hodnota+v"]
    M --> N["ODEBER balík<br/>ze vzoru"]
    N --> I
    I --> O{"Zůstaly ještě<br/>cesty k prozkoumání?"}
    O -->|Ne| K
    O -->|Ano| P["🟢 KONEC<br/>Zobrazit výsledky"]
```

---

## 🎯 Postupný běh

### Počáteční nastavení
- **Balíky**: 7 položek (A-G) s váhou a hodnotou
- **Limit váhy**: 120 kg
- **Cíl**: Maximalizovat celkovou hodnotu

| Balík | Váha (kg) | Hodnota (Kč) |
|-------|-----------|-------------|
| A     | 40        | 900         |
| B     | 30        | 700         |
| C     | 50        | 1200        |
| D     | 20        | 400         |
| E     | 10        | 200         |
| F     | 25        | 500         |
| G     | 35        | 800         |

### Rekurzivní funkce: `najdi_nejlepsi()`

**Parametry:**
- `index`: Aktuálně zvažovaný balík (0 až délka seznamu)
- `aktualni_vaha`: Aktuální celková váha v batohu
- `aktualni_hodnota`: Aktuální celková hodnota v batohu
- `vybrany_vyber`: Seznam vybraných balíků

**Logika algoritmu:**

1. **Kontrola prořezání**: Pokud váha překročí 120 kg → návrat (neprohledávej tuto cestu)
2. **Základní případ**: Pokud jsme zpracovali všechny balíky → aktualizuj nejlepší řešení, pokud je lepší
3. **Rekurzivní případ**: Pro každý balík zkus dvě možnosti:
   - **Možnost 1 (Vynechat)**: Jdi na další balík bez jeho brání
   - **Možnost 2 (Vzít)**: Přidej balík do batohu a jdi dál
   - **Návrat**: Odeber balík poté, co jsi prozkoumala cestu "vzít"

---

## 🔄 Příklad stromu provádění (zjednodušeno)

```
Úroveň 0: Start (0 balíků zváženo)
├─ Balík A se nebere → Úroveň 1
│  └─ Balík B se nebere → Úroveň 2
│     └─ ... zkoumání všech zbývajících kombinací
│
└─ Balík A se vezme (váha: 40, hodnota: 900) → Úroveň 1
   ├─ Balík B se nebere → Úroveň 2
   └─ Balík B se vezme (váha: 70, hodnota: 1600) → Úroveň 2
      └─ ... pokračování zkoumání kombinací
```

---

## ⏱️ Příklad výstupu

```
Čas výpočtu: X.XXX ms
OPTIMÁLNÍ NÁKLAD
------------------------
Vybrané balíky:
Balík C  (50 kg, 1200 Kč)
Balík A  (40 kg, 900 Kč)
Balík B  (30 kg, 700 Kč)
------------------------
Celková váha: 120 kg
Celková hodnota: 2800 Kč
```

---

## 🎓 Klíčové pojmy

| Pojem | Vysvětlení |
|-------|-----------|
| **Návraty (Backtracking)** | Zkoumá všechny možné kombinace větvením a prořezáváním neplatných cest |
| **Prořezání (Pruning)** | Brzké ukončení, pokud je překročen limit váhy (optimalizace) |
| **Globální proměnné** | Sledují nejlepší hodnotu a nejlepší výběr na všech úrovních rekurze |
| **Časová složitost** | O(2^n) kde n = počet balíků (zkoumá všechny kombinace) |
| **Prostorová složitost** | O(n) pro hloubku zásobníku rekurze |

---

## 📈 Proč tento algoritmus?

- ✅ **Zaručuje optimální řešení** (zkoušuje všechny platné kombinace)
- ✅ **Prořezává větve** pro vyhnutí se prozkoumávání neplatných cest
- ✅ **Funguje pro omezení 0/1** (každá položka se buď vezme, nebo ne)
- ⚠️ **Může být pomalý** pro velké datové sady (exponenciální časová složitost)

*Pro produkční použití s 20+ balíky zvažte místo toho přístup **Dynamického programování**.*
