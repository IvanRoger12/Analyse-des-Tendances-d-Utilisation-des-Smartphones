
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
file_path = 'user_behavior_dataset.csv'  # Assurez-vous que le fichier CSV est dans le même répertoire que ce script
data = pd.read_csv(file_path)

# Couleur de fond
background_color = '#D6EAF8'  # Bleu clair doux

# Graphique 1 : Histogramme du temps d'utilisation des applications par jour avec un fond bleu élégant
plt.figure(figsize=(10, 6))
plt.gcf().set_facecolor(background_color)
data['App Usage Time (min/day)'].plot(kind='hist', bins=15, color='navy', edgecolor='black')
plt.title("Distribution du temps d'utilisation des applications par jour", fontsize=14, color='darkblue')
plt.xlabel("Temps d'utilisation (min/jour)", fontsize=12, color='darkblue')
plt.ylabel("Nombre d'utilisateurs", fontsize=12, color='darkblue')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('app_usage_histogram_elegant_blue.png', facecolor=background_color)
plt.show()

# Graphique 2 : Comparaison Android vs iOS sur le temps d'utilisation avec un fond bleu élégant
plt.figure(figsize=(10, 6))
plt.gcf().set_facecolor(background_color)
os_usage = data.groupby('Operating System')['App Usage Time (min/day)'].mean()
os_usage.plot(kind='bar', color=['navy', 'steelblue'], edgecolor='black')
plt.title("Comparaison du temps d'utilisation des applications (Android vs iOS)", fontsize=14, color='darkblue')
plt.xlabel("Système d'exploitation", fontsize=12, color='darkblue')
plt.ylabel("Temps moyen d'utilisation (min/jour)", fontsize=12, color='darkblue')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('android_ios_comparison_elegant_blue.png', facecolor=background_color)
plt.show()

# Graphique 3 : Corrélation entre le temps d’écran et la consommation de batterie avec un fond bleu élégant
plt.figure(figsize=(10, 6))
plt.gcf().set_facecolor(background_color)
plt.scatter(data['Screen On Time (hours/day)'], data['Battery Drain (mAh/day)'], color='navy', alpha=0.7)
plt.title("Corrélation entre le temps d'écran et la consommation de batterie", fontsize=14, color='darkblue')
plt.xlabel("Temps d'écran (heures/jour)", fontsize=12, color='darkblue')
plt.ylabel("Consommation de batterie (mAh/jour)", fontsize=12, color='darkblue')
plt.grid(True)
plt.tight_layout()
plt.savefig('screen_battery_correlation_elegant_blue.png', facecolor=background_color)
plt.show()
