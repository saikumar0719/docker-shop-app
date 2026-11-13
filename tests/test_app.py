"""Tests for the shop app (same app as the Jenkins project)."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from app.main import clean_orders, load_orders, total_sales


def test_cleaning_counts_and_total():
    rows = load_orders()
    clean = clean_orders(rows)
    assert len(rows) == 11, f"expected 11 raw rows, got {len(rows)}"
    assert len(clean) == 8, f"expected 8 clean rows, got {len(clean)}"
    assert total_sales(clean) == 10550.00


def test_no_duplicate_order_ids():
    clean = clean_orders(load_orders())
    ids = [r["order_id"] for r in clean]
    assert len(ids) == len(set(ids)), "clean orders must have no duplicate order_id"


def test_no_missing_or_negative_amounts():
    clean = clean_orders(load_orders())
    assert all(r["amount"] >= 0 for r in clean)
