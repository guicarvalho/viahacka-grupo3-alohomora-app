import sqlalchemy as sa
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from sqlalchemy import func

from app.models import (
    CombosProdutos,
    Lojista,
    ValorSkuSellers,
    VendasLojistaFatuMedio,
    VendasLojistaMes,
    VendasLojistaSemana,
    VendasProdutosLojistaTop5,
)

app = Blueprint("seller", __name__, template_folder="templates")


@app.route("/")
def index():
    seller = int(session.get("seller", 0))

    if not seller:
        return redirect(url_for("seller.login"))

    monthly_sales = (
        VendasLojistaMes.query.with_entities(
            VendasLojistaMes.ano_mes,
            func.sum(VendasLojistaMes.qnt_venda).label("total_venda"),
            func.sum(VendasLojistaMes.qnt_itens_vendidos).label("total_itens"),
        )
        .filter(VendasLojistaMes.id_lojista == seller)
        .group_by(VendasLojistaMes.ano_mes)
        .order_by(VendasLojistaMes.ano_mes.desc())
        .limit(12)
        .all()
    )

    weekly_sales = (
        VendasLojistaSemana.query.with_entities(
            VendasLojistaSemana.id_lojista,
            (func.sum(VendasLojistaSemana.qnt_venda) + func.sum(VendasLojistaSemana.qnt_itens_vendidos)).label("total"),
        )
        .filter(VendasLojistaSemana.id_lojista == seller)
        .group_by(VendasLojistaSemana.id_lojista)
        .first()
    )

    top_five_skus = (
        VendasProdutosLojistaTop5.query.with_entities(
            VendasProdutosLojistaTop5.id_sku, func.sum(VendasProdutosLojistaTop5.qnt_itens_vendidos).label("total")
        )
        .filter(VendasProdutosLojistaTop5.id_lojista == seller)
        .group_by(VendasProdutosLojistaTop5.id_sku)
        .order_by(sa.text("total desc"))
        .limit(5)
        .all()
    )

    avg_conversion = (
        VendasLojistaFatuMedio.query.with_entities(
            func.coalesce(func.sum(VendasLojistaFatuMedio.media_conversao), 0).label("total")
        )
        .filter(VendasLojistaFatuMedio.id_lojista == seller)
        .first()
    )

    combo_sugestions = CombosProdutos.query.limit(5).all()
    combo_sugestions_total = CombosProdutos.query.count()

    monthly_sales = [
        {"ano_mes": s.ano_mes, "total_venda": s.total_venda, "total_itens": s.total_itens} for s in monthly_sales
    ]

    monthly_sales = sorted(monthly_sales, key=lambda sale: sale["ano_mes"])

    top_five_skus = [{"sku": p.id_sku, "total": p.total} for p in top_five_skus]

    return render_template(
        "index.html",
        current_user=seller,
        monthly_sales=monthly_sales,
        weekly_sales=weekly_sales[1],
        top_five_skus=top_five_skus,
        avg_conversion=avg_conversion[0],
        combo_sugestions=combo_sugestions,
        combo_sugestions_total=combo_sugestions_total,
    )


@app.route("/compare-skus", methods=["GET"])
def compare_skus():
    seller = int(session.get("seller", 0))

    if not seller:
        return redirect(url_for("seller.login"))

    values_sku_seller = (
        ValorSkuSellers.query.filter(ValorSkuSellers.id_lojista == seller, ValorSkuSellers.valor_via > 0)
        .limit(50)
        .all()
    )

    combo_sugestions = CombosProdutos.query.limit(5).all()
    combo_sugestions_total = CombosProdutos.query.count()

    return render_template(
        "compare_skus.html",
        current_user=seller,
        combo_sugestions=combo_sugestions,
        combo_sugestions_total=combo_sugestions_total,
        values_sku_seller=values_sku_seller,
    )


@app.route("/notifications", methods=["GET"])
def notifications():
    seller = int(session.get("seller", 0))

    if not seller:
        return redirect(url_for("seller.login"))

    combos = CombosProdutos.query.all()
    combo_sugestions = CombosProdutos.query.limit(5).all()
    combo_sugestions_total = CombosProdutos.query.count()

    return render_template(
        "notifications.html",
        current_user=seller,
        combos=combos,
        combo_sugestions=combo_sugestions,
        combo_sugestions_total=combo_sugestions_total,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        seller_id = request.form["seller"]

        seller = Lojista.query.with_entities(Lojista.id_lojista).filter(Lojista.id_lojista == seller_id).first()

        if not seller:
            flash("Usuário ou senha inválidos!", category="error")
            return redirect(url_for("seller.login"))

        session["seller"] = seller.id_lojista

        return redirect(url_for("seller.index"))

    return render_template("login.html", current_user=session.get("seller"))


@app.route("/logout")
def logout():
    session.pop("seller")
    return redirect("/login")
