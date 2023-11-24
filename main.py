
import file_bdc
import file_bde
import file_bdr
import file_var



# bdr = file_bdr.BonDeReclamation()
# bdr.add_page() # Open a new page
# # Ajouter les informations du bon de commande
# facturer_a = input(file_var.stick_facturer_a)
# num_client = input(file_var.stick_client)
# date_expedition = input(file_var.stick_exp)
# acheteur = input(file_var.stick_acheteur)
# num_recl = input(file_var.stick_num_recl)
# note = input(file_var.stick_note)

# # Add the table header row
# entetes = ['CODE', 'QTÉ', 'NO FACT.', 'RAISON']
# # Add the table rows with data
# lignes = [['ABC123', '1', '0000001', '1'],
# ['DEF456', '1', '0000002', '4']]

# bdr.body(facturer_a, num_client, date_expedition, acheteur, entetes, lignes, num_recl, note)
# bdr.output('bon_de_reclamation.pdf', 'F')



# bdc = file_bdc.BonDeCommande()
# bdc.add_page() # Open a new page
# # Ajouter les informations du bon de commande
# livrer_a = input(stick_livrer_a)
# facturer_a = input(stick_facturer_a)
# fournisseur = input(stick_fourn)
# num_client = input(stick_client)
# transport = input(stick_transport)
# date_requise = input(stick_date_requise)
# date_commande = input(stick_commande)
# acheteur = input(stick_acheteur)
# entetes = ['Quantité', 'Code', 'Desc. et format', 'Prix unitaire', 'Total']
# lignes = [['1', 'ABC123', 'Produit 1', '10.00', '10.00'],
# ['2', 'DEF456', 'Produit 2', '20.00', '40.00'],
# ['3', 'GHI789', 'Produit 3', '30.00', '90.00']]
# num_facture = input(stick_num_fact)
# bdc.body(livrer_a, facturer_a, fournisseur, num_client, transport, date_requise, date_commande, acheteur, entetes, lignes, num_facture)
# bdc.output('bon_de_commande.pdf', 'F')



# bde = file_bde.BonDExpedition()
# bde.add_page() # Open a new page
# # Ajouter les informations du bon de commande
# livrer_a = input(file_var.stick_livrer_a)
# facturer_a = input(file_var.stick_facturer_a)
# fournisseur = input(file_var.stick_fourn)
# num_client = input(file_var.stick_client)
# transport = input(file_var.stick_transport)
# date_requise = input(file_var.stick_date_requise)
# date_commande = input(file_var.stick_commande)
# acheteur = input(file_var.stick_acheteur)
# num_facture = input(file_var.stick_num_fact)
# paiement = input("Paiement dû le : ")

# # Add the table header row
# entetes = ['QTÉ', 'CODE', 'DESC.', 'PRIX UN.', 'ESC.', 'PRIX NET', 'TOTAL']
# # Add the table rows with data
# lignes = [['1', 'ABC123', 'Produit 1', '10.00', '0.50', '9.50', '9.50'],
# ['2', 'DEF456', 'Produit 2', '20.00', '1.00', '19.00', '38.00'],
# ['3', 'GHI789', 'Produit 3', '30.00', '1.50', '28.50', '85.50']]

# bde.body(livrer_a, facturer_a, fournisseur, num_client, transport, date_requise, date_commande, acheteur, entetes, lignes, num_facture,paiement)
# bde.output('bon_dexpedition.pdf', 'F')
