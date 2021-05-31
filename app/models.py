from app import db


class VendasLojistaMes(db.Model):
    __table_name__ = "vendas_lojista_mes"

    id_lojista = db.Column("idlojista", db.Integer, primary_key=True)
    bandeira = db.Column(db.Integer, primary_key=True)
    ano_mes = db.Column("anomes", db.String, primary_key=True)
    qnt_venda = db.Column(db.Integer, nullable=False)
    qnt_itens_vendidos = db.Column(db.Integer, nullable=False)


class VendasLojistaSemana(db.Model):
    __table_name__ = "vendas_lojista_semana"

    id_lojista = db.Column("idlojista", db.Integer, primary_key=True)
    bandeira = db.Column(db.Integer, primary_key=True)
    qnt_venda = db.Column(db.Integer, nullable=False)
    qnt_itens_vendidos = db.Column(db.Integer, nullable=False)


class VendasProdutosLojistaTop5(db.Model):
    __table_name__ = "vendas_produtos_lojista_top5"

    id_lojista = db.Column("idlojista", db.Integer, primary_key=True)
    bandeira = db.Column(db.Integer, primary_key=True)
    id_sku = db.Column("idsku", db.Integer, nullable=False)
    qnt_itens_vendidos = db.Column(db.Integer, nullable=False)
    nome_departamento = db.Column("nomedepartamento", db.Integer, nullable=False)


class VendasLojistaFatuMedio(db.Model):
    __table_name__ = "vendas_lojista_fatu_medio"

    id_lojista = db.Column("idlojista", db.Integer, primary_key=True)
    bandeira = db.Column(db.Integer, primary_key=True)
    menor_conversao = db.Column(db.Integer, nullable=False)
    media_conversao = db.Column(db.Integer, nullable=False)
    maior_conversao = db.Column(db.Integer, nullable=False)


class Lojista(db.Model):
    __table_name__ = "lojista"

    id_lojista = db.Column("idlojista", db.Integer, primary_key=True)


class CombosProdutos(db.Model):
    __table_name__ = "combos_produtos"

    produto_1 = db.Column(db.Integer, primary_key=True)
    produto_2 = db.Column(db.Integer, primary_key=True)
    nome_departamento_1 = db.Column("nomedepartamento_1", db.String, nullable=False)
    nome_setor_1 = db.Column("nomesetor_1", db.String, nullable=False)
    valor_venda_unidade_1 = db.Column("valorvendaunidade_1", db.String, nullable=False)
    nome_departamento_2 = db.Column("nomedepartamento_2", db.String, nullable=False)
    nome_setor_2 = db.Column("nomesetor_2", db.String, nullable=False)
    valor_venda_unidade_2 = db.Column("valorvendaunidade_2", db.String, nullable=False)


class ValorSkuSellers(db.Model):
    __table_name__ = "valor_sku_sellers"

    id_lojista = db.Column("idlojista", db.Integer, primary_key=True)
    id_sku = db.Column("idsku", db.Integer, nullable=False, primary_key=True)
    preco_anterior = db.Column("precoanterior", db.String, nullable=False)
    preco_venda = db.Column("precovenda", db.String, nullable=False)
    valor_via = db.Column("valor_via", db.String, nullable=False)
    diferenca = db.Column("diferenca", db.String, nullable=False)
    estoque_disponivel = db.Column("estoque_disponivel", db.String, nullable=False)
