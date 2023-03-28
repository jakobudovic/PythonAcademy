import unittest

import pandas as pd


class TestCsvFiles(unittest.TestCase):
    def test_csv_files(self):
        df_original = pd.read_excel("podatki_python_akademija.xlsx")
        df_created = pd.read_csv("out/one_line_data.csv", parse_dates=["DATUM"])

        self.assertEqual(pd.testing.assert_frame_equal(df_original, df_created), None)


if __name__ == "__main__":
    unittest.main(verbosity=3)
