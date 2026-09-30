# 1 superClasse ; 2 ou mais subClasses ok 
# Construtor chamando super e pelo menos +1 atr. ok
# 1 Metodo sobrescrito (toString) ok
# 1 lista do tipo da superClasse com as subclasses

class Veiculo:
  
    def __init__(self,nome,cor,ano,combustivel):
        self.nome = nome
        self.cor = cor
        self.ano = ano
        self.combustivel = combustivel

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    
    @property
    def ano(self):
        return self._ano
    @ano.setter
    def ano(self,ano):
        if ano < 1886:
            print("O ano do veiculo não pode ser anterior a 1886.")
        self._ano = ano
        
    @property
    def cor(self):
        return self._cor    
    @cor.setter
    def cor(self,cor):
        self._cor = cor
        
    @property
    def combustivel(self):
        return self._combustivel
    
    @combustivel.setter
    def combustivel(self,combustivel):
        if combustivel < 0:
            raise ValueError("A quantidade de combustível não pode ser negativa.")
        self._combustivel = combustivel
        
    def verificar_combustivel(self):
        if self.combustivel <= 10:
            print("Combustível baixo. Necessário abastecer.")
        else:
            print("Quantidade de combustível adequada.")
            
    def ficha_tecnica(self):
        return ("Nome : "+self.nome + " Ano: " + str(self.ano) + " Cor: " 
                + self.cor +" Combustivel: "+ str(self.combustivel) )
            
    
class Carro(Veiculo):#subClasse
       
    def __init__(self,nome,cor,ano,tm,combustivel=0):
        super().__init__(nome,cor,ano,combustivel)
        self.tipo_motor = tm
        
        
    @property
    def tipo_motor(self):
        return self._tipo_motor
    
    @tipo_motor.setter
    def tipo_motor(self,tm):
        self._tipo_motor = tm

    def ficha_tecnica(self):
        return (super().ficha_tecnica() +" Tipo Motor: "+ self.tipo_motor)

        
class Moto(Veiculo):#subclasse
    
    def __init__(self,nome,cor,ano,c,combustivel=0):
        super().__init__(nome,cor,ano,combustivel)
        self.cilindradas = c

    @property
    def cilindradas(self):
        return self._cilindradas
    @cilindradas.setter
    def cilindradas(self,c):
        self._cilindradas = c
        
    def ficha_tecnica(self):
        return (super().ficha_tecnica() +" Cilindradas: "+ str(self.cilindradas))
    
if __name__ =="__main__":
    
    c1 = Carro("Gol","azul",2000,"1.8 ap",5)
    #print(c1.ficha_tecnica())

    c2 = Carro("Uno","vermelho",2010,"1.3 fire", 15)
    #print(c2.ficha_tecnica())
    
    c3 = Carro("Fusca","preto", 1970,"1300 boxer")
    #print(c3.ficha_tecnica())
    
    m1 = Moto("Cg", "Branca", 2010, 150, 15)
    #print(m1.ficha_tecnica())
    
    lista = [c1,c2,c3,m1]
    
    v = Veiculo("","",0000,0)
    
    for v in lista:
        print(v.ficha_tecnica())
