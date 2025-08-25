# Logique de saut – Résumé

Ménage
- Consent = Non → Fin.
- incident_30d = Oui → afficher “incident_type” + “incident_date”.
- aware_proj = Oui → afficher “info_source”.
- see_public_light_100 = Non → afficher “dist_est”.
- has_youth = Oui → afficher Module Jeune:
  - youth_consent = Oui → poser y_sex, y_age, y_feel_safe, y_nights_out_7d, y_status.

Commerce
- Consent = Non → Fin.
- incident_30d = Oui → afficher “incident_type”.
- aware_proj = Oui → afficher “info_source”.
- has_private_light = Oui → afficher “private_light_type”.

Contraintes
- Âges: resp_age 15–99; y_age 15–24.
- Bornes: nights_out_7d et y_nights_out_7d 0–7; employees 0–50; days_open 0–7; clients 0–1000.

Notes
- Point GPS requis dans les deux formulaires.
- “site_id” (corridor) et “enumerator_id” requis.
