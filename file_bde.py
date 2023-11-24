from fpdf import FPDF
import file_var


class BonDExpedition(FPDF):
    
    # Ajouter une méthode pour l'en-tête du document
    def header(self):
        # Ajouter une image de logo si nécessaire
        # self.image('logo.png', 10, 10, 30)
        
        # Ajouter le titre du document
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, "BON D'EXPÉDITION", 0, 1, 'C')
  
    
    # Ajouter une méthode pour le corps du document
    def body(self, livrer_a, facturer_a, fournisseur, num_client, transport, date_requise, date_commande, acheteur, entetes, lignes, num_facture,paiement):        
        self.cell(0, 10, file_var.stick_num_fact + num_facture, 0, 1)
        # Add the payment terms line
        self.set_font('Arial', '', 12)          
        self.cell(0, 10, file_var.stick_livrer_a + livrer_a, 0, 1)
        self.cell(0, 10, file_var.stick_facturer_a + facturer_a, 0, 1)
        self.cell(0, 10, file_var.stick_fourn + fournisseur, 0, 1)
        self.cell(0, 10, file_var.stick_client + num_client, 0, 1)
        self.cell(0, 10, file_var.stick_transport + transport, 0, 1)
        self.cell(0, 10, file_var.stick_date_requise + date_requise, 0, 1)
        self.cell(0, 10, file_var.stick_exp + date_commande, 0, 1)
        self.cell(0, 10, file_var.stick_acheteur + acheteur, 0, 1)
        self.ln(10)
        
        # Ajouter l'entête des lignes du tableau
        self.set_fill_color(200)
        for entete in entetes:
            self.cell(file_var.width_bde, 10, entete, 1, 0, 'C', True)
        self.ln()
        
        # Ajouter les lignes du tableau
        self.set_fill_color(255)
        for ligne in lignes:
            for colonne in ligne:
                self.cell(file_var.width_bde, 10, colonne, 1, 0, 'C')
            self.ln()        
        
        # Ajouter la signature
        self.ln(20)
        self.cell(0, 10, file_var.stick_signature, 0, 1)
        self.ln(20)
        self.cell(60, 10, 'PAIEMENT DÛ LE :' + paiement, 0, 0)
        self.cell(0, 10, 'CONDITION DE PAIEMENT : NET 30, 2% 10', 0, 1, 'C')