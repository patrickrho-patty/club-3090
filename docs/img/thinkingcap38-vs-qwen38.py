"""ThinkingCap-Qwen3.8-27B vs base Qwen3.8-27B on 2x RTX 3090 (TP=2, vLLM) — decode + prefill.

Companion to the ThinkingCap-Qwen3.8 announcement. Each ThinkingCap bar is paired with a
same-day base Qwen3.8 (Frozenlock INT4) boot of the same tier on the same rig.

⚠️ NO CODE-DECODE PANEL, DELIBERATELY. ThinkingCap finishes the canonical quicksort prompt in
348-380 tokens vs base Qwen3.8's 572-779, and decode tok/s depends on completion length, so a
code-decode comparison between the two is not like-for-like until re-measured with FORCE_TOKENS.
Narrative lengths match (928-981 vs 968-978) and prefill has no completion component.

Data: learnings/thinkingcap-qwen3.8-27b.md, BENCHMARKS.md. 2x 3090 PCIe, 230 W cap, vLLM v0.30.0,
one fresh boot per arm, canonical bench (3 warm + 5 measured). ultrafast base = mean of two
same-day boots (108.8 / 111.1 narrative; 1,788-1,814 prefill@10K).

Re-run:  python3 docs/img/thinkingcap38-vs-qwen38.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).resolve().parent
TC, BASE = "#8E6BBF", "#9AA5B1"

tiers = ["dual-fast\n(int4 · MTP)", "dual-superfast\n(int4 · DFlash2)", "dual-ultrafast\n(int4 · DFlash2 · FA2)"]
narr_tc, narr_base = [74.0, 80.0, 108.3], [75.5, 84.0, 110.0]
pre_tc, pre_base = [1720, 1768, 1778], [1710, 1779, 1801]

fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.2), dpi=150)
x = np.arange(len(tiers))
w = 0.38
for ax, tc, base, title, fmt in (
    (axes[0], narr_tc, narr_base, "Narrative decode (tok/s)", "{:.0f}"),
    (axes[1], pre_tc, pre_base, "Prefill @10K (tok/s)", "{:,.0f}"),
):
    b1 = ax.bar(x - w / 2, base, w, color=BASE, label="Qwen3.8-27B (base, same day)")
    b2 = ax.bar(x + w / 2, tc, w, color=TC, label="ThinkingCap-Qwen3.8-27B")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height(), fmt.format(b.get_height()),
                    ha="center", va="bottom", fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels(tiers, fontsize=9)
    ax.set_title(title, fontsize=11, weight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_ylim(0, max(max(tc), max(base)) * 1.18)
axes[0].legend(frameon=False, fontsize=9, loc="upper left")
fig.suptitle("ThinkingCap-Qwen3.8-27B runs at base-model speed — 2× RTX 3090, vLLM v0.30.0, TP=2",
             fontsize=12.5, weight="bold")
fig.text(0.5, 0.005,
         "One fresh boot per arm, each paired with a same-day base Qwen3.8 boot. Largest gap: -4.8% (superfast narrative); narrative decode swings up to ~9% between identical boots here. "
         "Code decode omitted: ThinkingCap answers the code prompt in ~40% fewer tokens, so its tok/s is not comparable.",
         ha="center", fontsize=7.5, color="#555555", wrap=True)
fig.tight_layout(rect=(0, 0.04, 1, 0.95))
fig.savefig(OUT / "thinkingcap38-vs-qwen38.png")
print("wrote", OUT / "thinkingcap38-vs-qwen38.png")
