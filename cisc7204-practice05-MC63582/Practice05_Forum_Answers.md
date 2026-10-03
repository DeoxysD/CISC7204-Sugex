# Practice 05 Forum Answers
**Student:** Fan Ziqian (MC63582)  
**Forum:** CISC7204 Personal Learning Forum of Practice 05 - Day 05 2026SEP16  
**Due:** Wednesday, 23 September 2026, 11:00 PM  
**Submit on:** SUPPORT (HOME) UMMoodle (your class letter site), NOT the main CISC7204 site.

How to submit: create **six separate topics**. Copy the body under each heading. For Q5.10 / Q5.12, attach the PNG files in `sketches/`.

---

## Topic title
`My Answer to Activity 5.01 - Fan Ziqian`

### Q5.01: Which charts are suitable for this task?

This task compares **four employees** (Alex, Alice, Chris, Jennifer) across **five skill attributes** (efficiency, quality, commitment, responsible conduct, cooperation). It is a comparison of items / multiple groups on multiple quantitative variables.

Suitable charts:

1. **Grouped bar chart (column chart)** — Lecture 05 says bar charts are the best choice for comparison among items. Each skill is a category; each employee is a series. Bar length makes it easy to compare scores.
2. **Radar chart (spider / web chart)** — Lecture 05 says radar charts are great for visualizing multiple variables for multiple groups, and for showing which variables score high or low (performance profiles). Faceting (one radar per employee), as in Figure 5.2, is the recommended design practice when there are several groups.

A simple table of scores could support the charts, but it is not a visualization. Line charts are not suitable here (no time series). Pie charts are composition plots, not comparison plots.

### Q5.02: Advantages and disadvantages of the given bar and radar charts. Which is better, and why?

**Grouped bar chart (Figure 5.1)**

Advantages:
- Bar length is easy to compare, so I can quickly rank employees **within each skill**.
- Exact differences are clearer than on a radial axis (for example, who is highest on Quality or Cooperation).
- The y-axis starts at 0, which follows the bar-chart design practice in the lecture.

Disadvantages:
- It is harder to get an **overall skill profile** of one employee at a glance (I have to jump across five groups of bars).
- With four series, the chart can look busy; the legend uses A/B/C/D instead of the employees’ names.
- There is no title and no axis labels, so the chart is not fully self-explanatory.

**Radar chart (Figure 5.2)**

Advantages:
- Each employee is a polygon, so strengths and weaknesses (the “shape” of the person) are obvious. Employee A looks strong and balanced; D looks weaker and more uneven.
- Faceting (four small radars) avoids overlapping polygons, which matches the lecture design practice for multiple groups.
- Five axes is a reasonable number (the lecture suggests 10 or fewer).

Disadvantages:
- Humans judge **linear length more accurately than radial distance**, so close scores (3 vs 4) are harder to compare.
- It is harder to compare the **same skill across employees** than in the grouped bar chart (I must look at four separate plots).
- All four radars use the same color, so they are less distinct; there is no overall title.

**Which is better for this task?**  
The task is to **compare the employees and their skills**, i.e. comparison among items. I think the **grouped bar chart is better as the main chart**, because comparing bar lengths is more accurate and I can read every skill-by-employee contrast directly. The faceted radar chart is a good **complement** if the goal is to see each person’s overall profile, but it is weaker for precise comparison. If I could keep only one chart, I would keep the bar chart.

### Q5.03: What could be improved in the respective visualizations?

**Bar chart**
- Add a title (e.g. “Employee skill scores by attribute”).
- Label the y-axis (score, 0–5) and keep the x-axis skill names.
- Replace A/B/C/D in the legend with **Alex, Alice, Chris, Jennifer**.
- Use more contrasting colors if needed; keep bars grouped by skill.

**Radar chart**
- Add a figure title and, if useful, a shared score scale note (0–5).
- Use a **different color for each employee**, as the official design suggestion also points out.
- Keep faceting (do not overlay all four polygons on one radar — that would become unreadable).
- Optionally annotate the scores on the vertices so exact values are easier to read.

