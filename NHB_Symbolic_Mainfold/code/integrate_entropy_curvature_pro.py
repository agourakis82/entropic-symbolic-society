#!/usr/bin/env python3
# integrate_entropy_curvature_pro.py
# Gera source_fig2_entropy_curvature.csv a partir do *_all.csv (ou CSVs individuais).

import argparse, sys
import pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="CSV com H_rate,kappa,regime (ex.: entropy_curvature_all.csv)")
    ap.add_argument("--out", dest="out", default="source_fig2_entropy_curvature.csv")
    ap.add_argument("--select-beta", type=float, default=None)
    ap.add_argument("--rename-regimes", help="CSV mapping 'from,to'")
    args = ap.parse_args()

    df = pd.read_csv(args.inp)
    required = {"H_rate","kappa","regime"}
    missing = required - set(df.columns)
    if missing:
        print(f"[ERROR] faltam colunas: {missing}", file=sys.stderr)
        sys.exit(2)

    if args.select_beta is not None:
        df = df[df["beta"].round(8) == float(args.select_beta)]
        if df.empty:
            print(f"[ERROR] sem linhas para beta={args.select_beta}", file=sys.stderr)
            sys.exit(3)

    if args.rename_regimes:
        mp = pd.read_csv(args.rename_regimes)
        m = dict(zip(mp["from"], mp["to"]))
        df["regime"] = df["regime"].map(lambda x: m.get(x, x))

    out = df[["H_rate","kappa","regime"]].copy()
    out.to_csv(args.out, index=False)
    print(f"Wrote {args.out} ({len(out)} rows).")

if __name__ == "__main__":
    main()
