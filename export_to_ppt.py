#!/usr/bin/env python3
"""
Script pour exporter la présentation HTML en PDF optimisé pour PowerPoint
"""

import webbrowser
import time
import os

print("=" * 60)
print("EXPORT DE LA PRÉSENTATION EN PDF POUR POWERPOINT")
print("=" * 60)
print()
print("Instructions pour exporter en PDF :")
print()
print("1. La présentation Reveal.js va s'ouvrir dans Chrome")
print("2. Appuyez sur Ctrl+P (Windows) ou Cmd+P (Mac)")
print("3. Dans les paramètres d'impression :")
print("   - Destination : Enregistrer au format PDF")
print("   - Mise en page : Paysage")
print("   - Marges : Aucune")
print("   - Options : Cocher 'Graphiques d'arrière-plan'")
print("4. Cliquez sur 'Enregistrer'")
print()
print("5. Pour importer dans PowerPoint :")
print("   - Ouvrez PowerPoint")
print("   - Fichier > Ouvrir > Sélectionnez le PDF")
print("   - PowerPoint convertira automatiquement chaque page en slide")
print()
print("OU utilisez cette méthode alternative :")
print("   - Ouvrez PowerPoint")
print("   - Insertion > Images > Ce périphérique")
print("   - Sélectionnez le PDF (il sera importé comme images)")
print()
print("=" * 60)
print()

# Ouvrir la présentation
html_file = os.path.join(os.path.dirname(__file__), "presentation_revealjs.html")
if os.path.exists(html_file):
    print(f"Ouverture de {html_file}...")
    webbrowser.open(f"file://{html_file}")
    print("✓ Présentation ouverte dans le navigateur")
    print()
    print("Appuyez sur Ctrl+P ou Cmd+P pour exporter en PDF")
else:
    print(f"❌ Fichier non trouvé : {html_file}")

