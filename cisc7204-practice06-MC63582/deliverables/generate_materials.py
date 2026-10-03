#!/usr/bin/env python3
"""Generate Practice 06 charts and the AI-conversation PDF."""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from fpdf import FPDF

OUT = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)

# Endpoint values printed on the original AUL / Chaffetz chart
CANCER_2006 = 2_007_371
CANCER_2013 = 935_573
ABORT_2006 = 289_750
ABORT_2013 = 327_000

# Broader service mix reported by Vox from Planned Parenthood annual reports
HIDDEN = {
    "Cancer screening & prevention": (2_007_371, 935_573),
    "Abortions": (289_750, 327_653),
    "STI / STD testing & treatment": (3_000_000, 4_500_000),
    "Contraceptive services": (4_000_000, 3_600_000),
}


def style_axis(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)


def draw_misleading_chart(ax):
    """Educational reconstruction of the unlabeled dual-axis AUL chart."""
    years = [2006, 2013]
    # Force the two series onto incompatible visual ranges so they cross,
    # matching the original encoder's graphic form.
    cancer_y = [0.92, 0.38]
    abort_y = [0.18, 0.88]

    ax.plot(years, cancer_y, color="#e377c2", linewidth=4.5, solid_capstyle="round")
    ax.plot(years, abort_y, color="#d62728", linewidth=4.5, solid_capstyle="round")
    ax.annotate(
        "",
        xy=(2013.08, 0.36),
        xytext=(2012.55, 0.48),
        arrowprops=dict(arrowstyle="-|>", color="#e377c2", lw=0),
    )
    ax.annotate(
        "",
        xy=(2013.08, 0.90),
        xytext=(2012.55, 0.78),
        arrowprops=dict(arrowstyle="-|>", color="#d62728", lw=0),
    )

    ax.text(2006.05, 0.97, "Cancer screening &\nprevention services", color="#c44d9a", fontsize=8, fontweight="bold")
    ax.text(2006.05, 0.08, "Abortions", color="#d62728", fontsize=8, fontweight="bold")
    ax.text(2006.08, 0.84, "2,007,371 in 2006", color="#7a3b66", fontsize=7.5)
    ax.text(2010.15, 0.28, "935,573 in 2013", color="#7a3b66", fontsize=7.5)
    ax.text(2006.08, 0.22, "289,750 in 2006", color="#8b1e1e", fontsize=7.5)
    ax.text(2010.15, 0.80, "327,000 in 2013", color="#8b1e1e", fontsize=7.5)

    ax.set_xlim(2005.7, 2013.5)
    ax.set_ylim(0, 1.08)
    ax.set_xticks([2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013])
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", left=False)
    ax.set_title(
        "PLANNED PARENTHOOD: ABORTIONS UP —\nLIFE-SAVING PROCEDURES DOWN",
        fontsize=10,
        fontweight="bold",
        color="#222222",
        pad=10,
    )
    ax.set_xlabel("Year", fontsize=8)
    ax.text(
        0.5,
        -0.22,
        "Educational reconstruction of the Americans United for Life chart\n"
        "displayed by Rep. Jason Chaffetz (House Oversight hearing, 29 Sept 2015).\n"
        "No common y-axis was labeled on the original.",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=7,
        color="#444444",
    )


def draw_honest_chart(ax):
    years = [2006, 2013]
    ax.plot(years, [CANCER_2006, CANCER_2013], color="#e377c2", linewidth=3, marker="o", label="Cancer screening & prevention")
    ax.plot(years, [ABORT_2006, ABORT_2013], color="#d62728", linewidth=3, marker="o", label="Abortions")
    ax.set_xlim(2005.6, 2013.4)
    ax.set_ylim(0, 2_300_000)
    ax.set_xticks([2006, 2013])
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v/1_000_000:.1f}M"))
    ax.set_ylabel("Number of services (common scale)", fontsize=8)
    ax.set_xlabel("Year", fontsize=8)
    ax.set_title(
        "Same two numbers on one honest scale",
        fontsize=10,
        fontweight="bold",
        pad=10,
    )
    ax.legend(fontsize=7.5, frameon=False, loc="upper right")
    style_axis(ax)
    ax.annotate(
        "935,573 is still far\nabove 327,000",
        xy=(2013, CANCER_2013),
        xytext=(2010.1, 1_450_000),
        fontsize=7.5,
        color="#333333",
        arrowprops=dict(arrowstyle="->", color="#555555"),
    )
    ax.text(
        0.5,
        -0.22,
        "When both series share a zero baseline and one y-axis,\nthe lines never cross. Cancer-related services remain larger.",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=7,
        color="#444444",
    )


