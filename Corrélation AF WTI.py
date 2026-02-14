import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Récupération des données (Air France et le Pétrole Brent)
# 'AF.PA' pour Air France, 'BZ=F' pour le Brent
tickers = ["AF.PA", "BZ=F"]
data = yf.download(tickers, start="2023-01-01", end="2026-01-01")['Close']

# 2. On calcule les rendements quotidiens (plus précis que les prix bruts)
returns = data.pct_change().dropna()

# 3. Calcul de la corrélation glissante (Rolling Correlation)
# On regarde la corrélation sur les 30 derniers jours pour voir l'évolution
window = 30
correlation = returns['AF.PA'].rolling(window).corr(returns['BZ=F'])

# 4. Visualisation
plt.figure(figsize=(12, 6))
correlation.plot(title="Corrélation glissante (30j) entre Air France et le Pétrole")
plt.axhline(correlation.mean(), color='red', linestyle='--', label="Moyenne historique")
plt.legend()
plt.show()