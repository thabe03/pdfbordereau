from fpdf import FPDF
import file_var


class BonDeReclamation(FPDF):
    
    # Ajouter une méthode pour l'en-tête du document
    def header(self):
        # Ajouter une image de logo si nécessaire
        # self.image('logo.png', 10, 10, 30)
        
        # Ajouter le titre du document
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, "BON DE RÉCLAMATION", 0, 1, 'C')
  
    
    # Ajouter une méthode pour le corps du document
    def body(self, facturer_a, num_client, date_expedition, acheteur, entetes, lignes, num_recl, note):        
        self.cell(0, 10, file_var.stick_num_recl + num_recl, 0, 1)
        # Add the payment terms line
        self.set_font('Arial', '', 12)
        self.cell(0, 10, file_var.stick_facturer_a + facturer_a, 0, 1)
        self.cell(0, 10, file_var.stick_client + num_client, 0, 1)
        self.cell(0, 10, file_var.stick_exp + date_expedition, 0, 1)
        self.cell(0, 10, file_var.stick_acheteur + acheteur, 0, 1)
        self.ln(5)

        self.set_font('Arial', '', 8)
        self.cell(80, 5, '1. Défectueux/Bris de transport', 0, 0)
        self.cell(80, 5, '4. Facturé et pas reçu', 0, 1, 'C')
        self.cell(80, 5, '2. Erreur de commande', 0, 0)
        self.cell(80, 5, '5. Reçu et pas facturé', 0, 1, 'C')
        self.cell(76.5, 5, '3. Reçu un autre produit', 0, 0)
        self.cell(80, 5, '6. Erreur de prix', 0, 1, 'C')

        self.ln(5)

        self.set_font('Arial', '', 12)
        
        # Ajouter l'entête des lignes du tableau
        self.set_fill_color(200)
        for entete in entetes:
            self.cell(file_var.width_bdr, 10, entete, 1, 0, 'C', True)
        self.ln()
        
        # Ajouter les lignes du tableau
        self.set_fill_color(255)
        for ligne in lignes:
            for colonne in ligne:
                self.cell(file_var.width_bdr, 10, colonne, 1, 0, 'C')
            self.ln()        
        
        # Ajouter la signature
        self.ln(20)
        self.cell(0, 10, file_var.stick_signature, 0, 1)