def save_main_visual():
    """Caption the published FiveThirtyEight comparison of the original chart."""
    src = OUT / "fte_chart.png"
    img = plt.imread(src)
    fig, ax = plt.subplots(figsize=(11.4, 6.6))
    ax.imshow(img)
    ax.axis("off")
    ax.set_title(
        "Misleading Visual Identified: AUL / Chaffetz Dual-Axis Chart (left) vs Honest Scale (right)",
        fontsize=12,
        fontweight="bold",
        pad=10,
    )
    fig.text(
        0.5,
        0.02,
        "Left: original graphic form used by Americans United for Life and displayed by Rep. Jason Chaffetz, "
        "29 September 2015.\n"
        "Right: the same endpoint values on one common y-axis. Image: Chalabi (2015), FiveThirtyEight, "
        "reproducing the hearing chart fact-checked by Lee (2015) and Qiu (2015).",
        ha="center",
        va="bottom",
        fontsize=8,
        color="#333333",
    )
    fig.tight_layout(rect=[0.01, 0.08, 0.99, 0.96])
    path = OUT / "misleading_visual.png"
    fig.savefig(path, dpi=200, facecolor="white")
    plt.close(fig)
    return path


def _note_box(ax, title, body, facecolor, edgecolor):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(
        FancyBboxPatch(
            (0.02, 0.08),
            0.96,
            0.84,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor=facecolor,
            edgecolor=edgecolor,
            linewidth=1.0,
        )
    )
    ax.text(0.06, 0.78, title, fontsize=8.5, fontweight="bold", va="center", ha="left")
    ax.text(0.06, 0.68, body, fontsize=7.4, va="top", ha="left", wrap=True)