---

## Topic title
`My Answer to Activity 5.02 - Fan Ziqian`

### Q5.04: Identify the two years during which the number of road accidents occurring was the least.

The heatmap (Figure 5.3) encodes accident counts by **year (columns)** and **month (rows)**. Yellow ≈ 100 (low); red ≈ 700 (high).

The two lightest columns — the years with the **fewest accidents overall** — are **2014 and 2015**.  
In particular, **2015** is the clearest low year: January and July fall to about **100** accidents, and April / October are also relatively low (around 200–300), much lower than the mid-1990s.

(The early years around **1995** are the opposite: January is dark red, near 700.)

### Q5.05: For the past two decades, identify the month for which accidents showed a marked decrease.

**January.**

January starts as the **highest** cell on the heatmap (dark red, ~700 around 1995) and then becomes steadily lighter, ending as **yellow (~100)** by 2014–2015. No other month shows such a strong, consistent drop. April, July, and October stay in the orange–yellow range for most of the period; July is low in the last years as well, but January is the month with the marked long-term decrease.

---

## Topic title
`My Answer to Activity 5.03 - Fan Ziqian`

### Q5.06: Which manufacturer’s fourth-quarter performance is exceptional compared with the third quarter?

**Apple.**

On the line chart, Apple (blue) jumps sharply from Q3 to Q4 in both **2016 and 2017** (from about 45–46k up to about 75k+). No other brand has a Q4 spike of that size.

The others in Q4 vs Q3:
- **Samsung**: actually **falls** from 3Q17 to 4Q17.
- **Huawei**: a moderate Q4 rise, not on Apple’s scale.
- **Xiaomi / OPPO**: relatively small Q3–Q4 changes.

This matches Apple’s typical holiday / new-iPhone seasonality.

### Q5.07: Predict two companies with a downward trend and an upward trend.

- **Upward: Xiaomi.** After 1Q17 the red line rises almost every quarter (from ~13k toward ~33k by 2Q18). **Huawei** is also generally rising and even overtakes Apple in 2Q18, but Xiaomi’s climb is the most consistent.
- **Downward: Samsung.** Samsung is still the volume leader, but after the 3Q17 peak (~85k) the series drops (especially 4Q17) and 2Q18 is lower than 1Q18. The recent direction is down / unstable rather than steadily up.

(Apple’s post-Q4 drop is mostly seasonal, so I would not treat Apple as a structural downward trend.)

### Q5.08: Advantages and disadvantages of a stacked area chart instead of a line chart?

**Advantages of stacked area**
- It is a **composition plot**: each brand is shown as part of the **whole market**, and the top edge is total sales over time.
- Useful if the question is “how is the market shared?” or “is the whole market growing?”
- Area + color makes each company’s contribution more visible than a thin line.

**Disadvantages of stacked area**
- Only the **bottom** series is easy to read as a true trend. Upper series are stacked on top of others, so their outlines are not the actual sales level.
- Individual comparisons (Apple vs Samsung in Q4, Xiaomi’s slope) become harder — which is exactly what this activity asks.
- The visual depends on **stacking order**; a large, volatile series (Apple) can distort the layers above/below it.
- Overlapping / stacked areas are harder to read than separate lines if several series cross.

**Conclusion:** For **comparing manufacturers and spotting trends**, the **line chart is better**. Use a stacked area chart only if the story is about **market composition / total volume**.

---

## Topic title
`My Answer to Activity 5.04 - Fan Ziqian`

### Q5.09: Identify the interval during which a maximum number of trains arrive.

The histogram uses **2-hour bins** in the afternoon. The tallest bar is the **6:00 pm – 8:00 pm** interval (hours 6–8 on the x-axis), with a frequency of about **450–460** trains. That is clearly higher than 4–6 pm (~200), 8–10 pm (~390), and the other bins.

### Q5.10: How would the histogram change if, in the morning, the same total number of trains arrive as in the afternoon, and you have the same frequencies for all time intervals?

