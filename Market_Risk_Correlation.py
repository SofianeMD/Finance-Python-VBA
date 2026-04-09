import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

tickers = ["AF.PA", "BZ=F"]
data = yf.download(tickers, start="2023-01-01", end="2026-01-01")['Close']

returns = data.pct_change().dropna()

window = 30
correlation = returns['AF.PA'].rolling(window).corr(returns['BZ=F'])

# Graphique amélioré
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(correlation, color='#2E86AB', linewidth=1.5, label='Corrélation glissante 30j')
ax.axhline(correlation.mean(), color='#E84855', linestyle='--', linewidth=1.2, label=f'Moyenne : {correlation.mean():.2f}')
ax.axhline(0, color='gray', linestyle='-', linewidth=0.8, alpha=0.5)
ax.fill_between(correlation.index, correlation, alpha=0.1, color='#2E86AB')
ax.set_title('Corrélation glissante (30j) — Air France vs Pétrole Brent', fontsize=13, fontweight='bold')
ax.set_ylabel('Corrélation', fontsize=11)
ax.set_xlabel('')
ax.legend(fontsize=10)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('correlation_AF_Brent.png', dpi=150, bbox_inches='tight')
plt.show()
