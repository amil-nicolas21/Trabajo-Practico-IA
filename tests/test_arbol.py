import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd


notebook = json.loads(
    (Path(__file__).resolve().parents[1] / "src" / "TP_IA_DT_vs_RF.ipynb").read_text(encoding="utf-8")
)
namespace = {"np": np, "pd": pd}
exec(next("".join(cell["source"]) for cell in notebook["cells"]
          if "class ArbolDecision:" in "".join(cell.get("source", []))), namespace)
ArbolDecision = namespace["ArbolDecision"]


class TestMinimoPorHoja(unittest.TestCase):
    def test_divisiones(self):
        casos = [
            ([0] * 15 + [1] * 5, [0] * 15 + [1] * 5, True, 10, [20]),
            ([0] * 10 + [1] * 10, [0] * 10 + [1] * 10, True, 10, [10, 10]),
            ([0, 0, 1, 1, np.nan], [0, 0, 1, 1, 0], True, 3, [5]),
            ([0, 0, 0, 1, 1, np.nan], [0, 0, 0, 1, 1, 0], True, 2, [2, 4]),
            ([0, 0, 0, 1, 1], [0, 0, 0, 1, 1], True, 1, [2, 3]),
            (list(range(20)), [0] * 10 + [1] * 10, False, 10, [10, 10]),
            ([0, 1, 2], [0, 1, 1], False, 2, [3]),
        ]
        for criterio in ("ganancia", "razon_ganancia"):
            for valores, clases, categorico, minimo, esperados in casos:
                with self.subTest(criterio=criterio, categorico=categorico,
                                  minimo=minimo, esperados=esperados):
                    X = pd.DataFrame({"atributo": valores})
                    modelo = ArbolDecision(
                        criterio=criterio, min_muestras_hoja=minimo,
                        categoricos=["atributo"] if categorico else [],
                    ).fit(X, clases)
                    hojas = []
                    pendientes = [modelo.raiz_]
                    while pendientes:
                        nodo = pendientes.pop()
                        if nodo.es_hoja:
                            hojas.append(nodo.n)
                        else:
                            pendientes.extend(nodo.hijos.values())
                    self.assertEqual(sorted(hojas), esperados)
                    self.assertEqual(sum(hojas), len(clases))
                    self.assertEqual(len(modelo.predict(X)), len(clases))


if __name__ == "__main__":
    unittest.main()
