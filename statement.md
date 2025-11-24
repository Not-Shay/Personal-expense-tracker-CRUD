# Project Statement

## Problem Statement
Tracking personal expenses manually is tedious and prone to errors. Without a digital tool, it is difficult to calculate total spending or analyze where money is being spent.

## Scope
This is a CLI-based application that manages expenses using a persistent SQLite database.
* **In Scope:** CRUD operations, Category-based analytics, Input validation.
* **Out of Scope:** Bank integration, Multi-currency support.

## Target Users
Students and individuals looking for a simple, offline way to track daily spending.

## High-Level Features
* **Add Expenses:** Record amount, category, and date.
* **Analytics:** View total spending and spending by category.
* **Persistence:** Data is saved to `expenses.db`.
* **Validation:** Prevents invalid number/date inputs.