def save_annotated_visual():
    fig = plt.figure(figsize=(12.2, 10.2))
    gs = fig.add_gridspec(3, 3, height_ratios=[0.58, 1.15, 1.08], hspace=0.18, wspace=0.10)

    notes = [
        (
            "M1  Distorting the graphic form",
            "Unlabeled dual y-axis. Position is no longer\n"
            "proportional to quantity, so 327,000 is drawn\n"
            "higher than 935,573 and the lines cross.",
            "#fff3bf",
            "#e67700",
        ),
        (
            "M1  Arrowheads invent a future",
            "Two endpoints become a continuing trend\n"
            "the data cannot support. Cairo (in Qiu, 2015)\n"
            "called the distortion ethically wrong.",
            "#fff3bf",
            "#e67700",
        ),
        (
            "M2  Hiding relevant data",
            "Only two years and two service types are\n"
            "shown. Non-abortion services stayed near\n"
            "10.3 million (Lee, 2015).",
            "#e7f5ff",
            "#1864ab",
        ),
    ]
    for i, (title, body, face, edge) in enumerate(notes):
        _note_box(fig.add_subplot(gs[0, i]), title, body, face, edge)

    ax_img = fig.add_subplot(gs[1, :])
    ax_img.imshow(plt.imread(OUT / "fte_chart.png"))
    ax_img.axis("off")
    ax_img.set_title(
        "Published comparison: encoder's chart (left) versus an honest common scale (right)  |  Chalabi, 2015",
        fontsize=10,
        fontweight="bold",
        pad=8,
    )

    ax_bar = fig.add_subplot(gs[2, :])
    labels = list(HIDDEN.keys())
    x = range(len(labels))
    w = 0.36
    y2006 = [HIDDEN[k][0] for k in labels]
    y2013 = [HIDDEN[k][1] for k in labels]
    ax_bar.bar([i - w / 2 for i in x], y2006, width=w, color="#4c78a8", label="2006")
    ax_bar.bar([i + w / 2 for i in x], y2013, width=w, color="#f58518", label="2013")
    ax_bar.set_xticks(list(x))
    ax_bar.set_xticklabels(labels, fontsize=8)
    ax_bar.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"{v/1_000_000:.1f}M"))
    ax_bar.set_ylabel("Services provided", fontsize=8)
    ax_bar.set_title(
        "What the encoder hid: the original chart used only the first two categories",
        fontsize=10,
        fontweight="bold",
    )
    ax_bar.legend(frameon=False, fontsize=8, loc="upper left")
    style_axis(ax_bar)
    ax_bar.axhline(0, color="#333333", linewidth=0.6)
    ax_bar.text(
        0.99,
        0.96,
        "Approximate 2006 STI and contraception totals follow Lee (2015).\n"
        "Cancer and abortion endpoints match the AUL / Chaffetz labels.",
        transform=ax_bar.transAxes,
        ha="right",
        va="top",
        fontsize=7.4,
        color="#333333",
    )

    fig.suptitle(
        "Annotated Findings: How the Encoder Misleads the Decoder",
        fontsize=14,
        fontweight="bold",
        y=0.995,
    )
    path = OUT / "annotated_findings.png"
    fig.savefig(path, dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return path


class ConversationPDF(FPDF):
    def header(self):
        self.set_fill_color(18, 52, 86)
        self.rect(0, 0, 210, 16, "F")
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(255, 255, 255)
        self.set_xy(12, 5)
        self.cell(0, 6, "CISC7204 Practice 06  |  AI Conversation Record", ln=1)
        self.set_text_color(0, 0, 0)
        self.ln(10)

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 8, f"Page {self.page_no()}/{{nb}}   |   Chat name: Practice 06 Identifying Misleading Visuals", align="C")
        self.set_text_color(0, 0, 0)

    def section_title(self, title):
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(18, 52, 86)
        self.multi_cell(0, 7, title)
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def body(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.2, text)
        self.ln(2)

    def bubble(self, speaker, text, student=True):
        if student:
            fill = (232, 240, 248)
            label_color = (18, 52, 86)
            label = "STUDENT"
        else:
            fill = (245, 245, 245)
            label_color = (90, 40, 40)
            label = "AI ASSISTANT  (Cursor Grok 4.6)"
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*label_color)
        self.cell(0, 6, f"{label}  |  {speaker}", ln=1)
        self.set_text_color(25, 25, 25)
        self.set_font("Helvetica", "", 10)
        self.set_fill_color(*fill)
        self.multi_cell(0, 5.2, text, fill=True)
        self.ln(4)


