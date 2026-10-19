from django.db import models

class Representante(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=15)
    ie = models.CharField(max_length=9)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    codigo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    unid_med = models.CharField(max_length=10)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    ncm = models.CharField(max_length=10)

    def __str__(self):
        return self.descricao

class Item_entrada_saida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cfop = models.CharField(max_length=4)
    cst = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.produto.nome}{str(self.quantidade)}'

class Nota(models.Model):
    numero = models.IntegerField()
    serie = models.IntegerField()
    modelo = models.IntegerField()
    chave = models.CharField(max_length=100)
    data_emissao = models.DateTimeField()
    data_entrada_saida = models.DateTimeField()
    tipo = models.IntegerField()
    status = models.CharField(max_length=20)
    #emitente = models.OneToOneField(Empresa, on_delete=models.CASCADE)
    #destinatario = models.OneToOneField(Empresa, on_delete=models.CASCADE)
    cnpj_emitente = models.CharField(max_length=15)
    razao_social_emitente = models.CharField(max_length=100)
    uf_emitente = models.CharField(max_length=2)
    cnpj_destinatario = models.CharField(max_length=15)
    razao_social_destinatario = models.CharField(max_length=100)
    uf_destinatario = models.CharField(max_length=2)
    quant_produtos = models.IntegerField()
    itens_entrada_saida = models.ManyToManyField(Item_entrada_saida)

    def __str__(self):
        return f'{self.numero} {str(self.serie)}'

class Item_lmc(models.Model):
    cod_item = models.CharField(max_length=50)
    data_fechamento = models.DateTimeField()
    estoque_abertura = models.DecimalField(max_digits=10, decimal_places=2)
    estoque_fecha = models.DecimalField(max_digits=10, decimal_places=2)
    volume_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    volume_saidas = models.DecimalField(max_digits=10, decimal_places=2)
    ajustes_perdas = models.DecimalField(max_digits=10, decimal_places=2)
    ajustes_ganhos = models.DecimalField(max_digits=10, decimal_places=2)
    fechamento_fisico = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cod_item}'

class lmc(models.Model):
    emitente = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    itens_lmc = models.ManyToManyField(Item_lmc)