“Same frequencies for all time intervals” means a **uniform distribution**.

The afternoon histogram is skewed (peak at 6–8 pm). The morning histogram would **not** keep that shape. Because every 2-hour bin has the same count, **all bars would be equal in height**.

If the afternoon total is T and there are 5 bins, each morning bar would be T/5. Using the counts from the given figure (about 135 + 205 + 455 + 390 + 265 ≈ 1450), each morning interval would be about **290** trains. The plot becomes a **flat / rectangular histogram**.

Sketch attached: `sketches/Q5.10_morning_uniform_histogram.png`

---

## Topic title
`My Answer to Activity 5.05 - Fan Ziqian`

### Q5.11: What are the bad aspects of these visualizations?

**Figure 5.6 — Pie chart of the top 30 YouTube music channels**

1. A pie chart is for **part-of-a-whole**. The top 30 channels are **not** 100% of YouTube; they are a ranking of items.
2. **30 slices** are far too many. Many slices look similar, so comparison is almost impossible.
3. Slices are **not ordered by size**, so ranking is hidden.
4. There is **no unit** (subscribers in millions), no title that states the measure, and labels around the pie overlap.
5. Lecture 05: humans compare **bars more accurately than arc lengths**; pie charts should be used rarely.

**Figure 5.7 — Line chart of casino games over 2 days**

1. **Wrong chart type.** The x-axis is **categories** (Poker, Black Jack, Roulette, Craps), not a continuous time axis. A line implies a trend from one category to the next, which is misleading (Craps is not “after” Roulette in time).
2. Lecture 05: line charts are for **quantitative values over a continuous time period**. Here we only have **two days** and four games — a **grouped bar chart** is the comparison plot we need.
3. The chart is **not self-explanatory**: no title, no y-axis label (number of people), and the two lines are not named in a clear legend (Saturday vs Sunday).

### Q5.12: How could we improve the visualizations? Sketch the right visualization for both scenarios.

**YouTube:** use a **sorted horizontal bar chart**, one bar per channel, x-axis = subscribers (millions), ordered from largest to smallest. That turns the task into a ranking comparison. See sketch `sketches/Q5.12_youtube_horizontal_bar.png` (and the fuller official-style sketch `sketches/official_youtube_bar.png`).

**Casino:** use a **grouped (clustered) bar chart**: games on the x-axis, two bars per game (Saturday / Sunday), y-axis = number of people, with title, axis labels, and legend. See sketch `sketches/Q5.12_casino_grouped_bar.png` (and `sketches/official_casino_bar.png`).

Both replacements follow Lecture 05: bar charts for comparing items; titles, labels, and legends to make the plot self-explanatory.

---

## Topic title
`My Answer to Activity 5.06 - Fan Ziqian`

*(txt1/txt2 accidentally say “Activity 4.06” and Q4.13; the resource and Lecture 05 numbering are Activity 5.06 / Q5.13. I use 5.06 / Q5.13.)*

### Q5.13: Select the best suitable plot from the above plots, and explain why.

The dataset should show, for different income groups:

1. the **median**  
2. the **interquartile range (IQR)**  
3. the **underlying density** of the population  

| Plot | Median | IQR | Density | Verdict |
|------|--------|-----|---------|---------|
| **Density plot (Figure 5.8)** | not shown clearly | not shown | yes | incomplete |
| **Box plot (Figure 5.9)** | yes (line in the box) | yes (box) | **no** | incomplete |
| **Violin plot (Figure 5.10)** | yes (white dot) | yes (thick bar) | yes (kernel density on both sides) | **complete** |

Lecture 05: a violin plot is a **combination of a box plot and a density plot**. The box plot only shows median, IQR, and range; the violin also visualizes the density, so we can see skewness, peaks, and whether a group is unimodal or not.

Therefore the **violin plot is the best suitable plot**. The density plot misses the requested statistical summaries; the box plot misses the density that the activity explicitly asks for.
