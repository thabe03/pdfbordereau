from fpdf import FPDF
import file_var


class BonDeCommande(FPDF):
    
    # Ajouter une méthode pour l'en-tête du document
    def header(self):
        # Ajouter une image de logo si nécessaire
        # self.image('logo.png', 10, 10, 30)
        
        # Ajouter le titre du document
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'BON DE COMMANDE', 0, 1, 'C')
    
    # Ajouter une méthode pour le corps du document
    def body(self, livrer_a, facturer_a, fournisseur, num_client, transport, date_requise, date_commande, acheteur, entetes, lignes, num_facture):
        self.cell(0, 10, file_var.stick_num_fact + num_facture, 0, 1)
        # Ajouter les informations du client et du fournisseur
        self.set_font('Arial', '', 12)
        self.cell(0, 10, file_var.stick_livrer_a + livrer_a, 0, 1)
        self.cell(0, 10, file_var.stick_facturer_a + facturer_a, 0, 1)
        self.cell(0, 10, file_var.stick_fourn + fournisseur, 0, 1)
        self.cell(0, 10, file_var.stick_client + num_client, 0, 1)
        self.cell(0, 10, file_var.stick_transport + transport, 0, 1)
        self.cell(0, 10, file_var.stick_date_requise + date_requise, 0, 1)
        self.cell(0, 10, file_var.stick_acheteur + acheteur, 0, 1)
        self.ln(10)
        
        # Ajouter l'entête des lignes du tableau
        self.set_fill_color(200)
        for entete in entetes:
            self.cell(file_var.width_bdc, 10, entete, 1, 0, 'C', True)
        self.ln()
        
        # Ajouter les lignes du tableau
        self.set_fill_color(255)
        for ligne in lignes:
            for colonne in ligne:
                self.cell(file_var.width_bdc, 10, colonne, 1, 0, 'C')
            self.ln()
        
        # Ajouter le numéro de facture
        self.ln(3)
        
        self.set_font('Arial', '', 8)
        self.cell(0, 5, '1. Veuillez envoyer deux copies de votre facture.', 0, 1)
        self.cell(0, 5, '''2. Veuillez nous informer immédiatement si vous n'êtes pas en mesure d'expédier la marchandise telle que spécifiée.''', 0, 1)
        self.cell(0, 5, '''3. L'acceptation des marchandises
est conditionnelle à l'inspection de celle-ci.''', 0, 1)
        self.cell(0, 5, '''4. Permission d'annuler la
commande si celle-ci n'est pas livrée à la date convenue.''', 0, 1)
        self.ln(10)
        self.set_font('Arial', '', 12)
        self.cell(0, 10, file_var.stick_signature, 0, 1)
        self.cell(0, 10, file_var.stick_commande + date_commande, 0, 1)