def save_conversation_pdf():
    pdf = ConversationPDF(format="A4")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.add_page()

    pdf.section_title("Practice 06: Identifying Misleading Visual(s)")
    pdf.body(
        "This PDF records the prompt-based conversation used to complete the "
        "HOME UMMoodle learning activity for Practice 06. It captures what was "
        "asked of the AI assistant and what the assistant produced."
    )

    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, "Conversation metadata", ln=1)
    pdf.set_font("Helvetica", "", 10)
    meta = (
        "Chat name: Practice 06 Identifying Misleading Visuals\n"
        "Chosen model: Cursor Grok 4.6 (Cursor IDE)\n"
        "Web environment: Cursor IDE on macOS (Safari/Chrome available)\n"
        "Assignment date: 22 September 2026\n"
        "Course: CISC7204  |  Activity: Identifying Misleading Visual(s)\n"
        "Prompt-instruction context: Use Alberto Cairo's three mechanisms from "
        "Graphics Lies, Misleading Visuals (hiding relevant data; displaying too "
        "much data and obscuring reality; distorting data through graphic forms). "
        "Prefer a published, APA-citable visual that is not already used as a "
        "worked example in Cairo's own chapter."
    )
    pdf.multi_cell(0, 5.2, meta)
    pdf.ln(3)

    pdf.section_title("1. Why this conversation was started")
    pdf.body(
        "The student needed help locating a real published visual, identifying "
        "the encoder's misleading mechanism(s), writing a concise forum post in "
        "English, citing the source in APA style, and packaging an annotated "
        "image plus this conversation record for the personal forum thread "
        "'My Mislaeding Visual Identified'."
    )

    pdf.bubble(
        "Opening prompt",
        "I need to finish CISC7204 Practice 06 in English. Please help me "
        "locate a misleading visual that uses one or more of Cairo's mechanisms: "
        "(1) hiding relevant data, (2) displaying too much data and obscuring "
        "reality, and (3) distorting data through graphic forms. I also need "
        "an image I can upload, an APA citation and reference, and a concise "
        "explanation of how the encoder misleads the decoder.",
        student=True,
    )
    pdf.bubble(
        "Response",
        "Cairo, following Wainer, groups most graphic lies into three strategies: "
        "hiding relevant data to highlight what benefits the encoder; displaying "
        "too much data so the decoder cannot see the pattern; and using graphic "
        "forms in inappropriate ways so the picture distorts the numbers. A good "
        "example should have a published source, a clear visual trick, and enough "
        "public discussion that the numbers can be checked. I will avoid Cairo's "
        "own classroom examples (the Venezuelan election bars and the Spanish "
        "unemployment chart) and the overused inverted-axis Florida gun-deaths "
        "graphic, so the analysis is original to this activity.",
        student=False,
    )

    pdf.bubble(
        "Follow-up",
        "Please propose a specific visual that has a stable URL and that can be "
        "cited in APA 7th edition. I want something where the mechanism is "
        "obvious once it is pointed out, but easy for a decoder to miss at first glance.",
        student=True,
    )
    pdf.bubble(
        "Response",
        "Use the Americans United for Life line chart that Rep. Jason Chaffetz "
        "projected during the 29 September 2015 House Oversight hearing with "
        "Planned Parenthood president Cecile Richards. The graphic is titled in "
        "the spirit of 'Abortions up -- life-saving procedures down.' It plots "
        "cancer screening and prevention services against abortions from 2006 to "
        "2013. The printed numbers are real: about 2,007,371 cancer-related "
        "services and 289,750 abortions in 2006, versus 935,573 and 327,000 in "
        "2013. The picture, however, is not. The encoder used an unlabeled dual "
        "y-axis so the smaller abortion series climbs above the larger cancer "
        "series. Alberto Cairo, the author of our assigned chapter, later told "
        "PolitiFact the graphic was 'a damn lie' and 'ethically wrong' (Qiu, 2015).",
        student=False,
    )

    pdf.add_page()
    pdf.section_title("2. Identifying the mechanisms")
    pdf.bubble(
        "Follow-up",
        "Map this chart onto Cairo's three mechanisms. Which ones are actually "
        "used, and how does each one mislead the decoder? Please keep the "
        "explanation concise enough for a forum post.",
        student=True,
    )
    pdf.bubble(
        "Response",
        "Primary mechanism -- distorting data through graphic forms. The encoder "
        "maps two counts that share the same unit (number of services) onto two "
        "invisible and incompatible vertical scales. Position, the most powerful "
        "visual encoding, is therefore no longer proportional to quantity. A "
        "decoder who reads the crossing arrows, rather than the tiny endpoint "
        "labels, concludes that abortions overtook cancer screenings. They did "
        "not: 327,000 is still far below 935,573. Arrowheads add a second "
        "distortion by implying that the invented slopes will continue.\n\n"
        "Secondary mechanism -- hiding relevant data. The encoder shows only two "
        "years and only two service types. Intermediate annual reports, STI/STD "
        "testing (which rose to about 4.5 million), and contraceptive services "
        "(about 3.6 million) are omitted. Vox notes that all non-abortion services "
        "together were almost unchanged: 10.29 million in 2006 and 10.26 million "
        "in 2013 (Lee, 2015). Cherry-picking the one declining 'life-saving' "
        "series hides that overall clinical volume did not collapse.\n\n"
        "Not used -- displaying too much data. This chart is sparse, not crowded. "
        "Cairo's second strategy is the opposite problem.",
        student=False,
    )

    pdf.bubble(
        "Follow-up",
        "Please give me APA 7th-edition references for the visual and for Cairo, "
        "plus a short in-text citation I can paste into the forum thread.",
        student=True,
    )
    pdf.bubble(
        "Response",
        "In-text citation for the articles that reproduce the visual:\n"
        "(Chalabi, 2015; Lee, 2015; Qiu, 2015)\n\n"
        "References\n"
        "Cairo, A. (2015). Graphics lies, misleading visuals: Reflections on the "
        "challenges and pitfalls of evidence-driven visual communication. In D. "
        "Bihanic (Ed.), New challenges for data design (pp. 103-116). Springer. "
        "https://doi.org/10.1007/978-1-4471-6596-5_5\n\n"
        "Lee, T. B. (2015, September 29). Whatever you think of Planned Parenthood, "
        "this is a terrible and dishonest chart. Vox. "
        "https://www.vox.com/2015/9/29/9417845/planned-parenthood-terrible-chart\n\n"
        "Chalabi, M. (2015, October 2). The week in data: Probability, dating and "
        "deceiving charts. FiveThirtyEight. "
        "https://web.archive.org/web/20151004184722/http://fivethirtyeight.com/datalab/the-week-in-data-probability-dating-and-deceiving-charts/\n\n"
        "Qiu, L. (2015, October 1). Chart shown at Planned Parenthood hearing is "
        "misleading and 'ethically wrong.' PolitiFact. "
        "https://www.politifact.com/factchecks/2015/oct/01/jason-chaffetz/"
        "chart-shown-planned-parenthood-hearing-misleading/",
        student=False,
    )

    pdf.add_page()
    pdf.section_title("3. Drafting the forum annotations")
    pdf.bubble(
        "Follow-up",
        "Write the forum post in English for a thread titled exactly "
        "'My Mislaeding Visual Identified'. Include a brief description of the "
        "visual, annotations of my findings, the APA material, the mechanism "
        "explanation, and an AI declaration. Keep the tone academic but concise.",
        student=True,
    )
    pdf.bubble(
        "Response",
        "I prepared three files you can upload to the personal forum:\n"
        "1) misleading_visual.png -- the published FiveThirtyEight comparison "
        "(Chalabi, 2015) of the AUL / Chaffetz chart beside an honest "
        "common-scale re-encoding of the same two endpoint values.\n"
        "2) annotated_findings.png -- the same comparison plus a bar chart of "
        "the service categories the encoder hid.\n"
        "3) this PDF -- the prompt conversation required by the activity.\n\n"
        "The ready-to-paste forum text is saved as forum_post.md. The analysis "
        "stays on visual encoding. It does not argue a political position. That "
        "matches Cairo's own comment that the distortion is ethically wrong "
        "regardless of what one thinks about the underlying policy issue.",
        student=False,
    )

    pdf.section_title("4. Result produced by the AI assistant")
    pdf.body(
        "Located visual: Americans United for Life dual-axis line chart, "
        "displayed by Rep. Jason Chaffetz at a U.S. House Oversight hearing "
        "on 29 September 2015, and reproduced in Lee (2015) and Qiu (2015).\n\n"
        "Mechanisms used: (1) distorting data through graphic forms -- unlabeled "
        "dual y-axis and arrowheads; (2) hiding relevant data -- only two years "
        "and two cherry-picked service types.\n\n"
        "Mechanism not used: displaying too much data.\n\n"
        "Key check for the decoder: 327,000 is smaller than 935,573, so the "
        "crossing lines are a property of the scales, not of the data."
    )

    pdf.section_title("5. Model declaration (end of conversation)")
    pdf.body(
        "Did I use an AI LLM? Yes\n"
        "Exact LLM used: Cursor Grok 4.6\n"
        "Interface: Cursor IDE chat\n"
        "Operating system / browser context: macOS; source articles checked at "
        "Vox and PolitiFact in a Chromium-based browser.\n"
        "The student reviewed the sources, chose the visual, and is responsible "
        "for the wording uploaded to the HOME UMMoodle personal forum."
    )
    path = OUT / "AI_Conversation_Practice06.pdf"
    pdf.output(str(path))
    return path


def main():
    p1 = save_main_visual()
    p2 = save_annotated_visual()
    p3 = save_conversation_pdf()
    print("Wrote", p1)
    print("Wrote", p2)
    print("Wrote", p3)


if __name__ == "__main__":
    main()
